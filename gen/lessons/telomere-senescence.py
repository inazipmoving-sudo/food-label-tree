# Module 3 · Telomeres and Replicative Senescence. Numbers from gen/data/longevity-telomere-senescence.json.
# exec'd by gen/longevity.py while COURSE/OUT point at /longevity/.
D=json.load(open(os.path.join(GEN,'data','longevity-telomere-senescence.json'),encoding='utf-8'))
_H=D['hayflickObituary']; _A=D['allsopp']; _B=D['blasco']; _K=D['kipling']; _M=D['hemann']
_G=D['gomes']; _Z=D['muezzinler']; _R=D['martinRuiz']; _Kim=D['kim']; _C=D['cawthon']
_Y=D['haycock']; _V=D['vulliamy']; _P=D['baker2016']
assert _H['fetalIsolates']==25 and _H['subcultivationsAbout']==50 and _H['adultDoublingsAbout']==20
assert _H['fetalDoublingsAbout']==50 and _H['adultDonorAges']=='58 to 87'
assert D['wrightBpPerDivision']==[40,200] and D['bodnarExtraDoublingsAtLeast']==20
assert _A['donors']==31 and _A['bpPerYear']==-15 and _A['doublingsPerKb']==10 and _A['rCapacityLength']==0.76
assert _B['kbPerGeneration']==4.8 and _B['generationsViable']==6 and _K['humanBloodKbAbout']==10
assert _M['c57Days']==767 and _M['castDays']==681 and len(_M['bars'])==6
assert _G['ancestralKb']==18.6 and _G['pLifespan']==0.0032 and _Z['crossSectional']==124
assert _Kim['immortalPositive']==98 and _Kim['tumorPositive']==90 and _C['n']==143
assert _Y['cases']==420081 and _Y['rows'][0]['or']==5.27 and _Y['rows'][-1]['or']==0.09
assert _V['deletionBp']==821 and _P['medianMixedPct']==27 and _P['medianB6Pct']==24
TS_VERBATIM='Telomeres limit how many times many human cells can divide. They do not, by themselves, set how long a species lives.'
_sc=open(os.path.join(GEN,'scripts','telomere-senescence.json'),encoding='utf-8').read()
assert TS_VERBATIM in _sc and '"verbatim": true' in _sc
for _bit in ('25 independent','approximately 50 subcultivations','approximately 20 doublings','approximately 50 for fetal','58 to 87','3-prime','TTGGGG','TTAGGG','at least 20 doublings','40 and 200','10 doublings per kilobase','r = 0.76','31 donors','0 to 93','minus 15 base pairs','minus 0.43','minus 0.2 doublings','about 10 kilobases','up to 150 kilobases','8 to 10 kilobases','about 18 to 20','about 30 to 120','30 to 150','767','681','5 to 7 years','25 to 150','15 to 20','0.0032','18.6','0.998','98 of 100','90 of 101','none of 50','420,081','1,093,105','5.27','0.78','0.09','821-base-pair','74 bases','4.8','six generations','27 percent','24 percent','17 to 35','24 to 42','0.0295','9 percent fat','124 cross-sectional','minus 0.338','24.7','21.91','32.2 to 45.5','0.63 to 0.99','more than 20 percent','3.18','1.36 to 7.45','8.54','1.52 to 47.9','500 nanograms','about 50 base pairs','more than 50 kilobases','0.90','López-Otín'):
    assert _bit in _sc, _bit

def ts_esc(s): return _html.escape(str(s),quote=True)
def ts_doi(doi): return f'<a href="https://doi.org/{doi}">{doi}</a>'
def ts_or(x): return f'{float(x):.2f}'
TS_CSS='''<style>
.ts-note{margin:0 0 12px;line-height:1.5}
.ts-split{display:grid;grid-template-columns:1fr 1fr 1fr;gap:8px;margin:0 0 12px}
.ts-split p{margin:0;padding:10px 12px;border:1px solid var(--line);border-radius:4px;background:var(--bg);line-height:1.45}
.ts-split b,.ts-box b,.ts-col h4{font-family:var(--serif);font-weight:600}
.ts-tl{list-style:none;margin:0;padding:0;display:grid;gap:8px}
.ts-tl li{display:grid;grid-template-columns:72px minmax(0,1fr);gap:10px;border:1px solid var(--line);border-radius:4px;padding:8px 12px;background:var(--bg);line-height:1.45}
.ts-tl .yr{font-family:var(--serif);font-weight:600;color:var(--acc);font-size:1.2rem}
.ts-k{display:inline-block;font-size:.66rem;letter-spacing:.12em;text-transform:uppercase;color:var(--muted);margin-right:6px}
.ts-quote{margin:12px 0 0;padding:12px 16px;border-left:3px solid var(--acc);background:var(--acc-soft);font-family:var(--serif);font-size:1.28rem;font-weight:600;line-height:1.35}
.ts-flow{display:grid;gap:8px}
.ts-box{border:1px solid var(--line);border-radius:4px;padding:10px 12px;background:var(--bg);line-height:1.45}
.ts-arr{text-align:center;color:var(--muted);font-size:.78rem;letter-spacing:.12em;text-transform:uppercase}
.ts-3{display:grid;grid-template-columns:1fr 1fr 1fr;gap:8px}
.ts-two{display:grid;grid-template-columns:1fr 1fr;gap:10px}
.ts-col{border:1px solid var(--line);border-radius:4px;padding:12px 14px;background:var(--bg);line-height:1.45}
.ts-col.ok{border-top:3px solid var(--u)}
.ts-col.no{border-top:3px solid var(--s)}
.ts-col h4{margin:0 0 8px;font-size:1.2rem}
.ts-col ul{margin:0;padding-left:18px}
.ts-col li{margin:0 0 8px}
.ts-rates{display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-top:10px}
.ts-end{display:flex;align-items:flex-end;gap:18px;padding:8px 4px 0}
.ts-end div{text-align:center}
.ts-end i{display:block;margin:0 auto 6px;background:var(--acc);border-radius:2px 2px 0 0}
.ts-end span{display:block;color:var(--muted);font-size:.78rem}
.ts-leg{display:flex;flex-wrap:wrap;gap:8px 16px;margin:10px 0 0;color:var(--muted);font-size:.92rem;line-height:1.4}
.ts-leg i{display:inline-block;width:18px;height:8px;border-radius:2px;background:var(--u);margin-right:6px;vertical-align:-1px}
.ts-leg i.h{background:var(--acc)}
.ts-leg i.l{background:var(--s)}
.ts-leg i.c{background:color-mix(in srgb,var(--muted) 28%,transparent);border:1.5px dashed var(--muted);height:6px}
.ts-src{margin-top:12px}
.ts-src summary{cursor:pointer;color:var(--muted);font-size:.92rem}
.ts-src ul{margin:8px 0 0;padding-left:18px;color:var(--muted);font-size:.9rem;line-height:1.45}
.ts-src a{color:var(--acc)}
.ts-cards{display:grid;gap:10px}
.ts-cards a{display:block;border:1px solid var(--line);border-radius:4px;padding:10px 14px;text-decoration:none;background:var(--bg);line-height:1.45}
.ts-cards a:hover{border-color:var(--acc)}
.ts-cards small{display:block;color:var(--muted);font-size:.68rem;letter-spacing:.14em;text-transform:uppercase;margin-bottom:2px}
.ts-cards b{font-family:var(--serif);font-weight:600;font-size:1.15rem}
.art svg.ts{min-width:700px;max-height:none}
.ts text{font-size:12px;fill:var(--text)}
.ts text.sm{font-size:11px;fill:var(--muted)}
.ts .axis{stroke:var(--muted);stroke-width:1.2}
.ts .grid{stroke:var(--line);stroke-width:1}
@media(max-width:700px){.ts-split,.ts-3,.ts-two,.ts-rates{grid-template-columns:1fr}.ts-tl li{grid-template-columns:1fr;gap:2px}}
</style>'''
def ts_src(rows):
    return '<details class="ts-src"><summary>Sources, with DOIs</summary><ul>'+''.join(f'<li>{row}</li>' for row in rows)+'</ul></details>'
_S_H1=f'Hayflick L, Moorhead PS. The serial cultivation of human diploid cell strains. Exp Cell Res. 1961;25(3):585-621. {ts_doi("10.1016/0014-4827(61)90192-6")}'
_S_H5=f'Hayflick L. The limited in vitro lifetime of human diploid cell strains. Exp Cell Res. 1965;37(3):614-636. {ts_doi("10.1016/0014-4827(65)90211-9")}'
_S_OB=f'Serrano M. Leonard Hayflick (1928-2024) – obituary. npj Aging. 2024;10(1). {ts_doi("10.1038/s41514-024-00174-0")} The approximate subcultivation and doubling counts are this obituary\'s summary of the 1961 and 1965 papers.'
_S_WA=f'Watson JD. Origin of Concatemeric T7 DNA. Nat New Biol. 1972;239(94):197-201. {ts_doi("10.1038/newbio239197a0")} Crossref spells the title Concatemeric.'
_S_OL=f'Olovnikov AM. A theory of marginotomy. J Theor Biol. 1973;41(1):181-190. {ts_doi("10.1016/0022-5193(73)90198-7")}'
_S_GR=f'Greider CW, Blackburn EH. Identification of a specific telomere terminal transferase activity in Tetrahymena extracts. Cell. 1985;43(2):405-413. {ts_doi("10.1016/0092-8674(85)90170-9")}'
_S_HA=f'Harley CB, Futcher AB, Greider CW. Telomeres shorten during ageing of human fibroblasts. Nature. 1990;345(6274):458-460. {ts_doi("10.1038/345458a0")}'
_S_WR=f'Wright WE, Tesmer VM, Huffman KE, Levene SD, Shay JW. Normal human chromosomes have long G-rich telomeric overhangs at one end. Genes Dev. 1997;11(21):2801-2809. {ts_doi("10.1101/gad.11.21.2801")} The 40 to 200 base-pair range summarizes cultured human cells, Harley 1990 among the papers cited there.'
_S_AL=f'Allsopp RC, Vaziri H, Patterson C, et al. Telomere length predicts replicative capacity of human fibroblasts. Proc Natl Acad Sci U S A. 1992;89(21):10114-10118. {ts_doi("10.1073/pnas.89.21.10114")}'
_S_BO=f'Bodnar AG, Ouellette M, Frolkis M, et al. Extension of life-span by introduction of telomerase into normal human cells. Science. 1998;279(5349):349-352. {ts_doi("10.1126/science.279.5349.349")}'
_S_KI=f'Kipling D, Cooke HJ. Hypervariable ultra-long telomeres in mice. Nature. 1990;347(6291):400-402. {ts_doi("10.1038/347400a0")}'
_S_HE=f'Hemann MT, Greider CW. Wild-derived inbred mouse strains have short telomeres. Nucleic Acids Res. 2000;28(22):4474-4478. {ts_doi("10.1093/nar/28.22.4474")} The two maximal lifespans are a personal communication printed in that paper. The 5 to 7 years for Peromyscus leucopus are cited there from Sacher and Hart, 1978.'
_S_GO=f'Gomes NM, Ryder OA, Houck ML, et al. Comparative biology of mammalian telomeres: hypotheses on ancestral states and the roles of telomeres in longevity determination. Aging Cell. 2011;10(5):761-768. {ts_doi("10.1111/j.1474-9726.2011.00718.x")}'
_S_MU=f'Müezzinler A, Zaineddin AK, Brenner H. A systematic review of leukocyte telomere length and age in adults. Ageing Res Rev. 2013;12(2):509-519. {ts_doi("10.1016/j.arr.2013.01.003")}'
_S_MR=f'Martin-Ruiz CM, Baird D, Roger L, et al. Reproducibility of telomere length assessment: an international collaborative study. Int J Epidemiol. 2015;44(5):1673-1683. {ts_doi("10.1093/ije/dyu191")}'
_S_KIM=f'Kim NW, Piatyszek MA, Prowse KR, et al. Specific association of human telomerase activity with immortal cells and cancer. Science. 1994;266(5193):2011-2015. {ts_doi("10.1126/science.7605428")}'
_S_CA=f'Cawthon RM, Smith KR, O\'Brien E, Sivatchenko A, Kerber RA. Association between telomere length in blood and mortality in people aged 60 years or older. Lancet. 2003;361(9355):393-395. {ts_doi("10.1016/S0140-6736(03)12384-7")} The heart-disease interval is 1.36 to 7.45. PubMed prints the lower bound across a line break.'
_S_HY=f'Haycock PC, Burgess S, Nounu A, et al. Association between telomere length and risk of cancer and non-neoplastic diseases: a Mendelian randomization study. JAMA Oncol. 2017;3(5):636-651. {ts_doi("10.1001/jamaoncol.2016.5945")}'
_S_DK=f'Heiss NS, Knight SW, Vulliamy TJ, et al. X-linked dyskeratosis congenita is caused by mutations in a highly conserved gene with putative nucleolar functions. Nat Genet. 1998;19(1):32-38. {ts_doi("10.1038/ng0598-32")}'
_S_MI=f'Mitchell JR, Wood E, Collins K. A telomerase component is defective in the human disease dyskeratosis congenita. Nature. 1999;402(6761):551-555. {ts_doi("10.1038/990141")}'
_S_VU=f'Vulliamy T, Marrone A, Goldman F, et al. The RNA component of telomerase is mutated in autosomal dominant dyskeratosis congenita. Nature. 2001;413(6854):432-435. {ts_doi("10.1038/35096585")}'
_S_AR=f'Armanios M, Blackburn EH. The telomere syndromes. Nat Rev Genet. 2012;13(10):693-704. {ts_doi("10.1038/nrg3246")}'
_S_BL=f'Blasco MA, Lee HW, Hande MP, et al. Telomere shortening and tumor formation by mouse cells lacking telomerase RNA. Cell. 1997;91(1):25-34. {ts_doi("10.1016/S0092-8674(01)80006-4")}'
_S_LE=f'Lee HW, Blasco MA, Gottlieb GJ, Horner JW 2nd, Greider CW, DePinho RA. Essential role of mouse telomerase in highly proliferative organs. Nature. 1998;392(6676):569-574. {ts_doi("10.1038/33345")}'
_S_JA=f'Jaskelioff M, Muller FL, Paik JH, et al. Telomerase reactivation reverses tissue degeneration in aged telomerase-deficient mice. Nature. 2011;469(7328):102-106. {ts_doi("10.1038/nature09603")}'
_S_B1=f'Baker DJ, Wijshake T, Tchkonia T, et al. Clearance of p16Ink4a-positive senescent cells delays ageing-associated disorders. Nature. 2011;479(7372):232-236. {ts_doi("10.1038/nature10600")}'
_S_B6=f'Baker DJ, Childs BG, Durik M, et al. Naturally occurring p16Ink4a-positive cells shorten healthy lifespan. Nature. 2016;530(7589):184-189. {ts_doi("10.1038/nature16932")}'
_S_SE=f'Serrano M, Lin AW, McCurrach ME, Beach D, Lowe SW. Oncogenic ras provokes premature cell senescence associated with accumulation of p53 and p16INK4a. Cell. 1997;88(5):593-602. {ts_doi("10.1016/S0092-8674(00)81902-9")}'
_S_DF=f'd\'Adda di Fagagna F, Reaper PM, Clay-Farrace L, et al. A DNA damage checkpoint response in telomere-initiated senescence. Nature. 2003;426(6963):194-198. {ts_doi("10.1038/nature02118")}'
_S_L3=f'López-Otín C, Blasco MA, Partridge L, Serrano M, Kroemer G. The hallmarks of aging. Cell. 2013;153(6):1194-1217. {ts_doi("10.1016/j.cell.2013.05.039")}'
_S_L23=f'López-Otín C, Blasco MA, Partridge L, Serrano M, Kroemer G. Hallmarks of aging: an expanding universe. Cell. 2023;186(2):243-278. {ts_doi("10.1016/j.cell.2022.11.001")}'

def ts_chart():
    bars=_M['bars']
    L,R,T,row=268,930,28,52
    xmin,xmax=5.0,200.0
    def X(v): return L+(math.log10(float(v))-math.log10(xmin))/(math.log10(xmax)-math.log10(xmin))*(R-L)
    H=T+len(bars)*row+28
    col={'spretus':'var(--u)','human':'var(--acc)','leucopus':'var(--u)','cast':'var(--u)','fvb':'var(--s)','inbred':'var(--muted)'}
    o=[f'<svg class="ts" viewBox="0 0 980 {H+24}" role="img" aria-label="Logarithmic comparison of published telomere lengths. Human blood averages about 10 kilobases. CAST/Ei is about 18 to 20. FVB/NJ is about 30 to 120. Established inbred mice are cited at 30 to 150. Not one experiment.">']
    o.append('<g data-part="bars">')
    for v in (10,20,50,100,150):
        x=X(v)
        o.append(f'<line class="grid" x1="{x:.1f}" y1="{T-6}" x2="{x:.1f}" y2="{T+len(bars)*row-8}"/>')
        o.append(f'<text class="sm" x="{x:.1f}" y="{H}" text-anchor="middle">{v}</text>')
    o.append(f'<line class="axis" x1="{L}" y1="{T-6}" x2="{L}" y2="{T+len(bars)*row-8}"/>')
    o.append(f'<text class="sm" x="{(L+R)/2:.0f}" y="{H+18}" text-anchor="middle">Kilobases, logarithmic. A point is an average. A bar is a stated range.</text>')
    for i,b in enumerate(bars):
        y=T+i*row+22
        c=col[b['id']]
        o.append(f'<text x="{L-10}" y="{y+4}" text-anchor="end">{ts_esc(b["label"])}</text>')
        if b['kind']=='point':
            x=X(b['low'])
            o.append(f'<circle cx="{x:.1f}" cy="{y}" r="6" fill="{c}"/>')
            o.append(f'<text x="{x+12:.1f}" y="{y+4}" fill="{c}">about {b["low"]}</text>')
        else:
            x1,x2=X(b['low']),X(b['high'])
            if b['kind']=='cited':
                o.append(f'<rect x="{x1:.1f}" y="{y-6}" width="{x2-x1:.1f}" height="12" fill="{c}" fill-opacity="0.28" stroke="{c}" stroke-width="1.4" stroke-dasharray="4 3" rx="2"/>')
            else:
                o.append(f'<rect x="{x1:.1f}" y="{y-6}" width="{max(x2-x1,4):.1f}" height="12" fill="{c}" rx="2"/>')
            o.append(f'<text class="sm" x="{x2+6:.1f}" y="{y+4}">{b["low"]} to {b["high"]}</text>')
    o.append('</g></svg>')
    return ''.join(o)

def ts_table():
    src={'human':'Kipling and Cooke, 1990','inbred':'Hemann and Greider, 2000, citing Kipling and Cooke, 1990'}
    body=''.join('<tr>'+''.join(f'<td data-l="{h}">{v}</td>' for h,v in zip(('Row','As published','Source'),(ts_esc(b['label']),ts_esc(b['stat']),ts_esc(src.get(b['id'],'Hemann and Greider, 2000')))))+'</tr>' for b in _M['bars'])
    return '<div class="rtbl-wrap"><table class="rtbl"><thead><tr><th>Row</th><th>As published</th><th>Source</th></tr></thead><tbody>'+body+'</tbody></table></div>'

def ts_or_table():
    body=''
    for row in _Y['rows']:
        body+='<tr>'+''.join(f'<td data-l="{h}">{v}</td>' for h,v in zip(('Disease','Odds ratio per SD longer','95 percent interval'),(ts_esc(row['disease']),ts_or(row['or']),f'{ts_or(row["ci"][0])} to {ts_or(row["ci"][1])}')))+'</tr>'
    return '<div class="rtbl-wrap"><table class="rtbl"><thead><tr><th>Disease</th><th>Odds ratio per SD longer</th><th>95 percent interval</th></tr></thead><tbody>'+body+'</tbody></table></div>'

_w=D['wrightBpPerDivision']
_LEG=('<div class="ts-leg"><span><i class="h"></i>Human blood, an average</span>'
      '<span><i></i>Shorter mouse telomeres, Hemann and Greider</span>'
      '<span><i class="l"></i>FVB/NJ, their approximate range</span>'
      '<span><i class="c"></i>Established inbred mice, the range they cite from Kipling and Cooke</span></div>')
F1=('<!--noart-->'+TS_CSS
    +'<div class="ts-split" data-part="split"><p><b>Finite division.</b> Normal human diploid cells stop dividing after a limited time in culture. Hayflick and Moorhead, 1961, and Hayflick, 1965.</p>'
    '<p><b>An unfinished end.</b> DNA copying does not finish the extreme 3′ end of a linear chromosome. Olovnikov, 1973. Watson, 1972, is the independent statement.</p>'
    '<p><b>Adding the end back.</b> Telomerase. Greider and Blackburn, 1985, in Tetrahymena. Bodnar and colleagues, 1998, in normal human cells.</p></div>'
    +f'<p class="ts-quote" data-part="verbatim">{ts_esc(TS_VERBATIM)}</p>'
    +'<ol class="ts-tl" style="margin-top:12px">'
    f'<li data-part="hayflick61"><span class="yr">1961</span><div><span class="ts-k">Finite division</span><b>Hayflick and Moorhead, Experimental Cell Research.</b> Diploid cell strains stop. Cell lines do not. Serrano, npj Aging, 2024, summarizing that paper: {_H["fetalIsolates"]} independent fetal isolates degenerated after approximately {_H["subcultivationsAbout"]} subcultivations. That count is the obituary\'s, not a table reprinted here.</div></li>'
    f'<li data-part="hayflick65"><span class="yr">1965</span><div><span class="ts-k">Donor age</span><b>Hayflick, Experimental Cell Research.</b> The same obituary, citing this paper: adult lung fibroblasts, mostly donors aged {_H["adultDonorAges"]}, approximately {_H["adultDoublingsAbout"]} doublings, against approximately {_H["fetalDoublingsAbout"]} for fetal lung fibroblasts. Subcultivations and doublings are left in the words the obituary uses.</div></li>'
    '<li data-part="olovnikov"><span class="yr">1972</span><div><span class="ts-k">The end</span><b>Watson, Nature New Biology, then Olovnikov, Journal of Theoretical Biology, 1973.</b> Marginotomy is Olovnikov\'s name for the incomplete copying of the end. Watson\'s paper is Origin of Concatemeric T7 DNA. Wright and colleagues, 1997, cite both for the primer problem at the extreme 3′ end.</div></li>'
    '<li data-part="greider"><span class="yr">1985</span><div><span class="ts-k">Telomerase</span><b>Greider and Blackburn, Cell.</b> A Tetrahymena extract adds TTGGGG repeats. That is the ciliate repeat, not human TTAGGG. Heat and proteinase K destroy the activity.</div></li>'
    '<li data-part="harley"><span class="yr">1990</span><div><span class="ts-k">Shortening</span><b>Harley, Futcher, and Greider, Nature.</b> Telomeric DNA in human fibroblasts shortens with serial passage, and possibly with age. They say a causal role in senescence is not known. No base-pair rate in the abstract.</div></li>'
    f'<li data-part="bodnar"><span class="yr">1998</span><div><span class="ts-k">The test</span><b>Bodnar and colleagues, Science.</b> The human telomerase catalytic subunit in retinal pigment epithelial cells and foreskin fibroblasts. Telomeres lengthened. The clones had already exceeded their normal lifespan by at least {D["bodnarExtraDoublingsAtLeast"]} doublings, with a normal karyotype. Cells in a dish.</div></li>'
    +'</ol>'+ts_src([_S_H1,_S_H5,_S_OB,_S_WA,_S_OL,_S_GR,_S_HA,_S_WR,_S_BO,_S_KI]))
F2=('<!--noart-->'
    +'<p class="ts-note" data-part="scheme">Schematic, not to scale. The bars are not base pairs. Vertebrate repeat TTAGGG, Kipling and Cooke, 1990. The rates underneath are the published numbers.</p>'
    +'<div class="ts-end" aria-hidden="true"><div><i style="width:74px;height:18px"></i><span>Early passage</span></div><div><i style="width:48px;height:18px"></i><span>Later</span></div><div><i style="width:22px;height:18px"></i><span>Near the stop</span></div></div>'
    +'<div class="ts-rates">'
    f'<div class="ts-box" data-part="problem"><b>{_w[0]} to {_w[1]} base pairs per division.</b> Wright and colleagues, 1997, for normal diploid human cells in culture. A range across the studies they cite, Harley 1990 among them. Not the length of the RNA primer. Yeast, in the same paper, loses only a few base pairs per division without telomerase.</div>'
    f'<div class="ts-box" data-part="slope"><b>{_A["doublingsPerKb"]} doublings per kilobase.</b> Allsopp and colleagues, 1992. {_A["donors"]} donors, ages {_A["ageLow"]} to {_A["ageHigh"]}. Replicative capacity against starting telomere length, r = {_A["rCapacityLength"]}, P = {_A["pCapacityLength"]}. A regression across donors, not a conversion of the 40 to 200 range.</div>'
    f'<div class="ts-box" data-part="telomerase"><b>At least {D["bodnarExtraDoublingsAtLeast"]} extra doublings.</b> Bodnar and colleagues, 1998, after the human catalytic subunit. Greider and Blackburn, 1985, found the activity in Tetrahymena. Harley, 1990, had left the cause open.</div>'
    f'<div class="ts-box" data-part="age"><b>{_A["bpPerYear"]} base pairs per year in donors.</b> The same Allsopp paper. Telomeric DNA against donor age, r = {_A["rTelomereAge"]}, P = {_A["pTelomereAge"]}. Doublings against age, {_A["doublingsPerYear"]} per year, r = {_A["rDoublingsAge"]}, P = {_A["pDoublingsAge"]}. They call both relatively weak. Sperm telomeres did not shorten with donor age.</div>'
    +'</div>'+ts_src([_S_WR,_S_HA,_S_AL,_S_BO,_S_GR,_S_KI]))
F3=('<!--noart-->'
    +'<p class="ts-note" data-part="design">Not one experiment. Human blood is an average from Kipling and Cooke, 1990. The mouse rows are Hemann and Greider, 2000. Mus spretus is a range they state from earlier work. The dashed row is a citation, not a new gel. Logarithmic axis.</p>'
    +'<div class="art">'+ts_chart()+'</div>'+_LEG+ts_table()
    +f'<p class="ts-note" data-part="lifespan">Lifespan, from Hemann and Greider, printed beside length and not drawn as a second axis. C57BL/6J maximal lifespan {_M["c57Days"]} ± {_M["c57Sd"]} days. CAST/Ei {_M["castDays"]} ± {_M["castSd"]} days. They say the difference was not significant. The paper does not say what the plus-or-minus is. Those lifespans are a personal communication in the paper. C57BL/6J telomeres were long and heterogeneous, so they have no kilobase midpoint on the chart. P. leucopus, about {_M["bars"][2]["low"]} kb, averages {_M["leucopusYearsLow"]} to {_M["leucopusYearsHigh"]} years in Sacher and Hart, 1978, as cited there. The shortest telomeres they studied went with the longest lifespan.</p>'
    +f'<p class="ts-note" data-part="gomes">Gomes and colleagues, 2011, a different comparison. Laboratory mice {_G["labMouseKb"][0]} to {_G["labMouseKb"][1]} kb, human germline {_G["humanGermlineKb"][0]} to {_G["humanGermlineKb"][1]} kb. Not the blood average of about {_K["humanBloodKbAbout"]} kb. Telomere length co-evolved with lifespan, P = {_G["pLifespan"]}, no independent association with body size, P = {_G["pSize"]}. The direction is inverse. Ancestral placental length {_G["ancestralKb"]} kb. Probability telomerase was repressed, {_G["telomeraseRepressed"]}, against {_G["telomeraseExpressed"]} that it was expressed. Only differences above {_G["significantDifferenceKb"]} kb are treated as significant in that paper. Their species supplement is not replotted here.</p>'
    +f'<p class="enote" data-part="limit">Kipling and Cooke\'s up to {_K["mouseFragmentsUpToKb"]} kb is an upper end of mouse fragments, not a mean. The chart does not show that telomeres are irrelevant. It shows that a longer telomere is not a longer species life. Late-generation telomerase knockout mice are the next figure.</p>'
    +ts_src([_S_KI,_S_HE,_S_GO]))
_b0,_b1=_P['bySexPct']; _n0,_n1=_P['noTumorPct']
_zL,_zH=_Z['longitudinalBpYear']; _r0,_r1=_R['rankR']
F4=('<!--noart-->'
    +'<div class="ts-flow"><p class="ts-arr">One end, two consequences</p><div class="ts-3" data-part="tradeoff">'
    '<div class="ts-box"><b>Short.</b> The end is read as a DNA break. d\'Adda di Fagagna and colleagues, 2003: senescent fibroblasts show break markers, the chromosome ends contribute, and blocking the checkpoint kinases lets the cells enter S phase.</div>'
    '<div class="ts-box"><b>The brake.</b> Telomerase is off in the normal somatic tissues Kim tested, and on in most of the cancers. Senescence stops a cell that would keep dividing on a bare end.</div>'
    '<div class="ts-box"><b>Long, or telomerase on.</b> The division count is extended. The genetic studies put the cancer odds up, and some cardiovascular odds down.</div></div>'
    +f'<div class="ts-box" data-part="cancer"><b>Where telomerase is found.</b> Kim and colleagues, 1994. Immortal cultures {_Kim["immortalPositive"]} of {_Kim["immortal"]}. Mortal cultures {_Kim["mortalPositive"]} of {_Kim["mortal"]}. Tumor biopsies {_Kim["tumorPositive"]} of {_Kim["tumors"]}, {_Kim["tumorTypes"]} tumor types. Normal somatic tissues {_Kim["normalSomaticPositive"]} of {_Kim["normalSomatic"]}. Ovary and testis positive. Fibroids negative. <b>Mendelian randomization.</b> Haycock and colleagues, 2017. {_Y["cancers"]} cancers and {_Y["nonNeoplastic"]} non-neoplastic diseases. {_Y["cases"]:,} cases and {_Y["controls"]:,} controls. Odds ratio per standard deviation longer telomere. The table is the abstract\'s list.</div>'
    +ts_or_table()
    +f'<div class="ts-box" data-part="syndromes"><b>Telomere syndromes.</b> Heiss and colleagues, 1998, identified DKC1. Mitchell, Wood, and Collins, 1999: less telomerase RNA, less activity, shorter telomeres than matched cells. Vulliamy and colleagues, 2001: an {_V["deletionBp"]}-base-pair deletion removing the 3′ {_V["htrBasesRemoved"]} bases of telomerase RNA, plus mutations in two other families. Armanios and Blackburn, 2012: marrow failure and lung fibrosis on the same short-telomere spectrum. Inherited disease, not the ordinary rate of aging.</div>'
    +f'<div class="ts-box" data-part="mice"><b>Telomerase-deficient mice.</b> Blasco and colleagues, 1997: viable for {_B["generationsViable"]} generations, telomeres shorter by {_B["kbPerGeneration"]} ± {_B["kbPerGenerationSd"]} kb per generation. From generation {_B["abnormalFromGeneration"]}, ends with no detectable repeats, and fusions. Cells could still immortalize and form tumors. Lee and colleagues, 1998: late-generation failure in testis and in blood-forming organs. Jaskelioff and colleagues, 2011: switching telomerase back on in that deficient line reversed degeneration in testis, spleen, intestine, and brain. Not ordinary wild-type aging. <b>Senescent cells, a different entrance.</b> Baker and colleagues, 2011, BubR1 progeroid mice: clearing p16-positive cells delayed changes in fat, muscle, and eye. Baker and colleagues, 2016, wild-type mice from {_P["startAgeYear"]} year of age: median lifespan up {_P["medianMixedPct"]} percent on the mixed background and {_P["medianB6Pct"]} percent in C57BL/6, sexes combined. By sex, {_b0} to {_b1} percent. Without a tumor, {_n0} to {_n1} percent. Maximum lifespan rose for the mixed sexes combined, P = {_P["maxLifespanMixedP"]}, and did not rise in C57BL/6. No benefit without the transgene. The mixed cohort\'s {_P["mixedDietFatPct"]} percent fat diet shortens life relative to a {_P["standardDietFatPct"]} percent fat diet, which the paper says outright.</div></div>'
    +'<div class="ts-two" style="margin-top:10px"><div class="ts-col ok" data-part="agree"><h4>Broadly accepted</h4><ul>'
    '<li>Normal human diploid cells in culture have a finite division count.</li>'
    '<li>Telomeres shorten as human fibroblasts are passaged. Telomerase extended that count by at least 20 doublings in the Bodnar experiment, with a normal karyotype there.</li>'
    '<li>In the tissues Kim tested, telomerase is on in most cancers and off in normal somatic tissue.</li>'
    '<li>Inherited telomerase failure causes short-telomere disease, including dyskeratosis congenita.</li>'
    '<li>Telomerase-deficient mice shorten their telomeres across generations. Turning the enzyme back on reversed several failures in that model.</li>'
    '<li>Clearing p16-positive cells extended median lifespan in the 2016 wild-type mice, with the limits in the box above.</li>'
    '<li>Telomere attrition is a hallmark in López-Otín and colleagues, 2013, and remains one in the 2023 list of twelve.</li></ul></div>'
    +'<div class="ts-col no"><h4>Contested, or a different mechanism</h4><ul>'
    f'<li data-part="weak">Weak as a clock of age. Allsopp: r = {_A["rTelomereAge"]} against donor age, {_A["bpPerYear"]} base pairs per year. Müezzinler and colleagues: {_Z["crossSectional"]} cross-sectional studies, r = {_Z["rAbsolute"]} for absolute length, {_Z["bpYearFromMeans"]} base pairs per year from the study means, and {_zL} to {_zH} in the few longitudinal studies. Martin-Ruiz and colleagues: rankings correlate {_r0} to {_r1}, but absolute lengths do not travel between laboratories. Quantitative PCR varied by more than {_R["cvQpcrMoreThanPct"]} percent between laboratories. Cawthon and colleagues: {_C["n"]} people over {_C["ageOver"]}, an association, {_C["heartFold"]}-fold for heart-disease death and {_C["infectionFold"]}-fold for infection, the second interval {_C["infectionCi"][0]} to {_C["infectionCi"][1]}.</li>'
    '<li>Mice with long telomeres do not live long human lives, and within mice the short-telomere strains were not the short-lived ones. Across mammals, Gomes and colleagues found shorter telomeres with longer lifespan.</li>'
    '<li>The cancer tradeoff. Haycock and colleagues: longer telomeres, higher odds of several cancers, lower odds of coronary heart disease. Keeping the end long is not free.</li>'
    '<li data-part="open">Senescence has other entrances. Serrano and colleagues, 1997: oncogenic ras provokes a senescence-like arrest in primary cells. Baker\'s mice were not telomerase knockouts. Still open: how much of ordinary human aging is the division limit, how much is other damage, and how much of the mortality association is cause. The rescue and the extra doublings were in a deficient mouse and in a dish.</li></ul></div></div>'
    +ts_src([_S_DF,_S_KIM,_S_HY,_S_CA,_S_DK,_S_MI,_S_VU,_S_AR,_S_BL,_S_LE,_S_JA,_S_B1,_S_B6,_S_SE,_S_AL,_S_MU,_S_MR,_S_HE,_S_GO,_S_L3,_S_L23]))
def ts_card(href,kicker,title,text):
    return f'<a href="../literature/{href}"><small>{kicker}</small><b>{ts_esc(title)}</b><span>{text}</span></a>'
F5=('<!--noart-->'
    +'<p data-part="bridge">These cards open pages in Peer-Reviewed Literature, part of this course. Each line is only what that page says.</p>'
    +'<div class="ts-cards" data-part="measure" style="margin-top:12px">'
    +ts_card('nanoscale-imaging-single-molecule-telomere-length.html','Telomere measurement','One telomere at a time','A preprint method measures single telomeres, from about 50 base pairs to more than 50 kilobases, so a few critically short ends are not hidden by the average. The page says it is not peer reviewed, the synopsis is the abstract, and the test is not shown to predict disease or aging.')
    +'</div><div class="ts-cards" data-part="senescence" style="margin-top:10px">'
    +ts_card('tubulin-acetylation-nuclear-fluctuations-dna-repair.html','Senescence','A break, then a stop','Blocking a tag on tubulin stopped the nucleus fluctuating, impaired accurate repair, and the cells became senescent. The page says the abstract does not name the cells, and that this was not tested in a living animal. It does not say the breaks were short telomeres.')
    +'</div><div class="ts-cards" data-part="heart" style="margin-top:10px">'
    +ts_card('nad-replenishment-cardiomyocyte-senescence-aged-heart.html','Senescence, in mice','An aged male heart','In old male mice, two months of an NAD precursor reduced heart-cell senescence and improved filling between beats. Old females did not respond. The page says the abstract gives no doses or animal numbers, and that this is mice and cells. It does not blame short telomeres.')
    +'</div>')

TS_LESSON=[
 ('Where the idea came from','A finite number of divisions, an end that is hard to copy, and an enzyme that adds the end back.',F1),
 ('How the end shortens','A schematic of one division, then the rates the papers actually print.',F2),
 ('Length, in published numbers','Human blood and mouse telomeres, only the ranges and averages the papers state.',F3),
 ('Senescence, cancer, and the argument','The tradeoff, then what is broadly accepted and what is still contested.',F4),
 ('From the literature','Reading-room pages on measuring telomeres and on senescence. Only what those pages say.',F5),
]
TS_CAPS=[
 'Hayflick and Moorhead, 1961, and Hayflick, 1965, are the finite-division papers. The approximate counts are Serrano, npj Aging, 2024, summarizing those papers, which have no Europe PMC abstract. Olovnikov, 1973, is marginotomy. Watson, 1972, is the independent end-replication paper. Greider and Blackburn, 1985, is Tetrahymena telomerase. Harley, Futcher, and Greider, 1990, is shortening in human fibroblasts, cause left open. Bodnar and colleagues, 1998, is the extension by at least 20 doublings.',
 'The drawing is not to scale. 40 to 200 base pairs per division is Wright and colleagues, 1997, a range across cultured-cell studies. Ten doublings per kilobase, and minus 15 base pairs per year, are Allsopp and colleagues, 1992. The extra doublings are Bodnar and colleagues, 1998.',
 'Points and bars are published averages and ranges. Human blood, about 10 kb, is Kipling and Cooke, 1990. Mouse rows are Hemann and Greider, 2000, except the dashed 30 to 150 kb row, which they cite from Kipling and Cooke. Lifespans in the note are the ones Hemann and Greider print. Gomes and colleagues, 2011, is the cross-mammal note, not a second set of bars.',
 'The fork is the senescence and cancer tradeoff. Counts are Kim and colleagues, 1994, and Haycock and colleagues, 2017. Syndromes are Heiss 1998, Mitchell 1999, Vulliamy 2001, and Armanios and Blackburn 2012. Mouse telomerase is Blasco 1997, Lee 1998, and Jaskelioff 2011. Clearance of p16-positive cells is Baker 2011 and 2016. The two columns separate what those papers support from what they dispute. The age correlations are Allsopp 1992, Müezzinler 2013, Martin-Ruiz 2015, and Cawthon 2003. Ras senescence is Serrano and colleagues, 1997.',
 'Links open the existing reading-room pages. Nothing is added beyond what those pages say.',
]
TS_QUIZ=[
 ('What did Hayflick and Moorhead show in 1961?','That normal human diploid cell strains stop dividing in culture, unlike immortal cell lines. The approximate 50 subcultivations is Serrano\'s 2024 summary of that paper, not a table reprinted in this lesson (Figure 1).'),
 ('How is Olovnikov\'s marginotomy different from telomerase?','Marginotomy is the incomplete copying of a chromosome end. Telomerase is the enzyme that adds repeats back. Greider and Blackburn, 1985, found that activity in Tetrahymena, adding TTGGGG, not human TTAGGG (Figure 1).'),
 ('What did Harley, Futcher, and Greider show, and what did they leave open?','Telomeres shorten as human fibroblasts are passaged. They said it was not known whether that loss causes senescence (Figure 1).'),
 ('What did Bodnar and colleagues test?','Putting the human telomerase catalytic subunit into normal human cells lengthened telomeres and let the cultures pass their usual limit by at least 20 doublings, with a normal karyotype in that paper. It was cells in a dish (Figures 1 and 2).'),
 ('Why are 40 to 200 base pairs and 10 doublings per kilobase not the same number?','40 to 200 is a range of loss per division in cultured human cells, from Wright and colleagues, 1997. Ten doublings per kilobase is Allsopp\'s regression of remaining divisions on starting length, r = 0.76 (Figure 2).'),
 ('What does the species chart show about mice?','Laboratory mice can have very long telomeres. CAST/Ei, about 18 to 20 kb, and C57BL/6J, with long telomeres, did not differ significantly in the maximal lifespans Hemann and Greider report. Gomes and colleagues found shorter telomeres with longer mammal lifespans (Figure 3).'),
 ('What is the cancer side of a long telomere?','Kim and colleagues found telomerase in 90 of 101 tumor biopsies and in none of 50 normal somatic tissues. Haycock and colleagues found that genetically longer telomeres raise the odds of several cancers, including glioma, and lower the odds of coronary heart disease (Figure 4).'),
 ('What is dyskeratosis congenita doing on this figure?','It is an inherited short-telomere disease. DKC1, telomerase RNA, and short telomeres in patients\' cells show that telomere failure can cause proliferative disease. It is not a measurement of ordinary aging (Figure 4).'),
 ('What did Jaskelioff and colleagues reverse, and in which mice?','Tissue degeneration, including in the brain, after telomerase was switched back on. The mice were late-generation telomerase-deficient mice, not ordinary old wild-type mice (Figure 4).'),
 ('Why is telomere length still contested as a clock of human aging?','The correlation with age is weak, laboratories do not agree on absolute length, mice with long telomeres are not long-lived for that reason, and senescence is also triggered by oncogenic ras. Mortality findings such as Cawthon\'s are associations (Figure 4).'),
 ('What do the reading-room pages not show?','They do not show that a telomere assay, a nuclear fluctuation, or an NAD precursor produced the historical rise in population life expectancy. The measurement paper is a preprint about a method. The heart result is old male mice (Figure 5).')]
_figs=[figure_card(i,t,h,c,sub=s) for i,((t,s,h),c) in enumerate(zip(TS_LESSON,TS_CAPS),1)]
_quiz='<main class="lp-after"><section class="notes quiz" id="quiz"><h2>Quiz</h2><p class="lbl">Tap a question to see the answer</p>'+''.join(f'<details><summary>{n}. {q}</summary><p>{a}</p></details>' for n,(q,a) in enumerate(TS_QUIZ,1))+'</section></main>'
lesson_page('telomere-senescence','Module 3 · Telomeres and Replicative Senescence · '+COURSE+' · '+UNIVERSITY_NAME,
 '<nav class="crumbs">'+CRUMB_HOME+' › Module 3</nav><h1>Module 3 · Telomeres and Replicative Senescence</h1>'
 '<p>Telomeres, the repeated DNA at chromosome ends, and the limit on how many times many human cells can divide. The history runs from Hayflick to telomerase. The chart uses only published lengths. The argument separates what those papers agree on from the cancer tradeoff, the weak link to calendar age, and the fact that senescence has other causes. The figure is on the left and the lesson script on the right. The approximate Hayflick counts are a 2024 summary of the 1961 and 1965 papers. Every other number is taken from the paper named beside it.</p>',
 _figs,_quiz+pn(('Module 2 · The Mutation Theory of Aging','mutation-theory.html'),None))
