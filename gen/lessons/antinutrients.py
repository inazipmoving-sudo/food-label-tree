# ---------------- Module 4 · Antinutrients ----------------
MN=mk_lmol('antinutrients')
A=None
_L=[(75,'Phytate','Fig. 3','#fig-3','Grains, beans','soak, sprout','#fig-8'),(225,'Oxalate','Fig. 4','#fig-4','Spinach, rhubarb','boil','#fig-8'),
    (375,'Tannins','Fig. 5','#fig-5','Tea, red wine','between meals','#fig-8'),(525,'Lectins','Fig. 6','#fig-6','Raw kidney beans','soak, then boil','#fig-8'),
    (675,'Trypsin inhibitors','Fig. 6','#fig-6','Raw soybeans','cook','#fig-8'),(825,'Goitrogens','Fig. 7','#fig-7','Brassicas, cassava','cook; iodine','#fig-8')]
AN_NODES=[(450,30,300,'Antinutrients','natural plant compounds that block nutrients','nd root','#fig-2'),
 (225,150,430,'Bind minerals','iron, zinc, calcium · Figs. 3–5','nd l','#fig-3'),(600,150,280,'Block protein digestion','Fig. 6','nd l','#fig-6'),(825,150,130,'Block iodine use','Fig. 7','nd l','#fig-7')]
AN_NODES+=[(x,270,140,t,s,'nd u',h) for x,t,s,h,_,_,_ in _L]+[(x,390,140,t,s,'nd t',h) for x,_,_,_,t,s,h in _L]
_P={75:225,225:225,375:225,525:600,675:600,825:825}
AN_EDGES=[(450,52,x,128) for x in (225,600,825)]+[(_P[x],182,x,248) for x in _P]+[(x,302,x,368) for x in _P]
P1=('<!--noart-->'+ftree(AN_NODES,AN_EDGES,420,'Tree diagram: antinutrients grouped by what they block. Bind minerals: phytate (grains, beans; reduced by soaking and sprouting), oxalate (spinach, rhubarb; reduced by boiling) and tannins (tea, red wine; drink tea between meals). Block protein digestion: lectins (raw kidney beans; soak, then boil) and trypsin inhibitors (raw soybeans; cook). Block iodine use: goitrogens (brassicas, cassava; cook them and get enough iodine).')
 +lblock('label','What the tree shows',[('Three things they block','Antinutrients are compounds that plants make for their own reasons, such as storing phosphorus or deterring insects, which also reduce how well you absorb or use a nutrient. They bind minerals, block protein digestion, or get in the way of iodine.'),
   ('The bottom row is the fix','Each has a kitchen answer: soaking, sprouting, fermenting, boiling or simply cooking. Traditional ways of preparing grains and beans grew up partly because they work.'),
   ('Not on the label','Antinutrients occur naturally in whole foods, so they never appear in the ingredient list or the Nutrition Facts panel.')]))
P2=('<!--noart-->'+molbox('ions','The minerals they hold on to',[
   '<div class="mgrid">'+mcell(MN('zn','Zinc ion, Zn2+: a blue-gray ball',[],'Zinc ion, Zn2+',eager=True),'Zinc','Zn²⁺')
   +mcell(MN('fe','Ferric iron ion, Fe3+: a small orange ball',[],'Ferric iron ion, Fe3+'),'Iron','Fe³⁺')
   +mcell(MN('ca','Calcium ion, Ca2+: a green ball',[],'Calcium ion, Ca2+'),'Calcium','Ca²⁺')+'</div>'],
   fx='<p class="mfact">Minerals travel through your gut as small positive ions. Many antinutrients carry negative oxygen groups that grip these ions, making a clump too big or too insoluble to cross the gut wall, so the mineral leaves in the stool instead (see Trace Minerals and Major Minerals).</p>',head='Starting point')
 +table('kinds',['How it works','Antinutrients','Nutrient affected'],[
   ['Grips mineral ions in the gut','phytate, oxalate, tannins','iron, zinc, calcium, magnesium'],
   ['Blocks a digestive enzyme or sticks to the gut wall','trypsin inhibitors, lectins','protein; lectins can also cause stomach upset'],
   ['Gets in the way of the thyroid','goitrogens','iodine']],'Three ways to block a nutrient')
 +lblock('dose','Dose and context',[('A problem mainly when diets are narrow','For most people eating a varied diet, antinutrients matter little. They matter more when one staple supplies most of the calories, when mineral intake is already low, or in vegan diets that rely on whole grains and beans for iron and zinc.'),
   ('Often useful too','Many of the same compounds are studied for benefits: phytate and tannins are antioxidants, and the foods richest in them (whole grains, beans, tea) are linked to better health (see Bioactives).')])
 +legend('zn fe ca',note='ions drawn to the same scale as the molecules on this page · tap one to enlarge it'))
P3=('<!--noart-->'+molbox('parts','The two building blocks',[
   '<div class="mgrid">'+mcell(MN('inositol','Myo-inositol: a ring of six carbons, each with an OH group; every hydrogen shown',[('ring','1',A,A)],'Myo-inositol, C6H12O6',eager=True),'Inositol','C₆H₁₂O₆')
   +mcell(MN('phosphate','Phosphoric acid: an orange phosphorus atom with four oxygens',[('p','2',A,A)],'Phosphoric acid, H3PO4'),'Phosphate','H₃PO₄')+'</div>'],
   [('1','Inositol: a six-carbon ring with an OH on every carbon, a close cousin of glucose…',''),('2','…and phosphate, the same group that is in DNA and ATP.','')])
 +molbox('phytic','Phytic acid, C₆H₁₈O₂₄P₆',[MN('phytic','Phytic acid: an inositol ring with a phosphate group attached through oxygen to each of its six carbons; every hydrogen shown',[('ring','3',A,A),('p','4',A,A),('p2','4',A,A)],'Phytic acid, C6H18O24P6')],
   [('3','The same inositol ring…',''),('4','…with a phosphate on all six carbons. In the gut each phosphate loses hydrogens and carries negative charges, which grip zinc, iron and calcium ions.','')],
   fx=facts(what='Phytic acid, or phytate in its salt form, is how seeds store phosphorus: it holds most of the phosphorus in grains, beans, nuts and seeds, ready for the sprouting plant.',
     body='Humans make very little phytase, the enzyme that cuts phosphates off phytate, so most phytate passes through intact, taking bound zinc and iron with it. It is the main dietary factor that lowers zinc absorption. It also has an upside: it is an antioxidant, and diets rich in whole grains and beans are linked to lower risk of several chronic diseases.',
     high='High-phytate diets with little meat can lead to zinc and iron deficiency, especially where one unrefined grain or bean is the main food.',
     found='Bran of whole grains (wheat, rice, oats), beans, lentils, soy, nuts and seeds (sesame, almonds). Refined white flour has much less, because the bran is removed.'),head='Phytate')
 +legend('c h o p'))
P4=('<!--noart-->'+molbox('ox','Oxalic acid and oxalate',[
   '<div class="mgrid">'+mcell(MN('oxalic','Oxalic acid: two carbons joined directly, each with a C=O and an OH; every hydrogen shown',[('c','1',A,A)],'Oxalic acid, C2H2O4',eager=True),'Oxalic acid','C₂H₂O₄')
   +mcell(MN('oxalate','Oxalate ion: the same two carbons with no hydrogens; two oxygens carry a negative charge',[('c','2',A,A)],'Oxalate ion, C2O4 2-'),'Oxalate','C₂O₄²⁻')
   +mcell(MN('caox','Calcium oxalate: an oxalate ion with both charged oxygens facing a green calcium ion',[('ca','3',A,A)],'Calcium oxalate, CaC2O4'),'Calcium oxalate','CaC₂O₄')+'</div>'],
   [('1','The smallest acid with two acid groups: just two carbons and four oxygens.',''),('2','In food and in the body it loses both hydrogens, leaving oxalate with two negative charges…',''),('3','…which clamp onto a calcium ion. Calcium oxalate barely dissolves, so it forms crystals.','')],
   fx=facts(what='A small acid that many plants store, sometimes as needle-like calcium oxalate crystals that deter animals from eating them.',
     body='Oxalate binds calcium in the gut, so the calcium in spinach is poorly absorbed, only about a fifth as well as the calcium in milk. Oxalate that is absorbed leaves in urine, where it can join calcium to form kidney stones; most kidney stones are calcium oxalate. Your liver also makes oxalate, and very high doses of vitamin C are partly turned into it.',
     high='A risk mainly for people who form kidney stones, who are often advised to limit high-oxalate foods, drink plenty of fluid, and eat calcium-rich foods with them, which binds oxalate in the gut. Rhubarb leaves are poisonous, partly from their oxalate; eat only the stalks.',
     found='Spinach, rhubarb, Swiss chard, beet greens, beets, almonds, cashews, cocoa, sweet potatoes, black tea.'),head='Oxalate')
 +legend('c h o ca'))
P5=('<!--noart-->'+molbox('tannin','The two kinds of tannin building block',[
   '<div class="mgrid">'+mcell(MN('gallic','Gallic acid: a benzene ring with three neighboring OH groups and a carboxylic acid; every hydrogen shown',[('oh','1',A,A),('acid','2',A,A)],'Gallic acid, C7H6O5',eager=True),'Gallic acid','C₇H₆O₅')
   +mcell(MN('catechin','Catechin: two benzene rings linked through a ring containing oxygen, with five OH groups; every hydrogen shown',[('b','3',A,A),('c','4',A,A)],'Catechin, C15H14O6'),'Catechin','C₁₅H₁₄O₆')+'</div>'],
   [('1','Three OH groups side by side on a ring: a strong grip for iron.',''),('2','Hydrolyzable tannins are many gallic acids joined through their acid group to a sugar.',''),('3','Catechin has two neighboring OH groups on this ring, the same iron grip…',''),('4','…and condensed tannins are chains of catechin-type units linked end to end.','')],
   fx=facts(what='Large polyphenols that bind proteins. That binding is the dry, puckering feel of strong tea, red wine and unripe fruit, called astringency.',
     body='Tannins bind nonheme iron in the gut. Tea with a meal can cut the iron absorbed from that meal by more than half; coffee has a similar effect through related polyphenols. Heme iron from meat is much less affected.',
     high='Mainly a concern for people with low iron, who can drink tea and coffee between meals rather than with them. Tannins in sorghum and beans also make some protein harder to digest.',
     found='Black and green tea, red wine, coffee (related compounds), cocoa, pomegranate, persimmons, grape skins and seeds, sorghum, colored beans, walnuts.'),head='Tannins')
 +legend('c h o'))
_wall=''.join(f'<rect x="{10+k*80}" y="96" width="74" height="40" rx="10" fill="#E9DFD3" stroke="#B9A48F" stroke-width="2"/>' for k in range(5))
_sug=lambda x,y:f'<line x1="{x}" y1="96" x2="{x}" y2="{y+8}" stroke="#7A8256" stroke-width="3"/><polygon points="{x},{y-8} {x+7},{y-4} {x+7},{y+4} {x},{y+8} {x-7},{y+4} {x-7},{y-4}" fill="#7A8256"/>'
_lect=(_wall+''.join(_sug(x,70) for x in (30,90,150,210,270,330,390))
  +'<path d="M150,30 C150,8 210,8 210,30 L210,58 L196,58 L196,40 L164,40 L164,58 L150,58 Z" style="fill:var(--acc)"/>'
  +'<path d="M270,30 C270,8 330,8 330,30 L330,58 L316,58 L316,40 L284,40 L284,58 L270,58 Z" style="fill:var(--acc)"/>')
_lect=svgd(_lect,'0 0 420 140','Gut wall cells drawn as a row of rounded boxes with small sugar hexagons on stalks; two blue lectin proteins clamp onto pairs of sugars',420)
_enz=lambda cx,open_=True:f'<path d="M{cx},50 L{cx+42},{26 if open_ else 44} A48,48 0 1,0 {cx+42},{74 if open_ else 56} Z" fill="#A86B53"/>'
_chain=lambda x0:''.join(f'<circle cx="{x0+k*20}" cy="50" r="8" fill="{["#3E5C76","#7A8256","#5F7F99"][k%3]}"/>' for k in range(5))
_tr1=svgd(_enz(70)+_chain(118),'0 0 230 100','Trypsin drawn as an open Pac-Man shape about to bite a chain of amino acid beads',240)
_tr2=svgd(_enz(70)+'<path d="M86,50 L126,34 L150,50 L126,66 Z" fill="#3E5C76"/>'+_chain(170),'0 0 270 100','The same enzyme with a blue inhibitor wedged in its mouth; the bead chain waits outside, uncut',260)
_tr3=svgd(_enz(70)+_chain(118)+'<path d="M240,20 q12,10 0,20 q-12,10 0,20 q12,10 0,20 q-12,10 0,20" fill="none" stroke="#3E5C76" stroke-width="6" stroke-linecap="round"/>','0 0 270 100','After cooking, the inhibitor is a loose unfolded strand, and the enzyme is free to bite the bead chain again',240)
P6=('<!--noart-->'+stages('lectin','Lectins: proteins that grab sugars',[
   ('Sugars on the gut wall',_lect,'Lectins are proteins that bind specific sugars. The cells lining your gut are coated with sugar chains, and some lectins clamp onto them; they resist digestion and can damage the lining.')],
   cap='Cartoon, not to scale: each hexagon is a whole sugar; each blue shape is a whole lectin protein.')
 +molbox('lfacts','Lectins',[],fx=facts(what='Sugar-binding proteins found in many plants, highest in raw legumes. The best known is phytohemagglutinin in red kidney beans, so named because it makes red blood cells clump.',
     high='Raw or undercooked kidney beans can cause severe nausea, vomiting and diarrhea within a few hours; the US FDA notes as few as four or five raw beans can do it. Beans warmed but not boiled, as in some slow cookers, can be worse than raw. Fully cooked beans are safe: boiling destroys almost all lectin activity, and canned beans are already cooked.',
     found='Red and white kidney beans (most), other dried beans, lentils, peanuts, soybeans, raw wheat germ. Tomatoes and potatoes have small amounts that cause no known problems.'))
 +stages('tryp','Trypsin inhibitors: a plug in the enzyme',[
   ('1 · Normal digestion',_tr1,'Trypsin, an enzyme from your pancreas, cuts proteins into pieces in the small intestine (see Protein).'),
   ('2 · Blocked',_tr2,'A trypsin inhibitor is a small protein that fits tightly into trypsin’s cutting site, so less protein is digested.'),
   ('3 · Cooked',_tr3,'Heat unfolds the inhibitor, so it no longer fits, and digestion works again.')],
   cap='Cartoon, not to scale: each bead is a whole amino acid; the brown shape is the enzyme.')
 +molbox('tfacts','Trypsin inhibitors',[],fx=facts(what='Proteins in seeds that block protein-digesting enzymes, probably to protect the seed from insects.',
     body='They lower how much protein you can digest. Animals fed raw soybeans grow poorly and their pancreas enlarges as it tries to make more enzyme.',
     high='Rarely a problem in people, because soy and other legumes are almost always cooked, toasted or fermented, which inactivates most of the inhibitor.',
     found='Raw soybeans and other raw legumes, raw egg white (ovomucoid), raw potatoes; tofu, soy milk and tempeh have much less after heating.')))
P7=('<!--noart-->'+molbox('goit','Iodide and two goitrogens',[
   '<div class="mgrid">'+mcell(MN('iodide','Iodide ion, I-: a large purple ball',[],'Iodide ion, I-',eager=True),'Iodide','I⁻')
   +mcell(MN('thiocyanate','Thiocyanate ion: a yellow sulfur, a carbon and a blue nitrogen in a straight line',[('s','1',A,A)],'Thiocyanate ion, SCN-'),'Thiocyanate','SCN⁻')
   +mcell(MN('goitrin','Goitrin: a five-membered ring with oxygen, nitrogen and a C=S group, and a vinyl side chain; every hydrogen shown',[('s','2',A,A),('vinyl','3',A,A)],'Goitrin, C5H7NOS'),'Goitrin','C₅H₇NOS')+'</div>'],
   [('1','Thiocyanate is a small negative ion about the size of iodide, so it competes with iodide for the pump that pulls iodide into the thyroid.',''),('2','Goitrin’s C=S group interferes with the enzyme that attaches iodine to make thyroid hormone…',''),('3','…it forms from a glucosinolate in brassica vegetables when they are cut or chewed.','')],
   fx=facts(what='Goitrogens are compounds that can enlarge the thyroid (cause goiter) by reducing how much iodine it takes up or uses. Most come from glucosinolates, the sulfur compounds that give cabbage family vegetables their bite (see Bioactives).',
     body='The thyroid needs iodide to make thyroxine (T4) and T3 (see Trace Minerals). Goitrogens slow that, so with too little iodine the gland grows to compensate.',
     high='A real problem mainly where iodine intake is low and a goitrogenic food is a staple, notably cassava, whose cyanide-releasing compounds are turned into thiocyanate. Normal servings of cooked broccoli, kale or cabbage are not a concern for people who get enough iodine.',
     found='Raw cabbage, kale, Brussels sprouts, turnips, rutabaga, collards, bok choy; cassava; millet; soy isoflavones have a weak effect in lab studies.'),head='Goitrogens')
 +legend('i c h o n s'))
P8=('<!--noart-->'+table('methods',['Method','What it does','Reduces'],[
   ['Soaking','water draws out water-soluble compounds and wakes up the seed’s own phytase; pour the water away','phytate, oxalate, tannins, lectins (partly)'],
   ['Sprouting','the seed breaks down its phytate store to feed the growing shoot','phytate, trypsin inhibitors, lectins'],
   ['Fermenting','microbes and their phytase break compounds down; sourdough bread has much less phytate than yeast bread','phytate, trypsin inhibitors, tannins, goitrogens'],
   ['Boiling','heat unfolds proteins; soluble compounds leach into the water, which is thrown away','lectins, trypsin inhibitors, oxalate, goitrogens'],
   ['Milling and peeling','removes the bran or skin, where many antinutrients sit, but also removes fiber, vitamins and minerals','phytate, tannins']],'Traditional ways to cut antinutrients')
 +lblock('pair','Pairing foods',[('Vitamin C with plant iron','Vitamin C in the same meal counteracts phytate and tannins and raises nonheme iron absorption (see Trace Minerals).'),
   ('Calcium with oxalate','Eating dairy or another calcium source with high-oxalate foods binds the oxalate in the gut, so less is absorbed.'),
   ('Tea and coffee between meals','Waiting an hour or so after an iron-rich meal keeps their polyphenols away from the iron.')])
 +note('heat','Heat-stable or not','<p>Lectins and trypsin inhibitors are proteins, so thorough cooking destroys most of them. Phytate, oxalate and tannins are small, sturdy molecules that survive heat; they are reduced mainly by soaking, sprouting, fermenting, or boiling and discarding the water.</p>'))
P9=('<!--noart-->'+table('table',['Antinutrient','What it is','What it blocks','Main sources','Best fix'],[
  ['Phytate','inositol with six phosphates; the seed’s phosphorus store','zinc, iron, calcium','whole grains, beans, nuts, seeds','soak, sprout, ferment (sourdough)'],
  ['Oxalate','a small two-carbon acid','calcium; kidney stones','spinach, rhubarb, chard, almonds, cocoa','boil and drain; eat with calcium'],
  ['Tannins','polyphenols built from gallic acid or catechin','nonheme iron; some protein','tea, red wine, sorghum, colored beans','drink tea between meals'],
  ['Lectins','sugar-binding proteins','gut lining; can cause vomiting','raw kidney beans and other raw legumes','soak, then boil hard'],
  ['Trypsin inhibitors','proteins that plug trypsin','protein digestion','raw soybeans and legumes, raw egg white','cook'],
  ['Goitrogens','glucosinolate products such as goitrin and thiocyanate','iodine use by the thyroid','raw brassicas, cassava, millet','cook; get enough iodine']],'The six antinutrients')
 +worth([('Same compound, two sides','Phytate, tannins and glucosinolates are antinutrients in one lesson and bioactives in the next: whether they help or hinder depends on the amount, the rest of the diet and how the food is prepared.'),
   ('Cassava and bitter almonds','Some plants make cyanogenic glycosides, which release cyanide when crushed. Cassava is made safe by soaking, grating, fermenting and drying; raw bitter almonds and apricot kernels should not be eaten.'),
   ('Green potatoes','Potatoes that turn green in the light also make solanine, a bitter glycoalkaloid that is not destroyed by cooking. Cut away green parts and sprouts, and discard potatoes that taste bitter.')],
   note='General education, not medical advice. Facts follow mainstream sources (US FDA, NIH Office of Dietary Supplements, WHO, standard nutrition and food-science texts).'))
AN_LESSON=[('The Antinutrient Family Tree','Six natural compounds, grouped by what they block.',P1),
 ('What Makes an Antinutrient','The minerals they grip, and three ways to block a nutrient.',P2),
 ('Phytate','Inositol with six phosphates: the seed’s phosphorus store.',P3),
 ('Oxalate','A tiny acid that locks up calcium.',P4),
 ('Tannins','Polyphenols that grip iron and proteins.',P5),
 ('Lectins and Trypsin Inhibitors','Proteins that stick to the gut or plug an enzyme.',P6),
 ('Goitrogens','Compounds that get in the way of iodine.',P7),
 ('Soaking, Sprouting, Fermenting, Cooking','The kitchen fixes, and which foods to pair.',P8),
 ('Putting It All Together','The whole lesson in one table, plus a few extras.',P9)]
AN_QUIZ=[('What is an antinutrient?','A natural compound in food that reduces how well you absorb or use a nutrient (Figure 1).'),
 ('Why do phytate, oxalate and tannins hold on to minerals?','They carry negative oxygen groups that grip positive mineral ions such as Zn²⁺, Fe³⁺ and Ca²⁺ (Figure 2).'),
 ('What is phytic acid built from?','An inositol ring with a phosphate on each of its six carbons (Figure 3).'),
 ('Which mineral does phytate lower the most?','Zinc, along with iron and calcium (Figure 3).'),
 ('Which antinutrient is high in spinach, and what does it bind?','Oxalate; it binds calcium (Figure 4).'),
 ('What are most kidney stones made of?','Calcium oxalate (Figure 4).'),
 ('Why drink tea between meals rather than with them if your iron is low?','Tea tannins bind nonheme iron in the meal (Figure 5).'),
 ('How do you make dried kidney beans safe?','Soak them, then boil them hard; warming without boiling is not enough (Figure 6).'),
 ('What does a trypsin inhibitor do, and what inactivates it?','It plugs trypsin so less protein is digested; cooking inactivates it (Figure 6).'),
 ('What do goitrogens affect?','How the thyroid takes up or uses iodine (Figure 7).'),
 ('Why does sourdough bread have less phytate than ordinary yeast bread?','The long fermentation activates phytase, which breaks phytate down (Figure 8).'),
 ('Which antinutrients are destroyed by cooking, and which survive it?','Lectins and trypsin inhibitors (proteins) are destroyed; phytate, oxalate and tannins mostly survive (Figure 8).')]
build_lesson('antinutrients','Antinutrients','Antinutrients are natural compounds in plant foods that reduce how well you absorb or use a nutrient: phytate, oxalate, tannins, lectins, trypsin inhibitors and goitrogens. Each is shown in ball-and-stick form or as a labeled cartoon, with what it does, who should pay attention, where it is found, and how soaking, sprouting, fermenting and cooking reduce it. The figure is on the left and the lesson script on the right; the quiz is at the end.',AN_LESSON,AN_QUIZ,mols=MN,scale=11)
