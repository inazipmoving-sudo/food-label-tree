# ---------------- Longevity course: /longevity/ (its own course index + lessons), built with the same lesson player ----------------
# exec'd from curriculum.py after Anatomy and before site_pages.py (the home catalog counts LREG).
# Lessons live in gen/lessons/<slug>.py. While they build, REG/COURSE/OUT point at this course.
# Nutrition 101 URLs are left unchanged.
LREG=[(sl,mn,mname,t,os.path.exists(os.path.join(GEN,'lessons',sl+'.py'))) for sl,mn,mname,t in [
 ('five-hundred-years','1','Five Hundred Years','Five Hundred Years of Life Expectancy'),
 ('mutation-theory','2','Mutation Theory','The Mutation Theory of Aging'),
 ('telomere-senescence','3','Telomeres','Telomeres and Replicative Senescence'),
 ('free-radical-mitochondria','4','Free Radicals','Free Radical and Mitochondrial Theories'),
 ('epigenetic-information','5','Epigenetic Information','Epigenetic Information Loss'),
 ('antagonistic-pleiotropy','6','Evolutionary Trade-offs','Antagonistic Pleiotropy and Disposable Soma'),
 ('hyperfunction','7','Hyperfunction','Hyperfunction'),
 ('inflammaging','8','Inflammaging','Inflammaging'),
 ('proteostasis','9','Proteostasis','Proteostasis Loss')]]
_save=(REG,COURSE,CRUMB_HOME,OUT,COURSE_DIR)
try:
    REG,COURSE,COURSE_DIR=LREG,'Longevity','longevity'
    CRUMB_HOME='<a href="../">Home</a> › <a href="./">'+COURSE+'</a>'
    OUT=os.path.join(GEN,'..','longevity'); os.makedirs(OUT,exist_ok=True)
    for _r in LREG:
        if _r[4]: exec(open(os.path.join(GEN,'lessons',_r[0]+'.py'),encoding='utf-8').read())
    _lm=[]
    for r in LREG:
        if not _lm or _lm[-1][0]!=r[1]: _lm.append((r[1],r[2],[]))
        _lm[-1][2].append(r)
    _lc=''
    for n,nm,rs in _lm:
        items=''.join(f'<a class="les" href="{r[0]}.html">{r[3]} <span>{len(json.load(open(os.path.join(GEN,"scripts",r[0]+".json")))["figures"])} figures + script →</span></a>' if r[4] else f'<div class="les off">{r[3]} <span>coming soon</span></div>' for r in rs)
        _lc+=f'<section class="mod" style="--a:var(--acc)"><div class="mh"><span class="mn">{n}</span><span class="ico"></span><h2>Module {n} · {nm}</h2></div>{items}</section>'
    # Reading room stays at /literature/ (gen/literature.py). Linked here so it is part of LONG 101, not a separate catalog section. Not linked from Anatomy.
    _lc+='<section class="mod" id="literature" style="--a:var(--acc)"><div class="mh"><span class="mn">§</span><span class="ico"></span><h2>Peer-Reviewed Literature</h2></div><a class="les" href="../literature/">Peer-Reviewed Literature <span>Landmark and latest papers →</span></a></section>'
    open(os.path.join(OUT,'index.html'),'w').write(page(COURSE+' · '+UNIVERSITY_NAME,'<nav class="crumbs"><a href="../">Home</a> › '+COURSE+'</nav><h1>'+COURSE+'</h1><p>Lessons with numbered figures, made for teaching by phone. How long people have lived, from population life expectancy to the biology of aging. Every figure on a chart is rounded, and should be checked against the sources named on the page before publishing. The list below is the course outline. A lesson that is not written yet is marked coming soon.</p>',f'<main class="mods">{_lc}</main>'))
    print('longevity:',[r[0] for r in LREG if r[4]])
finally:
    REG,COURSE,CRUMB_HOME,OUT,COURSE_DIR=_save
