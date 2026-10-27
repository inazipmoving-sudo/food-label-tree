# "Inside a cell" panel in each "Where ... is used in the body" figure (data in gen/cell_uses.py, loaded as BODY_USES.CELL).
# One marble cell (400 x 300 viewBox), every organelle a data-k part; numbered pins + an HTML list, driven by the same SiteMap JS
# as the statue (bodymap.js). All text is HTML at page size; nothing is written inside the drawing.
# exec'd after bodymap*.py and before bodymap_sites.py (needs P, cr, sp, line; spread, _bh, _bj are looked up at call time).
import math as _m
def _circ(cx,cy,r): return f'M{cx-r},{cy}a{r},{r} 0 1 0 {2*r},0a{r},{r} 0 1 0 {-2*r},0Z'
def _ellpts(cx,cy,rx,ry,rot=0,n=24,wob=0,ph=0):
    c,s=_m.cos(_m.radians(rot)),_m.sin(_m.radians(rot));o=[]
    for i in range(n):
        t=2*_m.pi*i/n;k=1+wob*_m.sin(3*t+ph)+wob*.6*_m.sin(5*t+ph*2)
        x,y=rx*k*_m.cos(t),ry*k*_m.sin(t);o.append((cx+x*c-y*s,cy+x*s+y*c))
    return o
def _g(k,inner,cls='cg'): return f'<g class="{cls}" data-k="{k}">{inner}</g>'
CELL_C=(200,152);CELL_R=(186,134)
def cell_svg():
    o=[]
    out=cr(_ellpts(*CELL_C,*CELL_R,n=28,wob=.025,ph=.7))
    # cytosol (the fill) and the cytoskeleton behind everything
    o.append(_g('cytosol',P(out,'c-cyt')))
    fil=[[(212,108),(270,70),(330,52)],[(214,170),(290,170),(372,156)],[(150,200),(110,250),(80,262)],[(130,110),(80,100),(30,128)],[(196,206),(212,262),(206,282)],[(200,96),(180,40),(150,26)]]
    o.append(_g('cyto',''.join(P(sp(f),'c-fil') for f in fil)+''.join(P(sp([(x,y),(x+14,y+6),(x+30,y+2)]),'c-fil a') for x,y in ((292,128),(60,190),(250,40)))))
    # smooth ER: branching tubes, lower left
    ser=[[(60,212),(78,204),(96,212),(112,206)],[(70,230),(88,222),(104,230),(120,224)],[(78,204),(82,190),(96,186)],[(96,212),(98,228)],[(64,246),(84,240),(100,248)]]
    o.append(_g('ser',''.join(P(sp(t),'c-tb')+P(sp(t),'c-tb-in') for t in ser)))
    # rough ER: flattened sacs curving round the right side of the nucleus, studded with ribosomes
    rer='';dots=''
    for j,r in enumerate((66,80,94)):
        a0,a1=-62+j*4,58-j*4
        top=[(165+r*_m.cos(_m.radians(a)),150+r*_m.sin(_m.radians(a))) for a in range(a0,a1+1,8)]
        bot=[(165+(r+6)*_m.cos(_m.radians(a)),150+(r+6)*_m.sin(_m.radians(a))) for a in range(a1,a0-1,-8)]
        rer+=P(cr(top+bot),'c-er')
        for a in range(a0+3,a1,7):
            rr=r+9.5;dots+=P(_circ(round(165+rr*_m.cos(_m.radians(a)),1),round(150+rr*_m.sin(_m.radians(a)),1),1.7),'c-rb')
    o.append(_g('rer',rer+dots))
    # nucleus: double envelope with pores, chromatin (DNA on histones) and a nucleolus
    env=''.join(P(sp([(165+52*_m.cos(_m.radians(a)),150+52*_m.sin(_m.radians(a))) for a in range(a0,a0+56,8)]),'c-env') for a0 in range(0,360,60))
    env+=''.join(P(sp([(165+47*_m.cos(_m.radians(a)),150+47*_m.sin(_m.radians(a))) for a in range(a0,a0+56,8)]),'c-env') for a0 in range(0,360,60))
    chrom=''.join(P(sp(pts),'c-chr') for pts in ([(138,128),(146,122),(152,132),(160,126),(168,134)],[(140,168),(150,160),(158,170),(168,162),(176,172)],[(176,122),(184,114),(190,126),(196,120)],[(186,160),(194,152),(200,162),(196,176)],[(150,148),(156,142)]))
    o.append(_g('nucleus',P(_circ(165,150,50),'c-nuc')+env+chrom+P(_circ(170,146,12),'c-nl')))
    # Golgi: stacked curved cisternae, upper right, with vesicles budding off
    gol=''
    pol=lambda r,a:(165+r*_m.cos(_m.radians(a)),150+r*_m.sin(_m.radians(a)))
    for j,r in enumerate((124,133,142,151)):
        a0,a1=-50+j*1.5,-12-j*1.5;w=3.2
        top=[pol(r-w,a) for a in range(int(a0),int(a1)+1,4)];bot=[pol(r+w,a) for a in range(int(a1),int(a0)-1,-4)]
        gol+=P(cr(top+bot),'c-er c-gos')
        for a in (a0-1.5,a1+1.5): x,y=pol(r,a);gol+=P(_circ(round(x,1),round(y,1),3.6),'c-ves')
    for r,a in ((162,-44),(166,-30),(160,-18),(114,-36),(112,-22)): x,y=pol(r,a);gol+=P(_circ(round(x,1),round(y,1),3.2),'c-ves')
    o.append(_g('golgi',gol))
    # mitochondria: outer membrane + folded inner membrane (cristae)
    def mito(cx,cy,rx,ry,rot):
        c,s=_m.cos(_m.radians(rot)),_m.sin(_m.radians(rot));T=lambda x,y:(cx+x*c-y*s,cy+x*s+y*c)
        z=[T(-rx+6+i*(2*rx-12)/9,(ry-4)*(1 if i%2 else -1)*.8) for i in range(10)]
        return P(cr(_ellpts(cx,cy,rx,ry,rot,n=20)),'c-mt')+P(cr(_ellpts(cx,cy,rx-3,ry-3,rot,n=20)),'c-mt-in')+P(line(z),'c-cr')
    o.append(_g('mito',mito(318,196,26,12,24)+mito(92,78,22,11,-28)+mito(236,256,22,10,-6)))
    # lysosomes: round sacs full of enzymes
    lys=''.join(P(_circ(x,y,r),'c-ly')+''.join(P(_circ(x+dx,y+dy,1.3),'c-lyd') for dx,dy in ((-4,-2),(3,-4),(0,3),(5,2),(-3,5))) for x,y,r in ((352,140,11),(136,250,9)))
    o.append(_g('lyso',lys))
    # peroxisome, lipid droplet, glycogen granules
    o.append(_g('perox',P(_circ(52,150,8),'c-px')+P(_circ(52,150,3.2),'c-pxc')))
    o.append(_g('droplet',P(_circ(282,246,12),'c-ld')))
    gly=''.join(P(_circ(x+dx,y+dy,1.6),'c-gl') for x,y in ((232,40),(250,52),(222,58)) for dx,dy in ((0,0),(3,2),(-3,2),(0,-3),(3,-2),(-3,-2),(0,4)))
    o.append(_g('glycogen',gly))
    # free ribosomes in the cytosol
    fr=[(256,214),(262,222),(268,214),(270,226),(254,228),(262,206),(118,200),(112,190),(60,100),(66,108),(300,160),(214,226),(220,232),(330,190)]
    o.append(_g('ribo',''.join(P(_circ(x,y,1.9),'c-rb') for x,y in fr)))
    # plasma membrane on top: a bilayer (two lines) with channel proteins and receptors set through it
    mem=P(out,'c-mem')+P(cr(_ellpts(*CELL_C,CELL_R[0]-4,CELL_R[1]-4,n=28,wob=.025,ph=.7)),'c-mem2')
    ptsO=_ellpts(*CELL_C,*CELL_R,n=28,wob=.025,ph=.7)
    for i in (2,6,11,16,20,25):
        x,y=ptsO[i];cx,cy=CELL_C;a=_m.degrees(_m.atan2(y-cy,x-cx))
        mem+=f'<g transform="translate({x:.1f},{y:.1f}) rotate({a+90:.1f})"><rect x="-5" y="-6" width="4" height="12" rx="1.6" class="c-ch"/><rect x="1" y="-6" width="4" height="12" rx="1.6" class="c-ch"/></g>'
    for i in (4,9,14,23):
        x,y=ptsO[i];cx,cy=CELL_C;a=_m.degrees(_m.atan2(y-cy,x-cx))
        mem+=f'<g transform="translate({x:.1f},{y:.1f}) rotate({a+90:.1f})"><path d="M0,4L0,-6M0,-6L-4,-12M0,-6L4,-12" class="c-rc"/></g>'
    o.append(_g('membrane',mem))
    return ''.join(o)
CANCH={'nucleus':(165,150),'nucleolus':(170,146),'ribo':(262,220),'rer':(244,112),'golgi':(282,78),'cytosol':(98,128),'mito':(318,196),'cyto':(318,60),
       'membrane':(200,20),'channel':(366,126),'lyso':(352,140),'ser':(88,214),'perox':(52,150),'droplet':(282,246),'glycogen':(236,50),'mito2':(92,78),'mito3':(236,256),
       'mem-r':(361,85),'mem-l':(25,106),'mem-b':(107,268)}
def cell_sites(sites,title='',lead='',aria='',uid='cell-uses',part='cell-uses',cap=''):
    pins='';lis='';Pp=[]
    for n,s in enumerate(sites,1):
        for j,a in enumerate(s['at']): Pp.append((n,s,j,CANCH[a] if isinstance(a,str) else a))
    L=spread([q[3] for q in Pp],D=26);leads=''
    for (n,s,j,(ax,ay)),(x,y) in zip(Pp,L):
        y=min(290,y)
        if abs(x-ax)+abs(y-ay)>4: leads+=f'<g data-k="{s["k"]}"><line x1="{ax}" y1="{ay}" x2="{x:.1f}" y2="{y:.1f}"/><circle cx="{ax}" cy="{ay}" r="2.5"/></g>'
        pins+=(f'<button type="button" class="bm-pin bm-spin" data-k="{s["k"]}"'+(f' data-part="cell-{s["k"]}"' if not j else '')
               +f' style="left:{x/4:.2f}%;top:{y/3:.2f}%" aria-label="{_bh.escape(s["name"])}">{n}</button>')
    for n,s in enumerate(sites,1):
        lis+=(f'<li class="bm-part" data-k="{s["k"]}"><button type="button" class="bm-pb" data-k="{s["k"]}"><span class="bm-n">{n}</span><b>{s["name"]}</b></button>'
              f' <span class="bm-job">{s["role"]}</span>'+'</li>')
    svg=(f'<svg class="bm-svg c-svg" viewBox="0 0 400 300" role="img" aria-label="{_bh.escape(aria)}"><defs><radialGradient id="c-cyt" cx=".42" cy=".38" r=".7"><stop offset="0" class="s1"/><stop offset="1" class="t1"/></radialGradient></defs>'
         f'<rect class="bm-bg" x="-200" y="-200" width="800" height="700"/>'
         f'<g class="c-cell">{cell_svg()}</g><g class="bm-leads">{leads}</g></svg>')
    data={'hl':{s['k']:list(s.get('hl',())) for s in sites},'all':[]}
    return (f'<div class="bm bm-sites bm-cell" id="{uid}" data-part="{part}" data-mode="sites">'
            +(f'<p class="bm-h c-h">{title}</p>' if title else '')
            +'<div class="bm-stage"><div class="bm-figw"><div class="bm-fig">'+svg+f'<div class="bm-pins">{pins}</div></div>'+(f'<p class="ccap c-cap">{cap}</p>' if cap else '')+'</div>'
            +'<div class="bm-panel">'+(f'<p class="bm-lead">{lead}</p>' if lead else '')+'<p class="bm-sel" aria-live="polite" hidden></p>'+f'<ol class="bm-list">{lis}</ol>'+'</div></div>'
            +f'<script type="application/json" class="bm-data">{_bj.dumps(data)}</script></div>')
def cell_panel(slug):
    U=BODY_USES.CELL.get(slug)
    if not U: return ''
    sites=[dict(k=k,name=n,role=r,at=at,hl=hl) for k,n,r,at,hl in U['sites']]
    return cell_sites(sites,title=BODY_USES.CELL_TITLE,lead=U['lead'],aria=U['aria'],uid='cell-uses',cap=BODY_USES.CELL_CAP)
