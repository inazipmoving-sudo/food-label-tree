# Module 1 · Five Hundred Years of Life Expectancy. Charts from gen/data/longevity-life-expectancy.json.
# exec'd by gen/longevity.py while COURSE/OUT point at /longevity/.
D=json.load(open(os.path.join(GEN,'data','longevity-life-expectancy.json'),encoding='utf-8'))
_E=D['englandLifeExpectancyAtBirth']['points']
_W=D['worldLifeExpectancyAtBirth']['points']
_A=D['englandAge15PlusE15']['measured']['points']
_AE=D['englandAge15PlusE15']['earlySummary']
_CU=D['childMortalityUnder5']['unitedKingdom']['points']
_CW=D['childMortalityUnder5']['world']['points']
_BAND=D['childMortalityUnder5']['earlyEnglandBand']
def _yr(series,year,key='roundedYears'):
    return next(p[key] for p in series if p['year']==year)
# Spoken numbers are tied to these rounded anchors. If a source refresh changes one, update the script in the same edit.
assert _yr(_E,1558)==22 and _yr(_E,1683)==31 and _yr(_E,1728)==25 and _yr(_E,1841)==42 and _yr(_E,1849)==37
assert _yr(_E,1870)==41 and _yr(_E,1914)==52 and _yr(_E,1917)==46 and _yr(_E,1918)==41 and _yr(_E,1940)==61
assert _yr(_E,1950)==69 and _yr(_E,1960)==71 and _yr(_E,2019)==81 and _yr(_E,2020)==80
assert _yr(_W,1800)==29 and _yr(_W,1900)==32 and _yr(_W,1950)==46 and _yr(_W,1970)==56
assert _yr(_W,1990)==64 and _yr(_W,2000)==66 and _yr(_W,2019)==73 and _yr(_W,2021)==71
assert _yr(_A,1841)==59 and _yr(_A,2023)==82 and _AE['roundedYears']==58
assert _yr(_CU,1841,'roundedPer1000')==250 and _yr(_CU,1870,'roundedPer1000')==270 and _yr(_CU,1900,'roundedPer1000')==230
assert _yr(_CU,1950,'roundedPer1000')==37 and _yr(_CU,2023,'roundedPer1000')==5
assert _yr(_CW,1800,'roundedPer1000')==430 and _yr(_CW,1950,'roundedPer1000')==250 and _yr(_CW,2023,'roundedPer1000')==38
_US=D['annotations']['unitedStates1918']
assert _US['roundedStart']==51 and _US['roundedEnd']==39 and _US['roundedDrop']==12
LY_VERBATIM='In England, those early averages were low mainly because a quarter to a third of children died before age five, while anyone who reached 15 could usually expect to live into their late fifties.'
_sc=open(os.path.join(GEN,'scripts','five-hundred-years.json'),encoding='utf-8').read()
assert LY_VERBATIM in _sc and '"verbatim": true' in _sc

LY_CSS='''<style>
.art svg.ly{min-width:700px;max-height:none}
.art svg.ly.sm{min-width:0}
.ly text{font-size:12px;fill:var(--text)}
.ly text.sm{font-size:11px;fill:var(--muted)}
.ly text.inv{fill:var(--card);font-weight:700;font-size:12px}
.ly .axis{stroke:var(--muted);stroke-width:1.2;fill:none}
.ly .grid{stroke:var(--line);stroke-width:1;fill:none}
.ly .eng{stroke:var(--acc);stroke-width:2.2;fill:none;stroke-linejoin:round;stroke-linecap:round}
.ly .wld{stroke:var(--t);stroke-width:2;fill:none;stroke-dasharray:7 4;stroke-linejoin:round}
.ly .a15{stroke:var(--u);stroke-width:2;fill:none;stroke-linejoin:round}
.ly .a15e{stroke:var(--u);stroke-width:1.7;fill:none;stroke-dasharray:2 3.5}
.ly .stem{stroke:var(--acc);stroke-width:1;fill:none;opacity:.75}
.ly .era{stroke:none}
.ly .est{fill:var(--card);stroke:var(--t);stroke-width:1.5}
.ly .us{stroke:var(--s);stroke-width:1.6;fill:none}
.ly-flags{list-style:none;margin:12px 0 0;padding:0;display:grid;gap:8px}
.ly-flags li{border:1px solid var(--line);border-radius:4px;padding:8px 12px;background:var(--bg);line-height:1.45}
.ly-flags .n{font-family:var(--serif);font-weight:600;color:var(--acc);margin-right:6px}
.ly-leg{display:flex;flex-wrap:wrap;gap:8px 16px;margin:10px 0 0;color:var(--muted);font-size:.92rem;line-height:1.4}
.ly-leg i{display:inline-block;width:22px;height:0;border-top:2px solid var(--acc);vertical-align:3px;margin-right:6px}
.ly-leg i.d{border-top:2px dashed var(--t)}
.ly-leg i.a{border-top-color:var(--u)}
.ly-leg i.e{border-top:2px dotted var(--u)}
.ly-leg i.b{width:12px;height:12px;border:0;background:var(--acc);opacity:.18;vertical-align:-2px}
.ly-quote{margin:14px 0 0;padding:12px 16px;border-left:3px solid var(--acc);background:var(--acc-soft);font-family:var(--serif);font-size:1.35rem;font-weight:600;line-height:1.35}
.ly-split{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-top:12px}
.ly-split p{margin:0;padding:10px 12px;border:1px solid var(--line);border-radius:4px;background:var(--bg);line-height:1.45}
.ly-cards{display:grid;gap:10px}
.ly-cards a{display:block;border:1px solid var(--line);border-radius:4px;padding:10px 14px;text-decoration:none;background:var(--bg);line-height:1.45}
.ly-cards a:hover{border-color:var(--acc)}
.ly-cards small{display:block;color:var(--muted);font-size:.68rem;letter-spacing:.14em;text-transform:uppercase;margin-bottom:2px}
.ly-cards b{font-family:var(--serif);font-weight:600;font-size:1.15rem}
.ly-src{margin-top:12px}
.ly-src summary{cursor:pointer;color:var(--muted);font-size:.92rem}
.ly-src ul{margin:8px 0 0;padding-left:18px;color:var(--muted);font-size:.9rem;line-height:1.45}
@media(max-width:600px){.ly-split{grid-template-columns:1fr}}
</style>'''
def _esc(s): return _html.escape(str(s),quote=True)
def _chart(series_key,y_max,y_step,aria,parts,extra_body,y_label):
    """Shared frame. parts is a dict of data-part -> svg fragment inserted in order."""
    ax=D['axis']; x0,x1=ax['xMin'],ax['xMax']
    L,R,T,B=62,948,64,384
    def X(year): return L+(year-x0)/(x1-x0)*(R-L)
    def Y(v): return B-(v/y_max)*(B-T)
    o=[f'<svg class="ly" viewBox="0 0 980 460" role="img" aria-label="{_esc(aria)}">']
    o.append(f'<g data-part="{parts["axes"]}">')
    for v in range(0,y_max+1,y_step):
        y=Y(v)
        o.append(f'<line class="grid" x1="{L}" y1="{y:.1f}" x2="{R}" y2="{y:.1f}"/>')
        o.append(f'<text class="sm" x="{L-8}" y="{y+4:.1f}" text-anchor="end">{v}</text>')
    for year in (1526,1600,1700,1800,1900,2000,2026):
        x=X(year)
        o.append(f'<line class="grid" x1="{x:.1f}" y1="{T}" x2="{x:.1f}" y2="{B}"/>')
        o.append(f'<text class="sm" x="{x:.1f}" y="{B+18}" text-anchor="middle">{year}</text>')
    o.append(f'<line class="axis" x1="{L}" y1="{T}" x2="{L}" y2="{B}"/><line class="axis" x1="{L}" y1="{B}" x2="{R}" y2="{B}"/>')
    o.append(f'<text class="sm" x="{(L+R)/2:.0f}" y="{B+36}" text-anchor="middle">Year. Lines stop at {ax["lastDataYear"]}. {x1} is the end of the axis, not a measurement.</text>')
    o.append(f'<text class="sm" x="16" y="{(T+B)/2:.0f}" text-anchor="middle" transform="rotate(-90 16 {(T+B)/2:.0f})">{_esc(y_label)}</text>')
    o.append('</g>')
    o.append(extra_body(X,Y))
    o.append('</svg>')
    return ''.join(o),X,Y

def _poly(pts,X,Y,key,cls,part):
    xy=' '.join(f'{X(p["year"]):.1f},{Y(p[key]):.1f}' for p in pts)
    return f'<polyline data-part="{part}" class="{cls}" points="{xy}"/>'

def _life_svg():
    ax=D['axis']
    def body(X,Y):
        b=[]
        # eras behind the lines
        for e,op in zip(D['eras'],(0.14,0.12,0.16,0.12)):
            x1,x2=X(e['fromYear']),X(min(e['toYear'],ax['xMax']))
            b.append(f'<rect class="era" data-part="{e["part"]}" x="{x1:.1f}" y="{Y(90):.1f}" width="{x2-x1:.1f}" height="{Y(0)-Y(90):.1f}" fill="var(--acc)" opacity="{op}"/>')
            b.append(f'<text class="sm" x="{(x1+x2)/2:.1f}" y="{Y(8):.1f}" text-anchor="middle">{_esc(e["label"])}</text>')
        # early age-15 level, then measured companion, then world, then England on top
        b.append(f'<line data-part="age15-early" class="a15e" x1="{X(_AE["fromYear"]):.1f}" y1="{Y(_AE["roundedYears"]):.1f}" x2="{X(_AE["toYear"]):.1f}" y2="{Y(_AE["roundedYears"]):.1f}"/>')
        b.append(f'<text class="sm" x="{X(1572):.1f}" y="{Y(_AE["roundedYears"])-8:.1f}">reached 15: late 50s (summary)</text>')
        b.append(_poly(_A,X,Y,'roundedYears','a15','age15'))
        b.append(_poly(_W,X,Y,'roundedYears','wld','world'))
        for p in _W:
            if p['estimate']:
                b.append(f'<circle class="est" cx="{X(p["year"]):.1f}" cy="{Y(p["roundedYears"]):.1f}" r="3.5"/>')
        b.append(_poly(_E,X,Y,'roundedYears','eng','england'))
        by={p['year']:p['roundedYears'] for p in _E}
        for i,f in enumerate(D['flags']):
            x,y=X(f['year']),Y(by[f['year']])
            cy=22 if f['id']!=5 else 44  # 4 and 5 are only ~18 years apart; drop 5 so the circles do not touch
            b.append(f'<g data-part="{f["part"]}"><line class="stem" x1="{x:.1f}" y1="{cy+11}" x2="{x:.1f}" y2="{y:.1f}"/>')
            b.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="3.2" fill="var(--acc)"/>')
            b.append(f'<circle cx="{x:.1f}" cy="{cy}" r="10" fill="var(--acc)"/><text class="inv" x="{x:.1f}" y="{cy+4}" text-anchor="middle">{f["id"]}</text></g>')
        return ''.join(b)
    svg,_X,_Y=_chart('life',90,30,'Life expectancy from 1526 to 2026. England is a solid line, the world is dashed, and a companion line shows England at age 15. Four eras are shaded and six flags are numbered.',{'axes':'axes'},body,'Life expectancy, years')
    # the helper hardcodes data-part axes; pass-through already used 'axes'
    return svg

def _child_svg():
    def body(X,Y):
        b=[]
        x1,x2=X(_BAND['fromYear']),X(_BAND['toYear'])
        y_hi,y_lo=Y(_BAND['highPer1000']),Y(_BAND['lowPer1000'])
        b.append(f'<rect data-part="cm-early" x="{x1:.1f}" y="{y_hi:.1f}" width="{x2-x1:.1f}" height="{y_lo-y_hi:.1f}" fill="var(--acc)" opacity="0.16"/>')
        b.append(f'<text class="sm" x="{(x1+x2)/2:.1f}" y="{(y_hi+y_lo)/2:.1f}" text-anchor="middle">England, about a quarter to a third</text>')
        b.append(_poly(_CW,X,Y,'roundedPer1000','wld','cm-world'))
        for p in _CW:
            if p['estimate']:
                b.append(f'<circle class="est" cx="{X(p["year"]):.1f}" cy="{Y(p["roundedPer1000"]):.1f}" r="3.5"/>')
        b.append(_poly(_CU,X,Y,'roundedPer1000','eng','cm-england'))
        for p in _CU:
            if p['estimate']:
                b.append(f'<circle class="est" cx="{X(p["year"]):.1f}" cy="{Y(p["roundedPer1000"]):.1f}" r="3.2"/>')
        return ''.join(b)
    # y max 500, step 100. Reuse _chart but it uses life-expectancy copy in the x caption. Fine.
    svg,_X,_Y=_chart('cm',500,100,'Child deaths before age five per 1,000 live births, England as a band then the United Kingdom, and the world.',{'axes':'cm-axes'},body,'Deaths before age 5 per 1,000')
    return svg

def _grid_svg():
    # 10 by 10. Dots 1-25 filled (a quarter). Dots 26-33 ringed (up to a third).
    o=['<svg class="ly sm" viewBox="0 0 640 300" role="img" aria-label="One hundred births. Twenty-five dots are filled, a quarter. Eight more are ringed, taking the count to thirty-three, a third." data-part="grid">']
    for i in range(100):
        c,r=i%10,i//10
        cx,cy=36+c*28,36+r*26
        if i<25:
            o.append(f'<circle cx="{cx}" cy="{cy}" r="9" fill="var(--s)"/>')
        elif i<33:
            o.append(f'<circle cx="{cx}" cy="{cy}" r="9" fill="none" stroke="var(--s)" stroke-width="2"/>')
        else:
            o.append(f'<circle cx="{cx}" cy="{cy}" r="9" fill="none" stroke="var(--line)" stroke-width="1.4"/>')
    o.append('<text x="330" y="40">Filled: 25 of 100, a quarter</text>')
    o.append('<text x="330" y="64">Ringed as well: 33 of 100, a third</text>')
    o.append('<text x="330" y="100">Those children die before age five.</text>')
    o.append('<text x="330" y="136">Reach 15: the late fifties.</text>')
    o.append('</svg>')
    return ''.join(o)

_VERIFY=D['verifyBeforePublishing']
def _flags_html():
    items=''.join(f'<li data-part="note-{f["id"]}"><span class="n">{f["id"]} · {_esc(f["title"])}.</span>{_esc(f["note"])}</li>' for f in D['flags'])
    items+=f'<li data-part="epilogue"><span class="n">After 1970.</span>{_esc(D["epilogue"]["note"])}</li>'
    return f'<ol class="ly-flags">{items}</ol>'
def _src_html():
    lis=''.join(f'<li><b>{_esc(k)}.</b> {_esc(v)}</li>' for k,v in D['sources'].items())
    return f'<details class="ly-src"><summary>Sources for these rounded figures</summary><ul>{lis}</ul><p class="fnote">{_esc(D["rounding"])}</p></details>'
_LEGEND=('<div class="ly-leg"><span><i></i>England, life expectancy at birth</span>'
 '<span><i class="d"></i>World, dashed. Open circles are estimates, before 1950</span>'
 '<span><i class="a"></i>England, age 15 + e15, measured from 1841</span>'
 '<span><i class="e"></i>Before 1841, only a level: the late fifties, not a yearly series</span>'
 '<span><i class="b"></i>Shaded eras: crisis, slow gains, takeoff, medical</span></div>')
_LEGEND_CM=('<div class="ly-leg"><span><i></i>United Kingdom, under-5 mortality, from 1841</span>'
 '<span><i class="d"></i>World, from 1800</span>'
 '<span>Open circles, before 1950, are estimates</span>'
 '<span><i class="b"></i>England before 1841: a quarter to a third, not yearly points</span></div>')

F1=('<!--noart-->'+LY_CSS+f'<p class="enote" data-part="verify">{_esc(_VERIFY)} Every value on this page is approximate or rounded.</p>'
    +'<div class="art">'+_life_svg()+'</div>'+_LEGEND+_flags_html()+_src_html())
F2=('<!--noart-->'+'<div class="art">'+_child_svg()+'</div>'+_LEGEND_CM
    +f'<p class="enote">Same rule as Figure 1. {_esc(_VERIFY)}</p>')
F3=('<!--noart-->'+'<div class="art">'+_grid_svg()+'</div>'
    +f'<p class="ly-quote" data-part="verbatim">{_esc(LY_VERBATIM)}</p>'
    +'<div class="ly-split"><p data-part="gap">The birth average mixes children who died young with adults who did not. From 1841, someone who had reached 15 had a measured expectation of about 59, while the birth line was still about 42.</p>'
    '<p data-part="meet">When childhood deaths become rare, the birth line rises toward the age-15 line. By 2023 they are about 81 and about 82.</p></div>')
def _card(href,kicker,title,text):
    return f'<a href="../literature/{href}"><small>{kicker}</small><b>{_esc(title)}</b><span>{text}</span></a>'
F4=('<!--noart-->'
    '<div data-part="bridge"><p>The charts above are about when populations died. The reading room, which is not a course, has one-page reads of papers on the biology of aging. The lines below only say what those pages say.</p></div>'
    '<div class="ly-cards" data-part="clocks" style="margin-top:12px">'
    +_card('fourteen-epigenetic-clocks-174-diseases.html','Epigenetic clocks','14 clocks and 174 diseases','In 18,859 people the newer clocks predicted disease better than clocks trained only to guess age. Accuracy gains were often about 1 percent. The page does not show that changing a clock changes risk.')
    +_card('longitudinal-epigenetic-clocks-inchianti.html','Epigenetic clocks','Clocks followed for up to 24 years','In one Italian cohort, a clock that speeds up predicts death beyond the starting measurement. The page calls the study observational.')
    +_card('multivitamin-epigenetic-clocks-cosmos.html','Epigenetic clocks','A multivitamin trial','A daily multivitamin slightly slowed two of five clocks, by about 0.11 and about 0.21 years per year. Cocoa extract did not. The trial did not show a longer life.')
    +'</div><div class="ly-cards" data-part="repair" style="margin-top:10px">'
    +_card('bowhead-whale-dna-repair.html','Long-lived animals','Bowhead whale DNA repair','Whale cells repaired double-strand breaks more faithfully than human cells. The whale protein CIRBP extended life in fruit flies. The page says this was cells and flies, not a treatment for people.')
    +_card('myotis-bat-genomes-longevity.html','Long-lived animals','Myotis bat genomes','Long life in these bats lines up with changes in cancer pathways. Cells of one long-lived species had an unusual response to DNA damage, in culture. The page does not show that those changes lengthen life.')
    +'</div><div class="ly-cards" data-part="diet" style="margin-top:10px">'
    +_card('caloric-restriction-somatic-mutation.html','Diet, in mice','Caloric restriction and mutations','Eating less slowed the build-up of DNA mutations across several mouse tissues. The page does not give the level of restriction, and it does not show the same result in people.')
    +'</div>')

LY_LESSON=[
 ('Five hundred years, on one chart','Life expectancy at birth, England and the world, from 1526 to today.',F1),
 ('Deaths before age five','The childhood deaths that pulled the average down.',F2),
 ('Why the average was low','A hundred births, and the sentence to keep.',F3),
 ('From the literature','Population lifespan, then the biology of aging. Only what the reading-room pages say.',F4),
]
LY_CAPS=[
 'England is the solid line: Wrigley and Schofield, via Our World in Data, for 1543 to 1838, then England and Wales from the Human Mortality Database to 1949, then the United Kingdom. The world is dashed, from about 1800 (Riley, then the UN). Open circles before 1950 are estimates. The olive line is age 15 plus e15. Shaded bands are the four eras. Flags are the six drivers, and the note under them is the epilogue.',
 'Deaths before a fifth birthday, per 1,000 live births. The United Kingdom from 1841, the world from 1800. The band on the left is the English range before a continuous series: about a quarter to a third. Open circles are estimates.',
 'A schematic, not a life table. Twenty-five filled dots are a quarter. The ringed dots take it to a third. The sentence under the grid is the line to read word for word.',
 'Links open the existing reading-room pages. Nothing is added beyond what those pages say.',
]
LY_QUIZ=[
 ('What does period life expectancy at birth measure?','The average length of life if one year\'s death rates lasted a whole lifetime. It is not a prediction for one baby (Figure 1).'),
 ('Why was England\'s life expectancy at birth in the thirties for so long?','Mainly because a quarter to a third of children died before age five (Figure 3).'),
 ('In England, what could someone who reached 15 usually expect?','To live into their late fifties. From 1841 the measured line is about 59 (Figures 1 and 3).'),
 ('What should you not blame for the English dip in the 1680s, and why?','Plague. England\'s last major plague was 1665 to 1666. That decade\'s dip, to about 31, was smallpox, fevers and bad harvests (Figure 1, flag 1).'),
 ('Which country\'s 1918 drop was more than 10 years?','The United States, from about 51 in 1917 to about 39 in 1918, about 12 years. England fell from about 46 to about 41 (Figure 1, flag 5).'),
 ('Why did the English line barely rise between about 1800 and 1870?','Jenner\'s vaccine and the sanitation reforms of the 1850s were offset by crowded industrial cities. The line stays near 40 (Figure 1, flag 3).'),
 ('Did the world average fall in the years of HIV?','No. It rose from about 64 in 1990 to about 66 in 2000. In those years Eswatini fell from about 61 to about 44 and Zimbabwe from about 61 to about 46. The chart records the falls and does not separate causes (Figure 1, epilogue).'),
 ('What do the reading-room pages on clocks and caloric restriction not show?','They do not show that a methylation clock, or eating less, produced the rise in population life expectancy. The clock findings are associations, and the diet finding is in mice (Figure 4).')]
_figs=[figure_card(i,t,h,c,sub=s) for i,((t,s,h),c) in enumerate(zip(LY_LESSON,LY_CAPS),1)]
_quiz='<main class="lp-after"><section class="notes quiz" id="quiz"><h2>Quiz</h2><p class="lbl">Tap a question to see the answer</p>'+''.join(f'<details><summary>{n}. {q}</summary><p>{a}</p></details>' for n,(q,a) in enumerate(LY_QUIZ,1))+'</section></main>'
lesson_page('five-hundred-years','Module 1 · Five Hundred Years of Life Expectancy · '+COURSE+' · '+UNIVERSITY_NAME,
 '<nav class="crumbs">'+CRUMB_HOME+' › Module 1</nav><h1>Module 1 · Five Hundred Years of Life Expectancy</h1>'
 '<p>Life expectancy at birth, in England and in the world, from 1526 to today: why the early average was low, what lifted it, and what that rise does not say about the biology of aging. The figure is on the left and the lesson script on the right. Every value is rounded or approximate. '+_VERIFY+'</p>',
 _figs,_quiz+pn(None,None))
