# ---------------- Anatomy course: /anatomy/ (its own course index + lessons), built with the same lesson player ----------------
# exec'd from curriculum.py after Nutrition 101 is built and before site_pages.py (the home catalog counts AREG).
# Lessons live in gen/lessons/<slug>.py like Nutrition 101's; while they build, REG/COURSE/OUT point at this course.
# The course stands on its own: no links to or from Nutrition 101 pages.
AREG=[(sl,mn,mname,t,os.path.exists(os.path.join(GEN,'lessons',sl+'.py'))) for sl,mn,mname,t in [
 ('human-body','1','The Human Body','The Human Body')]]
_save=(REG,COURSE,CRUMB_HOME,OUT,COURSE_DIR)
REG,COURSE,COURSE_DIR=AREG,'Anatomy','anatomy'
CRUMB_HOME='<a href="../">Home</a> › <a href="./">'+COURSE+'</a>'
OUT=os.path.join(GEN,'..','anatomy'); os.makedirs(OUT,exist_ok=True)
for _r in AREG:
    if _r[4]: exec(open(os.path.join(GEN,'lessons',_r[0]+'.py'),encoding='utf-8').read())
_am=[]
for r in AREG:
    if not _am or _am[-1][0]!=r[1]: _am.append((r[1],r[2],[]))
    _am[-1][2].append(r)
_ac=''
# Module 2: interactive 3D joint models (static pages anatomy/<joint>-3d.html, listed in gen/data/joints3d.json)
JOINTS3D=json.load(open(os.path.join(GEN,'data','joints3d.json'),encoding='utf-8'))
AEXTRA=[('2','Joints',len(JOINTS3D))]
for n,nm,rs in _am:
    items=''.join(f'<a class="les" href="{r[0]}.html">{r[3]} <span>{len(json.load(open(os.path.join(GEN,"scripts",r[0]+".json")))["figures"])} figures + script →</span></a>' if r[4] else f'<div class="les off">{r[3]} <span>coming soon</span></div>' for r in rs)
    if n=='1': items+='<a class="les" href="body-3d.html">The Whole Body in 3D <span>interactive model →</span></a><p class="cdesc">Every body system from real scans: skeleton, muscles, brain and nerves, heart and vessels, lungs, digestive, urinary, glands and male reproductive organs under translucent skin. Each system has a master checkbox to hide it at once, with nested groups you can expand to toggle single structures. Systems load one at a time, skeleton first.</p>'
    _ac+=f'<section class="mod" style="--a:var(--acc)"><div class="mh"><span class="mn">{n}</span><span class="ico"></span><h2>Module {n} · {nm}</h2></div>{items}</section>'
_ac+='<section class="mod" style="--a:var(--acc)"><div class="mh"><span class="mn">2</span><span class="ico"></span><h2>Module 2 · Joints</h2></div>'+''.join(f'<a class="les" href="{j["href"]}">{j["title"]} <span>interactive model →</span></a><p class="cdesc">{j["desc"]}</p>' for j in JOINTS3D)+'</section>'
open(os.path.join(OUT,'index.html'),'w').write(page(COURSE+' · '+UNIVERSITY_NAME,'<nav class="crumbs"><a href="../">Home</a> › '+COURSE+'</nav><h1>'+COURSE+'</h1><p>Lessons with numbered figures, made for teaching by phone. The body as a marble statue you can peel back layer by layer and zoom into, then where the food you eat goes and what each nutrient does there.</p>',f'<main class="mods">{_ac}</main>'))
for _f in ('human-body.html','scripts/human-body.json'):   # briefly live as Nutrition 101 Module 6; gone from that course
    if os.path.exists(os.path.join(_save[3],_f)): os.remove(os.path.join(_save[3],_f))
print('anatomy:',[r[0] for r in AREG if r[4]])
REG,COURSE,CRUMB_HOME,OUT,COURSE_DIR=_save
