# ---------------- Lesson kit: shared builders for every lesson after Lipids ----------------
# exec'd from curriculum.py after lipids.py (shares figure_card, lesson_page, pn, box, edge, LIPID_JS, _png_size, _html, OUT, GEN, ZOOM).
# Each lesson lives in gen/lessons/<slug>.py and calls build_lesson(); its molecules come from /workspace/nutrition/lessons/<slug>_mols.py
# (images in curriculum/img/<slug>/, sizes + label anchors in gen/data/<slug>-mols.json), its script from
# /workspace/nutrition/lessons/<slug>_script.py (gen/scripts/<slug>.json). One molecule scale per page: --lb = 100cqw/17.5, 72 px per bond source.
import re as _re
def fsub(t):
    """chemical formula -> HTML subscripts (C6H12O6 -> C<sub>6</sub>H<sub>12</sub>O<sub>6</sub>); charges ^2+ -> superscript"""
    t=_re.sub(r'\^(\d*[+-])',r'<sup>\1</sup>',t)
    return _re.sub(r'(?<=[A-Za-z\)\]])(\d+)',r'<sub>\1</sub>',t)
_MASKS={}
def _auto_mark(slug,name,d,xp,yp,taken,R=0.5):
    """place a numbered marker near anchor (xp,yp in %) in the clearest nearby spot: returns (dx,dy) in bond units.
    Searches rings of offsets (0.55..2.2 bonds, 32 directions) for the first spot whose marker disc (radius R bonds) touches no atom or bond pixel."""
    import numpy as _np
    from PIL import Image as _I
    k=(slug,name)
    if k not in _MASKS:
        a=_np.asarray(_I.open(os.path.join(OUT,'img',slug,name+'.png')).convert('RGBA')).astype(int)
        _MASKS[k]=(a[...,3]>40)&(a[...,:3].min(axis=2)<235)
    M=_MASKS[k]; H,W=M.shape; ppb=W/d['units']; ax=xp/100*W; ay=yp/100*H; r=R*ppb
    yy,xx=_np.nonzero(M)
    best=None
    for dist in _np.arange(0.55,2.25,0.15):
        for t in range(32):
            th=t/32*2*_np.pi; cx=ax+dist*ppb*_np.cos(th); cy=ay+dist*ppb*_np.sin(th)
            if not(r*0.6<=cx<=W-r*0.6 and r*0.6<=cy<=H-r*0.6): continue
            if any((cx-tx)**2+(cy-ty)**2<(2.2*r)**2 for tx,ty in taken): continue
            dd=_np.min((xx-cx)**2+(yy-cy)**2) if len(xx) else 1e9
            sc=dd**0.5-r
            if sc>=0: return (cx-ax)/ppb,(cy-ay)/ppb
            if best is None or sc>best[0]: best=(sc,cx,cy)
    _,cx,cy=best; return (cx-ax)/ppb,(cy-ay)/ppb
def mk_lmol(slug):
    D=json.load(open(os.path.join(GEN,'data',slug+'-mols.json'),encoding='utf-8'))
    def lm(name,alt,marks=(),cap='',cls='',part=None,eager=False):
        d=D[name]; lm.used.add(name); w,h=_png_size(os.path.join(OUT,'img',slug,name+'.png')); mk=''
        _tk=[]
        for key,txt,dx,dy,*kind in marks:
            x,y=d['anchors'][key] if isinstance(key,str) else key
            if dx is None: dx,dy=_auto_mark(slug,name,d,x,y,taken=_tk)
            x+=dx/d['units']*100; y+=dy/d['hunits']*100
            _tk.append((x/100*w,y/100*h))
            mk+=f'<span class="mk{(" "+kind[0]) if kind else ""}" style="left:{x:.1f}%;top:{y:.1f}%">{txt}</span>'
        capt=_html.escape(_re.sub('<[^>]+>','',cap or alt))
        return (f'<div class="lm{(" "+cls) if cls else ""}" style="--u:{d["units"]};--hu:{d["hunits"]}"{f' data-part="{part}"' if part else ''}>'
                f'<button type="button" class="mz lmz" data-cap="{capt}" aria-label="Enlarge: {capt}"><img src="img/{slug}/{name}.png" width="{w}" height="{h}" alt="{_html.escape(alt)}" loading="{"eager" if eager else "lazy"}" decoding="async">{ZOOM}</button>{mk}</div>')
    lm.D=D; lm.used=set(); lm.taken={}; return lm
EL_NAMES={'c':'carbon','h':'hydrogen','o':'oxygen','n':'nitrogen','p':'phosphorus','s':'sulfur','na':'sodium','cl':'chlorine','kk':'potassium','ca':'calcium','mg':'magnesium','fe':'iron','zn':'zinc','cu':'copper','i':'iodine','se':'selenium','f':'fluorine','mn':'manganese','cr':'chromium','mo':'molybdenum','co':'cobalt','ti':'titanium'}
def legend(els='c h o n',note='every molecule on this page is drawn at the same scale with every hydrogen shown · tap one to enlarge it'):
    return '<p class="rleg">'+' '.join(f'<span class="k {e}"></span>{EL_NAMES[e]}' for e in els.split())+f' · {note}</p>'
def facts(what=None,body=None,low=None,high=None,found=None):
    o=''
    for k,v in (('What it is',what),('In your body',body),('Too little',low),('Too much',high),('Found in',found)):
        if v: o+=f'<p class="mfact"><b>{k}:</b> {v}</p>'
    return o
def molbox(part,title,mols,leg=(),fx='',head=None,pair=False):
    """one white molecule panel: optional section heading, title, molecule(s), numbered legend, fact lines"""
    m=''.join(mols) if not pair else '<div class="pair">'+''.join(f'<div class="pc">{x}</div>' for x in mols)+'</div>'
    return (f'<div class="part">{head}</div>' if head else '')+f'<div class="art mols" data-part="{part}">'+(f'<p class="mt">{title}</p>' if title else '')+m+(mleg(leg) if leg else '')+fx+'</div>'
def mcell(lmhtml,label,sub=''):
    return f'<div class="mc">{lmhtml}<p class="mcl">{label}{f"<small>{sub}</small>" if sub else ""}</p></div>'
def mgrid(part,cells,title=None):
    return f'<div class="art mols" data-part="{part}">'+(f'<p class="mt">{title}</p>' if title else '')+'<div class="mgrid">'+''.join(cells)+'</div></div>'
def ftree(nodes,edges,height,aria,extra=()):
    """Family-tree chart in exactly the Fats Figure 1 style. nodes: (x,y,w,title,sub,cls,href|None); edges: (x1,y1,x2,y2) Fats-style
    vertical curves, or ('side',x_trunk,y_from,x_to,y_to) S-curves off a trunk, or ('line',x1,y1,x2,y2)."""
    T=[]
    for e in edges:
        if e[0]=='side':
            _,xt,y0,ex,y=e; T.append(f'<path class="edge" d="M{xt},{y0} C{(xt+ex)/2:.0f},{y0} {(xt+ex)/2:.0f},{y} {ex},{y}"/>')
        elif e[0]=='line': T.append(f'<path class="edge" d="M{e[1]},{e[2]} L{e[3]},{e[4]}"/>')
        else: T.append(edge(*e))
    T+=list(extra)
    for x,y,w,t,sub,cls,href in nodes:
        b=box(x,y,w,t,sub,cls)
        T.append(f'<a class="tlk" href="{href}">{b}</a>' if href else b)
    return (f'<div class="art" data-part="tree"><svg class="tree ltree" viewBox="0 0 900 {height}" role="img" aria-label="{_html.escape(aria)}">'
            '<defs><marker id="lar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0L10,5L0,10z" class="arh"/></marker></defs>'+''.join(T)+'</svg></div>')
def table(part,head,rows,title=None,cls=''):
    return (f'<section class="rsec" data-part="{part}">'+(f'<div class="part">{title}</div>' if title else '')+f'<div class="rtbl-wrap"><table class="rtbl lrt {cls}"><thead><tr>'+''.join(f'<th>{h}</th>' for h in head)+'</tr></thead><tbody>'
            +''.join('<tr>'+''.join(f'<td data-l="{h}">{v}</td>' for h,v in zip(head,r))+'</tr>' for r in rows)+'</tbody></table></div></section>')
def worth(items,note='General education, not medical advice. Facts follow mainstream sources (US Dietary Guidelines, NIH Office of Dietary Supplements, standard biochemistry and food-science texts).'):
    return '<section class="rsec qa" data-part="worth"><div class="part">Worth knowing</div>'+''.join(f'<h4>{h}</h4><p>{p}</p>' for h,p in items)+f'<p class="fnote">{note}</p></section>'
def cart(part,svg_inner,vb,aria,title=None,cap=None):
    """labelled cartoon (not to scale, not a skeletal formula): SVG with page-size text"""
    return ((f'<div class="part">{title}</div>' if title else '')+f'<div class="art cartw" data-part="{part}"><svg class="cart" viewBox="{vb}" role="img" aria-label="{_html.escape(aria)}">{svg_inner}</svg>'
            +(f'<p class="ccap">{cap}</p>' if cap else '')+'</div>')
def flow(part,title,steps,cap=None):
    """vertical flow of HTML boxes joined by arrows: steps = [(heading, text)]"""
    return ((f'<div class="part">{title}</div>' if title else '')+f'<div class="art flw" data-part="{part}"><ol class="flow">'
            +''.join(f'<li><b>{t}</b><span>{x}</span></li>' for t,x in steps)+'</ol>'+(f'<p class="ccap">{cap}</p>' if cap else '')+'</div>')
def stages(part,title,rows,cap=None):
    """stacked labelled stages: rows = [(heading, drawing_html_or_svg, text[, data-part])]; text stays page HTML"""
    return ((f'<div class="part">{title}</div>' if title else '')+f'<div class="art stg" data-part="{part}">'
            +''.join(f'<div class="sg"{f' data-part="{r[3]}"' if len(r)>3 else ''}><p class="sgh">{r[0]}</p>{r[1]}<p class="sgt">{r[2]}</p></div>' for r in rows)+(f'<p class="ccap">{cap}</p>' if cap else '')+'</div>')
def svgd(inner,vb,aria,maxw=None):
    return f'<svg class="sgd" viewBox="{vb}" role="img" aria-label="{_html.escape(aria)}"{f' style="max-width:{maxw}px"' if maxw else ''}>{inner}</svg>'
def note(part,title,html): return f'<section class="rsec qa" data-part="{part}"><div class="part">{title}</div>{html}</section>'
def lblock(part,title,items):
    """coloured label/summary boxes like Lipids Figure 1's food-label block; items: (title, text)"""
    return f'<section class="rsec qa" data-part="{part}"><div class="part">{title}</div><div class="lcls">'+''.join(f'<div class="lc lc{k%3+1}"><b>{t}</b><span>{x}</span></div>' for k,(t,x) in enumerate(items))+'</div></section>'
def reg_of(slug): return next(r for r in REG if r[0]==slug)
def prev_next(slug):
    live=[r for r in REG if r[4]]; i=[r[0] for r in live].index(slug)
    p=live[i-1] if i>0 else None; n=live[i+1] if i+1<len(live) else None
    f=lambda r:(f'Module {r[1]} · {r[3]}',r[0]+'.html') if r else None
    return f(p),f(n)
def build_lesson(slug,title,intro,LESSON,QUIZ,after_extra='',mols=None,scale=None):
    """scale = bond lengths across a molecule panel (one px-per-bond scale for the whole page); default: widest molecule used + 1.1"""
    r=reg_of(slug); P,N=prev_next(slug)
    if mols is not None and scale is None and mols.used: scale=round(max(9.0,max(mols.D[n]['units'] for n in mols.used)+1.1),2)
    if scale: after_extra=f'<style>.mols .lm{{--lb:calc(100cqw / {scale})}}.mgrid{{column-gap:calc(100cqw / {scale} * .6)}}</style>'+after_extra
    if slug in BODY_USES.LIVE: LESSON=with_uses(slug,LESSON); after_extra=after_extra+bodymap_assets()
    figs=[figure_card(i,t,h,'',sub=s) for i,(t,s,h) in enumerate(LESSON,1)]
    lq='<main class="lp-after"><section class="notes quiz" id="quiz"><h2>Quiz</h2><p class="lbl">Tap a question to see the answer</p>'+''.join(f'<details><summary>{n}. {q}</summary><p>{a}</p></details>' for n,(q,a) in enumerate(QUIZ,1))+'</section></main>'
    nx=f'<p class="fwd" data-part="nextlesson">Next lesson: <a href="{N[1]}">{N[0]}</a> →</p>' if N else ''
    after=lq+'<main class="lp-after">'+nx+'</main>'+pn(P,N)+LIPID_JS+after_extra
    lesson_page(slug,f'Module {r[1]} · {title} · {COURSE} · {UNIVERSITY_NAME}',
     f'<nav class="crumbs">{CRUMB_HOME} › Module {r[1]}</nav><h1>Module {r[1]} · {title}</h1><p>{intro}</p>'
     +(f'<p class="pnl">Previous lesson: <a href="{P[1]}">{P[0]}</a></p>' if P else ''),figs,after)
    return len(LESSON)
for _r in REG:
    if _r[4] and _r[0] not in ('macronutrients-fats','macronutrients-lipids','food-label-tree'):
        exec(open(os.path.join(GEN,'lessons',_r[0]+'.py'),encoding='utf-8').read())
