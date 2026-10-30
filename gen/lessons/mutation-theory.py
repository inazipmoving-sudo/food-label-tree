# Module 2 · The Mutation Theory of Aging. Numbers from gen/data/longevity-mutation-theory.json.
# exec'd by gen/longevity.py while COURSE/OUT point at /longevity/.
import math
MT=json.load(open(os.path.join(GEN,'data','longevity-mutation-theory.json'),encoding='utf-8'))
def mt_rint(x): return int(math.floor(float(x)+0.5))
def mt_r1(x): return math.floor(float(x)*10+0.5)/10.0
MT_EXPECT={
 'Cat':(287,18.7),'Black-and-white colobus':(80,24.4),'Cow':(207,20.1),'Dog':(249,15.3),
 'Ferret':(496,7.8),'Giraffe':(99,24.1),'Horse':(128,31.5),'Human':(47,83.7),'Lion':(160,20.6),
 'Mouse':(796,3.7),'Naked mole-rat':(93,25.3),'Rabbit':(217,9.1),'Rat':(665,2.7),
 'Ring-tailed lemur':(104,28.0),'Tiger':(212,19.4)}
MT_PTS=[]
for _p in MT['cagan']['points']:
    _rr,_lr=mt_rint(_p['rateRaw']),mt_r1(_p['lifeRaw'])
    assert MT_EXPECT[_p['species']]==(_rr,_lr), (_p['species'],_rr,_lr)
    MT_PTS.append(dict(_p, rate=_rr, life=_lr))
assert len(MT_PTS)==MT['cagan']['speciesWithAge']==15
_C=MT['cagan']; _J=MT['jaiswal']
assert _C['crypts']==208 and _C['individuals']==56 and _C['speciesSurveyed']==16
assert _C['fveLogLog']==0.85 and _C['elbFold']==2.94 and _C['lifespanFold']==30.44 and _C['rateFold']==16.9
assert _C['codingElb']==31 and _J['n']==17182 and _J['bands'][0]['percent']==9.5 and _J['bands'][0]['count']==219
MT_VERBATIM='The somatic mutation theory is about changes that arise in the cells of one body. Mutation accumulation, in Medawar\'s sense, is about inherited mutations that act late and remain in a population because selection is weak by then. They are not the same theory.'
_sc=open(os.path.join(GEN,'scripts','mutation-theory.json'),encoding='utf-8').read()
assert MT_VERBATIM in _sc and '"verbatim": true' in _sc
for _bit in ('47 substitutions per year','796 substitutions per year','83.7 years','3.7 years','99 and 93','24 and 25','24.1 and 25.3','128 substitutions','207','0.85','3,206','2,684 to 3,729','1,828 to 5,379','30.44-fold','2.94-fold','31 coding','9.5 percent','219 of 2,300','11.7 percent','18.4 percent','hazard ratio of 11.1','1.4 for death','2.0 for coronary','2.6 for ischemic','median of 18 percent','More than a quarter','more than half','1,432 amino acids','60 percent','500-fold','2,500-fold','three- to fivefold','11-fold','more than 70-fold','16 months','25 months','15 to 45'):
    assert _bit in _sc, _bit

def mt_esc(s): return _html.escape(str(s),quote=True)
def mt_doi(doi): return f'<a href="https://doi.org/{doi}">{doi}</a>'
MT_CSS='''<style>
.mt-note{margin:0 0 12px;line-height:1.5}
.mt-split{display:grid;grid-template-columns:1fr 1fr 1fr;gap:8px;margin:0 0 12px}
.mt-split p{margin:0;padding:10px 12px;border:1px solid var(--line);border-radius:4px;background:var(--bg);line-height:1.45}
.mt-split b{font-family:var(--serif);font-weight:600}
.mt-tl{list-style:none;margin:0;padding:0;display:grid;gap:8px}
.mt-tl li{display:grid;grid-template-columns:72px minmax(0,1fr);gap:10px;border:1px solid var(--line);border-radius:4px;padding:8px 12px;background:var(--bg);line-height:1.45}
.mt-tl .yr{font-family:var(--serif);font-weight:600;color:var(--acc);font-size:1.2rem}
.mt-tl li.evo{border-left:3px solid var(--u)}
.mt-tl li.ref{border-left:3px solid var(--t)}
.mt-k{display:inline-block;font-size:.66rem;letter-spacing:.12em;text-transform:uppercase;color:var(--muted);margin-right:6px}
.mt-quote{margin:12px 0 0;padding:12px 16px;border-left:3px solid var(--acc);background:var(--acc-soft);font-family:var(--serif);font-size:1.28rem;font-weight:600;line-height:1.35}
.art svg.mt{min-width:700px;max-height:none}
.mt text{font-size:12px;fill:var(--text)}
.mt text.sm{font-size:11px;fill:var(--muted)}
.mt .axis{stroke:var(--muted);stroke-width:1.2;fill:none}
.mt .grid{stroke:var(--line);stroke-width:1;fill:none}
.mt-leg{display:flex;flex-wrap:wrap;gap:8px 16px;margin:10px 0 0;color:var(--muted);font-size:.92rem;line-height:1.4}
.mt-leg i{display:inline-block;width:10px;height:10px;border-radius:50%;background:var(--acc);margin-right:6px;vertical-align:-1px}
.mt-leg i.m{background:var(--s)}
.mt-leg i.g{background:var(--u)}
.mt-leg i.o{background:var(--muted)}
.mt-src{margin-top:12px}
.mt-src summary{cursor:pointer;color:var(--muted);font-size:.92rem}
.mt-src ul{margin:8px 0 0;padding-left:18px;color:var(--muted);font-size:.9rem;line-height:1.45}
.mt-src a{color:var(--acc)}
.mt-flow{display:grid;gap:8px}
.mt-box{border:1px solid var(--line);border-radius:4px;padding:10px 12px;background:var(--bg);line-height:1.45}
.mt-box b,.mt-col h4{font-family:var(--serif);font-weight:600}
.mt-arr{text-align:center;color:var(--muted);font-size:.78rem;letter-spacing:.12em;text-transform:uppercase}
.mt-3{display:grid;grid-template-columns:1fr 1fr 1fr;gap:8px}
.mt-two{display:grid;grid-template-columns:1fr 1fr;gap:10px}
.mt-col{border:1px solid var(--line);border-radius:4px;padding:12px 14px;background:var(--bg);line-height:1.45}
.mt-col.ok{border-top:3px solid var(--u)}
.mt-col.no{border-top:3px solid var(--s)}
.mt-col h4{margin:0 0 8px;font-size:1.2rem}
.mt-col ul{margin:0;padding-left:18px}
.mt-col li{margin:0 0 8px}
.mt-cards{display:grid;gap:10px}
.mt-cards a{display:block;border:1px solid var(--line);border-radius:4px;padding:10px 14px;text-decoration:none;background:var(--bg);line-height:1.45}
.mt-cards a:hover{border-color:var(--acc)}
.mt-cards small{display:block;color:var(--muted);font-size:.68rem;letter-spacing:.14em;text-transform:uppercase;margin-bottom:2px}
.mt-cards b{font-family:var(--serif);font-weight:600;font-size:1.15rem}
@media(max-width:700px){.mt-split,.mt-3,.mt-two{grid-template-columns:1fr}.mt-tl li{grid-template-columns:1fr;gap:2px}}
</style>'''
def mt_src(rows):
    lis=''.join(f'<li>{row}</li>' for row in rows)
    return f'<details class="mt-src"><summary>Sources, with DOIs</summary><ul>{lis}</ul></details>'
_S_SZ=f'Szilard L. On the nature of the aging process. Proc Natl Acad Sci U S A. 1959;45(1):30-45. {mt_doi("10.1073/pnas.45.1.30")}'
_S_FA=f'Failla G. The aging process and cancerogenesis. Ann N Y Acad Sci. 1958;71(6):1124-1140. {mt_doi("10.1111/j.1749-6632.1958.tb46828.x")} Crossref also records {mt_doi("10.1111/j.1749-6632.1958.tb54674.x")} for the same volume and pages.'
_S_ME='Medawar PB. An Unsolved Problem of Biology. London: H. K. Lewis; 1952. Inaugural lecture delivered at University College London, 6 December 1951. No DOI in Crossref. Do not substitute the 1953 journal notice of the lecture.'
_S_WI=f'Williams GC. Pleiotropy, natural selection, and the evolution of senescence. Evolution. 1957;11(4):398-411. {mt_doi("10.1111/j.1558-5646.1957.tb02911.x")}'
_S_OR=f'Orgel LE. The maintenance of the accuracy of protein synthesis and its relevance to ageing. Proc Natl Acad Sci U S A. 1963;49(4):517-521. {mt_doi("10.1073/pnas.49.4.517")}'
_S_HA=f'Harley CB, Pollard JW, Chamberlain JW, Stanners CP, Goldstein S. Protein synthetic errors do not increase during aging of cultured human fibroblasts. Proc Natl Acad Sci U S A. 1980;77(4):1885-1889. {mt_doi("10.1073/pnas.77.4.1885")}'
_S_CA=f'Cagan A, Baez-Ortega A, Brzozowska N, et al. Somatic mutation rates scale with lifespan across mammals. Nature. 2022;604(7906):517-524. {mt_doi("10.1038/s41586-022-04618-z")} Rates and lifespans: Supplementary Tables 3 and 6. The too-low passage is Supplementary Note 1.'
_S_JA=f'Jaiswal S, Fontanillas P, Flannick J, et al. Age-related clonal hematopoiesis associated with adverse outcomes. N Engl J Med. 2014;371(26):2488-2498. {mt_doi("10.1056/NEJMoa1408617")}'
_S_M5=f'Martincorena I, Roshan A, Gerstung M, et al. High burden and pervasive positive selection of somatic mutations in normal human skin. Science. 2015;348(6237):880-886. {mt_doi("10.1126/science.aaa6806")}'
_S_M8=f'Martincorena I, Fowler JC, Wabik A, et al. Somatic mutant clones colonize the human esophagus with age. Science. 2018;362(6417):911-917. {mt_doi("10.1126/science.aau3879")}'
_S_YU=f'Yu CE, Oshima J, Fu YH, et al. Positional cloning of the Werner\'s syndrome gene. Science. 1996;272(5259):258-262. {mt_doi("10.1126/science.272.5259.258")}'
_S_NI=f'Niedernhofer LJ, Garinis GA, Raams A, et al. A new progeroid syndrome reveals that genotoxic stress suppresses the somatotroph axis. Nature. 2006;444(7122):1038-1043. {mt_doi("10.1038/nature05456")}'
_S_L3=f'López-Otín C, Blasco MA, Partridge L, Serrano M, Kroemer G. The hallmarks of aging. Cell. 2013;153(6):1194-1217. {mt_doi("10.1016/j.cell.2013.05.039")}'
_S_L23=f'López-Otín C, Blasco MA, Partridge L, Serrano M, Kroemer G. Hallmarks of aging: an expanding universe. Cell. 2023;186(2):243-278. {mt_doi("10.1016/j.cell.2022.11.001")}'
_S_HO=f'Hoeijmakers JHJ. DNA damage, aging, and cancer. N Engl J Med. 2009;361(15):1475-1485. {mt_doi("10.1056/NEJMra0804615")}'
_S_VI=f'Vijg J, Dong X. Pathogenic mechanisms of somatic mutation and genome mosaicism in aging. Cell. 2020;182(1):12-23. {mt_doi("10.1016/j.cell.2020.06.024")}'
_S_TR=f'Trifunovic A, Wredenberg A, Falkenberg M, et al. Premature ageing in mice expressing defective mitochondrial DNA polymerase. Nature. 2004;429(6990):417-423. {mt_doi("10.1038/nature02517")}'
_S_V7=f'Vermulst M, Bielas JH, Kujoth GC, et al. Mitochondrial point mutations do not limit the natural lifespan of mice. Nat Genet. 2007;39(4):540-543. {mt_doi("10.1038/ng1988")}'
_S_V8=f'Vermulst M, Wanagat J, Kujoth GC, et al. DNA deletions and clonal mutations drive premature aging in mitochondrial mutator mice. Nat Genet. 2008;40(4):392-394. {mt_doi("10.1038/ng.95")}'
_S_AL=f'Albertson TM, Ogawa M, Bugni JM, et al. DNA polymerase ε and δ proofreading suppress discrete mutator and cancer phenotypes in mice. Proc Natl Acad Sci U S A. 2009;106(40):17101-17104. {mt_doi("10.1073/pnas.0907147106")}'

def mt_chart():
    L,R,T,B=92,930,36,392
    xmin,xmax,ymin,ymax=2.0,100.0,30.0,1200.0
    def X(v): return L+(math.log10(v)-math.log10(xmin))/(math.log10(xmax)-math.log10(xmin))*(R-L)
    def Y(v): return B-(math.log10(v)-math.log10(ymin))/(math.log10(ymax)-math.log10(ymin))*(B-T)
    by={p['species']:p for p in MT_PTS}
    o=[f'<svg class="mt" viewBox="0 0 980 460" role="img" aria-label="Logarithmic chart of lifespan against somatic substitutions per year. Human is 47 per year at 83.7 years. Mouse is 796 per year at 3.7 years. Fifteen mammal species, intestinal crypts, Cagan and colleagues 2022.">']
    o.append('<g data-part="axes">')
    for v in (3,10,30,80):
        x=X(v); o.append(f'<line class="grid" x1="{x:.1f}" y1="{T}" x2="{x:.1f}" y2="{B}"/>')
        o.append(f'<text class="sm" x="{x:.1f}" y="{B+18}" text-anchor="middle">{v}</text>')
    for v in (50,100,200,400,800):
        y=Y(v); o.append(f'<line class="grid" x1="{L}" y1="{y:.1f}" x2="{R}" y2="{y:.1f}"/>')
        o.append(f'<text class="sm" x="{L-8}" y="{y+4:.1f}" text-anchor="end">{v}</text>')
    o.append(f'<line class="axis" x1="{L}" y1="{T}" x2="{L}" y2="{B}"/><line class="axis" x1="{L}" y1="{B}" x2="{R}" y2="{B}"/>')
    o.append(f'<text class="sm" x="{(L+R)/2:.0f}" y="{B+38}" text-anchor="middle">Lifespan, years, logarithmic. Age at which 80 percent of adults had died.</text>')
    o.append(f'<text class="sm" x="16" y="{(T+B)/2:.0f}" text-anchor="middle" transform="rotate(-90 16 {(T+B)/2:.0f})">Substitutions per genome per year, logarithmic</text>')
    o.append('</g>')
    # unlabeled species first, then the labeled callouts
    # Giraffe and naked mole-rat sit on top of each other (24 years, ~100 substitutions). One label for the pair.
    named=('Human','Mouse','Rat','Naked mole-rat','Giraffe')
    spot={'Human':('end',-10,-14,'var(--acc)'),'Mouse':('start',10,-4,'var(--s)'),'Rat':('start',10,18,'var(--s)'),
          'Ferret':('start',10,-12,'var(--text)')}
    o.append('<g data-part="ends">')
    for sp in ('Human','Mouse','Rat'):
        p=by[sp]; x,y=X(p['life']),Y(p['rate']); anc,dx,dy,col=spot[sp]
        o.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="5.5" fill="{col}"/>')
        o.append(f'<text x="{x+dx:.1f}" y="{y+dy:.1f}" text-anchor="{anc}" fill="{col}">{mt_esc(sp)} {p["rate"]}</text>')
    o.append('</g><g data-part="size">')
    gx=gy=0
    for sp in ('Giraffe','Naked mole-rat'):
        p=by[sp]; x,y=X(p['life']),Y(p['rate']); gx+=x; gy+=y
        o.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="5.5" fill="var(--u)"/>')
    gx,gy=gx/2,gy/2
    g,n=by['Giraffe'],by['Naked mole-rat']
    o.append(f'<text x="{gx:.1f}" y="{gy-16:.1f}" text-anchor="middle" fill="var(--u)">Giraffe {g["rate"]} · mole-rat {n["rate"]}</text>')
    o.append('</g>')
    for p in MT_PTS:
        if p['species'] in named: continue
        x,y=X(p['life']),Y(p['rate'])
        o.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="4.2" fill="var(--muted)"/>')
    p=by['Ferret']; x,y=X(p['life']),Y(p['rate']); anc,dx,dy,col=spot['Ferret']
    o.append(f'<text x="{x+dx:.1f}" y="{y+dy:.1f}" text-anchor="{anc}" fill="{col}">Ferret {p["rate"]}</text>')
    o.append('</svg>')
    return ''.join(o)

def mt_table():
    rows=sorted(MT_PTS, key=lambda p:-p['life'])
    body=''.join('<tr>'+''.join(f'<td data-l="{h}">{v}</td>' for h,v in zip(('Species','Substitutions per year','Lifespan, years'),(mt_esc(p['species']),f'{p["rate"]}',f'{p["life"]:.1f}')))+'</tr>' for p in rows)
    return ('<div class="rtbl-wrap"><table class="rtbl"><thead><tr><th>Species</th><th>Substitutions per year</th><th>Lifespan, years</th></tr></thead><tbody>'
            +body+'</tbody></table></div>')

_LEG=('<div class="mt-leg"><span><i></i>Human</span><span><i class="m"></i>Mouse and rat</span>'
      '<span><i class="g"></i>Giraffe and naked mole-rat, similar rate and lifespan</span>'
      '<span><i class="o"></i>The other eleven species, named in the table</span></div>')
_b0,_b1,_b2=_J['bands']
F1=('<!--noart-->'+MT_CSS
    +'<div class="mt-split" data-part="split"><p><b>Somatic mutation.</b> Changes that arise in the cells of one body during life. Szilard, 1959, and Failla, 1958.</p>'
    '<p><b>Evolutionary mutation accumulation.</b> Inherited mutations that act late and stay in the population. Medawar, 1952. Not a count of mutations in your cells.</p>'
    '<p><b>Error catastrophe.</b> A possible runaway of mistakes in protein synthesis. Orgel, 1963. Tested, and not supported, by Harley and colleagues, 1980.</p></div>'
    +f'<p class="mt-quote" data-part="verbatim">{mt_esc(MT_VERBATIM)}</p>'
    +'<ol class="mt-tl" style="margin-top:12px">'
    '<li data-part="szilard"><span class="yr">1959</span><div><span class="mt-k">Somatic</span><b>Szilard, PNAS.</b> Aging hits: somatic mutations accumulating in the cells of the body. The classic statement of the somatic mutation theory. The numerical model in that paper is not used here.</div></li>'
    '<li data-part="failla"><span class="yr">1958</span><div><span class="mt-k">Somatic</span><b>Failla, Annals of the New York Academy of Sciences.</b> The aging process and cancerogenesis. Somatic mutation as a process shared by aging and cancer. The companion paper to Szilard, not a different theory. Two Crossref DOIs, one article.</div></li>'
    '<li class="evo" data-part="medawar"><span class="yr">1952</span><div><span class="mt-k">Evolutionary</span><b>Medawar, H. K. Lewis, London.</b> An Unsolved Problem of Biology. Harmful inherited variants that act only late are weakly selected, because in the wild most animals are already dead. Those variants can accumulate in the population. No DOI in Crossref.</div></li>'
    '<li class="evo" data-part="williams"><span class="yr">1957</span><div><span class="mt-k">Evolutionary</span><b>Williams, Evolution.</b> Pleiotropy, natural selection, and the evolution of senescence. A gene that helps early and harms late can be favored. That is antagonistic pleiotropy, not mutation accumulation, and not Szilard. Taught in full in a later module.</div></li>'
    '<li class="ref" data-part="orgel"><span class="yr">1963</span><div><span class="mt-k">Error catastrophe</span><b>Orgel, PNAS.</b> If the proteins that copy DNA or translate RNA are themselves mis-made, errors might feed on themselves. The strong form predicts a rising error rate. This is not the somatic mutation theory.</div></li>'
    '<li class="ref" data-part="harley"><span class="yr">1980</span><div><span class="mt-k">The test</span><b>Harley and colleagues, PNAS.</b> In cultured human fibroblasts, protein-synthesis errors did not rise with donor age, with passage, or in Werner or Hutchinson-Gilford cells. The authors wrote that the data fail to support the error catastrophe theory. Cells in a dish, not a whole life.</div></li>'
    +'</ol>'+mt_src([_S_SZ,_S_FA,_S_ME,_S_WI,_S_OR,_S_HA]))
F2=('<!--noart-->'
    +'<p class="mt-note" data-part="design">Cagan and colleagues, Nature, 2022. 208 intestinal crypts, 56 individuals, 16 mammal species. Fifteen had a known age. The harbour porpoise is omitted because its age was unknown. One dot is the species mean, rounded. Both axes are logarithmic.</p>'
    +'<div class="art">'+mt_chart()+'</div>'+_LEG
    +'<p class="mt-note" data-part="burden">End of life, from the paper, not from a new fit. Log-log fraction of variance explained 0.85, P = 1 × 10<sup>−6</sup>, slope not significantly different from −1. Mean end-of-lifespan burden 3,206 substitutions per genome (interval 2,684 to 3,729). Table 1: lifespan 30.44-fold, adult mass 39,024-fold, end-of-lifespan burden 2.94-fold, from 1,828 to 5,379 substitutions. The paper says around 30-fold, around 40,000-fold, and around 3-fold. Protein-coding mutations: 85 percent of the variance, 31 coding substitutions at the end of lifespan.</p>'
    +mt_table()
    +'<p class="enote" data-part="limit">One cell type, the intestinal crypt. The paper says the rates may contribute to aging. It does not show that they cause it, or that brain, muscle, and blood match these numbers. Human 47 per year at 83.7 years (Table 1 prints 83.67). Mouse 796 per year at 3.7 years. Giraffe and naked mole-rat, in the paper\'s own rounding, 99 and 93 per year at 24 and 25 years; on this chart, 24.1 and 25.3 years. Horse 128 and cow 207 per year are in the table.</p>'
    +mt_src([_S_CA]))
F3=('<!--noart-->'
    +'<div class="mt-flow"><div class="mt-box" data-part="damage"><b>DNA damage is the lesion.</b> A break, a crosslink, an adduct, a chemically changed base. It is not yet a mutation. Hoeijmakers, New England Journal of Medicine, 2009, reviews damage and repair together with aging and cancer. Vijg and Dong, Cell, 2020, review the mutations that remain, and the mosaic of cells they produce.</div>'
    '<div data-part="exits"><p class="mt-arr">Three exits</p><div class="mt-3">'
    '<div class="mt-box"><b>Faithful repair.</b> The sequence is put back. Nothing is passed on.</div>'
    '<div class="mt-box"><b>Mutation.</b> The sequence change remains, and daughter cells inherit it if the cell divides. This is Szilard\'s object.</div>'
    '<div class="mt-box"><b>Stall, without a new sequence.</b> An unrepaired lesion blocks transcription. The cell works badly, and no mutation has been written down.</div></div>'
    '<div class="mt-box"><b>When repair fails early.</b> Yu and colleagues, Science, 1996: Werner syndrome is WRN, a predicted protein of 1,432 amino acids with similarity to DNA helicases. One truncating splice mutation was homozygous in 60 percent of the Japanese patients they examined. Niedernhofer, Hoeijmakers, Vijg, and colleagues, Nature, 2006: XPF-ERCC1 cuts helix-distorting lesions and interstrand crosslinks. A severe XPF mutation produced dramatic progeroid symptoms. The mouse model links unrepaired damage to a drop in growth-hormone and IGF-1 signaling. That paper\'s claim is about damage, not a mutation count.</div></div>'
    '<p class="mt-arr">If a stem cell is selected, the mutation becomes a clone</p>'
    f'<div class="mt-box" data-part="clone"><b>Blood.</b> Jaiswal and colleagues, New England Journal of Medicine, 2014. Exomes of {_J["n"]:,} people. Rare under 40. Ages {_b0["ages"]}: {_b0["percent"]} percent, {_b0["count"]:,} of {_b0["of"]:,}. Ages {_b1["ages"]}: {_b1["percent"]} percent, {_b1["count"]} of {_b1["of"]}. Ages {_b2["ages"]}: {_b2["percent"]} percent, {_b2["count"]} of {_b2["of"]}. Mostly DNMT3A, TET2, and ASXL1. Hazard ratios: hematologic cancer {_J["hrCancer"]} (interval {_J["hrCancerCi"][0]} to {_J["hrCancerCi"][1]}), death {_J["hrDeath"]} ({_J["hrDeathCi"][0]} to {_J["hrDeathCi"][1]}), coronary heart disease {_J["hrChd"]} ({_J["hrChdCi"][0]} to {_J["hrChdCi"][1]}), ischemic stroke {_J["hrStroke"]} ({_J["hrStrokeCi"][0]} to {_J["hrStrokeCi"][1]}). Their summary: {_J["over70Percent"]} percent of people older than 70, and a median of {_J["medianClonePercent"]} percent of white blood cells in the clone. Prevalence depends on the gene list and on how small a clone can be seen.</div>'
    '<div class="mt-box" data-part="tissue"><b>Skin and esophagus, without a tumor.</b> Martincorena and colleagues, Science, 2015: 234 biopsies of normal sun-exposed skin from four people. Burden higher than many tumors. More than a quarter of normal skin cells carried a driver mutation, and every square centimeter held hundreds of competing clones. Science, 2018: normal esophagus from nine donors. By middle age, more than half the epithelium was colonized by mutant clones. NOTCH1 mutations were more common in normal esophagus than in esophageal cancer.</div>'
    '<div class="mt-box" data-part="hallmark"><b>A listed hallmark, and a stated limit.</b> López-Otín and colleagues, Cell, 2013: nine hallmarks, genomic instability first. Cell, 2023: twelve, and genomic instability is still on the list. The 2013 paper says syndromes such as Werner are a consequence of increased DNA damage, and that their relevance to normal aging remains unresolved, because they recapitulate only some aspects of aging.</div></div>'
    +mt_src([_S_HO,_S_VI,_S_YU,_S_NI,_S_JA,_S_M5,_S_M8,_S_L3,_S_L23]))
F4=('<!--noart-->'
    +'<div class="mt-two"><div class="mt-col ok" data-part="agree"><h4>Broadly accepted</h4><ul>'
    '<li>Somatic mutations accumulate with age in normal tissues.</li>'
    '<li>Across these mammals, substitutions per year in intestinal crypts scale inversely with lifespan. The burden at the end of life varies much less than lifespan does.</li>'
    '<li>Clonal hematopoiesis is common in later life and is associated with blood cancer, death, coronary disease, and stroke.</li>'
    '<li>Normal skin and normal esophagus are already mosaics of mutant clones, driver mutations included.</li>'
    '<li>Inherited failure of WRN, or of XPF-ERCC1, can cause a progeroid syndrome.</li>'
    '<li>Genomic instability is a hallmark in the 2013 list and remains one in the 2023 list of twelve.</li></ul></div>'
    '<div class="mt-col no"><h4>Contested, or a different theory</h4><ul>'
    '<li data-part="toolow">Too low for a simple knockout story. The 2022 supplement puts most human tissues on the order of 15 to 45 mutations per diploid genome per year, and says that appears too low to inactivate both copies of important genes in a relevant fraction of cells. The rise is approximately linear, not a runaway. A selected clone is a different route, and the note says so.</li>'
    '<li data-part="mice">Not proportional in the mitochondrial mutator. Homozygous Polg proofreading mutants age prematurely (Trifunovic and colleagues, 2004; their assay then read a three- to fivefold rise in point mutations, plus deletions). Heterozygotes carried a 500-fold higher point-mutation burden than normal mice without a significant cut in mean lifespan (Vermulst and colleagues, 2007). That paper revises the homozygous point-mutation burden to about 2,500-fold against the new baseline. The 2008 paper attributes the homozygous premature-aging phenotype to deletions and clonal mutations, not to the point mutations alone.</li>'
    '<li data-part="proof">Nuclear proofreading mutants raise cancer, not a described progeria. Polymerase epsilon: more than a 70-fold mutation-rate rise in fibroblasts, median survival 16 months against 25, dead of cancer. Heterozygotes matched wild-type at 25 months. Polymerase delta homozygotes died in the first year, primarily of lymphoma, skin tumors, and lung tumors (Albertson and colleagues, 2009).</li>'
    '<li data-part="open">Still open: whether ordinary burdens cause aging itself, or mainly cancer and clonal disease; how much of the harm is persistent damage rather than the mutation left behind; whether the lifespan scaling is a cause or a correlate. Progeroid syndromes copy only some of normal aging. Error catastrophe in its strong form is not supported. Medawar\'s theory is about evolution, not about somatic mutations.</li></ul></div></div>'
    +mt_src([_S_CA,_S_TR,_S_V7,_S_V8,_S_AL,_S_L3,_S_HA,_S_ME]))
def mt_card(href,kicker,title,text):
    return f'<a href="../literature/{href}"><small>{kicker}</small><b>{mt_esc(title)}</b><span>{text}</span></a>'
F5=('<!--noart-->'
    +'<p data-part="bridge">These cards open pages in Peer-Reviewed Literature, part of this course. Each line is only what that page says.</p>'
    '<div class="mt-cards" data-part="clones" style="margin-top:12px">'
    +mt_card('clonal-hematopoiesis-heart-failure.html','Clonal hematopoiesis','Clones and heart failure','In 417,616 adults, blood-stem-cell clones carrying acquired mutations were linked to a higher risk of heart failure. The page calls the study observational, and says exome sequencing can miss small clones.')
    +mt_card('somatic-mutations-microglia-ageing.html','Somatic mutations as barcodes','Cells entering the microglia','Bone-marrow-derived cells joined the brain\'s microglia in every older person studied. The page says the series was 20 people, all older, and that an Alzheimer\'s association is not proof those cells protect the brain.')
    +'</div><div class="mt-cards" data-part="repair" style="margin-top:10px">'
    +mt_card('mtdna-mutations-blood-aging.html','Mitochondrial DNA','Copying errors in blood','Mutations that rise with age in blood mitochondrial DNA fit copying errors made visible by expanding clones, not oxidative damage. The page limits that to blood, and says oxidative damage is not ruled out in aging generally.')
    +mt_card('bowhead-whale-dna-repair.html','Long-lived animals','Bowhead whale DNA repair','A mammal that can live about 200 years repaired double-strand breaks more accurately. The page says the work was in cultured cells and fruit flies, not a treatment for people.')
    +mt_card('dna-repeat-expansions-900000.html','Repeat instability','Repeats lengthen in blood','In 900,000 people, repeated DNA stretches lengthened in blood with age, and inherited genes set the pace. The page says the measurements are blood only, and the disease links are associations.')
    +'</div><div class="mt-cards" data-part="micelit" style="margin-top:10px">'
    +mt_card('caloric-restriction-somatic-mutation.html','Diet, in mice','Eating less, fewer mutations','Caloric restriction slowed somatic mutations across several mouse tissues. The page does not give the level of restriction, and says fewer mutations are not proof that those mutations were driving aging.')
    +mt_card('dna-protein-crosslinks-premature-aging.html','A repair defect, in mice','DNA-protein crosslinks','Unrepaired DNA-protein crosslinks set off an immune alarm and premature aging in a mouse model of a rare disease. Blocking the alarm helped. The page says this is not necessarily what drives ordinary human aging.')
    +'</div>')

MT_LESSON=[
 ('Where the theory came from','Somatic mutation, evolutionary mutation accumulation, and error catastrophe are three different ideas.',F1),
 ('Lifespan and the mutation rate','Intestinal crypts of mammals, from Cagan and colleagues, Nature, 2022.',F2),
 ('From damage to a mutation to a clone','A lesion, a sequence change, and a clone are three different objects.',F3),
 ('Where the argument stands','What is broadly accepted, and what is still contested.',F4),
 ('From the literature','Reading-room pages that bear on mutation, clones, and repair. Only what those pages say.',F5),
]
MT_CAPS=[
 'Szilard 1959 and Failla 1958 are the somatic theory. Medawar 1952 is evolutionary mutation accumulation, and it has no Crossref DOI. Williams 1957 is antagonistic pleiotropy, kept here so it is not mistaken for either. Orgel 1963 is error catastrophe. Harley and colleagues, 1980, did not find the predicted rise in protein-synthesis errors in cultured fibroblasts.',
 'Rounded to the nearest substitution per year and to one decimal year, from Supplementary Tables 3 and 6 of Cagan et al., Nature, 2022. Lifespan is the age at which 80 percent of adults had died. The harbour porpoise is omitted. The regression numbers are the paper\'s, not a new fit to these rounded dots.',
 'Damage, mutation, and clone are drawn apart on purpose. The blood percentages and hazard ratios are Jaiswal et al., New England Journal of Medicine, 2014. Skin and esophagus are Martincorena et al., Science, 2015 and 2018. Werner is Yu et al., Science, 1996. XPF-ERCC1 is Niedernhofer et al., Nature, 2006. The hallmark list is López-Otín et al., Cell, 2013 and 2023.',
 'The left column is what the cited papers support. The right column is the criticism those papers, and the papers named on it, already contain. Nothing on the right is a finding of this lesson beyond those sources.',
 'Links open the existing reading-room pages. Nothing is added beyond what those pages say.',
]
MT_QUIZ=[
 ('What does the somatic mutation theory claim?','That aging is caused by mutations arising in the cells of the body during life. Szilard, 1959, called them aging hits (Figure 1).'),
 ('How is Medawar\'s mutation accumulation different?','It is about inherited mutations that act late and remain in a population because selection is weak by then. It is not a count of mutations inside one body (Figure 1).'),
 ('What did Williams 1957 propose?','Antagonistic pleiotropy: a gene that helps early and harms late can be favored. It is not the somatic mutation theory, and it is not Medawar\'s mutation accumulation (Figure 1).'),
 ('What became of Orgel\'s error catastrophe?','The strong form predicted rising protein-synthesis errors. Harley and colleagues, 1980, did not find that rise in cultured human fibroblasts, including Werner cells. The test is cells in a dish (Figure 1).'),
 ('What did Cagan and colleagues measure, and what did they find?','Single-base substitutions per year in intestinal crypts of 15 mammal species. Humans about 47 per year, mice about 796. The rate runs inversely with lifespan, and the end-of-lifespan burden varies only about 3-fold (Figure 2).'),
 ('Why do the giraffe and the naked mole-rat matter on that chart?','Similar rates, about 99 and about 93 per year, and similar lifespans, 24 and 25 years in the paper\'s rounding, despite around a 23,000-fold difference in adult body mass (Figure 2).'),
 ('What is the difference between DNA damage and a mutation?','Damage is a lesion, and it may be repaired. A mutation is a sequence change that remains. An unrepaired lesion can also stall the cell without a new sequence being written (Figure 3).'),
 ('What did Jaiswal and colleagues find in blood?','Clonal hematopoiesis, mostly DNMT3A, TET2, and ASXL1, in 9.5 percent of people aged 70 to 79, associated with blood cancer, death, coronary disease, and stroke (Figure 3).'),
 ('Why is the theory still contested?','A simple gene-inactivation story looks short of mutations in ordinary tissues. Heterozygous mitochondrial mutator mice carried a 500-fold higher point-mutation burden without a significant lifespan cut. Nuclear proofreading mutants died of cancer, not of a described progeria. Progeroid syndromes copy only some of normal aging (Figure 4).'),
 ('What do the reading-room pages not show?','They do not show that a blood-cell clone, a mouse diet, or a whale protein produced the historical rise in population life expectancy. Associations stay associations, and the mouse and cell results stay in mice and cells (Figure 5).')]
_figs=[figure_card(i,t,h,c,sub=s) for i,((t,s,h),c) in enumerate(zip(MT_LESSON,MT_CAPS),1)]
_quiz='<main class="lp-after"><section class="notes quiz" id="quiz"><h2>Quiz</h2><p class="lbl">Tap a question to see the answer</p>'+''.join(f'<details><summary>{n}. {q}</summary><p>{a}</p></details>' for n,(q,a) in enumerate(MT_QUIZ,1))+'</section></main>'
lesson_page('mutation-theory','Module 2 · The Mutation Theory of Aging · '+COURSE+' · '+UNIVERSITY_NAME,
 '<nav class="crumbs">'+CRUMB_HOME+' › Module 2</nav><h1>Module 2 · The Mutation Theory of Aging</h1>'
 '<p>Somatic mutations, from Szilard and Failla to the crypts, the clones, and the repair diseases, and the reasons the theory is not settled. Medawar\'s evolutionary mutation accumulation and Williams\'s antagonistic pleiotropy are here only so they are not confused with it. The figure is on the left and the lesson script on the right. Rates and lifespans on the chart are rounded from Cagan et al., Nature, 2022, Supplementary Tables 3 and 6. Every other number is taken from the paper named beside it.</p>',
 _figs,_quiz+pn(('Module 1 · Five Hundred Years of Life Expectancy','five-hundred-years.html'),None))
