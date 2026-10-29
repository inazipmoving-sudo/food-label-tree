#!/usr/bin/env python3
"""3D ball-and-stick models for the 2D/3D toggle on curriculum molecule drawings.

Usage:  python3 gen/mol3d.py <lesson-slug> [--refresh-pubchem]
Reads   gen/mol3d/<slug>.json   (spec: one entry per molecule PNG name)
Writes  curriculum/mol3d/<slug>/<name>.json  (one small model per molecule) and curriculum/mol3d/<slug>/index.json

Spec entry:  "<png name>": {"cid": <PubChem CID>, "smiles": "<atom-mapped isomeric SMILES>",
                           "anchors": {"<anchor key used by the lesson's markers>": [map numbers]},
                           "view": optional {"ring": [maps], "axis": [map_from, map_to], "up": [map_from, map_to], "tilt": deg, "phi": deg}}
 - The SMILES must be the same compound and stereochemistry as PubChem's isomeric SMILES for the CID: this is checked
   (canonical isomeric SMILES compare) and the PubChem SMILES is cached in the spec as "pubchem" so later builds run offline.
 - Anchor keys are the same keys the lesson uses for its numbered markers (gen/data/<slug>-mols.json anchors), so the 3D
   viewer can put the matching number on the same atom(s). A key with several atoms is labelled at their centroid.
 - Optional "chairs": [{"ring": [6 maps in ring order], "eq": [map_a, map_b]}]: keep only conformers where each such ring is a
   chair with bond a-b equatorial (e.g. 4C1 for D-pyranoses: C5-C6 equatorial); vacuum MMFF otherwise often prefers twisted
   rings held by internal hydrogen bonds, which would misrepresent axial/equatorial (alpha/beta) groups.
 - Geometry: RDKit ETKDG v3, all hydrogens explicit, 40 conformers (300 with "chairs"), MMFF94 optimised, lowest energy kept; the stereo of the
   final 3D conformer is re-perceived and must match the SMILES (so alpha/beta anomers and D/L centres are right).
 - Coordinates are in bond units (mean heavy-atom bond = 1), the same unit as the PNGs (72 px per bond), so the 3D model
   opens at the same scale as the drawing. Element radii/colours are those of molkit/lipids_mol (CPK, H = 0.55 x C).
Needs RDKit (pip install rdkit); the site build (gen/curriculum.py) only reads the JSON files and does not need it.
"""
import sys, os, json, urllib.request, urllib.parse
import numpy as np
CH_UNITS = 0.66  # X-H length in the PNGs (fats_flat.CH)
GEN = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(GEN); OUT = os.path.join(ROOT, 'curriculum', 'mol3d')
# element style in bond units: (radius, fill, edge) -- same values as fats_flat / lipids_mol / molkit EXT
STYLE = {"C": (0.27, "#333333", "#111"), "O": (0.25, "#e02020", "#7a0000"), "H": (0.15, "#f2f2f2", "#6f6f6f"),
 "N": (0.26, "#3050F8", "#0b1f8a"), "P": (0.31, "#FF8000", "#8a4500"),
 "S": (0.30, "#E8D21E", "#7a6a00"), "Na": (0.34, "#AB5CF2", "#4b1f7a"), "Cl": (0.36, "#1FC01F", "#0a5a0a"),
 "K": (0.38, "#8F40D4", "#3f1170"), "Ca": (0.36, "#3DBB00", "#1a5500"), "Mg": (0.32, "#7FCC00", "#3d6200"),
 "Fe": (0.33, "#E06633", "#7a2a0a"), "Zn": (0.32, "#7D80B0", "#3a3c60"), "Cu": (0.32, "#C88033", "#6a3c0a"),
 "I": (0.38, "#940094", "#4a004a"), "Se": (0.33, "#FFA100", "#8a5500"), "F": (0.24, "#90E050", "#3f7a10"),
 "Mn": (0.33, "#9C7AC7", "#4a2f70"), "Cr": (0.33, "#8A99C7", "#3a4570"), "Mo": (0.34, "#54B5B5", "#1f5a5a"),
 "Co": (0.33, "#F090A0", "#8a3040"), "B": (0.26, "#FFB5B5", "#8a5050")}

def pubchem_smiles(cid):
    u = f'https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/{cid}/property/IsomericSMILES,MolecularFormula/JSON'
    p = json.load(urllib.request.urlopen(u, timeout=30))['PropertyTable']['Properties'][0]
    return p.get('IsomericSMILES') or p.get('SMILES')

def canon(smi):
    from rdkit import Chem
    m = Chem.MolFromSmiles(smi)
    for a in m.GetAtoms(): a.SetAtomMapNum(0)
    return Chem.MolToSmiles(m, isomericSmiles=True)

def ring_ok(X, maps, chairs):
    """every listed six-ring is a chair (ring torsions alternate in sign, each > 30 deg) with the given bond equatorial"""
    def tor(a, b, c, d):
        b0, b1, b2 = X[a] - X[b], X[c] - X[b], X[d] - X[c]; b1n = b1 / np.linalg.norm(b1)
        v = b0 - np.dot(b0, b1n) * b1n; w = b2 - np.dot(b2, b1n) * b1n
        return np.degrees(np.arctan2(np.dot(np.cross(b1n, v), w), np.dot(v, w)))
    for ch in chairs:
        r = [maps[k] for k in ch['ring']]; t = [tor(*(r[(i + k) % 6] for k in range(4))) for i in range(6)]
        if not all(abs(x) > 30 for x in t) or not all(t[i] * t[(i + 1) % 6] < 0 for i in range(6)): return False
        c = X[r].mean(0); nn = np.linalg.svd(X[r] - c)[2][2]; a, b = ch['eq']; v = X[maps[b]] - X[maps[a]]
        if abs(np.dot(v / np.linalg.norm(v), nn)) > 0.6: return False
    return True

def auto_chairs(m):
    """every saturated six-membered ring (all sp3 ring atoms) must come out as a chair"""
    from rdkit import Chem
    out = []
    for r in m.GetRingInfo().AtomRings():
        if len(r) == 6 and all(m.GetAtomWithIdx(i).GetHybridization() == Chem.HybridizationType.SP3 for i in r): out.append(list(r))
    return out

def chair_ok(X, rings):
    def tor(a, b, c, d):
        b0, b1, b2 = X[a] - X[b], X[c] - X[b], X[d] - X[c]; b1n = b1 / np.linalg.norm(b1)
        v = b0 - np.dot(b0, b1n) * b1n; w = b2 - np.dot(b2, b1n) * b1n
        return np.degrees(np.arctan2(np.dot(np.cross(b1n, v), w), np.dot(v, w)))
    for r in rings:
        t = [tor(*(r[(i + k) % 6] for k in range(4))) for i in range(6)]
        if not all(abs(x) > 30 for x in t) or not all(t[i] * t[(i + 1) % 6] < 0 for i in range(6)): return False
    return True

def kabsch(A, B):
    """proper rotation R (det +1) minimising |A R^T - B| for centred A, B; returns R, rmsd"""
    H = A.T @ B; U, S, Vt = np.linalg.svd(H); d = np.sign(np.linalg.det(Vt.T @ U.T)) or 1.0
    R = Vt.T @ np.diag([1, 1, d]) @ U.T
    return R, float(np.sqrt(((A @ R.T - B) ** 2).sum(1).mean()))

def embed(smi, n=40, seed=7, chairs=(), align=None, window=10.0):
    """ETKDG v3 conformers, MMFF94 (UFF if MMFF has no parameters, e.g. Mo); keep conformers that pass the ring checks;
    with align (drawing coordinates) pick, within `window` kcal/mol of the lowest energy, the one that best matches the drawing."""
    from rdkit import Chem
    from rdkit.Chem import AllChem
    m = Chem.AddHs(Chem.MolFromSmiles(smi))
    mmff = AllChem.MMFFHasAllMoleculeParams(m)
    opt = (lambda mol, **k: AllChem.MMFFOptimizeMoleculeConfs(mol, **k)) if mmff else (lambda mol, **k: AllChem.UFFOptimizeMoleculeConfs(mol, **k))
    if m.GetNumHeavyAtoms() == 1:
        AllChem.EmbedMolecule(m, randomSeed=seed); opt(m, maxIters=2000); return m, m.GetConformer().GetId(), ('MMFF94' if mmff else 'UFF')
    maps = {a.GetAtomMapNum(): a.GetIdx() for a in m.GetAtoms() if a.GetAtomMapNum()}
    rings = auto_chairs(m) if chairs == 'auto' else []
    ps = AllChem.ETKDGv3(); ps.randomSeed = seed; ps.pruneRmsThresh = 0.2
    if chairs: n = max(n, 300 if chairs != 'auto' or rings else n)
    if align and m.GetNumAtoms() > 40: n = max(n, 80)
    cids = list(AllChem.EmbedMultipleConfs(m, numConfs=n, params=ps))
    if not cids: ps.useRandomCoords = True; cids = list(AllChem.EmbedMultipleConfs(m, numConfs=n, params=ps))
    res = opt(m, maxIters=5000)
    def good(k):
        X = m.GetConformer(cids[k]).GetPositions()
        return (ring_ok(X, maps, chairs) if chairs and chairs != 'auto' else chair_ok(X, rings))
    ok = [k for k in range(len(cids)) if res[k][0] == 0 and good(k)]
    if not ok: ok = [k for k in range(len(cids)) if good(k)]
    assert ok, ('no conformer with the required chair rings', smi)
    e0 = min(res[k][1] for k in ok)
    if align:
        ids = [maps[a[0]] for a in align]; B = np.array([a[1:] for a in align], float); B = B - B.mean(0)
        def fit(k):
            X = m.GetConformer(cids[k]).GetPositions()[ids]; hb = bond_unit(m, m.GetConformer(cids[k]).GetPositions()); A = X / hb; A = A - A.mean(0)
            return kabsch(A, B)[1]
        best = min((k for k in ok if res[k][1] <= e0 + window), key=fit)
    else: best = min(ok, key=lambda k: res[k][1])
    return m, cids[best], ('MMFF94' if mmff else 'UFF')

def bond_unit(m, X):
    hb = [np.linalg.norm(X[b.GetBeginAtomIdx()] - X[b.GetEndAtomIdx()]) for b in m.GetBonds() if b.GetBeginAtom().GetAtomicNum() > 1 and b.GetEndAtom().GetAtomicNum() > 1]
    if hb: return float(np.mean(hb))
    xh = [np.linalg.norm(X[b.GetBeginAtomIdx()] - X[b.GetEndAtomIdx()]) for b in m.GetBonds()]; return float(np.mean(xh)) / CH_UNITS

def check_stereo(m, conf_id, smi):
    from rdkit import Chem
    c = Chem.Conformer(m.GetConformer(conf_id)); keep = Chem.Mol(m); keep.RemoveAllConformers(); keep.AddConformer(c, assignId=True)
    for a in keep.GetAtoms(): a.SetAtomMapNum(0)   # map numbers would make e.g. the two methyls of an isopropyl look different
    Chem.AssignStereochemistryFrom3D(keep)
    for a in keep.GetAtoms():   # P(=O)(O-)... / N+ / metal centres are not stereocentres (resonance, inversion)
        if a.GetSymbol() not in ('C', 'S'): a.SetChiralTag(Chem.ChiralType.CHI_UNSPECIFIED)
    q = Chem.RemoveHs(keep)
    if True:   # C=N-H imines (e.g. the arginine amidine) are left open by the model spec: do not compare them
        tgt = Chem.MolFromSmiles(smi)
        for b in q.GetBonds():
            if b.GetBondType() == Chem.BondType.DOUBLE and 'N' in (b.GetBeginAtom().GetSymbol(), b.GetEndAtom().GetSymbol()) \
               and tgt.GetBondBetweenAtoms(b.GetBeginAtomIdx(), b.GetEndAtomIdx()).GetStereo() == Chem.BondStereo.STEREONONE:
                b.SetStereo(Chem.BondStereo.STEREONONE)
                for a in (b.GetBeginAtom(), b.GetEndAtom()):
                    for nb in a.GetBonds(): nb.SetBondDir(Chem.BondDir.NONE)
    got = canon(Chem.MolToSmiles(q))
    assert got == canon(smi), ('3D stereo mismatch', got, canon(smi))

def orient(X, maps, view, heavy, align=None):
    """returns coordinates with x right, y up, z toward the viewer (a proper rotation, never a mirror)"""
    X = X - X[heavy].mean(0)
    if align:  # turn the model to best match the 2D drawing's atom positions (x, y; z for 3D-view drawings)
        ids = [maps[a[0]] for a in align]; B = np.array([a[1:] for a in align], float); c = X[ids].mean(0)
        R, _ = kabsch(X[ids] - c, B - B.mean(0)); Y = (X - c) @ R.T; return Y - Y[heavy].mean(0)
    if view:  # same view as molkit.from3d (the PNG): ring normal up, axis atom pair along x, spin phi, tilt toward the viewer
        ring = [maps[k] for k in view['ring']]; c = X[ring].mean(0)
        n = np.linalg.svd(X[ring] - c)[2][2]
        a, b = view['up']; n = n if np.dot(X[maps[b]] - X[maps[a]], n) > 0 else -n
        a, b = view['axis']; v = X[maps[b]] - X[maps[a]]; v = v - np.dot(v, n) * n; e1 = v / np.linalg.norm(v); e2 = np.cross(n, e1)
        Y = np.stack([(X - c) @ e1, (X - c) @ n, (X - c) @ e2], 1)  # x, up, depth (away from the viewer)
        ph = np.radians(view.get('phi', 0)); Rz = np.array([[np.cos(ph), 0, -np.sin(ph)], [0, 1, 0], [np.sin(ph), 0, np.cos(ph)]])
        Z = Y @ Rz.T; t = np.radians(view.get('tilt', 0))
        P = np.stack([Z[:, 0], Z[:, 1] * np.cos(t) + Z[:, 2] * np.sin(t), -(Z[:, 2] * np.cos(t) - Z[:, 1] * np.sin(t))], 1)
        return P - P[heavy].mean(0)
    if len(heavy) >= 3: _, _, vt = np.linalg.svd(X[heavy])
    else: _, _, vt = np.linalg.svd(X)
    R = vt.copy()
    if np.linalg.det(R) < 0: R[2] *= -1
    return X @ R.T

def write(out, name, model, index):
    p = os.path.join(out, name + '.json'); open(p, 'w').write(json.dumps(model, separators=(',', ':')) + '\n')
    index[name] = sorted(model['anchors'])
    print(f'{name:18s} CID {str(model["cid"]):<9} {model["formula"]:14s} {len(model["atoms"]):4d} atoms  {os.path.getsize(p)} B')

def inchi_flat(smi):
    from rdkit import Chem
    m = Chem.MolFromSmiles(smi)
    for a in m.GetAtoms(): a.SetAtomMapNum(0)
    return (Chem.MolToInchi(m, options='-SNon') or '').split('/p')[0].split('/q')[0]

def cip(m):
    from rdkit import Chem
    from rdkit.Chem import rdCIPLabeler
    q = Chem.Mol(m); rdCIPLabeler.AssignCIPLabels(q)
    return ({a.GetIdx(): a.GetProp('_CIPCode') for a in q.GetAtoms() if a.HasProp('_CIPCode')},
            {tuple(sorted((b.GetBeginAtomIdx(), b.GetEndAtomIdx()))): b.GetProp('_CIPCode') for b in q.GetBonds() if b.HasProp('_CIPCode')})

def same_compound(smi, pub, name):
    """smi (drawn form, atom-mapped) is PubChem's compound: identical canonical isomeric SMILES, or (drawn tautomer/charge form)
    the same InChI skeleton and every stereo element PubChem specifies is present with the same CIP label (matched by element + connectivity)"""
    from rdkit import Chem
    if canon(smi) == canon(pub): return
    assert inchi_flat(smi) == inchi_flat(pub), (name, 'not the PubChem compound', canon(smi), pub)
    d = Chem.MolFromSmiles(smi); p = Chem.MolFromSmiles(pub)
    sm = Chem.MolFragmentToSmiles(d, atomsToUse=list(range(d.GetNumAtoms())), atomSymbols=[f'[#{a.GetAtomicNum()}:{a.GetIdx()+1}]' for a in d.GetAtoms()], bondSymbols=['~'] * d.GetNumBonds(), canonical=False)
    q = Chem.MolFromSmarts(sm); qi = {a.GetIdx(): a.GetAtomMapNum() - 1 for a in q.GetAtoms()}
    da, db = cip(d); pa, pb = cip(p)
    for mt in p.GetSubstructMatches(q, uniquify=False, maxMatches=20000):
        inv = {pp: qi[k] for k, pp in enumerate(mt)}
        if all(da.get(inv[i]) == l for i, l in pa.items()) and all(db.get(tuple(sorted((inv[a], inv[b])))) == l for (a, b), l in pb.items()): return
    raise AssertionError((name, 'stereo differs from PubChem', canon(smi), pub))

def build(slug, refresh=False):
    from rdkit import Chem
    from rdkit.Chem.rdMolDescriptors import CalcMolFormula
    sp_path = os.path.join(GEN, 'mol3d', slug + '.json'); spec = json.load(open(sp_path, encoding='utf-8'))
    out = os.path.join(OUT, slug); os.makedirs(out, exist_ok=True); index = {}
    for name, s in spec.items():
        if name.startswith('_') or 'skip' in s: continue
        if 'coords' in s:  # a scene with real 3D atom positions (e.g. a PDB entry), drawn as-is
            els = [a[0] for a in s['coords']]; X = np.array([a[1:] for a in s['coords']], float); X -= X[[i for i, e in enumerate(els) if e != 'H']].mean(0)
            model = {'v': 1, 'name': name, 'cid': s.get('cid'), 'smiles': None, 'formula': s.get('formula', ''), 'source': s['source'] + '; coordinates in bond units',
                     'style': {e: STYLE[e] for e in sorted(set(els))}, 'atoms': [[els[i], *[round(float(v), 3) for v in X[i]]] for i in range(len(els))],
                     'bonds': [list(b) for b in s['bonds']], 'anchors': {k: [x - 1 for x in v] for k, v in s.get('anchors', {}).items()}}
            write(out, name, model, index); continue
        if refresh or 'pubchem' not in s: s['pubchem'] = pubchem_smiles(s['cid'])
        same_compound(s['smiles'], s['pubchem'], name)
        m, cid, ff = embed(s['smiles'], chairs=s.get('chairs', ()), align=s.get('align'))
        if not s.get('stereo_free'): check_stereo(m, cid, s['smiles'])
        X = m.GetConformer(cid).GetPositions()
        maps = {a.GetAtomMapNum(): a.GetIdx() for a in m.GetAtoms() if a.GetAtomMapNum()}
        heavy = [a.GetIdx() for a in m.GetAtoms() if a.GetAtomicNum() > 1]
        unit = bond_unit(m, X)
        X = orient(X / unit, maps, s.get('view'), heavy, s.get('align'))
        els = [a.GetSymbol() for a in m.GetAtoms()]
        model = {'v': 1, 'name': name, 'cid': s['cid'], 'smiles': canon(s['smiles']), 'formula': CalcMolFormula(m),
                 'source': f'PubChem CID {s["cid"]} ({s.get("title", "")}); RDKit ETKDGv3 + {ff}, all H explicit; coordinates in bond units (mean heavy-atom bond = 1, {unit:.3f} \u00c5)',
                 'style': {e: STYLE[e] for e in sorted(set(els))},
                 'atoms': [[els[i], *[round(float(v), 3) for v in X[i]]] for i in range(len(els))],
                 'bonds': [[b.GetBeginAtomIdx(), b.GetEndAtomIdx(), int(b.GetBondTypeAsDouble())] for b in m.GetBonds()],
                 'anchors': {k: [maps[x] for x in v] for k, v in s.get('anchors', {}).items()}}
        write(out, name, model, index)
    open(os.path.join(out, 'index.json'), 'w').write(json.dumps(index, indent=1, sort_keys=True) + '\n')
    json.dump(spec, open(sp_path, 'w', encoding='utf-8'), indent=1, ensure_ascii=False); open(sp_path, 'a').write('\n')
    print('wrote', out, len(index), 'models')

if __name__ == '__main__':
    build(sys.argv[1], refresh='--refresh-pubchem' in sys.argv)
