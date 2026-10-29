#!/usr/bin/env python3
"""Fats lesson: capture the drawn molecules of fats_omega.py (fig-06-reach-*, fig-10-*) and fats_omega_fam.py (fig-06-fam-*)
by hooking fats_flat.draw / fats_energy3.draw_tri (savefig is a no-op), and write mol3d specs with atom maps = drawing
order and 'align' = drawing x, y (bond units, y up), so each 3D model opens turned like its PNG.
Run from /workspace/nutrition:  python3 label-tree/gen/mol3d_tools/fats_capture.py"""
import sys, os, json, runpy
import numpy as np, matplotlib; matplotlib.use('Agg')
import matplotlib.figure
from rdkit import Chem
sys.path.insert(0, os.getcwd())
sys.argv = ['x', '/tmp/fo', '/tmp/fd']
import fats_flat as F, fats_energy3 as E
REC, FIGS = [], {}
_d, _t = F.draw, E.draw_tri
def draw(ax, m): REC.append(('mol', m)); return _d(ax, m)
def draw_tri(ax, ms, g): REC.append(('tri', ms, g)); return None
def save(self, p, **k):
    FIGS[os.path.basename(str(p))[:-4]] = list(REC); REC.clear()
matplotlib.figure.Figure.savefig = save
F.draw = draw; E.draw_tri = draw_tri
CIDS = {'stearic': 5281, 'oleic': 445639, 'elaidic': 637517, 'linoleic': 5280450, 'la': 5280450, 'ala': 5280934,
        'epa': 446284, 'dha': 445580, 'aa': 444899, 'triglyceride': 9544086}
for s in ('fats_omega.py', 'fats_omega_fam.py'):
    REC.clear(); runpy.run_path(s, run_name='__main__')

def graph(name, r):
    if r[0] == 'mol':
        m = r[1]; A = [a for a in m.A if a.get('tag') != 'spacer']; idx = {id(a): k for k, a in enumerate(m.A)}
        return [(a['el'], a['p']) for a in m.A], list(m.B)
    ms, g = r[1], r[2]; atoms, bonds = [], []
    for m in ms:
        o = len(atoms); atoms += [(a['el'], a['p']) for a in m.A]; bonds += [(i + o, j + o, b) for i, j, b in m.B]; m._o = o
    keep = [k for k, a in enumerate(g.A) if not a.get('ghost') and a.get('tag') != 'spacer']; gi = {}
    for k in keep: gi[k] = len(atoms); atoms.append((g.A[k]['el'], g.A[k]['p']))
    bonds += [(gi[i], gi[j], b) for i, j, b in g.B if i in gi and j in gi]
    bonds += [(gi[c], m._o + m.O2, 1) for c, m in zip(g.gc, ms)]
    return atoms, bonds

def spec(name, atoms, bonds, iso, cid):
    rw = Chem.RWMol()
    for el, p in atoms: a = Chem.Atom(el); a.SetNoImplicit(True); rw.AddAtom(a)
    for i, j, o in bonds: rw.AddBond(int(i), int(j), Chem.BondType.DOUBLE if o == 2 else Chem.BondType.SINGLE)
    dm = rw.GetMol(); Chem.SanitizeMol(dm)
    ref = Chem.AddHs(Chem.MolFromSmiles(iso))
    match = ref.GetSubstructMatch(dm)  # ref atom for each drawing atom
    assert match and ref.GetNumAtoms() == dm.GetNumAtoms(), (name, 'drawing does not match', iso)
    heavy = [k for k, (el, p) in enumerate(atoms) if el != 'H']; mp = {k: n + 1 for n, k in enumerate(heavy)}
    for a in ref.GetAtoms(): a.SetAtomMapNum(0)
    for k in heavy: ref.GetAtomWithIdx(match[k]).SetAtomMapNum(mp[k])
    smi = Chem.MolToSmiles(Chem.RemoveHs(ref))
    P = np.array([atoms[k][1] for k in heavy]); P = P - P.mean(0)
    s = {'cid': cid, 'smiles': smi, 'anchors': {}, 'align': [[mp[k], round(float(atoms[k][1][0]), 4), round(float(atoms[k][1][1]), 4), 0.0] for k in heavy]}
    if name == 'triglyceride': s['stereo_free'] = True  # glycerol C2 unspecified (food TAGs are mixtures); PubChem CID 9544086 has it unspecified too
    return s

ISO = {'stearic': 'CCCCCCCCCCCCCCCCCC(=O)O', 'oleic': 'CCCCCCCC/C=C\\CCCCCCCC(=O)O', 'elaidic': 'CCCCCCCC/C=C/CCCCCCCC(=O)O',
       'linoleic': 'CCCCC/C=C\\C/C=C\\CCCCCCCC(=O)O', 'ala': 'CC/C=C\\C/C=C\\C/C=C\\CCCCCCCC(=O)O',
       'epa': 'CC/C=C\\C/C=C\\C/C=C\\C/C=C\\C/C=C\\CCCC(=O)O', 'dha': 'CC/C=C\\C/C=C\\C/C=C\\C/C=C\\C/C=C\\C/C=C\\CCC(=O)O',
       'aa': 'CCCCC/C=C\\C/C=C\\C/C=C\\C/C=C\\CCCC(=O)O',
       'triglyceride': 'CCCCCCCCCCCCCCCC(=O)OCC(OC(=O)CCCCCCC/C=C\\CCCCCCCC)COC(=O)CCCCCCC/C=C\\C/C=C\\CCCCC'}
ISO['la'] = ISO['linoleic']
out = {'_doc': 'fats: gen/mol3d_tools/fats_capture.py (fats_omega*.py drawing capture, align = drawing x, y)'}
for f, recs in sorted(FIGS.items()):
    r = [x for x in recs if x[0] == 'tri'] or [x for x in recs if x[0] == 'mol']
    key = f.split('-')[-1]
    if key not in ISO or len(r) != 1: print('skip', f, len(recs)); continue
    at, bd = graph(f, r[0]); out[f] = spec(key, at, bd, ISO[key], CIDS[key]); print('ok', f, len(at))
json.dump(out, open('label-tree/gen/mol3d/fats.json', 'w'), indent=1)
