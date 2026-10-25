# ---------------- Module 1 · Lipids Beyond Fats ----------------
# exec'd from curriculum.py (shares its globals: figure_card, lesson_page, pn, _png_size, _html, OUT, GEN, ZOOM, json, os).
# Molecule images: curriculum/img/lipids/*.png, made by /workspace/nutrition/build_lipid_mols.py (outside the repo) at the
# Fats page's 72 px per C–C bond, every hydrogen drawn, no text in the images. gen/data/lipids-mols.json holds each image's
# width/height in bond units and label anchors (percent of the image). On the page every molecule is shown at ONE scale:
# --lb (px per bond) = 100cqw / 17.5 of the figure art box, so a 12-bond-wide molecule is always 12 x --lb wide.
LM=json.load(open(os.path.join(GEN,'data','lipids-mols.json'),encoding='utf-8'))
LB_SPAN=17.5
def lmol(name,alt,marks=(),cap='',zones=(),cls='',part=None):
    """one labelled molecule: image + numbered/text markers (page HTML, % positions) + optional side zones"""
    d=LM[name]; w,h=_png_size(os.path.join(OUT,'img','lipids',name+'.png'))
    mk=''
    for key,txt,dx,dy,*kind in marks:
        x,y=d['anchors'][key] if isinstance(key,str) else key
        x+=dx/d['units']*100; y+=dy/d['hunits']*100
        mk+=f'<span class="mk{(" "+kind[0]) if kind else ""}" style="left:{x:.1f}%;top:{y:.1f}%">{txt}</span>'
    zn=''.join(f'<span class="zb {c}" style="top:{t}%;height:{hh}%"><b>{txt}</b></span>' for t,hh,txt,c in zones)
    capt=_html.escape(cap or alt)
    return (f'<div class="lm{(" "+cls) if cls else ""}{" hz" if zones else ""}" style="--u:{d["units"]};--hu:{d["hunits"]}"{f' data-part="{part}"' if part else ''}>'
            f'<button type="button" class="mz lmz" data-cap="{capt}" aria-label="Enlarge: {capt}"><img src="img/lipids/{name}.png" width="{w}" height="{h}" alt="{_html.escape(alt)}" loading="lazy" decoding="async">{ZOOM}</button>{mk}{zn}</div>')
def mleg(items):
    return '<ol class="mleg">'+''.join(f'<li><span class="mk s{(" "+c) if c else ""}">{k}</span><span>{t}</span></li>' for k,t,c in items)+'</ol>'
LEGEND='<p class="rleg"><span class="k c"></span>carbon <span class="k h"></span>hydrogen <span class="k o"></span>oxygen <span class="k n"></span>nitrogen <span class="k p"></span>phosphorus · every molecule on this page is drawn at the same scale with every hydrogen shown · tap one to enlarge it</p>'

# ---- Figure 1: the lipid family tree ----
def lnode(key,parent,depth,cls,part,name,defn,facts='',link='',rail=False):
    return (f'<div class="rn {cls} t-{key} d{depth}" data-node="{key}"{f' data-parent="{parent}"' if parent else ''}{" data-rail" if rail else ""}{f' data-part="{part}"' if part else ''}>'
            f'<div class="rn-h"><span class="rn-k">{name}</span><span class="rn-d">{defn}</span></div>{f'<p class="rn-f">{facts}</p>' if facts else ''}{link}</div>')
def flink(n,label=None): return f'<a class="rn-go" href="#fig-{n}">{label or f"Figure {n}"} →</a>'
EN_Y='<b class="en y">Energy: yes</b>'; EN_N='<b class="en n">Energy: no</b>'
L1_TREE=('<div class="ft lt" data-part="tree"><svg class="tlines" aria-hidden="true"></svg><div class="tgrid">'
 +lnode('root','',0,'rn-root','','Lipids','Oily molecules that don’t dissolve in water. Fats are one kind.')
 +'<div class="tcol">'+lnode('g1','root',1,'lg1 rn-g','','Fatty acids and their kin','A carbon chain with an acid end, or made straight from one.')
 +lnode('fa','g1',2,'lg1','','Fatty acids','The building blocks; the Fats lesson was all about them.',EN_Y+'as part of fats',f'<a class="rn-go" href="macronutrients-fats.html#fig-3">Fats lesson →</a>',True)
 +lnode('wax','g1',2,'lg1','','Waxes','A fatty acid joined to a long alcohol chain.',EN_N+'we can’t digest them',flink(4),True)
 +lnode('eic','g1',2,'lg1','','Eicosanoids','Signals your body makes from 20-carbon fatty acids.',EN_N+'made in the body',flink(5),True)
 +'</div><div class="tcol">'+lnode('g2','root',1,'lg2 rn-g','','Built on a backbone','Fatty acids hung on glycerol or sphingosine.')
 +lnode('tg','g2',2,'lg2','','Triglycerides','Glycerol + 3 fatty acids. About 95% of the lipids we eat.',EN_Y+'9 kcal per gram',f'<a class="rn-go" href="macronutrients-fats.html#fig-3">Fats lesson →</a>',True)
 +lnode('pl','g2',2,'lg2','','Phospholipids','Glycerol + 2 fatty acids + a phosphate head.',EN_Y+'counted in total fat',flink(2),True)
 +lnode('sl','g2',2,'lg2','','Sphingolipids','Sphingosine + 1 fatty acid (+ a head).',EN_N+'tiny amounts in food',flink(4),True)
 +'</div><div class="tcol">'+lnode('g3','root',1,'lg3 rn-g','','Rings and building blocks','Not built from fatty acids at all.')
 +lnode('st','g3',2,'lg3','','Sterols','Four fused carbon rings: cholesterol, plant sterols.',EN_N+'not burned for fuel',flink(3),True)
 +lnode('vit','g3',2,'lg3','','Fat-soluble vitamins & carotenoids','A, D, E, K; beta-carotene, lycopene.',EN_N+'micronutrients',flink(6),True)
 +'</div></div></div>')
L1_CLASS=('<section class="rsec qa" data-part="label"><div class="part">Which ones count as “fat” on a food label</div><div class="lcls">'
 '<div class="lc lc1"><b>Total fat (a macronutrient, 9 kcal per gram)</b><span>Triglycerides, plus phospholipids and the fatty acids in them. Triglycerides are about 95% of the lipid we eat.</span></div>'
 '<div class="lc lc2"><b>Cholesterol (its own line, in milligrams)</b><span>A sterol: no calories, so it isn’t counted in total fat or in the calories.</span></div>'
 '<div class="lc lc3"><b>Vitamins A, D, E, K (micronutrients)</b><span>Needed in micrograms to milligrams, listed with the vitamins and minerals. Module 2.</span></div>'
 '</div></section>')
L1_HTML='<!--noart-->'+L1_TREE+L1_CLASS

# ---- Figure 2: phospholipids and membranes ----
pc=LM['phosphatidylcholine']['anchors']
zt=round((pc['glycerol'][1]+3)*1,1)  # head zone ends just below glycerol
L2_MOL=('<div class="art mols" data-part="molecule">'
 +lmol('phosphatidylcholine','Phosphatidylcholine (lecithin), C42H82NO8P: choline and phosphate head on top, glycerol, then two fatty-acid tails pointing down, one straight (palmitic) and one kinked (oleic); every hydrogen shown',
   [('choline','1',1.3,0),('phosphate','2',-0.85,-0.4),('glycerol','3',1.6,0.2),('tail1','4',-1.3,0),('kink','5',1.1,0)],
   'Phosphatidylcholine (lecithin), C42H82NO8P',
   zones=[(0,zt,'Water-loving head','zh'),(zt,100-zt,'Water-avoiding tails','zt')])
 +mleg([('1','<b>Choline</b>: the N+ group at the very top. Swap it and you get other phospholipids.',''),('2','<b>Phosphate</b>: phosphorus (orange) with four oxygens; it carries a negative charge.',''),
        ('3','<b>Glycerol</b>: the same 3-carbon backbone as in a triglyceride.',''),('4','<b>Fatty acid 1</b>: palmitic acid, straight.',''),('5','<b>Fatty acid 2</b>: oleic acid; its cis double bond kinks the tail.','')])
 +'</div>')
def _bilayer():
    o=['<svg class="bil" viewBox="0 0 600 250" role="img" aria-label="Cartoon of a lipid bilayer: two rows of phospholipids, heads facing the water on both sides, tails meeting in an oily middle">',
       '<rect x="0" y="0" width="600" height="38" fill="#d9ecf7"/><rect x="0" y="212" width="600" height="38" fill="#d9ecf7"/>']
    for row,(hy,s) in enumerate(((50,1),(200,-1))):
        for i in range(15):
            x=20+i*40; kink=(i+row)%3==1
            t1=f'M{x-5},{hy+s*10} L{x-5},{hy+s*72}'
            t2=(f'M{x+5},{hy+s*10} L{x+5},{hy+s*38} L{x+13},{hy+s*52} L{x+13},{hy+s*72}' if kink else f'M{x+5},{hy+s*10} L{x+5},{hy+s*72}')
            o.append(f'<path d="{t1}" stroke="#555" stroke-width="3.5" fill="none" stroke-linecap="round"/><path d="{t2}" stroke="#555" stroke-width="3.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>')
            o.append(f'<circle cx="{x}" cy="{hy}" r="12" fill="#FF8000" stroke="#8a4500" stroke-width="1.5"/><circle cx="{x}" cy="{hy-s*6}" r="4.5" fill="#3050F8"/>')
    o.append('</svg>')
    return ''.join(o)
L2_BIL=('<div class="part">Thousands of them together: the cell membrane</div><div class="art bilw" data-part="bilayer">'
 '<p class="bl t">Water outside the cell</p>'+_bilayer()+'<p class="bl b">Water inside the cell</p>'
 '<p class="bnote">A cartoon, not to scale: each <span class="bk h"></span> ball is one water-loving head and each pair of lines its two tails. '
 'The heads face the water on both sides; the tails hide from it in the oily middle. That double layer, two molecules thick, wraps every cell you have.</p></div>')
L2_HTML='<!--noart-->'+'<div class="part">One phospholipid</div>'+L2_MOL+L2_BIL+LEGEND

# ---- Figure 3: cholesterol and sterols ----
L3_HTML=('<!--noart--><div class="part">Cholesterol, next to a fat at the same scale</div><div class="art mols" data-part="molecule">'
 '<p class="mt">Cholesterol, C<sub>27</sub>H<sub>46</sub>O</p>'
 +lmol('cholesterol','Cholesterol, C27H46O: four fused carbon rings (three six-sided, one five-sided), one OH group on the left ring, and a short branched tail on the right; every hydrogen shown',
   [('oh','1',0.2,-0.9),('rings','2',0,0.15),('tail','3',0.3,1.2)],'Cholesterol, C27H46O')
 +mleg([('1','<b>OH</b>: one hydroxyl group, the only water-loving bit.',''),('2','<b>Four fused rings</b>: three six-carbon rings and one five-carbon ring, flat and stiff.',''),('3','<b>Short branched tail</b>: 8 carbons.','')])
 +'<p class="mt" data-part="compare">A triglyceride (from the Fats lesson), C<sub>55</sub>H<sub>100</sub>O<sub>6</sub></p>'
 +lmol('triglyceride','A triglyceride, C55H100O6: glycerol (purple box) holding palmitic, oleic and linoleic acid by ester links (red); orange marks the C=C double bonds; every hydrogen shown','',
   'Triglyceride: glycerol + 3 fatty acids, C55H100O6')
 +'<p class="mnote">Same scale. The fat has a glycerol backbone, three fatty acids and three ester links (red); cholesterol has none of them, which is why it isn’t a fat. Orange marks C=C double bonds, as on the Fats page.</p></div>'
 '<div class="part">Plant sterols</div><div class="art mols" data-part="plant"><p class="mt">Beta-sitosterol, C<sub>29</sub>H<sub>50</sub>O</p>'
 +lmol('sitosterol','Beta-sitosterol, C29H50O: the same four rings, OH and tail as cholesterol, plus an extra two-carbon (ethyl) branch on the tail; every hydrogen shown',
   [('ethyl','1',1.3,-0.2)],'Beta-sitosterol (a plant sterol), C29H50O')
 +mleg([('1','<b>The only difference</b>: an extra two-carbon branch on the tail. Close enough to cholesterol to compete with it in the gut.','')])
 +'</div>'+LEGEND)

# ---- Figure 4: sphingolipids and waxes ----
L4_HTML=('<!--noart--><div class="art mols" data-part="molecules"><div class="pair">'
 '<div class="pc" data-part="ceramide"><p class="mt">A ceramide (sphingolipid)<br><small>C<sub>36</sub>H<sub>71</sub>NO<sub>3</sub></small></p>'
 +lmol('ceramide','A ceramide, C36H71NO3: the sphingosine backbone (left tail with a trans double bond, two OH groups and an NH at the top) joined by an amide link to a stearic acid tail (right); every hydrogen shown',
   [('head','1',-1.4,-0.6),('amide','2',0.6,0.9),('fa','3',1.0,0)],'Ceramide: sphingosine + stearic acid, C36H71NO3')
 +'</div><div class="pc" data-part="wax"><p class="mt">A wax: cetyl palmitate<br><small>C<sub>32</sub>H<sub>64</sub>O<sub>2</sub></small></p>'
 +lmol('wax','Cetyl palmitate, a wax, C32H64O2: palmitic acid (left chain) joined by an ester link at the top to cetyl alcohol, a 16-carbon alcohol (right chain); every hydrogen shown',
   [('ester','A',0.1,-1.2),('acid','B',-1.1,0),('alcohol','C',1.1,0)],'Cetyl palmitate (a wax), C32H64O2')
 +'</div></div>'
 +mleg([('1','<b>Sphingosine</b>: an 18-carbon backbone with two OH groups and an N, used instead of glycerol.',''),('2','<b>Amide link</b> (N–C=O) holding one fatty acid.',''),('3','<b>Fatty acid</b>: here stearic acid.',''),
        ('A','<b>Ester link</b>, the same kind that holds fatty acids to glycerol.','w'),('B','<b>Fatty acid</b>: palmitic acid.','w'),('C','<b>Long-chain alcohol</b>: cetyl alcohol, 16 carbons ending in O.','w')])
 +'</div>'+LEGEND)

# ---- Figure 5: eicosanoids ----
L5_HTML=('<!--noart--><div class="part">The two starting fatty acids (20 carbons each)</div><div class="art mols" data-part="sources">'
 '<p class="mt">Arachidonic acid (omega-6), C<sub>20</sub>H<sub>32</sub>O<sub>2</sub></p>'
 +lmol('arachidonic','Arachidonic acid, C20H32O2: a 20-carbon chain with four cis double bonds, the last one 6 carbons from the omega end; every hydrogen shown',
   [('cooh','acid end',0,-1.0,'tx'),('omega','ω end',0,1.0,'tx'),('db14','ω6',0,-1.0,'w6')],'Arachidonic acid (omega-6), C20H32O2')
 +'<p class="mt">EPA (omega-3), C<sub>20</sub>H<sub>30</sub>O<sub>2</sub></p>'
 +lmol('epa','EPA, eicosapentaenoic acid, C20H30O2: a 20-carbon chain with five cis double bonds, the last one 3 carbons from the omega end; every hydrogen shown',
   [('cooh','acid end',0,-1.0,'tx'),('omega','ω end',0,1.0,'tx'),('db17','ω3',0,-1.0,'w3')],'EPA (omega-3), C20H30O2')
 +'</div><div class="arrow" data-part="enzymes">↓ enzymes in your cells (COX and LOX) fold and oxidize the chain ↓</div>'
 '<div class="art mols" data-part="pge2"><p class="mt">Prostaglandin E2, made from arachidonic acid, C<sub>20</sub>H<sub>32</sub>O<sub>5</sub></p>'
 +lmol('pge2','Prostaglandin E2, C20H32O5: the same 20 carbons, now folded with a five-carbon ring in the middle and extra oxygens; every hydrogen shown',
   [('ring','1',0,0),('cooh','2',0.9,0),('oh15','3',-0.9,0)],'Prostaglandin E2 (PGE2), C20H32O5')
 +mleg([('1','<b>A new five-carbon ring</b>, closed in the middle of the chain.',''),('2','<b>Acid end</b>, still there.',''),('3','<b>New oxygens</b>: OH and C=O groups added by the enzymes.','')])
 +'</div>'
 '<div class="rsec" data-part="families"><div class="part">Three families of signals</div><div class="rtbl-wrap"><table class="rtbl"><thead><tr><th>Family</th><th>Main jobs</th><th>Made from</th></tr></thead><tbody>'
 '<tr><td data-l="Family">Prostaglandins</td><td data-l="Main jobs">Inflammation, pain and fever; protect the stomach lining; widen or narrow blood vessels</td><td data-l="Made from">AA or EPA, by COX enzymes</td></tr>'
 '<tr><td data-l="Family">Thromboxanes</td><td data-l="Main jobs">Make platelets clump to form a clot; narrow blood vessels</td><td data-l="Made from">AA or EPA, by COX enzymes</td></tr>'
 '<tr><td data-l="Family">Leukotrienes</td><td data-l="Main jobs">Call in white blood cells; tighten the airways (part of asthma)</td><td data-l="Made from">AA or EPA, by LOX enzymes</td></tr>'
 '</tbody></table></div></div>'+LEGEND)

# ---- Figure 6: fat-soluble vitamins ----
L6_HTML=('<!--noart--><div class="art mols" data-part="molecule"><p class="mt">Retinol (vitamin A), C<sub>20</sub>H<sub>30</sub>O</p>'
 +lmol('retinol','Retinol, vitamin A, C20H30O: a six-carbon ring on the left and a chain of alternating double bonds ending in an OH group on the right; every hydrogen shown',
   [('ring','1',0,0),('chain','2',0,-1.2),('oh','3',0,-0.9)],'Retinol (vitamin A), C20H30O')
 +mleg([('1','<b>Ring</b>: oily, like the rest of the molecule.',''),('2','<b>Chain of alternating double bonds</b>: built from 5-carbon units, the same building block as carotenoids and cholesterol.',''),('3','<b>OH</b>: one small water-loving end; not enough to make it dissolve in water.','')])
 +'</div><div class="rsec" data-part="four"><div class="rtbl-wrap"><table class="rtbl"><thead><tr><th>Lipid</th><th>Best known for</th><th>Found in</th></tr></thead><tbody>'
 '<tr><td data-l="Lipid">Vitamin A</td><td data-l="Best known for">Vision, skin, immune system</td><td data-l="Found in">Liver, eggs, dairy; made from beta-carotene</td></tr>'
 '<tr><td data-l="Lipid">Vitamin D</td><td data-l="Best known for">Absorbing calcium; bones</td><td data-l="Found in">Oily fish, egg yolk, fortified milk; made in skin in sunlight</td></tr>'
 '<tr><td data-l="Lipid">Vitamin E</td><td data-l="Best known for">Antioxidant that protects membranes</td><td data-l="Found in">Nuts, seeds, vegetable oils</td></tr>'
 '<tr><td data-l="Lipid">Vitamin K</td><td data-l="Best known for">Blood clotting; bones</td><td data-l="Found in">Leafy greens; small amounts in fermented foods</td></tr>'
 '<tr><td data-l="Lipid">Carotenoids</td><td data-l="Best known for">Orange and red colour; beta-carotene becomes vitamin A, lycopene does not</td><td data-l="Found in">Carrots, sweet potato, tomatoes, leafy greens</td></tr>'
 '</tbody></table></div></div>'+LEGEND)

# ---- Figure 7: putting it all together (recap table only, no figure-by-figure list) ----
RT=[('Fatty acids','none: a chain','carbon chain with an acid end','building blocks; fuel','yes, as part of fats','every food fat and oil','<a href="macronutrients-fats.html#fig-3">Fats lesson</a>'),
('Triglycerides','glycerol','glycerol + 3 fatty acids, ester links','storing energy','yes, 9 kcal/g','oils, butter, meat fat, nuts','<a href="macronutrients-fats.html#fig-3">Fats lesson</a>'),
('Phospholipids','glycerol','glycerol + 2 fatty acids + phosphate head','cell membranes; emulsifier','yes (counted in total fat)','egg yolk, soybeans, liver','<a href="#fig-2">Figure 2</a>'),
('Sterols','four fused rings','4 rings + OH + short tail','membranes; hormones; vitamin D; bile','no','cholesterol: animal foods; plant sterols: nuts, seeds, oils','<a href="#fig-3">Figure 3</a>'),
('Sphingolipids','sphingosine','sphingosine + 1 fatty acid (+ head)','skin barrier; myelin','not a real source','small amounts in milk, eggs, meat','<a href="#fig-4">Figure 4</a>'),
('Waxes','none: two chains','fatty acid + long-chain alcohol, ester link','waterproof coatings','no, indigestible','apple peel, leaf coatings, beeswax','<a href="#fig-4">Figure 4</a>'),
('Eicosanoids','20-carbon fatty acid','made in cells from AA or EPA','short-lived signals','no, not a nutrient','made in your body','<a href="#fig-5">Figure 5</a>'),
('Fat-soluble vitamins & carotenoids','5-carbon units','rings and chains','vision, bones, clotting, antioxidants','no','liver, eggs, oily fish, nuts, greens, orange veg','<a href="#fig-6">Figure 6</a>')]
RTH=['Group','Backbone','Structure','Main job','Energy?','Example foods','See']
L7_HTML=('<!--noart--><section class="rsec" data-part="table"><div class="part">Every lipid in one table</div><div class="rtbl-wrap"><table class="rtbl lrt"><thead><tr>'+''.join(f'<th>{h}</th>' for h in RTH)+'</tr></thead><tbody>'
 +''.join('<tr>'+''.join(f'<td data-l="{h}">{v}</td>' for h,v in zip(RTH,r))+'</tr>' for r in RT)+'</tbody></table></div></section>'
 '<section class="rsec qa" data-part="energy"><div class="part">The two big ideas</div>'
 '<h4>Only fatty acids give energy</h4><p>Triglycerides and phospholipids give energy because of their fatty acids. Sterols, waxes, eicosanoids and the vitamins don’t: their jobs are building, signalling and protecting.</p>'
 '<h4>Most lipids have a water-loving end</h4><p>Phospholipids, cholesterol and ceramides each have a small water-loving part and a large oily part. That two-sided shape is what lets them build membranes and barriers.</p>'
 '<p class="fnote">General education, not medical advice. Facts follow mainstream sources (US Dietary Guidelines, NIH Office of Dietary Supplements, standard biochemistry texts).</p></section>')

LIPID_LESSON=[
 ('The Lipid Family Tree','Oily molecules that don’t dissolve in water. Fats are one branch.',L1_HTML),
 ('Phospholipids and Cell Membranes','A fat with one fatty acid swapped for a water-loving head.',L2_HTML),
 ('Cholesterol and Other Sterols','Four rings, no fatty acids, no calories.',L3_HTML),
 ('Sphingolipids and Waxes','A different backbone, and a lipid we can’t digest.',L4_HTML),
 ('Eicosanoids: Signals Made From Fatty Acids','Made in your body from omega-6 and omega-3 fatty acids.',L5_HTML),
 ('Fat-Soluble Vitamins and Carotenoids','Lipids too, so they need fat to be absorbed. Full lesson in Module 2.',L6_HTML),
 ('Putting It All Together','Every lipid group side by side.',L7_HTML)]
LQUIZ=[('What makes a molecule a lipid?','It is oily and doesn’t dissolve in water (Figure 1). Fats are one kind of lipid.'),
('About what share of the lipids we eat are triglycerides?','About 95% (Figure 1).'),
('How is a phospholipid different from a triglyceride?','It has 2 fatty acids instead of 3; the third glycerol slot holds a phosphate head, often with choline on it (Figure 2).'),
('Why do phospholipids form a double layer in water?','Their heads are water-loving and their tails water-avoiding, so the tails hide in the middle and the heads face the water on both sides (Figure 2).'),
('What is lecithin, and why is it added to food?','Phosphatidylcholine (or a phospholipid mix) from egg yolk, soy or sunflower; it is an emulsifier, E322, that keeps oil and water mixed (Figure 2).'),
('Why isn’t cholesterol a fat?','It has no glycerol, no fatty acids and no ester links: it is four fused rings with one OH. It isn’t burned for energy, so it has no calories (Figure 3).'),
('Name three things your body makes from cholesterol.','Steroid hormones (estrogen, testosterone, cortisol), vitamin D and bile acids; it also goes into cell membranes (Figure 3).'),
('Which foods contain cholesterol, and how do plant sterols differ?','Only animal foods. Plant sterols such as beta-sitosterol, in nuts, seeds and oils, look almost the same and compete with cholesterol for absorption (Figure 3).'),
('What do ceramides do, and what is a wax made of?','Ceramides help seal the skin barrier; a wax is a fatty acid joined by an ester link to a long-chain alcohol, and we can’t digest it (Figure 4).'),
('Which fatty acids are eicosanoids made from?','The 20-carbon fatty acids arachidonic acid (omega-6) and EPA (omega-3) (Figure 5).'),
('Why do vitamins A, D, E and K need some fat in the meal?','They are lipids, so they are absorbed along with fat (Figure 6).')]
def build_lipids():
    figs=[figure_card(i,t,h,'',sub=s) for i,(t,s,h) in enumerate(LIPID_LESSON,1)]
    lq='<main class="lp-after"><section class="notes quiz" id="quiz"><h2>Quiz</h2><p class="lbl">Tap a question to see the answer</p>'+''.join(f'<details><summary>{n}. {q}</summary><p>{a}</p></details>' for n,(q,a) in enumerate(LQUIZ,1))+'</section></main>'
    after=lq+pn(('Module 1 · Fats','macronutrients-fats.html'),None)+LIPID_JS
    lesson_page('macronutrients-lipids','Module 1 · Lipids Beyond Fats · Curriculum · Food Label Tree',
     '<nav class="crumbs"><a href="../">Food Label Tree</a> › <a href="./">Curriculum</a> › Module 1</nav><h1>Module 1 · Lipids Beyond Fats</h1>'
     '<p>Fats are one kind of lipid. This lesson meets the rest of the family, one group at a time: phospholipids that build every cell membrane, cholesterol and plant sterols, sphingolipids and waxes, the eicosanoid signals your body makes from fatty acids, and the fat-soluble vitamins, then puts them all in one table. Every molecule is drawn at the same scale with every hydrogen shown. The figure is on the left and the lesson script on the right; the quiz is at the end.</p>'
     '<p class="pnl">Previous lesson: <a href="macronutrients-fats.html">Module 1 · Fats</a></p>',
     figs,after)
    return len(LIPID_LESSON)
# tree connectors (curves from the root, rails down each column) + tap-to-enlarge for every labelled molecule
LIPID_JS=('<dialog class="lbx lbm" aria-label="Molecule, full size"><button type="button" class="lbx-x" aria-label="Close">×</button><div class="lbx-b"></div><p class="lbx-c"></p></dialog>'
 '<script>(()=>{const dlg=document.querySelector("dialog.lbm");'
 'document.querySelectorAll(".ft.lt").forEach(ft=>{const svg=ft.querySelector(".tlines"),G=ft.querySelector(".tgrid");'
 'function draw(){const R=ft.getBoundingClientRect(),wide=getComputedStyle(G).display==="grid";let d="";'
 'ft.querySelectorAll("[data-parent]").forEach(n=>{const p=ft.querySelector(`[data-node="${n.dataset.parent}"]`),a=p.getBoundingClientRect(),b=n.getBoundingClientRect();'
 'if(wide&&!n.hasAttribute("data-rail")){const px=a.left+a.width/2-R.left,py=a.bottom-R.top,cx=b.left+b.width/2-R.left,cy=b.top-R.top,g=Math.min(30,cy-py),y0=cy-g;d+=`M${px},${py}V${y0}C${px},${y0+g/2} ${cx},${y0+g/2} ${cx},${cy}`;}'
 'else{const x=a.left-R.left+11,py=a.bottom-R.top,cy=b.top-R.top+22,cx=b.left-R.left;d+=`M${x},${py}V${cy-8}Q${x},${cy} ${x+8},${cy}H${cx}`;}});'
 'svg.setAttribute("width",R.width);svg.setAttribute("height",R.height);svg.innerHTML=`<path d="${d}"/>`;}'
 'new ResizeObserver(draw).observe(ft);addEventListener("load",draw);draw();});'
 'document.addEventListener("click",e=>{const b=e.target.closest(".lmz");if(!b||!dlg)return;const lm=b.closest(".lm"),c=lm.cloneNode(true),u=+lm.style.getPropertyValue("--u"),hu=+lm.style.getPropertyValue("--hu");'
 'c.querySelectorAll("button").forEach(x=>x.replaceWith(...x.childNodes));c.querySelectorAll(".zi").forEach(x=>x.remove());'
 'const lb=Math.min((innerWidth*0.94-40)/(u+(lm.classList.contains("hz")?3:0)),Math.max((innerHeight*0.92-90)/hu,lm.querySelector("img").getBoundingClientRect().width/u*1.6),72);c.style.setProperty("--lb",lb+"px");c.removeAttribute("data-part");'
 'const box=dlg.querySelector(".lbx-b");box.replaceChildren(c);dlg.querySelector(".lbx-c").textContent=b.dataset.cap;dlg.showModal();});'
 'if(dlg){dlg.addEventListener("click",()=>dlg.close());dlg.addEventListener("keydown",e=>{if(e.key!=="Escape")e.stopPropagation()});}})();</script>')
