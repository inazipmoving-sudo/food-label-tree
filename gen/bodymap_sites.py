# Reusable statue embed: the Module 6 marble body with one chosen layer and numbered, highlighted sites.
# exec after bodymap_geo.py, bodymap.py and bodymap_widget.py (needs layer_svg, PARTS). Page needs bodymap_assets() once.
# body_sites(sites, layer='organs', ...) -> HTML; sites = [dict(k, name, role, at=[anchor name or (x,y), ...], hl=[data-k of parts to highlight])]
ANCH={
 'hair':(200,30),'brain':(200,56),'eyes':(191,80),'nose':(200,90),'mouth':(200,101),'tongue':(200,101),'teeth':(200,101),'thyroid':(200,138),
 'trachea':(200,150),'lung-r':(162,210),'lung-l':(240,206),'heart':(222,226),'sternum':(200,196),'armpit':(264,196),
 'liver':(166,276),'gallbladder':(183,304),'stomach':(240,290),'spleen':(256,288),'pancreas':(224,316),'small-intestine':(200,366),'colon':(156,358),
 'kidney-r':(166,310),'kidney-l':(236,318),'adrenal-r':(168,294),'adrenal-l':(234,300),'bladder':(200,422),'pelvis':(244,384),
 'shoulder':(286,180),'upper-arm':(304,250),'forearm':(342,330),'hand':(372,425),'skin-arm':(296,214),'nerve-arm':(318,292),
 'belly-fat':(222,348),'hip-fat':(262,410),'thigh':(252,480),'knee':(237,557),'shin':(238,640),'calf':(222,630),'foot':(246,730),'blood':(222,226),
 'aorta':(204,270),'femur':(246,500),'spinal-cord':(200,250),
}
SITE_LAYERS={'organs','muscles','bones','nerves','circulation','skin','route'}
def bodymap_assets():
    """the CSS, shared SVG gradients/filters and JS that every page with a statue needs, once per page"""
    return f'<link rel="stylesheet" href="{_asset("bodymap.css")}">'+BM_DEFS+f'<script src="{_asset("bodymap.js")}"></script>'
def spread(pts,D=30,it=300):
    """pin centres pushed apart until no two are closer than D viewBox units (about a pin's width at phone size), each kept as near its anchor as it can be; a leader line joins a moved pin to its anchor"""
    import math
    Q=[list(p) for p in pts]
    for _ in range(it):
        for q,p in zip(Q,pts): q[0]+=(p[0]-q[0])*.02;q[1]+=(p[1]-q[1])*.02
        moved=False
        for i in range(len(Q)):
            for j in range(i+1,len(Q)):
                dx,dy=Q[j][0]-Q[i][0],Q[j][1]-Q[i][1];d=math.hypot(dx,dy)
                if d<D:
                    # fan crowded pins out sideways (leader lines stay short and level), away from the midline
                    if abs(dx)<2: dx=(1 if (Q[j][0]>=200)==(j%2==0) else -1)*2.0
                    ux,uy=dx,dy*.35;u=math.hypot(ux,uy);k=(D-d)/2/u
                    Q[i][0]-=ux*k;Q[i][1]-=uy*k;Q[j][0]+=ux*k;Q[j][1]+=uy*k;moved=True
        for q in Q: q[0]=min(386,max(14,q[0]));q[1]=min(786,max(14,q[1]))
        if not moved: break
    return [tuple(q) for q in Q]
def body_sites(sites,layer='organs',title='',lead='',aria='',part='body-uses',uid=None):
    assert layer in SITE_LAYERS, layer
    if not uid: _BM_N[0]+=1;uid=f'bm{_BM_N[0]}'
    hl=sorted({k for s in sites for k in s.get('hl',())})
    svg=(f'<svg class="bm-svg" viewBox="0 0 400 800" role="img" aria-label="{_bh.escape(aria)}"><rect class="bm-bg" x="-400" y="-200" width="2000" height="1200"/>'
         f'<g class="bm-l" data-layer="{layer}">{layer_svg()[layer]}</g>LEADS</svg>')
    pins='';lis='';P=[]
    for n,s in enumerate(sites,1):
        for j,a in enumerate(s['at']): P.append((n,s,j,ANCH[a] if isinstance(a,str) else a))
    L=spread([q[3] for q in P]);leads=''
    for (n,s,j,(ax,ay)),(x,y) in zip(P,L):
        if abs(x-ax)+abs(y-ay)>4: leads+=f'<g data-k="{s["k"]}"><line x1="{ax}" y1="{ay}" x2="{x:.1f}" y2="{y:.1f}"/><circle cx="{ax}" cy="{ay}" r="3"/></g>'
        pins+=(f'<button type="button" class="bm-pin bm-spin" data-k="{s["k"]}"'+(f' data-part="site-{s["k"]}"' if not j else '')
               +f' style="left:{x/4:.2f}%;top:{y/8:.2f}%" aria-label="{_bh.escape(s["name"])}">{n}</button>')
    for n,s in enumerate(sites,1):
        lis+=(f'<li class="bm-part" data-k="{s["k"]}"><button type="button" class="bm-pb" data-k="{s["k"]}"><span class="bm-n">{n}</span><b>{s["name"]}</b></button>'
              f' <span class="bm-job">{s["role"]}</span></li>')
    svg=svg.replace('LEADS',f'<g class="bm-leads">{leads}</g>')
    data={'hl':{s['k']:list(s.get('hl',())) for s in sites},'all':hl}
    return (f'<div class="bm bm-sites" id="{uid}" data-part="{part}" data-layer="{layer}" data-mode="sites">'
            +'<div class="bm-stage"><div class="bm-figw"><div class="bm-fig">'+svg+f'<div class="bm-pins">{pins}</div></div></div>'
            +'<div class="bm-panel">'+(f'<p class="bm-h">{title}</p>' if title else '')+(f'<p class="bm-lead">{lead}</p>' if lead else '')+'<p class="bm-sel" aria-live="polite" hidden></p>'+f'<ol class="bm-list">{lis}</ol></div></div>'
            +f'<script type="application/json" class="bm-data">{_bj.dumps(data)}</script></div>')

# "Where [category] is used in the body" figures (data in gen/body_uses.py): (title, subtitle, html) for a lesson's figure list
import importlib.util as _ilu
_bus=_ilu.spec_from_file_location('body_uses',os.path.join(GEN,'body_uses.py')); BODY_USES=_ilu.module_from_spec(_bus); _bus.loader.exec_module(BODY_USES)
def uses_figure(slug):
    U=BODY_USES.USES[slug]
    sites=[dict(k=k,name=n,role=r,at=at,hl=hl) for k,n,r,at,hl in U['sites']]
    return (U['title'],BODY_USES.SUB,'<!--noart--><div class="art bmw">'+body_sites(sites,layer='organs',lead=U['lead'],aria=U['aria'],uid='bm-uses')+f'<p class="ccap">{BODY_USES.CAP}</p></div>')
def with_uses(slug,figs):
    """insert the body-uses figure just before the last figure ("Putting It All Together") of a lesson's figure list"""
    if slug not in BODY_USES.LIVE: return figs
    assert figs[-1][0]=='Putting It All Together', slug
    return figs[:-1]+[uses_figure(slug)]+figs[-1:]
