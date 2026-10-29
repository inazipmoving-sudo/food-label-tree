import pickle,glob,os,json,numpy as np
from PIL import Image
REAL="/workspace/nutrition/label-tree/curriculum/img"
R={}
for f in glob.glob("*_mols.pkl"): R.update(pickle.load(open(f,"rb")))
byslugname={}
for p,r in R.items(): byslugname[(p.split("/")[-2],os.path.basename(p)[:-4])]=r
# images: real -> record (same slug/name, else identical pixels anywhere)
def px(p): return np.asarray(Image.open(p).convert("RGBA"))
sbimgs={k:"/tmp/m3sb/label-tree/curriculum/img/%s/%s.png"%k for k in byslugname}
out={}; stats={"same":0,"diffpx":0,"copy":0,"none":0}
cache={}
for slug in sorted(os.listdir(REAL)):
    if slug in("fats",): continue
    for f in sorted(glob.glob(f"{REAL}/{slug}/*.png")):
        n=os.path.basename(f)[:-4]; a=px(f); hit=None
        if (slug,n) in byslugname:
            b=px(sbimgs[(slug,n)]); hit=(slug,n); stats["same" if a.shape==b.shape and (a==b).all() else "diffpx"]+=1
            if not(a.shape==b.shape and (a==b).all()): print("DIFF",slug,n,a.shape,b.shape)
        else:
            for k,p in sbimgs.items():
                if k not in cache: cache[k]=px(p)
                b=cache[k]
                if b.shape==a.shape and (a==b).all(): hit=k; break
            stats["copy" if hit else "none"]+=1
            if not hit: print("NONE",slug,n)
        out[f"{slug}/{n}"]=hit and "%s/%s"%hit
print(stats); json.dump(out,open("imgmap.json","w"),indent=0)
pickle.dump(byslugname,open("all.pkl","wb"))
