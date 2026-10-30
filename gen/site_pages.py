# ---------------- Home page (course catalog) and Module 5 · Food Label Tree ----------------
# exec'd at the end of gen/curriculum.py (needs page(), pn(), REG, MODS, TREE_N, COURSE, UNIVERSITY_NAME, COURSES from site.py).
ROOT=os.path.join(GEN,'..')
# --- Module 5: the Food Label Tree page, built from gen/tree_page.src.html (the tree app that used to be the site root) ---
_t=open(os.path.join(GEN,'tree_page.src.html'),encoding='utf-8').read()
_live=[r for r in REG if r[4]]; _i=[r[0] for r in _live].index('food-label-tree')
_P=(f'Module {_live[_i-1][1]} · {_live[_i-1][3]}',_live[_i-1][0]+'.html')
_N=(f'Module {_live[_i+1][1]} · {_live[_i+1][3]}',_live[_i+1][0]+'.html') if _i+1<len(_live) else None
def _sub(s,o,n):
    assert s.count(o)==1,o; return s.replace(o,n)
_t=_sub(_t,'<title>Food Label Tree</title>',f'<title>Module 5 · Food Label Tree · {COURSE} · {UNIVERSITY_NAME}</title>')
_hero=re.search(r'<nav class="topnav">.*?</nav><h1>Food Label Tree</h1><p>(.*?)</p>',_t,re.S)
_t=_t.replace(_hero.group(0),f'<div><a class="brand" href="../">{brand_html()}</a></div><nav class="crumbs">{CRUMB_HOME} › Module 5</nav><h1>Module 5 · Food Label Tree</h1><p>{_hero.group(1)}</p>'
              f'<p class="pnl">Previous lesson: <a href="{_P[1]}">{_P[0]}</a></p>')
_t=_sub(_t,'<script src="data.js"></script>','<script src="../data.js"></script>')
_t=_sub(_t,'</main>','</main>'+pn(_P,_N))
_PNCSS=('.pn{display:flex;justify-content:space-between;gap:14px;max-width:920px;margin:40px auto 60px;padding:0 24px}.pn a{flex:1;background:var(--card);border:1px solid var(--line);border-radius:6px;padding:14px 18px;text-decoration:none;font-family:var(--serif);font-size:1.25rem;font-variant-numeric:lining-nums}'
        '.pn a:hover{border-color:var(--acc)}.pn a.nx{text-align:right}.pn small{display:block;font-family:var(--sans);font-size:.64rem;text-transform:uppercase;letter-spacing:.2em;color:var(--muted);margin-bottom:2px}'
        '@media(max-width:600px){.pn{flex-direction:column;padding:0 12px}}\n')
_t=_sub(_t,'</style>',_PNCSS+BRAND_CSS+'</style>')
assert 'href="curriculum/' not in _t
open(os.path.join(OUT,'food-label-tree.html'),'w',encoding='utf-8').write(_t)
# --- Home page: course catalog, data-driven from COURSES ---
def _course_card(c):
    reg=globals()[c['reg']] if c.get('reg') else None
    nmod=c.get('modules') or len({r[1] for r in reg}); nles=c.get('lessons') or sum(1 for r in reg if r[4])
    mods=[]
    if reg:
        for r in reg:
            if not mods or mods[-1][0]!=r[1]: mods.append((r[1],r[2]))
    ml=''.join(f'<li><span>{n}</span>{nm}</li>' for n,nm in mods)
    return (f'<section class="mod course" id="{c["slug"]}" style="--a:var(--acc)"><div class="mh"><span class="mn">{c.get("code","").split(" ")[-1]}</span><span class="ico"></span>'
            f'<h2><a href="{c["href"]}">{c["title"]}</a></h2></div><p class="cdesc">{c["desc"]}</p>'
            f'<p class="cmeta">{nmod} module{'s'*(nmod!=1)} · {nles} lesson{'s'*(nles!=1)}</p>'+(f'<ol class="cmods">{ml}</ol>' if ml else '')
            +f'<a class="les" href="{c["href"]}">Open the course <span>{c["title"]} →</span></a></section>')
_cards=''.join(_course_card(c) for c in COURSES)
# Literature is part of LONG 101 (see gen/longevity.py). It is not a home-page section and not part of Anatomy.
# Old home anchors #literature and #reading must not fall through to the food-label tree.
_HOME_CSS=('<style>.hero p.tagline{margin:4px 0 0;font-family:var(--serif);font-variant:small-caps;font-size:clamp(1.05rem,2.2vw,1.25rem);letter-spacing:.12em;color:var(--muted)}.course .mn{font-variant-numeric:lining-nums}.course h2 a{text-decoration:none}.course h2 a:hover{color:var(--acc)}.cdesc{margin:10px 0 0 44px;line-height:1.6}'
           '.cmeta{margin:8px 0 0 44px;font-size:.72rem;text-transform:uppercase;letter-spacing:.18em;color:var(--muted)}'
           '.cmods{list-style:none;margin:12px 0 0 44px;padding:0;display:flex;flex-wrap:wrap;gap:8px}.cmods li{border:1px solid var(--line);border-radius:4px;padding:4px 10px;font-size:.9rem;background:var(--bg)}'
           '.cmods li span{font-family:var(--serif);font-variant-numeric:lining-nums;color:var(--acc);margin-right:6px;font-size:1.05rem}'
           '.secl{font-family:var(--serif);font-weight:500;font-size:1.5rem;margin:36px 0 10px;padding-top:18px;border-top:1px solid var(--hair);color:var(--muted)}'
           '@media(max-width:600px){.cdesc,.cmeta,.cmods{margin-left:0}}</style>')
# A hash or query that isn't a home-page anchor belongs to the old root tree page: forward it to Module 5 with the same hash/query.
_FWD=('<script>(function(){var h=location.hash.slice(1);try{h=decodeURIComponent(h)}catch(e){}'
      'if(h==="literature"||h==="reading"){location.replace("longevity/#literature");return;}'
      'if((h&&!document.getElementById(h))||location.search)location.replace("curriculum/food-label-tree.html"+location.search+location.hash)})()</script>')
_home=page(f'{UNIVERSITY_NAME} · Course Catalog',f'<nav class="crumbs">Home</nav><h1 class="site">{brand_html()}</h1>'+(f'<p class="tagline">{TAGLINE}</p>' if TAGLINE else '')+'<p>Course catalog. Choose a course to start.</p>',
           f'<main class="mods">{_cards}</main>',extra=_FWD,head=_HOME_CSS,brand=None)
open(os.path.join(ROOT,'index.html'),'w',encoding='utf-8').write(_home)
print('home:',len(COURSES),'course(s); tree page: prev',_P,'next',_N)
