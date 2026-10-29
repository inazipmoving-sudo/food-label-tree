# Auto-spec: capture records + PubChem -> gen/mol3d/<slug>.json (atom-mapped PubChem isomeric SMILES, anchors, align view)
import pickle, json, os, sys, time, itertools, urllib.request, urllib.parse, hashlib
import numpy as np
from rdkit import Chem, RDLogger
from rdkit.Chem.rdMolDescriptors import CalcMolFormula
RDLogger.DisableLog('rdApp.*')
ROOT="/workspace/nutrition/label-tree"; CAP="/workspace/nutrition/mol3d_cap"
R=pickle.load(open(f"{CAP}/all.pkl","rb")); IM=json.load(open(f"{CAP}/imgmap.json"))
MAN=json.load(open(f"{CAP}/manual.json"))   # {"slug/name" or "name": {"cid":..} | {"skip": reason} | {"stereo_free": true}}
def pc(path, data=None):
    k=hashlib.md5((path+str(data)).encode()).hexdigest(); f=f"{CAP}/pc/{k}.json"
    if os.path.exists(f): return json.load(open(f))
    u="https://pubchem.ncbi.nlm.nih.gov/rest/pug/"+path
    for t in range(4):
        try:
            req=urllib.request.Request(u, data=urllib.parse.urlencode(data).encode() if data else None)
            j=json.load(urllib.request.urlopen(req, timeout=30)); break
        except urllib.error.HTTPError as e:
            if e.code in (400,404): j={"_404":e.code}; break
            time.sleep(2+t*3)
        except Exception: time.sleep(2+t*3)
    else: raise RuntimeError(u)
    json.dump(j,open(f,"w")); time.sleep(0.25); return j
def cid_by_smiles(smi):
    j=pc("compound/smiles/cids/JSON",{"smiles":smi}); c=j.get("IdentifierList",{}).get("CID",[0])[0]; return c or None
def cid_by_name(n):
    j=pc("compound/name/"+urllib.parse.quote(n)+"/cids/JSON"); return j.get("IdentifierList",{}).get("CID",[None])[0]
def pc_smiles(cid):
    p=pc(f"compound/cid/{cid}/property/IsomericSMILES,MolecularFormula,IUPACName,Title/JSON")["PropertyTable"]["Properties"][0]
    return p.get("IsomericSMILES") or p.get("SMILES"), p.get("Title"), p.get("MolecularFormula")
VAL={"O":2,"N":3,"S":2,"Cl":1,"F":1,"I":1,"Br":1,"C":4,"P":5,"H":1,"Se":2}
def drawing_mol(r):
    if r["rd"]:
        m=Chem.MolFromSmiles(r["rd"]); return m, "smiles"
    rw=Chem.RWMol()
    for e in r["el"]:
        a=Chem.Atom(e); a.SetNoImplicit(True); rw.AddAtom(a)
    for i,j,o in r["B"]: rw.AddBond(i,j,{1:Chem.BondType.SINGLE,2:Chem.BondType.DOUBLE,3:Chem.BondType.TRIPLE}[o])
    for a in rw.GetAtoms():
        v=sum(b.GetBondTypeAsDouble() for b in a.GetBonds()); e=a.GetSymbol()
        if e in ("O","S","Cl","F","I","Se") and e in VAL and v!=VAL[e]: a.SetFormalCharge(int(v-VAL[e]))
        if e=="N" and v==4: a.SetFormalCharge(1)
        if a.GetAtomicNum()>1: a.SetAtomMapNum(a.GetIdx()+1)
    m=rw.GetMol(); Chem.SanitizeMol(m); m=Chem.RemoveHs(m); Chem.AssignStereochemistry(m,cleanIt=True,force=True); return m,"graph"
def flat(m):
    q=Chem.Mol(m); Chem.RemoveStereochemistry(q)
    for a in q.GetAtoms(): a.SetAtomMapNum(0)
    return Chem.MolToSmiles(q)
def iso(m):
    q=Chem.Mol(m)
    for a in q.GetAtoms(): a.SetAtomMapNum(0)
    return Chem.MolToSmiles(q)
def cip(m):
    from rdkit.Chem import rdCIPLabeler
    q=Chem.Mol(m); rdCIPLabeler.AssignCIPLabels(q)
    at={a.GetIdx():a.GetProp("_CIPCode") for a in q.GetAtoms() if a.HasProp("_CIPCode")}
    bd={tuple(sorted((b.GetBeginAtomIdx(),b.GetEndAtomIdx()))):b.GetProp("_CIPCode") for b in q.GetBonds() if b.HasProp("_CIPCode")}
    return at,bd
def inchi_flat(m):
    q=Chem.Mol(m)
    for a in q.GetAtoms(): a.SetAtomMapNum(0)
    i=Chem.MolToInchi(q,options="-SNon") or ""
    return i.split("/p")[0].split("/q")[0]
def topo_match(dm,pm):
    """match drawing atoms onto PubChem atoms by element + connectivity only (tautomers/charges/bond orders may differ)"""
    sm=Chem.MolFragmentToSmiles(dm,atomsToUse=list(range(dm.GetNumAtoms())),atomSymbols=[f"[#{a.GetAtomicNum()}:{a.GetIdx()+1}]" for a in dm.GetAtoms()],
        bondSymbols=["~"]*dm.GetNumBonds(),canonical=False,allHsExplicit=False)
    qm=Chem.MolFromSmarts(sm); qi={a.GetIdx():a.GetAtomMapNum()-1 for a in qm.GetAtoms()}
    ms=pm.GetSubstructMatches(qm,uniquify=False,maxMatches=20000,useChirality=False)
    out=[]
    for m in ms:
        mt=[0]*dm.GetNumAtoms()
        for k,p in enumerate(m): mt[qi[k]]=p
        out.append(mt)
    return out or None
def transfer(dm,pm,mts):
    """drawing molecule with every stereo element PubChem specifies (tetrahedral by CIP label, double bonds by CIP label);
    stereo the drawing already specifies must agree. Returns (mol, n disagreements, n set)."""
    from rdkit.Chem import rdCIPLabeler
    pa,pb=cip(pm); da,db=cip(dm); best=None
    for mt in mts:
        bad=sum(1 for i,l in da.items() if pa.get(mt[i],l)!=l)+sum(1 for (i,j),l in db.items() if pb.get(tuple(sorted((mt[i],mt[j]))),l)!=l)
        if best is None or bad<best[0]: best=(bad,mt)
        if bad==0: break
    bad,mt=best
    if bad: return None,bad,0
    inv={p:i for i,p in enumerate(mt)}
    q=Chem.RWMol(dm); nset=0
    want={inv[p]:l for p,l in pa.items() if p in inv}
    wantb={tuple(sorted((inv[a],inv[b]))):l for (a,b),l in pb.items() if a in inv and b in inv}
    for i,l in want.items():
        if i in da: continue
        for tag in (Chem.ChiralType.CHI_TETRAHEDRAL_CW,Chem.ChiralType.CHI_TETRAHEDRAL_CCW):
            q.GetAtomWithIdx(i).SetChiralTag(tag); Chem.AssignStereochemistry(q,cleanIt=True,force=True)
            if cip(q)[0].get(i)==l: nset+=1; break
        else: return None,1,0
    for (i,j),l in wantb.items():
        if (i,j) in db: continue
        b=q.GetBondBetweenAtoms(i,j)
        if b is None or b.GetBondType()!=Chem.BondType.DOUBLE: continue
        a1=[n.GetIdx() for n in q.GetAtomWithIdx(i).GetNeighbors() if n.GetIdx()!=j][0]; a2=[n.GetIdx() for n in q.GetAtomWithIdx(j).GetNeighbors() if n.GetIdx()!=i][0]
        for st in (Chem.BondStereo.STEREOCIS,Chem.BondStereo.STEREOTRANS):
            b.SetStereoAtoms(a1,a2); b.SetStereo(st); Chem.AssignStereochemistry(q,cleanIt=True,force=True)
            if cip(q)[1].get((i,j))==l: nset+=1; break
        else: return None,1,0
    m=q.GetMol(); Chem.AssignStereochemistry(m,cleanIt=True,force=True)
    return m,0,nset
def find_anchor(r, pct, heavy_only_map):
    xy=np.array(r["xy"]); t=np.array(pct)
    near=[i for i in range(len(xy)) if np.linalg.norm(xy[i]-t)<40]
    near.sort(key=lambda i:np.linalg.norm(xy[i]-t)); near=near[:14]
    for k in (1,2,3,4,5,6):
        for c in itertools.combinations(near,k):
            if np.linalg.norm(xy[list(c)].mean(0)-t)<0.03: return list(c),True
    return [near[0]],False
def heavy_of(r,i):
    if r["el"][i]!="H": return i
    for a,b,o in r["B"]:
        if a==i: return b
        if b==i: return a
def run(slug):
    D=json.load(open(f"{ROOT}/gen/data/{slug}-mols.json")); spec={"_doc":"auto: gen/mol3d_auto.py (drawing capture + PubChem); see gen/mol3d.py"}; rep=[]
    for name,d in D.items():
        key=IM.get(f"{slug}/{name}"); mo=MAN.get(f"{slug}/{name}",MAN.get(name,{}))
        if "skip" in mo: rep.append((name,"SKIP",mo["skip"])); continue
        if not key: rep.append((name,"SKIP","no captured drawing")); continue
        r=R[tuple(key.split("/"))]
        heavy=r["heavy"]
        if len(heavy)==1 and len(r["el"])==1: rep.append((name,"SKIP","lone ion/atom: a single sphere, 3D adds nothing")); continue
        # anchors
        anc={}; bad=[]
        for k,v in d.get("anchors",{}).items():
            ix,ok=find_anchor(r,v,None); hs=sorted({heavy_of(r,i) for i in ix})
            anc[k]=[i+1 for i in hs]
            if not ok: bad.append(k)
        P=np.array(r["p"]); Z=np.array(r["z"])
        if mo.get("coords"):  # real 3D scene coordinates (e.g. from a PDB entry), drawn as-is
            spec[name]={"coords":[[r["el"][i],round(P[i][0],4),round(P[i][1],4),round(Z[i],4)] for i in range(len(r["el"]))],"bonds":[list(b) for b in r["B"]],
                        "anchors":anc,"source":mo["coords"],"cid":mo.get("cid")}
            rep.append((name,"COORDS",mo["coords"],bad)); continue
        if key.startswith("macronutrients-carbohydrates/") and slug!="macronutrients-carbohydrates":  # reuse the checked Carbohydrates model spec
            cs=json.load(open(f"{ROOT}/gen/mol3d/macronutrients-carbohydrates.json"))[key.split("/")[1]]
            spec[name]=dict(cs); rep.append((name,"CARBS",cs["cid"])); continue
        dm,how=drawing_mol(r)
        if mo.get("override_stereo"):
            Chem.RemoveStereochemistry(dm)
            for b in dm.GetBonds(): b.SetBondDir(Chem.BondDir.NONE); b.SetStereo(Chem.BondStereo.STEREONONE)
        unspec=any(s_.specified==Chem.StereoSpecified.Unspecified and s_.type==Chem.StereoType.Atom_Tetrahedral for s_ in Chem.FindPotentialStereo(dm))
        if unspec and not (mo.get("cid") or mo.get("name")): rep.append((name,"NEEDCID",iso(dm))); continue
        cid=mo.get("cid") or (mo.get("name") and cid_by_name(mo["name"])) or cid_by_smiles(iso(dm))
        if not cid: rep.append((name,"NOCID",iso(dm))); continue
        psmi,title,pf=pc_smiles(cid); pm=Chem.MolFromSmiles(psmi)
        if mo.get("parent"):  # PubChem record is a salt / neutral acid of the drawn ion: compare the largest fragment, charge-neutral
            from rdkit.Chem.MolStandardize import rdMolStandardize as S
            pm=S.Uncharger().uncharge(S.LargestFragmentChooser().choose(pm))
            dn=S.Uncharger().uncharge(Chem.Mol(dm))
            if inchi_flat(pm)!=inchi_flat(dn): rep.append((name,"DIFF",cid,title,flat(dm),flat(pm))); continue
            pm=dm  # same skeleton; the drawn ion is the model (no stereo to take)

        same=inchi_flat(pm)==inchi_flat(dm) or flat(pm)==flat(dm)
        if not same: rep.append((name,"DIFF",cid,title,flat(dm),flat(pm))); continue
        mt=topo_match(dm,pm)
        if mt is None: rep.append((name,"NOMATCH",cid,title)); continue
        if mo.get("override_stereo") and inchi_flat(pm)==inchi_flat(dm) and flat(pm)==flat(dm):  # drawing = PubChem record exactly: take PubChem's molecule, mapped to the drawing atoms
            q=Chem.RWMol(pm)
            for i,p in enumerate(mt[0]): q.GetAtomWithIdx(p).SetAtomMapNum(dm.GetAtomWithIdx(i).GetAtomMapNum())
            nbad=0
        else: q,nbad,nset=transfer(dm,pm,mt)
        if nbad: rep.append((name,"STEREODIFF",cid,title,iso(dm),psmi)); continue
        smi=Chem.MolToSmiles(q); st="drawing+pubchem"
        und=[s for s in Chem.FindPotentialStereo(Chem.MolFromSmiles(smi)) if s.specified==Chem.StereoSpecified.Unspecified]
        # only real stereocentres (not e.g. the amidine C=N of arginine, where PubChem also leaves it open)
        e={"cid":cid,"title":title,"smiles":smi,"anchors":{k:v for k,v in anc.items()},
           "align":[[int(a.GetAtomMapNum()),round(P[a.GetAtomMapNum()-1][0],4),round(P[a.GetAtomMapNum()-1][1],4),round(Z[a.GetAtomMapNum()-1],4)] for a in dm.GetAtoms()],
           "chairs":"auto"}
        if st=="graph": e["graph"]=True
        if mo.get("stereo_free"): e["stereo_free"]=True; e["note"]=mo.get("note","")
        elif [u for u in und if u.type==Chem.StereoType.Atom_Tetrahedral and Chem.MolFromSmiles(smi).GetAtomWithIdx(u.centeredOn).GetSymbol() in ("C","S","N")]: rep.append((name,"OPENSTEREO",cid,title,smi)); continue
        if mo.get("override_stereo"): e["note"]=mo.get("note","")
        spec[name]=e
        rep.append((name,"OK",cid,title,"draw-stereo-unspec" if any(s.specified==Chem.StereoSpecified.Unspecified for s in Chem.FindPotentialStereo(dm)) else "",("open:"+str(len(und))) if und else "",bad))
    return spec,rep
if __name__=="__main__":
    for slug in sys.argv[1:]:
        spec,rep=run(slug)
        json.dump(spec,open(f"{CAP}/spec-{slug}.json","w"),indent=1)
        for x in rep: print(slug,*x,sep=" | ")
