# Generates curriculum/index.html and curriculum/macronutrients-fats.html (inline SVG drawn from real geometry)
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
T=[edge(450,52,200,128),edge(450,52,450,128),edge(450,52,720,128),edge(200,160,110,248),edge(200,160,300,248),edge(300,280,220,368),edge(300,280,390,368),
 '<path class="edge dash" d="M240,182 C380,250 600,250 712,184" marker-end="url(#ar)"/>','<text class="lab hotl" x="560" y="250" text-anchor="middle">partial hydrogenation</text>',
 box(450,30,150,'Fats','9 kcal/g','nd root'),box(200,150,170,'Unsaturated','double bonds · liquid','nd u'),box(450,150,170,'Saturated','no double bonds · solid','nd s'),box(720,150,170,'Trans','straightened · semi-solid','nd t'),
 box(110,270,170,'Monounsaturated','1 double bond','nd u'),box(300,270,170,'Polyunsaturated','2+ double bonds','nd u'),box(220,390,150,'Omega-3','ALA · EPA · DHA','nd u'),box(390,390,150,'Omega-6','LA · GLA · AA','nd u')]
fig('The fat family tree','Fats split into unsaturated, saturated and trans. Trans fats are mostly made from unsaturated oils by partial hydrogenation.',
 '<svg viewBox="0 0 900 430" role="img" aria-label="Tree diagram of fat types"><defs><marker id="ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0L10,5L0,10z" class="arh"/></marker></defs>'+''.join(T)+'</svg>')
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
CSS=open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'curr.css')).read()
THEME='''<script>const setT=t=>{document.documentElement.dataset.theme=t;theme.textContent=t=='dark'?'☀️ Light':'🌙 Dark'};let st=null;try{st=localStorage.getItem('theme')}catch(e){}setT(st||(matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light'));theme.onclick=()=>{const t=document.documentElement.dataset.theme=='dark'?'light':'dark';setT(t);try{localStorage.setItem('theme',t)}catch(e){}};</script>'''
def page(title,hero,body,extra=''):
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{title}</title><style>{CSS}</style></head><body>
<div class="hero"><div class="in"><button id="theme">🌙 Dark</button>{hero}</div></div>{body}{THEME}{extra}</body></html>'''
NOTES='''<section class="notes"><h2>Key facts</h2><ul>
<li><b>9 kcal per gram</b> for all fats, whether saturated, unsaturated or trans (protein and carbs give 4 kcal/g).</li>
<li><b>Melting:</b> straight chains (saturated, trans) pack tightly and are solid at room temperature. Kinked cis chains (unsaturated) are liquid. Longer chains melt higher.</li>
<li><b>Body fat</b> is mostly triglycerides, and most of its fatty acids are unsaturated, with oleic acid the single most common.</li>
<li><b>Firmer near the cooler skin, softer deeper in:</b> fat gets firmer as it cools. The body also tends to keep its outer fat layers slightly more unsaturated so they don't harden.</li></ul></section>'''
BODY={
3:[('Saturated fat','Part of the structure of cell membranes (in phospholipids), a dense backup fuel stored in fat tissue, and used to make some signaling lipids. The liver can also build cholesterol, the raw material for steroid hormones, from fat breakdown products. Eating a lot raises LDL ("bad") cholesterol.')],
4:[('Monounsaturated fat','The main fatty acids in stored body fat, your energy reserve; oleic acid is the most common. Helps keep cell membranes flexible. Diets that swap saturated fat for monounsaturated fat are linked to a better LDL/HDL cholesterol profile.')],
6:[('All polyunsaturated fats (Figures 6–7)','The parent omega-3 (ALA) and omega-6 (linoleic acid) are essential: the body cannot make them, so they must come from food. They are raw material for signaling molecules called eicosanoids.'),
   ('Omega-3','Its signaling molecules tend to calm inflammation. DHA is a major structural fat in the brain and retina. ALA from plants converts only poorly to EPA and DHA, so fish or algae are the direct sources.')],
7:[('Omega-6','Through arachidonic acid it makes signals for immune responses, inflammation and blood clotting. Too much omega-6 relative to omega-3 may tilt the balance toward inflammation.')],
9:[('Trans fat','The body does not handle the straight trans shape like natural unsaturated fat; it packs into cell membranes much like saturated fat. It raises LDL and lowers HDL and is strongly linked to heart disease, which is why industrial trans fat is now mostly banned in the US.')]}
def callout(i):
    if i not in BODY: return ''
    return '<aside class="body"><div class="bh">🫀 What it does in your body <span>Fig '+str(i)+'</span></div>'+''.join(f'<p><b>{t}:</b> {x}</p>' for t,x in BODY[i])+'</aside>'
figs=''.join(f'<figure class="fig" id="fig-{i}"><div class="fh"><a class="badge" href="#fig-{i}">{i}</a><div><div class="fl">Figure {i}</div><h3>{t}</h3></div></div><div class="art">{b}</div><figcaption>{c}</figcaption>{callout(i)}</figure>' for i,(t,c,b) in enumerate(FIG,1))
idx=''.join(f'<a href="#fig-{i}" title="{t}">{i}</a>' for i,(t,c,b) in enumerate(FIG,1))
SPY='''<script>const links=[...document.querySelectorAll('.findex a')],figs=[...document.querySelectorAll('.fig')];let cur='';function spy(){let id=figs[0].id;for(const f of figs)if(f.getBoundingClientRect().top<=window.innerHeight*0.35)id=f.id;if(innerHeight+scrollY>=document.body.scrollHeight-4&&!location.hash)id=figs[figs.length-1].id;if(id!=cur){cur=id;links.forEach(a=>a.classList.toggle('on',a.getAttribute('href')=='#'+id));const a=links.find(a=>a.classList.contains('on'));a&&a.parentNode.scrollTo({left:a.offsetLeft-a.parentNode.clientWidth/2,behavior:'smooth'})}}addEventListener('scroll',spy,{passive:true});addEventListener('hashchange',()=>setTimeout(spy,400));spy();</script>'''
open(os.path.join(OUT,'macronutrients-fats.html'),'w').write(page('Fats · Curriculum · Food Label Tree',
 '<nav class="crumbs"><a href="../">Food Label Tree</a> › <a href="./">Curriculum</a> › Module 1</nav><h1>Module 1 · Macronutrients: Fats</h1><p>Shapes, double bonds and why some fats are solid. Tell students "go to Figure N".</p>',
 f'<div class="findex"><span>Figures</span>{idx}</div><main>{figs}{NOTES}</main>',SPY))
MOD=[('1','Macronutrients','🍗','#f97316',[('Fats','macronutrients-fats.html')],['Protein','Carbohydrates','Water & ethanol']),('2','Micronutrients','💊','#8b5cf6',[],[]),('3','Additives','🧪','#ef4444',[],[]),('4','Antinutrients','🚫','#64748b',[],[]),('5','Processing','🏭','#0ea5e9',[],[])]
cards=''
for n,nm,ic,c,live,soon in MOD:
    items=''.join(f'<a class="les" href="{h}">{t} <span>{len(FIG)} figures →</span></a>' for t,h in live)+''.join(f'<div class="les off">{t} <span>coming soon</span></div>' for t in soon)
    if not live: items='<div class="les off">Coming soon</div>'
    cards+=f'<section class="mod" style="--a:{c}"><div class="mh"><span class="mn">{n}</span><span class="ico">{ic}</span><h2>Module {n} · {nm}</h2></div>{items}</section>'
open(os.path.join(OUT,'index.html'),'w').write(page('Curriculum · Food Label Tree','<nav class="crumbs"><a href="../">Food Label Tree</a> › Curriculum</nav><h1>📚 Curriculum</h1><p>Lessons with numbered figures, made for teaching by phone.</p>',f'<main class="mods">{cards}</main>'))
print(len(FIG),'figures')
