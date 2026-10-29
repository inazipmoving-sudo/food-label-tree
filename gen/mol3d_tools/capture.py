# Re-run every lesson's molecule builder in a sandbox copy of the repo, recording the molecule behind every rendered PNG.
import sys, os, shutil, pickle, hashlib, glob, subprocess, json
REAL="/workspace/nutrition/label-tree"; SB="/tmp/m3sb/label-tree"
script=sys.argv[1]; tag=sys.argv[2]
sys.path.insert(0,"/workspace/nutrition"); sys.path.insert(0,"/workspace/nutrition/lessons")
import lipids_mol as LM, numpy as np
from rdkit import Chem
REC={}
_orig=LM.render
def render(m,path,*a,**k):
    meta,pct=_orig(m,path,*a,**k)
    heavy=[i for i,x in enumerate(m.A) if x["el"]!="H"]
    rd=getattr(m,"rd",None); rds=None
    if rd is not None:
        try:
            rh=[at for at in rd.GetAtoms() if at.GetAtomicNum()>1]
            if len(rh)==len(heavy) and all(rh[k].GetSymbol()==m.A[heavy[k]]["el"] and rh[k].GetIdx()==heavy[k] for k in range(len(heavy))):
                q=Chem.Mol(rd)
                for at in q.GetAtoms(): at.SetAtomMapNum(at.GetIdx()+1 if at.GetAtomicNum()>1 else 0)
                q=Chem.RemoveHs(q) if q.GetNumAtoms()>len(heavy) else q
                rds=Chem.MolToSmiles(q)
        except Exception as e: rds=None
    REC[os.path.abspath(path)]=dict(p=[list(map(float,x["p"])) for x in m.A],el=[x["el"] for x in m.A],xy=[list(map(float,pct(np.array(x["p"])))) for x in m.A],
        z=[float(x.get("z",0)) for x in m.A],B=[tuple(map(int,b)) for b in m.B],heavy=heavy,rd=rds,smi=getattr(m,"smi",None),maps={int(k):int(v) for k,v in getattr(m,"maps",{}).items()} if isinstance(getattr(m,"maps",{}),dict) else {})
    return meta,pct
LM.render=render
import molkit; molkit.render=render; molkit.ROOT=SB
src=open(script).read().replace(REAL,SB)
g={"__name__":"__main__","__file__":script}
sys.argv=[script]
os.chdir(os.path.dirname(script))
exec(compile(src,script,"exec"),g)
pickle.dump(REC,open(f"/workspace/nutrition/mol3d_cap/{tag}.pkl","wb")); print("captured",len(REC))
