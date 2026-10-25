# Generates curriculum/index.html, the merged Module 1 · Fats lesson (macronutrients-fats.html) and the old step-by-step redirect.
# Ball-and-stick images live in curriculum/img/fats/fig-NN.png (made by /workspace/nutrition/fats_basics.py + fats_merged.py).
# The FIG list below builds the legacy SVG figures; only the tree, melting-point chart and body-fat diagram are reused.
import math, os
OUT=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','curriculum')
L=24  # bond length px
def chain(n,dbl={},start=(0,0),ang=-30.0,first=-1):
    """Skeletal zigzag. n carbons, C1 = carboxyl carbon. dbl={bond_index p: 'c'|'t'} meaning C(p)=C(p+1).
    Turn at each carbon alternates; cis double bond => same turn sign at both ends (chain bends ~60 deg)."""
    pts=[start];th=ang;last=first
    x,y=start;x+=L*math.cos(math.radians(th));y+=L*math.sin(math.radians(th));pts.append((x,y))
    for k in range(2,n):
        s=last if dbl.get(k-1)=='c' else -last
        th+=60*s;last=s
        x+=L*math.cos(math.radians(th));y+=L*math.sin(math.radians(th));pts.append((x,y))
    return pts
def draw(pts,dbl={},cls='bond',hl='dbl',cooh=True,inner=None):
    o=[]
    cx=sum(p[0] for p in pts)/len(pts);cy=sum(p[1] for p in pts)/len(pts)
    for i in range(len(pts)-1):
        (x1,y1),(x2,y2)=pts[i],pts[i+1];p=i+1
        if p in dbl:
            o.append(f'<line class="{hl}" x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}"/>')
            dx,dy=x2-x1,y2-y1;ln=math.hypot(dx,dy);nx,ny=-dy/ln,dx/ln
            # put 2nd line on the inside (toward neighbours' side)
            px=pts[i-1] if i>0 else pts[i+2];mx,my=(px[0]+pts[min(i+2,len(pts)-1)][0])/2,(px[1]+pts[min(i+2,len(pts)-1)][1])/2
            if (mx-x1)*nx+(my-y1)*ny<0: nx,ny=-nx,-ny
            a,b=0.2,0.8;off=6
            o.append(f'<line class="{hl}" x1="{x1+dx*a+nx*off:.1f}" y1="{y1+dy*a+ny*off:.1f}" x2="{x1+dx*b+nx*off:.1f}" y2="{y1+dy*b+ny*off:.1f}"/>')
        else: o.append(f'<line class="{cls}" x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}"/>')
    if cooh:
        (x1,y1),(x2,y2)=pts[0],pts[1];th=math.atan2(y2-y1,x2-x1)
        for d,lab in((120,'O'),(-120,'OH')):
            a=th+math.radians(d);ex,ey=x1+L*math.cos(a),y1+L*math.sin(a)
            o.append(f'<line class="bond" x1="{x1:.1f}" y1="{y1:.1f}" x2="{x1+(ex-x1)*.62:.1f}" y2="{y1+(ey-y1)*.62:.1f}"/>')
            if lab=='O':
                nx,ny=-math.sin(a)*4,math.cos(a)*4
                o.append(f'<line class="bond" x1="{x1+nx:.1f}" y1="{y1+ny:.1f}" x2="{x1+(ex-x1)*.62+nx:.1f}" y2="{y1+(ey-y1)*.62+ny:.1f}"/>')
            o.append(f'<text class="atom" x="{ex:.1f}" y="{ey+5:.1f}" text-anchor="middle">{lab}</text>')
    return o
def bbox(pts,pad=40):
    xs=[p[0] for p in pts];ys=[p[1] for p in pts]
    return min(xs)-pad,min(ys)-pad,max(xs)-min(xs)+2*pad,max(ys)-min(ys)+2*pad
def label(p,t,dx=0,dy=-14,cls='lab'):
    return f'<text class="{cls}" x="{p[0]+dx:.1f}" y="{p[1]+dy:.1f}" text-anchor="middle">{t}</text>'
def dot(p,cls='hot'): return f'<circle class="{cls}" cx="{p[0]:.1f}" cy="{p[1]:.1f}" r="4"/>'
def svg(body,vb,aria): x,y,w,h=vb;return f'<svg viewBox="{x:.0f} {y:.0f} {w:.0f} {h:.0f}" role="img" aria-label="{aria}">'+''.join(body)+'</svg>'
def out(pts,i,d=20):
    if i==len(pts)-1: a,b=pts[-2],pts[-1];vx,vy=b[0]-a[0],b[1]-a[1]
    else: a,b,c=pts[i-1],pts[i],pts[i+1];vx,vy=b[0]-(a[0]+c[0])/2,b[1]-(a[1]+c[1])/2
    ln=math.hypot(vx,vy) or 1;return pts[i][0]+vx/ln*d,pts[i][1]+vy/ln*d+5
def fatty(n,dbl,aria,omega=None,start_ang=-30,extra=[]):
    pts=chain(n,dbl,ang=start_ang);b=draw(pts,dbl)
    x,y=pts[0];b.append(f'<text class="lab" x="{x-30:.1f}" y="{y+58:.1f}" text-anchor="middle">carboxyl end (C1)</text>')
    x,y=out(pts,n-1,30);b.append(f'<text class="lab" x="{x:.1f}" y="{y:.1f}" text-anchor="middle">ω end</text>')
    if omega:
        for k in (range(1,omega+1) if omega<=6 else (1,omega)):
            i=n-k;x,y=out(pts,i,16 if k<omega else 20)
            if k==omega: b+=[dot(pts[i]),f'<text class="lab hotl" x="{x:.1f}" y="{y:.1f}" text-anchor="middle">ω{k}</text>']
            elif k==1: b.append(f'<text class="num" x="{out(pts,i,14)[0]:.1f}" y="{out(pts,i,14)[1]+12:.1f}" text-anchor="middle">ω1</text>')
            else: b.append(f'<text class="num" x="{x:.1f}" y="{y:.1f}" text-anchor="middle">ω{k}</text>')
    b+=extra
    allp=pts+[(pts[0][0]-80,pts[0][1]+60),(out(pts,n-1,60)[0],out(pts,n-1,60)[1])]
    return svg(b,bbox(allp,30),aria)
FIG=[]
def fig(title,cap,body):FIG.append((title,cap,body))
# 1 tree
def box(x,y,w,t,sub='',cls='nd'):
    return f'<g class="{cls}"><rect x="{x-w/2}" y="{y-22}" width="{w}" height="{44 if not sub else 54}" rx="12"/><text x="{x}" y="{y+(0 if not sub else -4)+5}" text-anchor="middle" class="nt">{t}</text>'+(f'<text x="{x}" y="{y+18}" text-anchor="middle" class="ns">{sub}</text>' if sub else '')+'</g>'
def edge(x1,y1,x2,y2,cls='edge'):
    my=(y1+y2)/2;return f'<path class="{cls}" d="M{x1},{y1} C{x1},{my} {x2},{my} {x2},{y2}"/>'
T=[edge(450,52,170,128),edge(450,52,450,128),edge(450,52,730,128),edge(450,182,330,268),edge(450,182,600,268),edge(330,300,330,388),edge(600,300,520,388),edge(600,300,690,388),
 '<path class="edge dash" d="M545,182 C575,222 665,222 712,184" marker-end="url(#ar)"/>','<text class="lab hotl" x="668" y="238" text-anchor="middle">partial hydrogenation</text>',
 box(450,30,150,'Fats','9 kcal/g','nd root'),box(170,150,200,'Saturated','no double bonds · solid','nd s'),box(450,150,200,'Unsaturated','double bonds · liquid','nd u'),box(730,150,200,'Trans','straightened · semi-solid','nd t'),
 box(330,290,190,'Monounsaturated','1 double bond','nd u'),box(600,290,190,'Polyunsaturated','2+ double bonds','nd u'),box(330,410,160,'Omega-9','oleic · body makes it','nd u'),box(520,410,160,'Omega-3','ALA · EPA · DHA','nd u'),box(690,410,160,'Omega-6','LA · GLA · AA','nd u')]
fig('The fat family tree','Fats split into saturated, unsaturated and trans. Trans fats are mostly made from unsaturated oils by partial hydrogenation.',
 '<svg class="tree" viewBox="0 0 900 450" role="img" aria-label="Tree diagram of fat types"><defs><marker id="ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0L10,5L0,10z" class="arh"/></marker></defs>'+''.join(T)+'</svg>')
# 2 triglyceride
tb=[];gx=60;TP=[]
for i,(nm,n,d,flip) in enumerate([('linoleic (omega-6)',18,{9:'c',12:'c'},False),('palmitic (saturated)',16,{},False),('oleic (cis, omega-9)',18,{9:'c'},True)]):
    y=150+i*95
    tb.append(f'<text class="atom" x="{gx}" y="{y+5}" text-anchor="middle">{"CH₂" if i!=1 else "CH"}</text>')
    if i<2: tb.append(f'<line class="bond" x1="{gx}" y1="{y+12}" x2="{gx}" y2="{y+83}"/>')
    tb.append(f'<line class="bond" x1="{gx+20}" y1="{y}" x2="{gx+48}" y2="{y}"/><text class="atom" x="{gx+58}" y="{y+5}" text-anchor="middle">O</text><line class="bond" x1="{gx+68}" y1="{y}" x2="{gx+92}" y2="{y}"/>')
    pts=chain(n,d,start=(gx+92,y),ang=-30)
    if flip: pts=[(a,2*y-b) for a,b in pts]
    TP.extend(pts)
    # carbonyl O on C1 (pointing down-left side)
    x1,y1=pts[0];tb.append(f'<line class="bond" x1="{x1}" y1="{y1}" x2="{x1}" y2="{y1+18}"/><line class="bond" x1="{x1+4}" y1="{y1}" x2="{x1+4}" y2="{y1+18}"/><text class="atom" x="{x1+2}" y="{y1+32}" text-anchor="middle">O</text>')
    tb+=draw(pts,d,cooh=False)
    tb.append(f'<text class="lab" x="{pts[-1][0]+12:.0f}" y="{pts[-1][1]+5:.0f}">{nm}</text>')
tb.append(f'<rect class="glyc" x="{gx-30}" y="128" width="60" height="232" rx="10"/><text class="lab hotl" x="{gx}" y="386" text-anchor="middle">glycerol</text><text class="lab" x="20" y="{max(p[1] for p in TP)+30:.0f}">3 fatty-acid chains attached by ester (–O–C=O) links</text>')
fig('A fat molecule: the triglyceride','One glycerol backbone holds three fatty-acid chains. Food fats and body fat are mostly triglycerides.',svg(tb,(0,min(p[1] for p in TP)-20,760,max(max(p[1] for p in TP)+50,500)-min(p[1] for p in TP)+20),'Triglyceride: glycerol plus three fatty acids'))
# 3 stearic
fig('Saturated: stearic acid (C18:0)','No double bonds, so the zigzag chain stays straight. Straight chains pack tightly, making fat solid (stearic acid melts at about 69 °C).',fatty(18,{},'Stearic acid skeletal formula'))
# 4 oleic
fig('Monounsaturated: oleic acid (C18:1 cis-9)','One cis double bond (highlighted) puts a kink in the chain. Oleic acid melts at about 13 °C, so olive oil is liquid.',fatty(18,{9:'c'},'Oleic acid skeletal formula',omega=9))
# 5 packing
pk=[]
for i in range(6):
    p=chain(12,{},start=(40,40+i*16),ang=-30);pk+=draw(p,{},cooh=False)
import random;random.seed(4)
spots=[(430,55,-10),(545,70,25),(650,50,-30),(440,165,35),(555,150,-20),(655,170,10)]
for x,y,r in spots:
    p=chain(10,{5:'c'},start=(0,0),ang=-30);cx=sum(a for a,_ in p)/len(p);cy=sum(b for _,b in p)/len(p)
    pk.append(f'<g transform="translate({x},{y}) rotate({r}) scale(.72) translate({-cx:.1f},{-cy:.1f})">'+''.join(draw(p,{5:'c'},cooh=False))+'</g>')
pk.append('<text class="nt" x="170" y="225" text-anchor="middle">Straight chains stack tight</text><text class="lab" x="170" y="248" text-anchor="middle">→ SOLID (butter, lard, cocoa butter)</text>')
pk.append('<text class="nt" x="520" y="245" text-anchor="middle">Kinked chains can\'t stack</text><text class="lab" x="520" y="268" text-anchor="middle">→ LIQUID (olive, canola, sunflower oil)</text><line class="edge" x1="345" y1="10" x2="345" y2="270"/>')
fig('Why shape decides solid vs liquid','Straight saturated chains line up and pack closely, so the fat is solid. Kinked unsaturated chains leave gaps, so the fat is liquid.',svg(pk,(0,0,700,285),'Packing of straight versus kinked chains'))
# 6 ALA
fig('Omega-3: alpha-linolenic acid, ALA (C18:3)','Three cis double bonds. Counting from the methyl (ω) end, the first double bond starts at carbon 3, which makes it an omega-3.',fatty(18,{9:'c',12:'c',15:'c'},'ALA skeletal formula',omega=3))
# 7 LA
fig('Omega-6: linoleic acid, LA (C18:2)','Two cis double bonds. Counting from the ω end, the first double bond starts at carbon 6, which makes it an omega-6.',fatty(18,{9:'c',12:'c'},'Linoleic acid skeletal formula',omega=6))
# 8 cis vs trans
def ct(x,cis):
    C1=(x-30,110);C2=(x+30,110)
    o=[f'<line class="dbl" x1="{C1[0]}" y1="105" x2="{C2[0]}" y2="105"/><line class="dbl" x1="{C1[0]}" y1="115" x2="{C2[0]}" y2="115"/>']
    subs=[(C1,-1,'H' ,'up'),(C1,-1,'R','down'),(C2,1,'H' if cis else 'R','up'),(C2,1,'R' if cis else 'H','down')]
    for (cx,cy),sx,t,pos in subs:
        ex,ey=cx+sx*40,cy+(-60 if pos=='up' else 60)
        o.append(f'<line class="bond" x1="{cx}" y1="{cy}" x2="{ex-sx*8:.0f}" y2="{ey+(10 if pos=="up" else -10)}"/>')
        o.append(f'<text class="{"atom hatom" if t=="H" else "atom rgrp"}" x="{ex+sx*6}" y="{ey+(0 if pos=="up" else 12)}" text-anchor="middle">{t}</text>')
    o.append(f'<text class="atom" x="{C1[0]}" y="{C1[1]+28}" text-anchor="middle" font-size="13">C</text><text class="atom" x="{C2[0]}" y="{C2[1]+28}" text-anchor="middle" font-size="13">C</text>')
    o.append(f'<text class="nt" x="{x}" y="215" text-anchor="middle">{"CIS: H atoms on the SAME side" if cis else "TRANS: H atoms on OPPOSITE sides"}</text><text class="lab" x="{x}" y="238" text-anchor="middle">{"→ chain bends (kink)" if cis else "→ chain stays straight"}</text>')
    return o
cb=ct(170,True)+ct(530,False)+['<line class="edge" x1="350" y1="20" x2="350" y2="240"/>','<text class="lab" x="350" y="262" text-anchor="middle">R = rest of the carbon chain</text>']
fig('Close-up: cis vs trans double bond','Same atoms, different arrangement. Cis has both hydrogens on one side, so the chain bends. Trans has them on opposite sides, so the chain stays straight.',svg(cb,(0,0,700,275),'Cis versus trans double bond'))
# 9 elaidic
fig('Trans: elaidic acid (C18:1 trans-9)','It has a double bond at the same spot as oleic acid, but in the trans shape the chain stays straight. That lets it pack like saturated fat (melts at about 45 °C).',fatty(18,{9:'t'},'Elaidic acid skeletal formula',omega=9))
# 10 hydrogenation
hb=[];HP=[]
def mini(n,d,x,y,cap,sub):
    p=chain(n,d,start=(x,y),ang=-30);xs=[a for a,_ in p];shift=x-(min(xs)+max(xs))/2+x-x
    p=[(a+(x-(min(xs)+max(xs))/2),b) for a,b in p];HP.extend(p)
    return draw(p,d)+[f'<text class="nt" x="{x}" y="{y+70}" text-anchor="middle">{cap}</text><text class="lab" x="{x}" y="{y+92}" text-anchor="middle">{sub}</text>']
hb+=mini(18,{9:'c'},170,70,'Liquid oil','cis double bond (oleic)')
hb+=mini(18,{9:'t'},660,40,'PARTIAL hydrogenation','some cis bonds flip to trans (elaidic)')
hb+=mini(18,{},660,215,'FULL hydrogenation','all double bonds gone: saturated (stearic)')
hb+=['<path class="edge" d="M320,110 C380,90 420,60 455,52" marker-end="url(#ar2)"/>','<path class="edge" d="M320,130 C380,160 420,215 455,225" marker-end="url(#ar2)"/>',
 '<text class="lab hotl" x="360" y="70" text-anchor="middle">+ H₂, nickel catalyst, heat</text>',
 '<defs><marker id="ar2" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0L10,5L0,10z" class="arh"/></marker></defs>']
fig('Hydrogenation: how oils become solid fats','Adding hydrogen removes double bonds. Partial hydrogenation leaves some of them and flips some to trans; full hydrogenation makes saturated fat. Industrial trans fat is banned in the US and limited in the EU.',svg(hb,(0,min(p[1] for p in HP)-25,900,340-min(p[1] for p in HP)),'Hydrogenation diagram'))
# 11 melting points
mp=[('Stearic (saturated)',69,'s'),('Elaidic (trans)',45,'t'),('Oleic (cis, mono)',13,'u'),('Linoleic (omega-6)',-5,'u'),('ALA (omega-3)',-11,'u')]
mb=['<line class="edge" x1="330" y1="20" x2="330" y2="270"/>','<line class="edge dash" x1="430" y1="20" x2="430" y2="270"/><text class="lab hotl" x="434" y="16">room temp ≈ 20 °C</text>']
for i,(n,t,c) in enumerate(mp):
    y=40+i*48;x0=330;w=t*5
    mb.append(f'<text class="lab" x="250" y="{y+6}" text-anchor="end">{n}</text><rect class="bar {c}" x="{min(x0,x0+w)}" y="{y-14}" width="{abs(w)}" height="28" rx="6"/><text class="nt" x="{x0+w+8 if w>0 else x0+8}" y="{y+6}">{t} °C</text>')
fig('Melting points compared','Approximate melting points of the pure fatty acids. Straighter chains melt higher; every cis kink lowers the melting point.',svg(mb,(0,0,760,280),'Melting point bar chart'))
# 12 body fat
bf=['<rect class="skin" x="40" y="30" width="620" height="34" rx="8"/><text class="nt" x="350" y="53" text-anchor="middle">Skin (cooler, ~32-34 °C)</text>',
 '<rect class="fat1" x="40" y="70" width="620" height="70" rx="8"/><text class="nt" x="350" y="100" text-anchor="middle">Outer fat layer: firmer</text><text class="lab" x="350" y="124" text-anchor="middle">cooler, so the same fat is less fluid</text>',
 '<rect class="fat2" x="40" y="146" width="620" height="70" rx="8"/><text class="nt" x="350" y="176" text-anchor="middle">Deeper fat: softer</text><text class="lab" x="350" y="200" text-anchor="middle">at core body temperature (~37 °C)</text>',
 '<rect class="core" x="40" y="222" width="620" height="34" rx="8"/><text class="nt" x="350" y="245" text-anchor="middle">Muscle / organs (warm core)</text>']
fig('Body fat: mostly unsaturated triglycerides','Stored human fat is mostly triglycerides rich in oleic acid, so it stays soft at body temperature. It is firmer near the cooler skin and softer deeper in.',svg(bf,(0,0,700,270),'Body fat layers'))

PN_CSS=''
def pn(prev=None,nxt=None):
    o='<nav class="pn">'
    o+=f'<a class="pv" href="{prev[1]}"><small>← Previous lesson</small>{prev[0]}</a>' if prev else '<span style="flex:1"></span>'
    o+=f'<a class="nx" href="{nxt[1]}"><small>Next lesson →</small>{nxt[0]}</a>' if nxt else '<span style="flex:1"></span>'
    return o+'</nav>'
CSS=open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'curr.css')).read()
THEME='''<script>const setT=t=>{document.documentElement.dataset.theme=t;theme.textContent=t=='dark'?'Light':'Dark'};let st=null;try{st=localStorage.getItem('theme')}catch(e){}setT(st||(matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light'));theme.onclick=()=>{const t=document.documentElement.dataset.theme=='dark'?'light':'dark';setT(t);try{localStorage.setItem('theme',t)}catch(e){}};</script>'''
def page(title,hero,body,extra='',head=''):
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{title}</title><style>{CSS}</style>{head}</head><body>
<div class="hero"><div class="in"><button id="theme">Dark</button>{hero}</div></div>{body}{THEME}{extra}</body></html>'''


# ---------------- Lesson player (shared by every curriculum page) ----------------
# A module needs only: figure cards (figure_card) + a script JSON in gen/scripts/<module>.json.
# lesson_page() validates the script, embeds it, publishes curriculum/scripts/<module>.json and
# copies gen/player.js + gen/player.css to curriculum/assets/ (cache-busted by content hash).
import json, re, html as _html, hashlib
GEN=os.path.dirname(os.path.abspath(__file__))
SITE='https://inazipmoving-sudo.github.io/food-label-tree/'
def _asset(name):
    src=open(os.path.join(GEN,name),encoding='utf-8').read()
    os.makedirs(os.path.join(OUT,'assets'),exist_ok=True)
    open(os.path.join(OUT,'assets',name),'w',encoding='utf-8').write(src)
    return f'assets/{name}?v='+hashlib.sha1(src.encode()).hexdigest()[:10]
def slugify(t): return re.sub(r'[^a-z0-9]+','-',t.lower()).strip('-')
def load_script(module,figs_html):
    d=json.load(open(os.path.join(GEN,'scripts',module+'.json'),encoding='utf-8'))
    assert d.get('schemaVersion')==1 and d.get('module')==module, 'script: schemaVersion 1 and matching module id required'
    assert [f['fig'] for f in d['figures']]==list(range(1,len(figs_html)+1)), 'script figures must be 1..N, one per figure card'
    for f,fh in zip(d['figures'],figs_html):
        f.setdefault('anchor',f"fig-{f['fig']}")
        for k,sg in enumerate(f['segments'],1):
            assert sg['id']==f"{f['fig']}.{k}" and sg.get('seg',k)==k, f"segment id {sg['id']} out of order"
            sg['seg']=k; assert sg['text'].strip()
            if sg.get('name'):
                sg['slug']=slugify(sg['name']); assert not sg['slug'].startswith('seg-') and sg['slug']
                assert sum(1 for x in f['segments'] if x.get('name') and slugify(x['name'])==sg['slug'])==1, f"segment {sg['id']}: duplicate name in figure {f['fig']}"
            if sg.get('part'): assert f'data-part="{sg["part"]}"' in fh, f"segment {sg['id']}: no data-part={sg['part']} in figure {f['fig']}"
    return d
def _seg_li(sg):
    e=_html.escape
    tags=''
    if sg.get('box')=='body': tags+='<span class="lp-tag box">In your body</span>'
    elif sg.get('box')=='note': tags+='<span class="lp-tag box">Note</span>'
    if sg.get('verbatim'): tags+='<span class="lp-tag">Word for word</span>'
    cue=f'<span class="lp-cue">{tags}{e(sg["cue"]) if sg.get("cue") else ""}</span>' if (tags or sg.get('cue')) else ''
    q=f'<h4 class="lp-q">{e(sg["q"])}</h4>' if sg.get('q') else ''
    if sg.get('name'): q=f'<h4 class="lp-name">{e(sg["name"])}</h4>'+q
    box=f' data-box="{sg["box"]}"' if sg.get('box') else ''
    return f'<li class="lp-seg" id="seg-{sg["id"]}" data-id="{sg["id"]}"{box}{f' data-slug="{sg["slug"]}"' if sg.get('slug') else ''} tabindex="0"><span class="lp-sid">{sg["id"]}</span><div>{q}<p class="lp-tx">{e(sg["text"])}</p>{cue}</div></li>'
IC={'prevfig':'<path d="M3 2h2v12H3zM14 2v12L6 8z"/>','prevseg':'<path d="M10.5 2.5 5 8l5.5 5.5 1.2-1.2L7.4 8l4.3-4.3z"/>','nextseg':'<path d="M5.5 2.5 11 8l-5.5 5.5-1.2-1.2L8.6 8 4.3 3.7z"/>','nextfig':'<path d="M11 2h2v12h-2zM2 2v12l8-6z"/>'}
def _ib(act,label,keys):
    return f'<button type="button" class="lp-btn" data-act="{act}" aria-label="{label}" title="{label} ({keys})"><svg viewBox="0 0 16 16" aria-hidden="true">{IC[act]}</svg></button>'
CONTROLS=('<div class="lp-ctl" role="toolbar" aria-label="Lesson controls"><button type="button" class="lp-now" data-act="now" title="Show this line in the script"></button>'
 '<div class="lp-pos"><span class="lp-nowk">Now</span><span class="lp-where">1.1</span><span class="lp-nm"></span><span class="lp-of"></span></div><span class="lp-nx"></span><span class="lp-brk"></span>'
 +_ib('prevfig','Previous figure','Shift + Left')+_ib('prevseg','Previous line','Left arrow')
 +'<button type="button" class="lp-btn next" data-act="nextseg" aria-label="Next line" title="Next line (Right arrow)"><span class="lp-bl">Next</span><span class="lp-nl"></span><svg viewBox="0 0 16 16" aria-hidden="true">'+IC['nextseg']+'</svg></button>'
 +_ib('nextfig','Next figure','Shift + Right')
 +'<button type="button" class="lp-btn pz" data-act="play" aria-pressed="false" title="Pause and mark this spot (Space)"><span class="lp-pl">Pause</span></button>'
 +'<button type="button" class="lp-btn q" data-act="question" title="Stop for a question and mark this spot">Question</button></div>')
HINT='<p class="lp-hint">Nutrition reads this on your call. Tap Next as we go, or tell Nutrition the line number.</p>'
def lesson_page(module,title,hero,figs_html,after_html='',out_name=None):
    """Two-column lesson page: sticky figure left, script right, controls, then after_html (the quiz)."""
    out_name=out_name or module+'.html'
    d=load_script(module,figs_html)
    nseg=sum(len(f['segments']) for f in d['figures'])
    pub=dict(d); pub.update({'page':f'curriculum/{out_name}','pageUrl':SITE+f'curriculum/{out_name}','scriptUrl':SITE+f'curriculum/scripts/{module}.json',
        'hashFormat':'#fig-{fig}/seg-{seg}','hashAliases':'#fig-{fig}/{slug} for segments with a name','figureCount':len(d['figures']),'segmentCount':nseg})
    os.makedirs(os.path.join(OUT,'scripts'),exist_ok=True)
    open(os.path.join(OUT,'scripts',module+'.json'),'w',encoding='utf-8').write(json.dumps(pub,ensure_ascii=False,indent=1)+'\n')
    css,js=_asset('player.css'),_asset('player.js')
    idx=''.join(f'<a href="#fig-{f["fig"]}" title="{_html.escape(f["title"])}">{f["fig"]}</a>' for f in d['figures'])
    lists=''.join(f'<ol class="lp-segs" data-fig="{f["fig"]}" data-label="Figure {f["fig"]} script" aria-label="Figure {f["fig"]} script">'+''.join(_seg_li(sg) for sg in f['segments'])+'</ol>' for f in d['figures'])
    script_col=('<aside class="lp-scriptcol" aria-label="Lesson script">'+CONTROLS+HINT+'<div class="lp-scripthead"></div>'
        '<button type="button" class="lp-resume" data-act="resume" hidden>Resume where you left off<span class="lp-rs"></span></button>'
        '<p class="lp-qbanner" role="status" hidden></p>'+lists+
        '<p class="lp-keys"><kbd>→</kbd> next line · <kbd>←</kbd> previous · <kbd>Space</kbd> pause or continue · <kbd>Shift</kbd> + <kbd>←</kbd> <kbd>→</kbd> figures · click a line to jump</p><div class="lp-live lp-sr" aria-live="polite"></div></aside>')
    data=json.dumps(pub,ensure_ascii=False).replace('</','<\\/')
    body=(f'<div class="findex"><span>Figures</span>{idx}</div><div class="lp" data-player data-module="{module}"><div class="lp-figcol">{"".join(figs_html)}</div>{script_col}</div>{after_html}'
        f'<script type="application/json" id="lesson-script">{data}</script>')
    open(os.path.join(OUT,out_name),'w',encoding='utf-8').write(page(title,hero,body,f'<script src="{js}"></script>',head=f'<link rel="stylesheet" href="{css}">'))
    print(module,len(d['figures']),'figures',nseg,'segments',{f['fig']:len(f['segments']) for f in d['figures']})
    return d

# ---------------- Merged lesson: Module 1 · Fats (basic -> complex) ----------------
SUB={2:'Same kind of molecule, different packing.',6:'Counted from the tail end; only omega-9 can be made by your body.',10:'A recap of the whole module.'}  # muted subtitle under a figure title
SVG_TREE,SVG_MELT,SVG_BODY=FIG[0][2],FIG[10][2],FIG[11][2]
import struct
def _png_size(path):
    with open(path,'rb') as f: f.read(16); return struct.unpack('>II',f.read(8))
def img(fname,n,alt,part=None):
    w,h=_png_size(os.path.join(OUT,'img','fats',fname))  # width/height reserve space so #fig-N jumps land correctly
    cls=('bleed f9-narrow' if fname=='fig-09-breakdown-3.png' else 'bleed') if fname.startswith("fig-09-") else ''
    tag=f'<img{f' class="{cls}"' if cls else ''} src="img/fats/{fname}" width="{w}" height="{h}" alt="Figure {n}: {alt}"{f' data-part="{part}"' if part else ''} loading="{"eager" if n<2 else "lazy"}" decoding="async">'
    dname=fname.replace('.png','-d.png')
    if os.path.exists(os.path.join(OUT,'img','fats',dname)):  # Figure 9: desktop variant with labels drawn smaller so they match page text
        dw,dh=_png_size(os.path.join(OUT,'img','fats',dname))
        tag=f'<picture><source media="(min-width:601px)" srcset="img/fats/{dname}" width="{dw}" height="{dh}">{tag}</picture>'
    return tag
# (title, caption, art) ; art None => ball-and-stick image img/fats/fig-NN.png
LESSON=[
('The fat family tree: the map of this lesson','',SVG_TREE),
('Fats and Oils Are the Same Thing','<b>Fat vs oil</b> (top image): butter and olive oil are the same kind of molecule, made of the same elements (C, H, O). The difference is which fatty acids sit on the glycerol. Fats such as butter, lard and cocoa butter carry more saturated, straight chains; oils such as olive, canola and sunflower carry more cis double bonds, so kinked chains with slightly fewer hydrogens. That mix sets the melting point (pure tristearin melts at about 72 °C, pure triolein at about 5 °C). "Fat" or "oil" only names the state at room temperature (about 20–25 °C), not a different chemical class, and every real fat is a mix, so it is a matter of degree: coconut oil is mostly saturated and melts around 24 °C, so it is solid in a cool room and liquid in a warm one. Why the shape matters: the packing image below. Trans fats (Figure 4) are mostly man-made.<br><br><b>Packing</b> (lower image): Drawn space-filling, at true atom sizes, each fatty acid is a solid rod. Straight saturated chains stack tightly like pencils in a box, so they hold on to each other and need more heat to melt: butter, lard and cocoa butter are solid at room temperature. Trans chains are almost straight, so they pack almost as tightly as saturated ones, which is why partially hydrogenated oil turns solid. Cis kinks keep chains from packing and leave gaps, so the chains slide past each other and melt below room temperature: olive and canola oil are liquid. In real fats the chains sit on triglycerides (Figure 3), and the same rule holds.',None),
('Fats: the molecule','Almost all fat in food and in your body is a <b>triglyceride</b>: a <b>glycerol backbone</b> (3 carbons) holding <b>3 fatty acids</b>. Each fatty acid has an <b>acid head</b> and a <b>carbon tail</b>. The acid head is a carboxyl group, –COOH (a carbon double-bonded to one oxygen and single-bonded to an O–H). It reacts with one of glycerol\'s –OH groups, giving off water, to form an <b>ester link</b>, which is what holds the fatty acid on the glycerol. The tail is a zigzag of carbons (bond angle about 109.5°), numbered from the head (C1); the far end is the omega (ω) end. Only three elements: carbon makes 4 bonds, oxygen 2, hydrogen 1. Tail carbons are joined by <b>single C–C bonds</b> (one line) or <b>C=C double bonds</b> (two lines, orange); a double-bonded carbon has room for fewer hydrogens. Every fat gives 9 kcal per gram (protein and carbs give 4). This lesson draws molecules as ball-and-stick models; textbooks often use skeletal line drawings, where each corner is a carbon and the hydrogens are left out.',
 'IMG2'),
('Saturated vs unsaturated vs trans','The same 18-carbon chain three ways. <b>Saturated</b> (stearic acid, C18:0): no double bonds, so every tail carbon holds as many hydrogens as it can (two; the end carbon three) and the zigzag runs straight. It melts at about 69 °C, so stearic-rich fats like cocoa butter and beef fat are solid. <b>Unsaturated, cis</b> (oleic acid, C18:1 cis-9): a double bond between C9 and C10 takes the place of two hydrogens, which is what "unsaturated" means. Both remaining hydrogens sit on the same side, which bends the chain; it melts at about 13 °C, so olive oil is liquid. <b>Trans</b> (elaidic acid, C18:1 trans-9): the same double bond, but the hydrogens sit on opposite sides, so the chain stays nearly straight, packs like saturated fat and melts at about 45 °C. Plant oils and most natural fats are cis.',None),
('Monounsaturated vs polyunsaturated','Unsaturated fats are grouped by how many double bonds they have. <b>Monounsaturated</b> ("one"): oleic acid, C18:1, one cis double bond at C9=C10; the main fat in olive oil, and an omega-9 (Figure 6). <b>Polyunsaturated</b> ("many"): linoleic acid, C18:2, two cis double bonds at C9=C10 and C12=C13; found in sunflower, corn and other seed oils. Each extra cis kink lowers the melting point further: about 13 °C for oleic, about −5 °C for linoleic.',None),
('Omega-3, omega-6 and omega-9','Unsaturated fats are named by counting from the tail (ω) end, where ω1 is the last carbon. ALA (C18:3, three cis double bonds; flax, chia, walnuts) has its first double bond at ω3, so it is an omega-3. Linoleic acid (C18:2, two cis double bonds; sunflower, corn and other seed oils) starts at ω6, so it is an omega-6. Oleic acid (C18:1; olive oil, avocados, almonds, macadamias), the main monounsaturated fat, has its one double bond at ω9, so it is an omega-9. The lower diagram shows why your body can make omega-9 but not omega-3 or omega-6.',None),
('Hydrogenation: how oils become solid fats','Factories add hydrogen gas with a nickel catalyst and heat. Full hydrogenation removes every double bond and gives saturated fat. Partial hydrogenation stops partway: some double bonds remain and some flip from cis to trans, which is where most trans fat in food came from (Figure 4). Industrial trans fat is banned in the US and limited in the EU.',None),
('Melting points and body fat','<b>Top:</b> approximate melting points of the pure fatty acids; the dashed line is room temperature. Straighter chains (saturated, trans) melt higher, every cis kink lowers the melting point, and longer chains melt higher. <b>Bottom:</b> stored human fat is mostly triglycerides, and most of their fatty acids are unsaturated, with oleic acid the single most common, so it stays soft at body temperature (about 37 °C). Fat gets firmer as it cools, so it is firmer near the cooler skin and softer deeper in.','<div class="artstack">'+SVG_MELT.replace('<svg ','<svg data-part="melt" ',1)+SVG_BODY.replace('<svg ','<svg data-part="bodyfat" ',1)+'</div>'),
('Breaking a fat down for energy','<b>A, many kinds:</b> the glycerol backbone has 3 slots and any fatty acid can sit in any of them, so with about 20 common fatty acids there are about 8,000 possible triglycerides: tristearin (S-S-S), triolein (O-O-O) and a mixed palmitic-oleic-linoleic one are three examples, and every food fat is a mix of many. <b>B, breakdown:</b> when energy is low, adrenaline and glucagon rise and insulin falls, switching on the lipases in fat tissue (ATGL, then HSL). They cut the 3 ester links, adding water at each, to release 1 glycerol and 3 free fatty acids. Glycerol goes to the liver, which can make glucose from it; the fatty acids ride on albumin in the blood to muscle and the heart and are burned for fuel by beta-oxidation, 2 carbons at a time. In a deeper fast the liver turns some into ketones. The energy is in the C–H bonds of the chain, which is why fat gives 9 kcal per gram.','IMG2'),
('Putting It All Together','','F10'),
]
ARTIMG={9:[('fig-09-kinds-1.png','A, many kinds: tristearin, three stearic acids (S S S) on glycerol slots 1 to 3','kinds'),
           ('fig-09-kinds-2.png','triolein, three oleic acids (O O O), each with one cis kink','kinds'),
           ('fig-09-kinds-3.png','a mixed triglyceride: palmitic, oleic and linoleic (P O L), with legend','kinds'),
           ('fig-09-breakdown-1.png','B, breakdown step 1: lipases cut the 3 ester links, adding water','breakdown'),
           ('fig-09-breakdown-2.png','step 2: 1 glycerol plus 3 free fatty acids carried on albumin in the blood','breakdown'),
           ('fig-09-breakdown-3.png','step 3: where they go, glycerol to the liver, fatty acids to muscle and heart','breakdown')],
        2:[('fig-02-fatoil.png','fat vs oil: tristearin above, triolein below','fatoil'),('fig-02-packing.png','space-filling chains: saturated, trans and cis packing','packing')],
        3:[('fig-03a.png','the triglyceride molecule','molecule')]}
BODY={
4:[('Saturated fat','Part of the structure of cell membranes (in phospholipids), a dense backup fuel stored in fat tissue, and used to make some signaling lipids. The liver can also build cholesterol, the raw material for steroid hormones, from fat breakdown products. Eating a lot raises LDL ("bad") cholesterol.'),
   ('Trans fat','The body does not handle the straight trans shape like natural unsaturated fat; it packs into cell membranes much like saturated fat. It raises LDL and lowers HDL and is strongly linked to heart disease, which is why industrial trans fat is now mostly banned in the US.'),
   ('Ruminant trans fat','Eaten in much smaller amounts. At normal intakes the evidence of harm is weaker; in high-dose trials it raises LDL much like industrial trans fat.')],
5:[('Monounsaturated fat','The main fatty acids in stored body fat, your energy reserve; oleic acid is the most common. Helps keep cell membranes flexible. Diets that swap saturated fat for monounsaturated fat are linked to a better LDL/HDL cholesterol profile.'),
   ('All polyunsaturated fats','The parent omega-3 (ALA) and omega-6 (linoleic acid) are essential: the body cannot make them, so they must come from food. They are raw material for signaling molecules called eicosanoids.')],
6:[('Omega-3','Its signaling molecules tend to calm inflammation. DHA is a major structural fat in the brain and retina. ALA from plants converts only poorly to EPA and DHA, so fish or algae are the direct sources.'),
   ('Omega-6','Through arachidonic acid it makes signals for immune responses, inflammation and blood clotting. Too much omega-6 relative to omega-3 may tilt the balance toward inflammation.')]}
NOTE={4:'<b>Trans fat is mostly man-made.</b> Most trans fat in food came from partial hydrogenation of vegetable oils (Figure 7). Small natural amounts come from ruminant animals (cows, sheep, goats) and are found in dairy, beef and lamb; the main one is vaccenic acid.',
8:'<b>Evidence note:</b> It is often said the body keeps its outer fat layers slightly more unsaturated so they don\'t harden. That is well shown in pigs and other animals, but the evidence in humans is weaker.'}
QUIZ=[('How many bonds does carbon make, and how many does hydrogen make?','Carbon 4, hydrogen 1, oxygen 2 (Figure 3).'),
('What are the parts of a triglyceride, and which part of a fatty acid joins the glycerol?','A glycerol backbone plus 3 fatty acids. Each fatty acid\'s acid head (–COOH) joins glycerol through an ester link; the carbon tail sticks out (Figure 3).'),
('Are fats and oils different kinds of molecule?','No. Both are triglycerides made of C, H and O. Oils carry more cis-unsaturated, kinked chains, so they melt below room temperature; "fat" or "oil" just names the state at about 20–25 °C (Figure 2).'),
('What does "saturated" mean?','Every tail carbon holds as many hydrogens as it can, because there are no double bonds (Figure 4).'),
('Why is butter solid at room temperature while olive oil is liquid?','Butter is rich in saturated fatty acids with straight chains that pack tightly. Olive oil is mostly oleic acid, whose cis double bond kinks the chain so it can\'t pack (Figures 2 and 4).'),
('What does the "3" in omega-3 mean, and where do you start counting?','Count from the tail (ω) end, ω1 = last carbon; the first double bond starts at carbon 3 (Figure 6).'),
('Which omega-3s come straight from fish or algae?','EPA and DHA. Plant ALA converts to them only poorly (Figure 6, pink box).'),
('Why is omega-9 not essential, while omega-3 and omega-6 are?','Human desaturase enzymes can only add double bonds up to carbon 9 counted from the acid end. That is enough to turn stearic acid into oleic acid, an omega-9, so the body makes it. On an 18-carbon chain the omega-6 and omega-3 double bonds sit at carbons 12 and 15, out of reach, so linoleic acid and ALA must come from food (Figure 6, lower diagram).'),
('How is industrial trans fat made, and why does it behave like saturated fat?','By partial hydrogenation of vegetable oil, which flips some cis double bonds to trans (Figure 7). A trans double bond keeps the chain nearly straight, so it packs and solidifies like saturated fat (Figures 2 and 4).'),
('Name a natural source of trans fat.','Milk, butter, cheese, beef or lamb: vaccenic acid made by bacteria in cows, sheep and goats (Figure 4, note).'),
('Do steroid hormones come from saturated fat?','No. They are made from cholesterol, which the liver can build from fat breakdown products (Figure 4, pink box).'),
('What happens to a triglyceride when your body needs energy?','Lipases (ATGL, then HSL) cut its 3 ester links, adding water at each, into 1 glycerol and 3 free fatty acids. Glycerol goes to the liver, which can make glucose from it; the fatty acids ride on albumin to muscle and the heart to be burned for fuel, and in a deeper fast the liver turns some into ketones (Figure 9).')]
def art(i,t,a):
    if a=='F10': return F10_HTML
    if i==9:  # panel A images, then panel B heading/intro as page text, then panel B images
        A,B=ARTIMG[9][:3],ARTIMG[9][3:]
        return ''.join(img(fn,i,al,pt) for fn,al,pt in A)+'</div>'+F9B+'<div class="art">'+''.join(img(fn,i,al,pt) for fn,al,pt in B)
    if i in ARTIMG: return ''.join(img(fn,i,al,pt) for fn,al,pt in ARTIMG[i])
    return a if a else img(f'fig-{i:02d}.png',i,t)
QA_HTML=(img('fig-03-bonds.png',3,'meet the atoms: what is a bond','atoms')+'</div><div class="qa" data-part="qa"><h4>What is a bond?</h4><p>A bond is the attraction that holds two atoms together in a molecule. In the fats we\'re looking at, it\'s mostly carbon sharing electrons with hydrogen or with another carbon, and that sharing is what builds the chains.</p><h4>How does that work exactly?</h4><p>Atoms have electrons in shells around them, and atoms are happiest when their outer shell is full. A bond is when two atoms share a pair of those outer electrons so each one gets to count them. One shared pair is a single bond, which lets the atoms spin freely around each other. Two shared pairs is a double bond, which is shorter, stronger, and locks the atoms in place so they can\'t rotate. That\'s the whole trick behind saturated versus unsaturated fat: saturated chains are all single bonds, so they lie straight and pack tight. Unsaturated ones have double bonds that put a kink in the chain, and that\'s what keeps oils liquid.</p><p class="fnote">The kink comes from cis double bonds; trans double bonds stay nearly straight. See Figure 4.</p></div>')
F9A='<div class="qa f9h" data-part="kinds"><h4>A. Many kinds of triglyceride</h4><p>The glycerol backbone has 3 slots (1, 2, 3), and any fatty acid can sit in any slot. About 20 common fatty acids give 20 × 20 × 20 = 8,000 combinations.</p></div>'
F9B='<div class="qa f9h" data-part="breakdown"><h4>B. Breakdown and release</h4><p>Low on energy (between meals, exercise, overnight): adrenaline and glucagon rise, insulin falls, and the fat-releasing lipases switch on.</p></div>'
PRE={9:F9A,3:'<div class="part">Meet the atoms</div><div class="art">'+QA_HTML+'<div class="part">The fat molecule</div>'}
# ---------------- Figure 6 lower diagram: counting from both ends, and how far human enzymes reach ----------------
R6=json.load(open(os.path.join(GEN,'data','fig06-reach.json'),encoding='utf-8'))  # made by /workspace/nutrition/fats_omega.py
KEY_A={1,9,12,15,18}; KEY_W={1,3,6,9}
def _reach_row(name,title,status,inside):
    r=R6['rows'][name]; w,h=_png_size(os.path.join(OUT,'img','fats',r['file'])); om=r['omega']
    labs=''
    for l in r['labels']:
        ka=l['n'] in KEY_A or l['hi']; kw=l['w'] in KEY_W
        if l['n'] in (1,18): continue  # carbon 1 and carbon 18 (= ω1) are named in the end labels
        labs+=f'<span class="cn{" k" if ka else ""}{" hi" if l["hi"] else ""}" style="left:{l["a"][0]}%;top:{l["a"][1]}%">{l["n"]}</span>'
        if kw: labs+=f'<span class="cw{" k" if kw else ""}{" fam" if l["w"]==om else ""}" style="left:{l["o"][0]}%;top:{l["o"][1]}%">ω{l["w"]}</span>'
    e=r['ends']
    labs+=f'<span class="cend ca" style="left:{e["acid"][0]}%;top:{e["acid"][1]}%">acid end<br>COOH<br>carbon 1</span><span class="cend co {e["odir"]}" style="left:{e["omega"][0]}%;top:{e["omega"][1]}%">omega end<br>CH<sub>3</sub><br>carbon 18 = ω1</span>'
    return (f'<div class="rrow {"in" if inside else "out"}" data-row="{name}"><div class="rrh"><span class="rrn">{title}</span><span class="rrs">{status}</span></div>'
            f'<div class="rimg"><img src="img/fats/{r["file"]}" width="{w}" height="{h}" alt="Figure 6: {title}, carbons numbered from the acid end and from the omega end; {status}" loading="lazy" decoding="async">{labs}</div></div>')
F6_REACH=('<section class="reach" data-part="ends"><div class="part">Counting from both ends: what your enzymes can reach</div>'
 '<p class="rlead">Blue numbers count from the acid end (carbon 1 joins glycerol); grey ω numbers count from the omega end (shown at ω1, ω3, ω6 and ω9). The ringed double bond names the family.</p>'
 '<div class="zleg" data-part="reach"><span><i class="z zb"></i><b>Human enzymes reach</b> double bonds at carbon 9 or closer to the acid end (Δ9)</span><span><i class="z zg"></i><b>Plants and algae only</b> carbon 12 (Δ12) and carbon 15 (Δ15)</span></div>'
 '<div class="rrows">'
 +_reach_row('oleic','Oleic acid · omega-9','ω9 = carbon 9: inside reach, so your body makes it',True)
 +_reach_row('linoleic','Linoleic acid (LA) · omega-6','ω6 = carbon 12: out of reach, so it is essential',False)
 +_reach_row('ala','Alpha-linolenic acid (ALA) · omega-3','ω3 = carbon 15: out of reach, so it is essential',False)
 +'</div><ul class="rkey" data-part="essential">'
 '<li><b>Omega-9 is not essential.</b> Adding one double bond at carbon 9 turns stearic acid into oleic acid, and that is within reach.</li>'
 '<li><b>LA and ALA are essential.</b> Humans lack the Δ12 and Δ15 desaturases; plants, algae and some microbes have them, and animals and fish get these fats from them.</li>'
 '<li><b>Longer chains, edited at the acid end.</b> LA → arachidonic acid; ALA → EPA → DHA, but only a small share of ALA becomes EPA and even less DHA, so fish and algae (EPA and DHA ready-made) matter.</li>'
 '<li><b>No switching families.</b> The omega end is never changed, so omega-6 and omega-3 can\'t be turned into each other: you need both.</li></ul>'
 '<p class="rrule" data-part="rule">Rule of thumb: your body can edit a chain near the acid end, but not near the omega end.</p></section>')
def callout(i):
    o=''
    if i in BODY: o+='<aside class="body" data-part="body"><div class="bh">What it does in your body <span>Fig '+str(i)+'</span></div>'+''.join(f'<p><b>{t}:</b> {x}</p>' for t,x in BODY[i])+'</aside>'
    if i in NOTE: o+=f'<aside class="enote" data-part="note">{NOTE[i]}</aside>'
    if i==6: o+=F6_REACH
    return o
# ---------------- Figure 10: Putting It All Together (recap) ----------------
T10=json.load(open(os.path.join(GEN,'data','fig10-tree.json'),encoding='utf-8'))  # widths in C–C bond units, so every molecule shows at one scale
ZOOM='<svg class="zi" viewBox="0 0 16 16" aria-hidden="true"><circle cx="6.5" cy="6.5" r="4.5"/><path d="M10 10l4 4M4.5 6.5h4M6.5 4.5v4"/></svg>'
def _mol(name,label,alt):
    w,h=_png_size(os.path.join(OUT,'img','fats',f'fig-10-{name}.png'))
    return (f'<div class="rn-mol"><button type="button" class="mz" data-cap="{_html.escape(label)}" aria-label="Enlarge {_html.escape(label)}">'
            f'<img src="img/fats/fig-10-{name}.png" width="{w}" height="{h}" style="--u:{T10[name]["units"]}" alt="Figure 10: {alt}" loading="lazy" decoding="async">{ZOOM}</button></div>')
def _node(key,parent,depth,cls,part,name,defn,mol='',found=''):
    return (f'<div class="rn {cls} t-{key} d{depth}" data-node="{key}"{f' data-parent="{parent}"' if parent else ''}{f' data-part="{part}"' if part else ''}>'
            f'<div class="rn-h"><span class="rn-k">{name}</span><span class="rn-d">{defn}</span></div>{mol}{f'<p class="rn-f"><b>e.g.</b> {found}</p>' if found else ''}</div>')
F10_TREE=('<div class="part">The whole family, molecule by molecule</div><div class="ft" data-part="tree"><svg class="tlines" aria-hidden="true"></svg><div class="tgrid">'
 +_node('root','',0,'rn-root','family','Fats: the triglyceride','Glycerol holding 3 fatty acids. 9 kcal per gram.',
   _mol('triglyceride','Triglyceride: palmitic, oleic and linoleic acid on glycerol (C55H100O6)','a triglyceride: glycerol (purple box) holding palmitic, oleic and linoleic acid by ester links (red), every hydrogen shown'),
   'every food fat and oil is a mix of many')
 +_node('sat','root',1,'rn-s','sat','Saturated','No double bonds: a straight chain.',
   _mol('stearic','Stearic acid, C18:0 (C18H36O2): straight, melts at about 69 °C','stearic acid, a straight saturated chain of 18 carbons, every hydrogen shown'),
   'butter, cheese, beef fat, coconut')
 +_node('unsat','root',1,'rn-u rn-g','unsat','Unsaturated','One or more cis double bonds: kinked.')
 +_node('mono','unsat',2,'rn-u rn-g','','Monounsaturated','One double bond; mostly omega&#8209;9.')
 +_node('o9','mono',3,'rn-u','','Omega-9','First double bond at ω9. Your body makes it.',
   _mol('oleic','Oleic acid, omega-9, C18:1 cis-9 (C18H34O2): one kink, melts at about 13 °C','oleic acid, an omega-9: 18 carbons with one cis double bond (orange) at C9=C10 that kinks the chain'),
   'olive oil, avocado, almonds, macadamias')
 +_node('poly','unsat',2,'rn-u rn-g','','Polyunsaturated','Two or more double bonds.')
 +_node('o3','poly',3,'rn-u','','Omega-3','First double bond at ω3. Essential.',
   _mol('ala','Alpha-linolenic acid (ALA), omega-3, C18:3 (C18H30O2): three kinks','alpha-linolenic acid, ALA, 18 carbons with three cis double bonds (orange), the first at omega-3'),
   'flax, chia, walnuts; EPA and DHA from oily fish, algae')
 +_node('o6','poly',3,'rn-u','','Omega-6','First double bond at ω6. Essential.',
   _mol('linoleic','Linoleic acid (LA), omega-6, C18:2 (C18H32O2): two kinks, melts at about −5 °C','linoleic acid, LA, 18 carbons with two cis double bonds (orange), the first at omega-6'),
   'sunflower and pumpkin seeds, soybeans, poultry')
 +_node('trans','root',1,'rn-t','trans','Trans','Trans double bond: stays nearly straight.',
   _mol('elaidic','Elaidic acid, C18:1 trans-9 (C18H34O2): nearly straight, melts at about 45 °C','elaidic acid, 18 carbons with one trans double bond (orange) at C9=C10; the chain stays nearly straight'),
   'partially hydrogenated oils (banned in the US); traces in dairy, beef')
 +'</div></div><p class="rleg"><span class="k c"></span>carbon <span class="k h"></span>hydrogen <span class="k o"></span>oxygen <span class="k d"></span>C=C double bond · every molecule at the same scale with every hydrogen shown · tap a molecule to enlarge it</p>'
 '<dialog class="lbx" aria-label="Molecule, full size"><button type="button" class="lbx-x" aria-label="Close">×</button><img alt=""><p class="lbx-c"></p></dialog>'
 '<script>(()=>{const ft=document.querySelector(".ft");if(!ft)return;const svg=ft.querySelector(".tlines"),G=ft.querySelector(".tgrid"),dlg=document.querySelector("dialog.lbx");'
 'function draw(){const R=ft.getBoundingClientRect(),wide=getComputedStyle(G).display==="grid";let d="";'
 'ft.querySelectorAll("[data-parent]").forEach(n=>{const p=ft.querySelector(`[data-node="${n.dataset.parent}"]`),a=p.getBoundingClientRect(),b=n.getBoundingClientRect();'
 'if(wide){const px=a.left+a.width/2-R.left,py=a.bottom-R.top,cx=b.left+b.width/2-R.left,cy=b.top-R.top,g=Math.min(30,cy-py),y0=cy-g;d+=`M${px},${py}V${y0}C${px},${y0+g/2} ${cx},${y0+g/2} ${cx},${cy}`;}'
 'else{const x=a.left-R.left+11,py=a.bottom-R.top,cy=b.top-R.top+24,cx=b.left-R.left;d+=`M${x},${py}V${cy-8}Q${x},${cy} ${x+8},${cy}H${cx}`;}});'
 'svg.setAttribute("width",R.width);svg.setAttribute("height",R.height);svg.innerHTML=`<path d="${d}"/>`;}'
 'new ResizeObserver(draw).observe(ft);addEventListener("load",draw);draw();'
 'ft.addEventListener("click",e=>{const b=e.target.closest(".mz");if(!b||!dlg)return;const i=b.querySelector("img");dlg.querySelector("img").src=i.src;dlg.querySelector("img").alt=i.alt;dlg.querySelector(".lbx-c").textContent=b.dataset.cap;dlg.showModal();});'
 'if(dlg){dlg.addEventListener("click",()=>dlg.close());dlg.addEventListener("keydown",e=>{if(e.key!=="Escape")e.stopPropagation()});}})();</script>')
RECAP=[(2,'Fats and oils are the same thing','Both are triglycerides made of C, H and O. Straight saturated chains pack tightly and are solid at room temperature; cis-kinked chains can\'t pack and stay liquid.'),
(3,'The molecule','A glycerol backbone holds 3 fatty acids by ester links. Carbon makes 4 bonds, oxygen 2, hydrogen 1. A bond is a shared pair of electrons; a double bond is shorter, stronger and can\'t rotate.'),
(4,'Saturated, cis and trans','Saturated: no double bonds, straight. Cis: hydrogens on the same side, so the chain kinks. Trans: opposite sides, so it stays nearly straight and packs like saturated fat.'),
(5,'Mono vs poly','Monounsaturated has one double bond (oleic acid, olive oil); polyunsaturated has two or more (linoleic acid, seed oils). Each cis kink lowers the melting point.'),
(6,'Omega-3, omega-6 and omega-9','Omega numbers count from the tail end. Your enzymes only add double bonds near the acid end, so you make omega-9 (oleic acid) but ALA (omega-3) and linoleic acid (omega-6) are essential; EPA and DHA come directly from fish or algae.'),
(7,'Hydrogenation','Adding hydrogen removes double bonds. Full hydrogenation gives saturated fat; partial hydrogenation flips some cis bonds to trans, the source of most trans fat in food.'),
(8,'Melting points and body fat','Straighter and longer chains melt higher. Body fat is mostly unsaturated triglycerides, oleic acid most of all, so it stays soft at body temperature.'),
(9,'Breaking a fat down for energy','Lipases (ATGL, then HSL) cut the 3 ester links. Glycerol goes to the liver, which can make glucose; fatty acids ride on albumin to muscle and the heart and are burned by beta-oxidation, 2 carbons at a time. In a deeper fast the liver makes ketones. The energy is in the C–H bonds.')]
F10_RECAP=('<section class="rsec" data-part="recap"><div class="part">Recap, figure by figure</div><ol class="recap">'+''.join(f'<li><a class="rfig" href="#fig-{n}">Figure {n}</a><div><b>{t}.</b> {x}</div></li>' for n,t,x in RECAP)+'</ol></section>')
TBL=[('Saturated','0','straight','solid','butter, cheese, beef, lamb, coconut','Raises LDL; US and WHO guidelines advise under 10% of daily calories.'),
('Monounsaturated (omega-9)','1 (cis), at ω9','one kink','liquid','olives, avocados, almonds, macadamias','Not essential: your body makes oleic acid. Linked to better cholesterol levels when it replaces saturated fat.'),
('Omega-3 (poly)','2 or more (cis), first at ω3','several kinks','liquid','flax, chia, walnuts, oily fish','ALA is essential; oily fish about twice a week is a common recommendation.'),
('Omega-6 (poly)','2 or more (cis), first at ω6','several kinks','liquid','sunflower and pumpkin seeds, walnuts, soybeans','Linoleic acid is essential; replacing saturated fat with it lowers LDL.'),
('Trans','1 or more (trans)','nearly straight','solid or semi-solid','small natural amounts in dairy, beef, lamb','Raises LDL and lowers HDL; industrial trans fat is banned in the US.')]
TH=['Type','C=C double bonds','Chain shape','At room temperature','Whole-food examples','Mainstream health note']
F10_EXTRA=('<section class="rsec qa" data-part="extras"><div class="part">Worth knowing</div>'
 '<h4>Energy per gram</h4><p>Fat gives about 9 kcal per gram; carbohydrate and protein about 4, and alcohol about 7. A tablespoon of oil (about 14 g) is roughly 120 kcal.</p>'
 '<h4>The fat types side by side</h4><div class="rtbl-wrap"><table class="rtbl"><thead><tr>'+''.join(f'<th>{h}</th>' for h in TH)+'</tr></thead><tbody>'
 +''.join('<tr>'+''.join(f'<td data-l="{h}">{v}</td>' for h,v in zip(TH,r))+'</tr>' for r in TBL)+'</tbody></table></div>'
 '<h4>The two essential fatty acids</h4><p>Your body can\'t make ALA (omega-3) or linoleic acid (omega-6), so they must come from food. Its enzymes only add double bonds near the acid end, up to carbon 9, which is enough to make oleic acid (omega-9) but not the omega-6 or omega-3 bonds at carbons 12 and 15 (Figure 6). It can turn ALA into EPA and DHA, but only a small fraction gets converted, so oily fish and algae are the direct sources of EPA and DHA.</p>'
 '<h4>Fat-soluble vitamins</h4><p>Vitamins A, D, E and K dissolve in fat, not water, and are absorbed along with the fat in a meal.</p>'
 '<h4>Cholesterol is a different lipid</h4><p>Cholesterol is not a triglyceride: it is a sterol, built from four fused carbon rings, with no glycerol and no fatty acids. Your liver makes most of what you need; it goes into cell membranes and is the raw material for steroid hormones, vitamin D and bile acids. In food it comes only from animal products (eggs, meat, dairy, shellfish). LDL and HDL are not kinds of cholesterol but lipoprotein particles that carry cholesterol and triglycerides in the blood.</p>'
 '<h4>Every food fat is a mix</h4><p>No food fat is just one type. Olive oil is about three-quarters monounsaturated, butter about two-thirds saturated, and coconut oil over 80% saturated; a fat is named for the type that dominates.</p>'
 '<p class="fnote">General education, not medical advice. Health notes follow mainstream guidance (US Dietary Guidelines, WHO, American Heart Association).</p></section>')
F10_HTML='<!--noart-->'+F10_TREE+F10_RECAP+F10_EXTRA
def figure_card(n,title,art_html,caption,pre='',after=''):
    """One numbered figure card. Give images/boxes a data-part="..." so script segments can point at them."""
    return (f'<figure class="fig" id="fig-{n}" data-fig="{n}"><div class="fh" data-part="head"><a class="badge" href="#fig-{n}">{n}</a><div><div class="fl">Figure {n}</div><h3>{title}</h3>{f'<p class="fsub">{SUB[n]}</p>' if n in SUB else ''}</div></div>'
            f'{pre}{art_html[12:] if art_html.startswith("<!--noart-->") else f'<div class="art">{art_html}</div>'}{f'<figcaption data-part="caption">{caption}</figcaption>' if caption else ''}{after}</figure>')
quiz='<main class="lp-after"><section class="notes quiz" id="quiz"><h2>Quiz</h2><p class="lbl">Tap a question to see the answer</p>'+''.join(f'<details><summary>{n}. {q}</summary><p>{a}</p></details>' for n,(q,a) in enumerate(QUIZ,1))+'</section></main>'
FATS_FIGS=[figure_card(i,t,art(i,t,a),c,PRE.get(i,''),callout(i)) for i,(t,c,a) in enumerate(LESSON,1)]
lesson_page('macronutrients-fats','Module 1 · Fats · Curriculum · Food Label Tree',
 '<nav class="crumbs"><a href="../">Food Label Tree</a> › <a href="./">Curriculum</a> › Module 1</nav><h1>Module 1 · Fats</h1><p>The fat family tree first, then one fat molecule broken down step by step: 10 figures covering why fats and oils are the same thing, what a fat molecule is, the kinds of fatty acid, hydrogenation and body fat, how your body breaks a fat down for energy, and finally a recap that puts it all together. The figure is on the left and the lesson script on the right; every script line has an ID like 3.2 (Figure 3, segment 2). Pink boxes show what each fat does in your body; the quiz is at the end.</p>',
 FATS_FIGS,quiz)
# Old step-by-step page -> tiny redirect (maps #step-N to the new #fig-N)
STEP2FIG={1:3,2:3,3:3,4:3,5:3,6:3,7:4,8:4,9:4,10:4,11:4,12:5,13:2,14:2,15:6,16:3}
open(os.path.join(OUT,'macronutrients-fats-basics.html'),'w').write('<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Moved: Module 1 · Fats</title><meta http-equiv="refresh" content="0; url=macronutrients-fats.html"><link rel="canonical" href="macronutrients-fats.html"><script>var m={'+','.join(f'{k}:{v}' for k,v in STEP2FIG.items())+'},s=/^#step-(\\d+)$/.exec(location.hash);location.replace("macronutrients-fats.html"+(s&&m[s[1]]?"#fig-"+m[s[1]]:""))</script></head><body><p>This lesson moved to <a href="macronutrients-fats.html">Module 1 · Fats</a>.</p></body></html>\n')
MOD=[('1','Macronutrients','','var(--c-macronutrients)',[('Fats','macronutrients-fats.html',f'{len(LESSON)} figures + script')],['Protein','Carbohydrates','Water & ethanol']),('2','Micronutrients','','var(--c-micronutrients)',[],[]),('3','Additives','','var(--c-additives)',[],[]),('4','Antinutrients','','var(--c-antinutrients)',[],[]),('5','Processing','','var(--c-processing)',[],[])]
cards=''
for n,nm,ic,c,live,soon in MOD:
    items=''.join(f'<a class="les" href="{h}">{t} <span>{k} →</span></a>' for t,h,k in live)+''.join(f'<div class="les off">{t} <span>coming soon</span></div>' for t in soon)
    if not live: items='<div class="les off">Coming soon</div>'
    cards+=f'<section class="mod" style="--a:{c}"><div class="mh"><span class="mn">{n}</span><span class="ico">{ic}</span><h2>Module {n} · {nm}</h2></div>{items}</section>'
open(os.path.join(OUT,'index.html'),'w').write(page('Curriculum · Food Label Tree','<nav class="crumbs"><a href="../">Food Label Tree</a> › Curriculum</nav><h1>Curriculum</h1><p>Lessons with numbered figures, made for teaching by phone.</p>',f'<main class="mods">{cards}</main>'))
print(len(LESSON),'figures')
