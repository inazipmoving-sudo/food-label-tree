# ---------------- Module 1 · Carbohydrates ----------------
C_=mk_lmol('macronutrients-carbohydrates')
def _cf(n): return fsub(C_.D[n]['formula'])
# Figure 1: family tree (Fats Figure 1 style). Sugars branch: only single and double sugars are KINDS of sugar; sugar alcohols (made from
# sugars, dotted link) and added sugars (a label category) sit below in a dashed "related" group, tied to Sugars by a faint dotted line.
# Starch branch: amylose and amylopectin are its two kinds; resistant starch hangs from Starch itself (it can come from either), and the
# dashed digestion arrow also leaves Starch itself into an "in your body" frame: glucose, stored as glycogen.
# Box widths fit the mobile font sizes (svg.tree .nt 18px/.ns 15px); gaps between Double sugars/Amylose and around Amylopectin carry the lines.
CB_NODES=[(500,30,170,'Carbohydrate','4 kcal/g','nd root',None),
 (175,150,230,'Sugars','1 or 2 units · Fig. 2','nd l','#fig-2'),(500,150,230,'Starch','long glucose chains · Fig. 5','nd l','#fig-5'),(792,150,200,'Fiber','not digested · Fig. 6','nd l','#fig-6'),
 (82,290,160,'Single sugars','glucose & co · Fig. 3','nd u','#fig-3'),(268,290,160,'Double sugars','sucrose & co · Fig. 4','nd u','#fig-4'),
 (420,290,128,'Amylose','straight · Fig. 5','nd s','#fig-5'),(585,290,140,'Amylopectin','branched · Fig. 5','nd s','#fig-5'),
 (738,290,104,'Soluble','gels · Fig. 6','nd t','#fig-6'),(847,290,102,'Insoluble','bulk · Fig. 6','nd t','#fig-6'),
 (82,440,152,'Sugar alcohols','sorbitol · Fig. 8','nd u','#fig-8'),(245,440,156,'Added sugars','on the label · Fig. 8','nd u','#fig-8'),
 (500,440,156,'Resistant','acts as fiber · Fig. 6','nd s','#fig-6'),
 (600,568,180,'Glucose','from digestion · Fig. 7','nd s','#fig-7'),(810,568,160,'Glycogen','your store · Fig. 7','nd root','#fig-7')]
CB_EDGES=[(500,52,175,128),(500,52,500,128),(500,52,792,128),(175,182,82,268),(175,182,268,268),(500,182,420,268),(500,182,585,268),(792,182,738,268),(792,182,847,268),
 ('line',500,182,500,418)]
CB_EXTRA=['<path class="edge" d="M175,182 L175,402" style="stroke-dasharray:2 5;opacity:.75"/>',
 '<rect class="grp" x="2" y="402" width="328" height="84" rx="14" style="fill:none;stroke:var(--muted);stroke-width:1.3;stroke-dasharray:3 5"/>',
 '<text class="lab" x="166" y="510" text-anchor="middle">related groups, not kinds of sugar</text>',
 '<path class="edge dash" d="M60,322 L60,414" marker-end="url(#lar)"/>',
 '<text class="lab hotl" x="69" y="372">made from</text>',
 '<rect class="grp" x="492" y="500" width="406" height="142" rx="16" style="fill:none;stroke:var(--muted);stroke-width:1.3;stroke-dasharray:3 5"/>',
 '<text class="lab" x="695" y="628" text-anchor="middle">how your body stores glucose: liver and muscle</text>',
 '<path class="edge dash" d="M615,150 C650,150 670,165 670,200 L670,468 C670,506 610,500 610,542" marker-end="url(#lar)"/>',
 '<a class="tlk" href="#fig-7"><text class="lab hotl" x="682" y="430">digestion</text></a>',
 '<path class="edge dash" d="M692,568 L726,568" marker-end="url(#lar)"/>',
 '<text class="lab hotl" x="709" y="530" text-anchor="middle">stored as</text>']
P1=('<!--noart-->'+ftree(CB_NODES,CB_EDGES,650,'Tree diagram of carbohydrate. Three branches: sugars (single sugars and double sugars), starch (amylose, straight, and amylopectin, branched; also from starch, resistant starch, which acts as fiber), and fiber (soluble and insoluble). Below the sugars, in a separate related group linked to sugars, are sugar alcohols, made from sugars, and added sugars, a label category; neither is a kind of single or double sugar. Beside the tree, in your body: starch is digested to glucose, and glucose is stored as glycogen in the liver and muscle.',CB_EXTRA)
 +lblock('label','Carbohydrate on a food label',[('Total Carbohydrate','Every gram of digestible carbohydrate gives about 4 kcal. The total includes starch, sugars, fiber and any sugar alcohols. The Daily Value is 275 g.'),
   ('Dietary Fiber','Counted inside the total, but mostly not digested, so it gives fewer calories. The Daily Value is 28 g.'),
   ('Total Sugars, then Added Sugars','Total sugars counts all single and double sugars, including those naturally in fruit and milk. “Includes … Added Sugars” counts only the sugars put in during making; its Daily Value is 50 g.')]))
# Figure 2: atoms to a sugar
P2=('<!--noart-->'+molbox('atoms','Three atoms, three ways to bond',[
   '<div class="mgrid">'+mcell(C_('methane','Methane, CH4: one carbon with four hydrogens',[],'Methane, CH4'),'Carbon makes 4 bonds','methane, CH<sub>4</sub>')
   +mcell(C_('water','Water, H2O: one oxygen with two hydrogens',[],'Water, H2O'),'Oxygen makes 2','water, H<sub>2</sub>O')+'</div>'],
   fx='<p class="mfact">Hydrogen makes 1 bond. Carbohydrates use only these three atoms, carbon, hydrogen and oxygen, in roughly the ratio C<sub>n</sub>(H<sub>2</sub>O)<sub>n</sub>: one carbon for every water’s worth of H and O. That is where the name comes from: “hydrated carbon”. No water molecules are actually inside.</p>',head='The atoms')
 +molbox('chain','Glucose as a chain, '+_cf('glucose_open'),[C_('glucose_open','Open-chain glucose: six carbons in a zigzag; carbon 1 on the left is an aldehyde (C=O with one H); carbons 2 to 5 each carry an OH; carbon 6 on the right is CH2OH; every hydrogen shown',
   [('ald','1',-0.45,0.5),('c5','2',0,0.25),('c6','3',0.1,-0.95)],'Open-chain glucose, C6H12O6',eager=True)],
   [('1','<b>Carbon 1</b>: a C=O group at the end of the chain (an aldehyde). This is the reactive end.',''),('2','<b>Carbon 5</b> and its OH group.',''),('3','<b>Carbon 6</b>: a CH<sub>2</sub>OH at the other end.','')],
   fx='<p class="mfact">Six carbons, and an OH on almost every one: that is what makes sugars dissolve so easily in water and taste sweet.</p>',head='Six carbons in a row')
 +'<div class="part">The chain closes into a ring</div><div class="art mols" data-part="ring"><div class="pair rx">'
 +'<div class="pc"><p class="mt">Chain</p>'+C_('glucose_open','Open-chain glucose',[('o5','2',0,0.25),('ald','1',-0.2,-0.75)],'Open-chain glucose')+'</div><div class="op">→</div>'
 +'<div class="pc"><p class="mt">Ring (beta-glucose)</p>'+C_('glucose_b','Ring glucose drawn as a 3D model: five carbons and one oxygen form a six-membered ring; every hydrogen shown',[('o5','3',0,-0.6),('oh1','4',0.35,0.3)],'Beta-glucose ring, C6H12O6')+'</div></div>'
 +mleg([('1','The C=O on carbon 1…',''),('2','…is attacked by the OH oxygen on carbon 5.',''),('3','That oxygen becomes part of a <b>six-membered ring</b>: five carbons and one oxygen.',''),('4','The old C=O oxygen ends up as a new OH on carbon 1. No atoms are added or lost: it is still C<sub>6</sub>H<sub>12</sub>O<sub>6</sub>.','')])
 +'<p class="mfact">In water, more than 99% of glucose is in the ring form at any moment. The ring models on this page are drawn in 3D, tilted so you can see which groups point up and which point down.</p></div>'
 +legend('c h o'))
# Figure 3: the three single sugars
P3=('<!--noart-->'+molbox('anomers','Alpha and beta glucose',[
   '<p class="mt">Alpha-glucose</p>'+C_('glucose_a','Alpha-glucose as a 3D ring model: the OH on carbon 1 points down, below the ring; every hydrogen shown',[('oh1','1',0.4,0.15)],'Alpha-glucose, C6H12O6'),
   '<p class="mt">Beta-glucose</p>'+C_('glucose_b','Beta-glucose as a 3D ring model: the OH on carbon 1 points out sideways, level with the ring; every hydrogen shown',[('oh1','2',0,-0.55)],'Beta-glucose, C6H12O6')],
   [('1','<b>Alpha</b>: the OH on carbon 1 points down, below the ring.',''),('2','<b>Beta</b>: the same OH points out to the side, roughly level with the ring.','')],
   fx='<p class="mfact">When the ring closes, the new OH can end up either way, and in water the two forms keep switching: about one third alpha, two thirds beta. Once glucose is locked into a chain, the choice is fixed, and it matters: starch is built from alpha links, cellulose from beta links (Figures 5 and 6).</p>'
   +facts(what='The main sugar in your blood, and the unit that starch and glycogen are made of.',body='Fuel for every cell; the brain uses roughly 120 g a day, and red blood cells run on glucose alone.',
    low='If you eat little carbohydrate, the liver makes glucose from protein and the glycerol of fats, and the body uses more fat-derived ketones for fuel.',
    high='Blood glucose that stays high, as in diabetes, damages blood vessels, nerves, kidneys and eyes over time.',
    found='Free glucose in fruit, honey and some vegetables; as starch in grains, potatoes and beans.'),pair=True,head='Glucose')
 +molbox('galactose','Galactose, '+_cf('galactose')+' <small>glucose with one OH flipped</small>',[
   '<p class="mt">Beta-glucose</p>'+C_('glucose_b','Beta-glucose for comparison: the OH on carbon 4 points out to the left',[('oh4','1',0,-0.55)],'Beta-glucose, C6H12O6'),
   '<p class="mt">Beta-galactose</p>'+C_('galactose','Beta-galactose as a 3D ring model: identical to beta-glucose except that the OH on carbon 4 points up; every hydrogen shown',[('oh4','2',-0.45,-0.3)],'Beta-galactose, C6H12O6')],
   [('1','On glucose, the OH on <b>carbon 4</b> points out to the side.',''),('2','On galactose it points <b>up</b>. That one flip is the only difference.','')],
   fx=facts(what='A single sugar that is almost never free in food; it comes as half of lactose.',body='The liver turns it into glucose; it is also built into the sugar chains on cell surfaces and in brain tissue.',
    high='People with the rare inherited condition galactosemia can’t process it and must avoid milk sugar.',found='Milk, yogurt and cheese, as part of lactose.'),pair=True,head='Galactose')
 +molbox('fructose','Fructose, '+_cf('fructose')+' <small>a five-sided ring</small>',[C_('fructose','Fructose ring drawn flat: four carbons and one oxygen form a five-membered ring, with a CH2OH group on each side of the ring oxygen; every hydrogen shown',
   [('c2','1',0.4,-0.3),('o5','2',0,0.55)],'Fructose, C6H12O6')],
   [('1','<b>Carbon 2</b>: in the chain form, fructose’s C=O is here, on the second carbon rather than the first.',''),('2','The ring oxygen. Closing on carbon 2 gives a <b>five-membered ring</b>.','')],
   fx='<p class="mfact">Same formula as glucose, C<sub>6</sub>H<sub>12</sub>O<sub>6</sub>, different arrangement. Fructose is the sweetest natural sugar. The flat drawing here shows every atom but not which way each OH points.</p>'
   +facts(what='The main sugar of fruit and honey, and half of table sugar.',body='Absorbed more slowly than glucose and handled mainly by the liver, which turns most of it into glucose, glycogen, lactate or fat.',
    high='Large amounts eaten as added sugar are linked to fatty liver and higher blood fats; some people get bloating or loose stools from a lot of fructose at once.',
    found='Fruit, honey, and some vegetables such as onions; whole fruit also brings fiber and water.'),head='Fructose')
 +legend('c h o'))
# Figure 4: double sugars
P4=('<!--noart-->'+molbox('maltose','Maltose, '+_cf('maltose')+' <small>glucose + glucose</small>',[C_('maltose','Maltose: two glucose rings joined through an oxygen bridge from carbon 1 of the left ring, pointing down, to carbon 4 of the right ring; every hydrogen shown',
   [('c1','1',0.45,-0.25),('link','2',0.3,0.45),('c4','3',0.45,0.25)],'Maltose, C12H22O11',eager=True)],
   [('1','Carbon 1 of the first glucose, with its OH pointing down: an <b>alpha</b> link.',''),('2','The <b>glycosidic bond</b>: one oxygen bridging the two rings. Making it releases one water, just like a peptide bond.',''),('3','Carbon 4 of the second glucose.','')],
   fx='<p class="mfact">This alpha 1→4 link is the same one that holds starch together, so maltose is what you get when starch is cut into pairs.</p>'
   +facts(what='Two glucoses with an alpha 1→4 link.',body='Split by maltase on the gut wall into two glucoses.',found='Formed when starch breaks down: malted and sprouted grains, sweet potatoes, and in your own gut as starch is digested.'),head='The glycosidic bond')
 +molbox('sucrose','Sucrose, '+_cf('sucrose')+' <small>table sugar: glucose + fructose</small>',[C_('sucrose','Sucrose: a glucose ring on the left joined through an oxygen bridge to a five-membered fructose ring on the right; every hydrogen shown',
   [('c1','1',-0.45,0.3),('link','2',0.45,0.05),('c2','3',0.05,0.55)],'Sucrose, C12H22O11')],
   [('1','Carbon 1 of glucose (alpha).',''),('2','The glycosidic bond.',''),('3','Carbon 2 of fructose. Both reactive carbons are used up in the link.','')],
   fx=facts(what='Glucose and fructose joined: ordinary table sugar.',body='Split by sucrase on the gut wall; the glucose and fructose are absorbed separately.',
    high='Too much added sugar raises the risk of tooth decay and is linked to weight gain, type 2 diabetes and heart disease.',
    found='Naturally in fruit (bananas, mangoes, peaches), sweet vegetables such as carrots and beets, and maple sap; refined from sugar cane and sugar beets.'),head='Sucrose')
 +molbox('lactose','Lactose, '+_cf('lactose')+' <small>milk sugar: galactose + glucose</small>',[C_('lactose','Lactose: a galactose ring on the left, with its carbon-4 OH pointing up, joined through an oxygen bridge level with the rings to a glucose ring on the right; every hydrogen shown',
   [('c1','1',0.3,-0.5),('link','2',0,-0.55),('c4','3',-0.15,-0.65)],'Lactose, C12H22O11')],
   [('1','Carbon 1 of galactose, linked <b>beta</b>: the bridge runs out level with the ring.',''),('2','The glycosidic bond, beta 1→4.',''),('3','Carbon 4 of glucose.','')],
   fx=facts(what='Galactose and glucose joined by a beta link: the sugar of milk.',body='Split by lactase on the gut wall. Babies make plenty; most adults worldwide make much less after childhood.',
    low='If lactase is low, lactose reaches the colon, where bacteria ferment it into gas: bloating, cramps and loose stools (lactose intolerance). Yogurt and hard cheeses have little lactose left and are often fine.',
    found='Milk, yogurt, soft cheeses; human milk has more than cow’s milk.'),head='Lactose')
 +legend('c h o'))
# Figure 5: starch and glycogen (cartoons; text is page HTML)
def _hx(x,y,c,r=11): return f'<polygon points="'+' '.join(f'{x+r*math.cos(math.radians(a)):.1f},{y+r*math.sin(math.radians(a)):.1f}' for a in range(30,390,60))+f'" fill="{c}" stroke="#2c3e50" stroke-width="1.2"/>'
import math
_G='#5F7F99'
_amylose=svgd(''.join(_hx(20+k*22,40+14*math.sin(k*0.7),_G) for k in range(16)),'0 0 370 80','A long unbranched chain of glucose hexagons, gently coiling',360)
def _branch(pts): return ''.join(_hx(x,y,_G) for x,y in pts)
_ap=[(20+k*22,30) for k in range(14)]+[(130+k*22,52+k*0) for k in range(0)]
for bx,by,n in ((86,30,6),(218,30,5)):
    _ap+=[(bx+12+k*20,by+22+k*12) for k in range(n)]
_amylopectin=svgd(_branch(_ap),'0 0 340 132','A glucose chain with side branches every so often',340)
_gl=[]
def _tree(x,y,a,d,n):
    for k in range(n):
        x+=17*math.cos(a); y+=17*math.sin(a); _gl.append((x,y))
    if d<2:
        _tree(x,y,a-0.55,d+1,n-1); _tree(x,y,a+0.55,d+1,n-1)
for k in range(5): _tree(0,0,k*2*math.pi/5+0.3,0,3)
_gx=[p[0] for p in _gl]; _gy=[p[1] for p in _gl]; _x0=min(_gx)-12; _y0=min(_gy)-12; _W=max(_gx)-_x0+12; _H=max(_gy)-_y0+12
_glycogen=svgd('<circle cx="0" cy="0" r="10" fill="#A86B53"/>'+''.join(_hx(x,y,_G,8) for x,y in _gl),f'{_x0:.0f} {_y0:.0f} {_W:.0f} {_H:.0f}','Glycogen: a dense, bushy ball of glucose chains branching again and again around a central protein',300)
_cell=svgd(''.join(_hx(20+k*22,22+row*30,'#7A8256') for row in range(4) for k in range(14))+''.join(f'<line x1="{30+k*44}" y1="{33+row*30}" x2="{30+k*44}" y2="{41+row*30}" style="stroke:var(--acc)" stroke-width="2" stroke-dasharray="2 2"/>' for row in range(3) for k in range(7)),'0 0 330 120','Cellulose: straight glucose chains lying side by side, held together by many hydrogen bonds',330)
P5=('<!--noart-->'+stages('starch','Starch: plants’ glucose store',[
   ('Amylose: one long chain',_amylose,'Hundreds to thousands of glucoses joined by alpha 1→4 links. The alpha link makes the chain turn, so it coils into a helix. Usually about a quarter of starch.'),
   ('Amylopectin: a branched chain',_amylopectin,'The same chain with a branch (an alpha 1→6 link) every 20 to 30 glucoses. Usually about three quarters of starch.'),
   ('Glycogen: your own store',_glycogen,'Animals store glucose as glycogen: like amylopectin but branched about every 8 to 12 glucoses, around a protein core. Many branch ends mean glucose can be released fast.')],
   cap='Cartoons, not to scale: each hexagon is one glucose ring.')
 +lblock('cook','Starch in the kitchen',[('Cooking swells it','Heat and water make starch granules soak up water and burst (gelatinizing), which is why rice softens and gravy thickens. Gelatinized starch is much easier to digest.'),
   ('Cooling firms it','When cooked starch cools, amylose chains line up again (retrogradation). Some of this becomes resistant starch, which acts like fiber (Figure 6). Day-old rice and potato salad have a little more.'),
   ('Found in','Grains (wheat, rice, oats, corn), potatoes and other root vegetables, beans, lentils and peas, and unripe (green) bananas.')])
 +'<p class="rleg">hexagon cartoons: each is one glucose ring · not molecular drawings</p>')
# Figure 6: fiber
P6=('<!--noart-->'+molbox('ab','Alpha link vs beta link, same scale',[
   '<p class="mt">Maltose: alpha 1→4 (starch)</p>'+C_('maltose','Maltose: two glucoses with an alpha link, the bridge oxygen below the first ring',[('link','1',0.3,0.45)],'Maltose, C12H22O11'),
   '<p class="mt">Cellobiose: beta 1→4 (cellulose)</p>'+C_('cellobiose','Cellobiose: two glucoses with a beta link, the bridge oxygen level between the rings; every hydrogen shown',[('link','2',0,-0.55)],'Cellobiose, C12H22O11')],
   [('1','<b>Alpha link</b>: your enzymes (amylase, maltase) fit this shape and cut it.',''),('2','<b>Beta link</b>: the same atoms, but the bridge points the other way. Human enzymes can’t cut it, so cellulose passes through undigested.','')],
   fx='<p class="mfact">Same two glucoses, same formula; only the direction of one bond differs. Cows and termites digest cellulose only because microbes in their guts can cut beta links.</p>',head='Why fiber isn’t digested')
 +stages('cellulose',None,[('Cellulose: straight chains packed side by side',_cell,'Beta links keep each chain straight, so chains stack tightly and lock together with hydrogen bonds (dotted). That makes plant cell walls strong and insoluble.')],cap='Cartoon, not to scale.')
 +table('types',['Kind','What it does','Found in'],[
  ['Soluble fiber (beta-glucan, pectin, gums)','Dissolves into a gel; slows digestion, helps lower LDL cholesterol, and is food for gut bacteria','Oats, barley, beans and lentils, apples, citrus, carrots'],
  ['Insoluble fiber (cellulose, hemicellulose, lignin)','Holds water and adds bulk, so food moves through the gut more easily','Whole wheat and bran, brown rice, nuts, vegetable and fruit skins'],
  ['Resistant starch','Starch that escapes digestion and is fermented like soluble fiber','Beans, lentils, green bananas, cooked-and-cooled potatoes and rice']],'Kinds of fiber')
 +molbox('butyrate','Butyric acid, '+_cf('butyrate')+' <small>what gut bacteria make from fiber</small>',[C_('butyrate','Butyric acid: a chain of three carbons ending in a carboxyl group (COOH); every hydrogen shown',[('acid','1',0.55,-0.6)],'Butyric acid, C4H8O2')],
   [('1','A <b>carboxyl group</b>: in the body it gives up its H and is called butyrate.','')],
   fx='<p class="mfact">Bacteria in the colon ferment fiber into short-chain fatty acids, mainly acetate (2 carbons), propionate (3) and butyrate (4). Fiber gives about 2 kcal per gram this way.</p>'
   +facts(what='A four-carbon short-chain fatty acid made by gut bacteria.',body='The main fuel of the cells lining the colon; helps keep the gut lining healthy.',found='Made in your gut from fiber and resistant starch; small amounts are also in butter.'),head='Fiber feeds your gut bacteria')
 +lblock('need','How much fiber',[('14 g per 1000 kcal','The US target (from the Institute of Medicine, used by the Dietary Guidelines) is 14 g of fiber per 1000 kcal: about 25 g a day for women and 38 g for men aged 19 to 50. Most Americans eat about half that.'),
   ('Too little','Constipation, and over the long term a higher risk of heart disease, type 2 diabetes and colon cancer in population studies.'),
   ('Too much, too fast','Gas and bloating; raising fiber slowly and drinking enough water helps.')])
 +legend('c h o'))
# Figure 7: digestion and blood sugar
_dg=[('Mouth','salivary amylase starts cutting starch into shorter pieces'),('Stomach','acid stops amylase; little carbohydrate digestion here'),('Small intestine','pancreatic amylase cuts starch down to maltose; maltase, sucrase and lactase on the gut wall split double sugars into single ones'),
 ('Into the blood','glucose, fructose and galactose are absorbed and go to the liver first'),('Colon','fiber and resistant starch are fermented by bacteria into gas and short-chain fatty acids')]
P7=('<!--noart-->'+flow('path','From plate to glucose',_dg,cap='Only single sugars can be absorbed, so every starch and double sugar has to be cut down first.')
 +flow('balance','Keeping blood sugar steady',[('After a meal','blood glucose rises'),('Insulin','the pancreas releases insulin, so muscle, fat and liver cells take up glucose'),('Stored','extra glucose becomes glycogen in liver and muscle, and beyond that, fat'),
   ('Between meals','glucose falls; the pancreas releases glucagon'),('Released','the liver breaks down glycogen and sends glucose back into the blood')])
 +lblock('store','Glycogen and the glycemic index',[('Glycogen stores','Roughly 100 g in the liver, which keeps blood glucose steady overnight, and a few hundred grams in muscle, which only that muscle can use.'),
   ('Glycemic index','How fast a food raises blood glucose compared with pure glucose. Fiber, fat, protein, intact grains and cooling cooked starch all lower it; the same food can vary with ripeness and cooking.'),
   ('How much you need','The US RDA is 130 g of carbohydrate a day for adults, set from the brain’s glucose use. The acceptable range is 45 to 65% of calories.')]))
# Figure 8: sugars on the label, sugar alcohols
P8=('<!--noart-->'+table('sugars',['Food','Main sugars','Comes with'],[
  ['Fruit','Fructose, glucose, sucrose','Fiber, water, vitamin C, potassium'],['Milk, plain yogurt','Lactose','Protein, calcium'],['Honey','Fructose and glucose','Water and small amounts of other compounds; on a jar of honey its sugars are listed as added sugars'],
  ['Sweet vegetables (carrots, beets, sweet potatoes)','Sucrose, glucose, fructose, maltose','Fiber, vitamin A precursors'],['Sprouted and malted grains','Maltose','Starch, fiber']],'Sugars in whole foods')
 +lblock('label','Reading the sugar lines',[('Total Sugars','All single and double sugars, whether they grew in the food or were added. There is no Daily Value for total sugars.'),
   ('Includes Added Sugars','Sugars added during making, plus honey, syrups and concentrated fruit juice. Daily Value: 50 g. The US Dietary Guidelines advise keeping added sugars under 10% of calories.'),
   ('Sugar alcohols','An optional line, required only if the package makes a claim about sugars or sugar alcohols. Not counted as sugars, but included in Total Carbohydrate.')])
 +molbox('sorbitol','Sorbitol, '+_cf('sorbitol')+' <small>a sugar alcohol</small>',[
   '<p class="mt">Glucose (chain)</p>'+C_('glucose_open','Open-chain glucose with its C=O on carbon 1',[('ald','1',-0.2,-0.75)],'Open-chain glucose'),
   '<p class="mt">Sorbitol</p>'+C_('sorbitol','Sorbitol: the same six-carbon chain with an OH on every carbon; carbon 1 is now CH2OH; every hydrogen shown',[('c1','2',0,0.7)],'Sorbitol, C6H14O6')],
   [('1','The C=O on carbon 1 of glucose…',''),('2','…gains two hydrogens and becomes CH<sub>2</sub>OH. Now every carbon carries an OH: a <b>sugar alcohol</b> (polyol).','')],
   fx='<p class="mfact">Sugar alcohols are partly absorbed, so they give fewer calories than sugar (about 2.6 kcal/g for sorbitol), raise blood glucose less, and mouth bacteria can’t ferment them, so they don’t cause cavities.</p>'
   +facts(what='The sugar alcohol made from glucose.',body='Absorbed slowly and only in part; the rest reaches the colon.',high='Large amounts draw water into the gut and ferment, causing gas and diarrhea; this is why prunes and pears can have a laxative effect.',
    found='Prunes, pears, apples, peaches and stone fruit.'),head='Sugar alcohols')
 +legend('c h o'))
# Figure 9: putting it all together
P9=('<!--noart-->'+table('table',['Carbohydrate','Made of','Bond','Digested?','Found in'],[
  ['Glucose','single sugar, 6-ring','—','absorbed as is','fruit, honey; starch'],['Fructose','single sugar, 5-ring','—','absorbed as is','fruit, honey'],['Galactose','single sugar, 6-ring','—','absorbed as is','milk (in lactose)'],
  ['Maltose','glucose + glucose','alpha 1→4','yes, by maltase','malted grains; from starch'],['Sucrose','glucose + fructose','alpha 1→2 beta','yes, by sucrase','fruit, sweet vegetables'],
  ['Lactose','galactose + glucose','beta 1→4','by lactase, if you make it','milk, yogurt'],['Starch','many glucoses','alpha 1→4, branches 1→6','yes, by amylase','grains, potatoes, beans'],
  ['Glycogen','many glucoses, very branched','alpha 1→4, 1→6','yes','your liver and muscle'],['Cellulose','many glucoses','beta 1→4','no: fiber','vegetables, whole grains'],
  ['Sorbitol','sugar alcohol','—','partly','prunes, pears']],'Every carbohydrate in this lesson')
 +worth([('Brown sugar, raw sugar and white sugar','All are almost entirely sucrose. Brown sugar is sucrose with some molasses, which adds color, flavor and tiny amounts of minerals.'),
   ('Honey vs sugar','Honey is mostly free fructose and glucose plus water; table sugar is the same two joined. The body handles them similarly. Honey should not be given to babies under 1 year because of the risk of infant botulism.'),
   ('Whole grains vs refined','A whole grain keeps its bran (fiber, B vitamins, minerals) and germ (healthy fats, vitamin E). Refining removes both and leaves mostly starch.'),
   ('Why bread tastes sweet when you chew it','Amylase in your saliva starts cutting starch into maltose while it’s still in your mouth.')]))
CARB_LESSON=[('The Carbohydrate Family Tree','Sugars, starch and fiber, and how they show up on a label.',P1),
 ('From Atoms to a Sugar','Carbon, hydrogen and oxygen; a six-carbon chain that closes into a ring.',P2),
 ('The Single Sugars','Glucose, galactose and fructose: same formula, different shapes.',P3),
 ('The Double Sugars','Two single sugars joined by a glycosidic bond.',P4),
 ('Starch and Glycogen','Long glucose chains: how plants and you store fuel.',P5),
 ('Fiber','Beta links you can’t digest, and the bacteria that can.',P6),
 ('Digestion and Blood Sugar','Cut down to single sugars, absorbed, and kept in balance.',P7),
 ('Sugars on the Label','Total sugars, added sugars and sugar alcohols.',P8),
 ('Putting It All Together','The whole lesson in one table, plus a few extras.',P9)]
CARB_QUIZ=[('How many kcal does a gram of digestible carbohydrate give?','About 4, the same as protein (Figure 1).'),
 ('Which three kinds of atom make up carbohydrates?','Carbon, hydrogen and oxygen (Figure 2).'),
 ('When open-chain glucose closes into a ring, which atom joins the ring?','The oxygen of the OH on carbon 5 (Figure 2).'),
 ('What is the only difference between alpha- and beta-glucose?','Which way the OH on carbon 1 points: down for alpha, out to the side for beta (Figure 3).'),
 ('How does galactose differ from glucose?','Only the OH on carbon 4 points the other way (Figure 3).'),
 ('What two sugars make up sucrose, and lactose?','Sucrose is glucose + fructose; lactose is galactose + glucose (Figure 4).'),
 ('What causes the symptoms of lactose intolerance?','Too little lactase, so lactose reaches the colon and bacteria ferment it into gas (Figure 4).'),
 ('How do amylose and amylopectin differ?','Amylose is a straight chain; amylopectin has branches every 20 to 30 glucoses (Figure 5).'),
 ('Why can’t you digest cellulose?','Its glucoses are joined by beta links, which human enzymes can’t cut (Figure 6).'),
 ('What do gut bacteria make from fiber?','Short-chain fatty acids such as acetate, propionate and butyrate, plus gas (Figure 6).'),
 ('Which hormone lowers blood glucose after a meal, and which raises it between meals?','Insulin lowers it; glucagon raises it, by releasing glucose from liver glycogen (Figure 7).'),
 ('What is the Daily Value for added sugars on a US label?','50 g (Figure 8).')]
build_lesson('macronutrients-carbohydrates','Carbohydrates','Carbohydrates from the atoms up: how carbon, hydrogen and oxygen make a six-carbon sugar that closes into a ring, the single and double sugars drawn as 3D models at one scale, how glucose chains become starch, glycogen and fiber, how you digest them and keep blood sugar steady, and how to read the sugar lines on a label. The figure is on the left and the lesson script on the right; the quiz is at the end.',CARB_LESSON,CARB_QUIZ,mols=C_,scale=11)
