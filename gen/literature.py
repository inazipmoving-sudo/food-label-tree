#!/usr/bin/env python3
"""Peer-Reviewed Literature, the reading room of the Longevity course (LONG 101).
Reads gen/literature/posts.json and writes literature/index.html plus literature/<slug>.html (one-page reads).
Paths stay /literature/. This file does not import the course generators. Daily posts are still:
add an object to gen/literature/posts.json, then run python3 gen/literature.py.
Post schema (one object per paper): see /workspace/nutrition/literature/README.md.
  group: "landmark" (ordered by impactRank) or "latest" (ordered by pubDate, newest first; fed by the daily job).
"""
import json, os, html, sys
from datetime import date
GEN=os.path.dirname(os.path.abspath(__file__)); ROOT=os.path.join(GEN,'..'); OUT=os.path.join(ROOT,'literature')
_ns={}; exec(open(os.path.join(GEN,'site.py'),encoding='utf-8').read(),_ns)  # gen/site.py: brand only
UNIVERSITY_NAME,brand_html,BRAND_CSS=_ns['UNIVERSITY_NAME'],_ns['brand_html'],_ns['BRAND_CSS']
SITE='https://orcuttshortcut.com/'
E=lambda s: html.escape(str(s or ''), quote=True)
CSS=r''':root{--hdr:#E4E4E4;--bg:#F0F0F0;--hair:#CBCBCB;--card:#F7F7F5;--text:#2B2B2B;--muted:#6E6E6E;--line:#D9D8D4;--chip:#ECEBE7;--acc:#3E5C76;--acc-soft:#3E5C7614;--warn:#A86B53;--vein:.045;--serif:"Cormorant Garamond","Cormorant",Garamond,"EB Garamond",Georgia,"Times New Roman",serif;--sans:ui-sans-serif,system-ui,-apple-system,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif}
[data-theme=dark]{--hdr:#262625;--bg:#1F1F1E;--hair:#3A3936;--card:#2A2A28;--text:#E8E6E1;--muted:#A19E97;--line:#3A3936;--chip:#32322F;--acc:#8FA9C2;--acc-soft:#8FA9C21c;--warn:#C99582;--vein:.04}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--text);font-family:var(--sans);font-size:16px;line-height:1.6;-webkit-font-smoothing:antialiased;transition:background .2s,color .2s;font-variant-numeric:lining-nums}
a{color:inherit}
.hero{position:relative;background-color:var(--hdr);border-bottom:1px solid var(--hair);padding:44px 24px 40px;overflow:hidden}
.hero::before{content:"";position:absolute;inset:0;pointer-events:none;opacity:var(--vein);background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='900' height='260' viewBox='0 0 900 260'%3E%3Cg fill='none' stroke='%23000' stroke-linecap='round'%3E%3Cpath d='M-20 70 C 120 40, 210 120, 340 90 S 560 20, 700 70 S 860 140, 940 100' stroke-width='1.1'/%3E%3Cpath d='M-20 190 C 90 170, 180 210, 300 175 S 520 120, 640 160 S 820 230, 940 190' stroke-width='.8'/%3E%3Cpath d='M180 -10 C 220 60, 200 120, 260 170 S 300 250, 330 280' stroke-width='.6'/%3E%3Cpath d='M610 -10 C 590 50, 640 90, 620 150 S 660 230, 650 280' stroke-width='.5'/%3E%3C/g%3E%3C/svg%3E");background-size:900px 260px}
[data-theme=dark] .hero::before{filter:invert(1)}
.hero .in{max-width:820px;margin:auto;position:relative}
.hero h1{font-family:var(--serif);font-weight:500;font-size:clamp(1.9rem,4.6vw,2.9rem);line-height:1.12;margin:8px 0 0}
.hero p{margin:10px 0 0;color:var(--muted);max-width:680px}
#theme{position:absolute;right:0;top:0;background:transparent;border:1px solid var(--hair);color:var(--muted);border-radius:4px;padding:5px 12px;cursor:pointer;font:inherit;font-size:.72rem;text-transform:uppercase;letter-spacing:.16em}#theme:hover{color:var(--text);border-color:var(--muted)}
.crumbs{font-size:.72rem;text-transform:uppercase;letter-spacing:.18em;color:var(--muted)}.crumbs a{text-decoration:none;border-bottom:1px solid var(--hair)}.crumbs a:hover{color:var(--acc);border-color:var(--acc)}
main{max-width:820px;margin:32px auto 80px;padding:0 24px}
.lbl{font-size:.68rem;text-transform:uppercase;letter-spacing:.18em;color:var(--muted);font-weight:500}
.grp{margin:0 0 34px}.grp h2{font-family:var(--serif);font-weight:500;font-size:1.8rem;margin:0 0 4px}.grp>p{margin:0 0 14px;color:var(--muted)}
.card{display:grid;grid-template-columns:44px 1fr;gap:14px;background:var(--card);border:1px solid var(--line);border-radius:6px;padding:16px 18px;margin:0 0 12px;text-decoration:none}
.card:hover{border-color:var(--acc)}.rk{font-family:var(--serif);font-size:1.6rem;color:var(--acc);border-bottom:1px solid var(--acc);text-align:center;line-height:1.2;height:fit-content}
.card h3{margin:0;font-family:var(--serif);font-weight:600;font-size:1.25rem;line-height:1.25}
.meta{font-size:.82rem;color:var(--muted);margin:4px 0 0}.meta b{color:var(--text);font-weight:600}
.card p.w{margin:6px 0 0}
.sig{display:flex;flex-wrap:wrap;gap:6px;margin:8px 0 0}.sig span{font-size:.72rem;border:1px solid var(--line);background:var(--bg);border-radius:3px;padding:1px 8px;color:var(--muted)}
.tag{display:inline-block;font-size:.66rem;text-transform:uppercase;letter-spacing:.14em;border-radius:3px;padding:1px 7px;border:1px solid currentColor;margin-left:6px;vertical-align:2px}
.tag.oa{color:#3E7A5C}[data-theme=dark] .tag.oa{color:#7FC29B}.tag.pw{color:var(--muted)}.tag.pp{color:var(--warn)}
.empty{background:var(--card);border:1px dashed var(--line);border-radius:6px;padding:16px 18px;color:var(--muted)}
.doi{display:flex;flex-wrap:wrap;align-items:center;gap:10px 16px;margin:18px 0 0}
.doi a.btn{display:inline-block;background:var(--acc);color:var(--card);text-decoration:none;border-radius:4px;padding:9px 16px;font-weight:600;letter-spacing:.01em}.doi a.btn:hover{filter:brightness(1.1)}
.doi code{font-size:.85rem;color:var(--muted)}
.note{margin:14px 0 0;border-radius:4px;padding:10px 14px;background:var(--chip);border:1px solid var(--line);border-left:3px solid var(--muted);font-size:.95rem}
.note.pp{border-left-color:var(--warn);background:color-mix(in srgb,var(--warn) 10%,var(--card))}.note.oa{border-left-color:var(--acc)}
.one{margin:22px 0 0;padding:12px 16px;border-left:3px solid var(--acc);background:var(--acc-soft);font-family:var(--serif);font-size:1.3rem;font-weight:600;line-height:1.35}
article section{background:var(--card);border:1px solid var(--line);border-radius:6px;padding:18px 22px;margin:16px 0 0}
article h2{font-family:var(--serif);font-weight:500;font-size:1.55rem;margin:0 0 6px}
article section p{margin:6px 0 0}
dl.terms{margin:6px 0 0}dl.terms dt{font-weight:600;margin-top:10px}dl.terms dd{margin:2px 0 0 0;color:var(--text)}
.src{font-size:.9rem;color:var(--muted)}.src ul{margin:6px 0 0;padding-left:20px}.src a{color:var(--acc)}
.pn{display:flex;justify-content:space-between;gap:14px;margin:26px 0 0}.pn a{flex:1;background:var(--card);border:1px solid var(--line);border-radius:6px;padding:12px 16px;text-decoration:none;font-family:var(--serif);font-size:1.1rem;line-height:1.3}.pn a:hover{border-color:var(--acc)}.pn a.nx{text-align:right}.pn small{display:block;font-family:var(--sans);font-size:.64rem;text-transform:uppercase;letter-spacing:.2em;color:var(--muted);margin-bottom:2px}
.back{margin:14px 0 0}.back a{color:var(--acc);text-decoration:none;border-bottom:1px solid currentColor}
@media(max-width:600px){main{padding:0 12px;margin-top:20px}#theme{position:static;margin-bottom:12px}.card{grid-template-columns:1fr}.rk{width:40px}.pn{flex-direction:column}article section{padding:14px 16px}}
'''
THEME="<script>const setT=t=>{document.documentElement.dataset.theme=t;theme.textContent=t=='dark'?'Light':'Dark'};let st=null;try{st=localStorage.getItem('theme')}catch(e){}setT(st||(matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light'));theme.onclick=()=>{const t=document.documentElement.dataset.theme=='dark'?'light':'dark';setT(t);try{localStorage.setItem('theme',t)}catch(e){}};</script>"
SECTION='Peer-Reviewed Literature'
def page(title,hero,body,desc=''):
    return (f'<!doctype html><html lang="en"><head><meta charset="utf-8"><link rel="icon" href="/favicon.ico" sizes="any"><link rel="icon" type="image/png" href="/favicon-32.png"><link rel="apple-touch-icon" href="/apple-touch-icon.png"><meta name="viewport" content="width=device-width,initial-scale=1">'
            f'<title>{E(title)}</title>'+(f'<meta name="description" content="{E(desc)}">' if desc else '')+f'<style>{CSS}{BRAND_CSS}</style></head><body>'
            f'<div class="hero"><div class="in"><button id="theme">Dark</button><div><a class="brand" href="../">{brand_html()}</a></div>{hero}</div></div>{body}{THEME}</body></html>')
def fdate(s):
    try: y,m,d=[int(x) for x in str(s)[:10].split('-')]; return date(y,m,d).strftime('%-d %b %Y')
    except Exception: return E(s)
def oa_tag(p):
    if p.get('preprint') or p.get('type')=='preprint': return '<span class="tag pp">Preprint</span>'
    return '<span class="tag oa">Open access</span>' if (p.get('openAccess') or {}).get('isOpen') else '<span class="tag pw">Paywalled</span>'
def sig_chips(p):
    s=p.get('signals') or {}; c=(s.get('citations') or {}); out=[]
    if c.get('openalex') is not None: out.append(f"{c['openalex']} citations (OpenAlex)")
    if c.get('semanticScholar') is not None: out.append(f"{c['semanticScholar']} (Semantic Scholar)")
    a=(s.get('altmetric') or {}).get('score'); out.append(f'Altmetric {a}' if a is not None else 'Altmetric n/a')
    n=s.get('newsMentions'); 
    if n is not None: out.append(f'{len(n)} news/press mention'+('s' if len(n)!=1 else ''))
    return '<div class="sig">'+''.join(f'<span>{E(x)}</span>' for x in out)+'</div>'
def card(p,rank=None):
    lead=f'<span class="rk">{rank}</span>' if rank else '<span class="rk">·</span>'
    return (f'<a class="card" href="{E(p["slug"])}.html">{lead}<div><h3>{E(p["title"])}{oa_tag(p)}</h3>'
            f'<p class="meta"><b>{E(p["journal"])}</b> · {fdate(p["pubDate"])} · {E(p.get("authorsShort") or p.get("firstAuthor"))}</p>'
            f'<p class="w">{E(p["whyItMatters"])}</p>{sig_chips(p)}</div></a>')
def build():
    P=json.load(open(os.path.join(GEN,'literature','posts.json'),encoding='utf-8'))
    seen=set()
    for p in P:
        k=p['doi'].lower(); assert k not in seen, 'duplicate DOI '+k; seen.add(k)
        assert p['group'] in ('landmark','latest'), p['slug']
        for f in ('why','did','found','limits','terms'): assert p['synopsis'].get(f), (p['slug'],f)
    os.makedirs(OUT,exist_ok=True)
    land=sorted([p for p in P if p['group']=='landmark'],key=lambda p:p['impactRank'])
    late=sorted([p for p in P if p['group']=='latest'],key=lambda p:p['pubDate'],reverse=True)
    order=land+late
    hero=(f'<nav class="crumbs"><a href="../">Home</a> › <a href="../longevity/">Longevity</a> › {SECTION}</nav><h1>{SECTION}</h1>'
          '<p>Cutting-edge research on DNA and aging: DNA damage and repair, somatic mutation, epigenetic clocks, telomeres and genome instability. '
          'Each paper gets a one-page plain-language read with a link to the original. '
          'Part of the <a href="../longevity/">Longevity</a> course (LONG 101).</p>'
          '<p class="back"><a href="../longevity/">← Back to the Longevity course</a></p>')
    lg=('<section class="grp" id="latest"><h2>Latest</h2><p>New papers found by the daily literature sweep, newest first.</p>'+
        (''.join(card(p) for p in late) if late else '<div class="empty">Nothing new posted yet. The daily sweep adds new papers here.</div>')+'</section>')
    lm=('<section class="grp" id="landmark"><h2>Landmark papers of the past year</h2><p>Published 28 Oct 2025 to 28 Oct 2026, ranked by impact: citations (OpenAlex), journal, and coverage by science news and press offices. '
        'Altmetric scores were not available. <a href="#how">How these were chosen</a>.</p>'+''.join(card(p,p['impactRank']) for p in land)+'</section>')
    how=('<section class="grp" id="how"><h2>How these were chosen</h2><p>Searches of OpenAlex for papers about aging together with DNA damage, DNA repair, somatic mutation, epigenetic clocks, telomeres, genome instability, '
         'clonal hematopoiesis or mitochondrial DNA; each candidate was screened by hand for being about DNA or genome mechanisms of aging. '
         'Impact score = 2 × log2(1 + citations) + journal tier + news/press mentions (up to 3). Citation counts are as of 28 Oct 2026 and grow fast for recent papers, so the ranking favours older papers. '
         'Synopses are written from each paper\'s published abstract; they never add findings that are not in the source.</p></section>')
    open(os.path.join(OUT,'index.html'),'w',encoding='utf-8').write(page(f'{SECTION} · {UNIVERSITY_NAME}',hero,f'<main>{lm}{lg}{how}</main>',
        'Plain-language reads of landmark and new peer-reviewed papers on DNA and aging.'))
    for i,p in enumerate(order):
        s=p['synopsis']; prv=order[i-1] if i>0 else None; nxt=order[i+1] if i+1<len(order) else None
        oa=p.get('openAccess') or {}
        if p.get('preprint') or p.get('type')=='preprint':
            warn='<p class="note pp"><b>Preprint, not yet peer reviewed.</b> These results have not been checked by independent reviewers and may change.</p>'
        else: warn=''
        oan=(f'<p class="note oa"><b>Open access.</b> The full paper is free to read'+(f' (<a href="{E(oa.get("url"))}">free copy</a>)' if oa.get('url') and oa.get('url')!=p['url'] else '')+'.</p>') if oa.get('isOpen') else '<p class="note"><b>Paywalled.</b> The full paper needs a subscription; the abstract is free at the DOI link.</p>'
        basis=('This synopsis was written from the published abstract only.' if p.get('synopsisBasis','abstract')=='abstract'
               else 'This synopsis was written from the abstract and the open-access full text.')
        hero=(f'<nav class="crumbs"><a href="../">Home</a> › <a href="../longevity/">Longevity</a> › <a href="./">{SECTION}</a> › '+('Landmark #'+str(p['impactRank']) if p['group']=='landmark' else 'Latest')+'</nav>'
              f'<h1>{E(p["title"])}</h1><p>{E(", ".join(p.get("authors") or []) if len(p.get("authors") or [])<=8 else p.get("authorsShort"))}</p>'
              f'<p><b>{E(p["journal"])}</b> · {fdate(p["pubDate"])} · {E(p.get("type","research")).capitalize()}</p>'
              '<p class="back"><a href="../longevity/">← Back to the Longevity course</a></p>')
        sig=p.get('signals') or {}; news=sig.get('newsMentions') or []
        src=('<section class="src"><h2>Sources and signals</h2><p>'+E(basis)+' Key terms are general definitions added for readers.</p><ul>'
             f'<li>Original paper: <a href="{E(p["url"])}">{E(p["url"])}</a>'+(f' · PubMed <a href="https://pubmed.ncbi.nlm.nih.gov/{E(p["pmid"])}/">{E(p["pmid"])}</a>' if p.get('pmid') else '')+'</li>'
             f'<li>Citations: {E((sig.get("citations") or {}).get("openalex"))} (OpenAlex), {E((sig.get("citations") or {}).get("semanticScholar"))} (Semantic Scholar), as of 28 Oct 2026.</li>'
             '<li>Altmetric: '+(E(sig.get('altmetric',{}).get('score')) if (sig.get('altmetric') or {}).get('score') is not None else 'not available')+'.</li>'
             +('<li>Coverage: '+', '.join(f'<a href="{E(n["url"])}">{E(n["outlet"])}</a>' for n in news)+'.</li>' if news else '<li>Coverage: none found in a news search.</li>')+'</ul></section>')
        body=(f'<main><article>{warn}<div class="doi"><a class="btn" href="{E(p["url"])}">Read the original paper →</a><code>doi:{E(p["doi"])}</code></div>{oan}'
              f'<p class="one">{E(p["whyItMatters"])}</p>'
              f'<section><h2>Why it matters</h2><p>{E(s["why"])}</p></section>'
              f'<section><h2>What they did</h2><p>{E(s["did"])}</p></section>'
              f'<section><h2>What they found</h2><p>{E(s["found"])}</p></section>'
              f'<section><h2>Limits</h2><p>{E(s["limits"])}</p></section>'
              '<section><h2>Key terms</h2><dl class="terms">'+''.join(f'<dt>{E(t["term"])}</dt><dd>{E(t["definition"])}</dd>' for t in s['terms'])+'</dl></section>'
              f'{src}</article><nav class="pn">'
              +(f'<a href="{E(prv["slug"])}.html"><small>Previous</small>{E(prv["title"])}</a>' if prv else '<a href="./"><small>Back</small>All papers</a>')
              +(f'<a class="nx" href="{E(nxt["slug"])}.html"><small>Next</small>{E(nxt["title"])}</a>' if nxt else '<a class="nx" href="./"><small>Back</small>All papers</a>')
              +'</nav></main>')
        open(os.path.join(OUT,p['slug']+'.html'),'w',encoding='utf-8').write(page(f'{p["title"]} · {SECTION} · {UNIVERSITY_NAME}',hero,body,p['whyItMatters']))
    print(f'literature: {len(land)} landmark, {len(late)} latest -> {OUT}')
if __name__=='__main__': build()
