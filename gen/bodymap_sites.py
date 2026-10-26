# Reusable statue embed: the Module 6 marble body with one chosen layer and numbered, highlighted sites.
# exec after bodymap_geo.py, bodymap.py and bodymap_widget.py (needs layer_svg, PARTS). Page needs bodymap_assets() once.
# body_sites(sites, layer='organs', ...) -> HTML; sites = [dict(k, name, role, at=[anchor name or (x,y), ...], hl=[data-k of parts to highlight])]
ANCH={
 'hair':(200,30),'brain':(200,56),'eyes':(191,80),'nose':(200,90),'mouth':(200,104),'tongue':(200,104),'teeth':(200,104),'thyroid':(200,138),
 'trachea':(200,150),'lung-r':(162,210),'lung-l':(240,206),'heart':(222,226),'sternum':(200,196),'armpit':(264,196),
 'liver':(166,276),'gallbladder':(183,304),'stomach':(240,290),'spleen':(256,288),'pancreas':(224,316),'small-intestine':(200,366),'colon':(156,358),
 'kidney-r':(166,310),'kidney-l':(236,318),'adrenal-r':(168,294),'adrenal-l':(234,300),'bladder':(200,422),'pelvis':(244,384),
 'shoulder':(286,180),'upper-arm':(304,250),'forearm':(326,330),'hand':(340,420),'skin-arm':(296,214),'nerve-arm':(318,292),
 'belly-fat':(222,348),'hip-fat':(262,410),'thigh':(252,480),'knee':(237,557),'shin':(238,640),'calf':(222,630),'foot':(246,730),'blood':(222,226),
}
SITE_LAYERS={'organs','muscles','bones','nerves','circulation','skin','route'}
def bodymap_assets():
    """the CSS, shared SVG gradients/filters and JS that every page with a statue needs, once per page"""
    return f'<link rel="stylesheet" href="{_asset("bodymap.css")}">'+BM_DEFS+f'<script src="{_asset("bodymap.js")}"></script>'
def body_sites(sites,layer='organs',title='',lead='',aria='',part='body-uses'):
    assert layer in SITE_LAYERS, layer
    _BM_N[0]+=1;uid=f'bm{_BM_N[0]}'
    hl=sorted({k for s in sites for k in s.get('hl',())})
    svg=(f'<svg class="bm-svg" viewBox="0 0 400 800" role="img" aria-label="{_bh.escape(aria)}"><rect class="bm-bg" x="-400" y="-200" width="2000" height="1200"/>'
         f'<g class="bm-l" data-layer="{layer}">{layer_svg()[layer]}</g></svg>')
    pins='';lis=''
    for n,s in enumerate(sites,1):
        pts=[ANCH[a] if isinstance(a,str) else a for a in s['at']]
        for j,(x,y) in enumerate(pts):
            pins+=(f'<button type="button" class="bm-pin bm-spin" data-k="{s["k"]}"'+(f' data-part="site-{s["k"]}"' if not j else '')
                   +f' style="left:{x/4:.2f}%;top:{y/8:.2f}%" aria-label="{_bh.escape(s["name"])}">{n}</button>')
        lis+=(f'<li class="bm-part" data-k="{s["k"]}"><button type="button" class="bm-pb" data-k="{s["k"]}"><span class="bm-n">{n}</span><b>{s["name"]}</b></button>'
              f' <span class="bm-job">{s["role"]}</span></li>')
    data={'hl':{s['k']:list(s.get('hl',())) for s in sites},'all':hl}
    return (f'<div class="bm bm-sites" id="{uid}" data-part="{part}" data-layer="{layer}" data-mode="sites">'
            +'<div class="bm-stage"><div class="bm-figw"><div class="bm-fig">'+svg+f'<div class="bm-pins">{pins}</div></div></div>'
            +'<div class="bm-panel">'+(f'<p class="bm-h">{title}</p>' if title else '')+(f'<p class="bm-lead">{lead}</p>' if lead else '')+f'<ol class="bm-list">{lis}</ol></div></div>'
            +f'<script type="application/json" class="bm-data">{_bj.dumps(data)}</script></div>')
