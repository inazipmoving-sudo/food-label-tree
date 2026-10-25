# ---------------- Module 2 · Water-Soluble Vitamins ----------------
import math
W2=mk_lmol('micronutrients-water-soluble-vitamins')
def _wf(n): return fsub(W2.D[n]['formula'].replace('+','^+'))
A=None
WS_NODES=[(450,30,260,'Water-Soluble Vitamins','eight B vitamins and C','nd root',None),
 (330,150,230,'B vitamins','all become coenzymes · Fig. 2','nd l','#fig-2'),(780,150,190,'Vitamin C','ascorbic acid · Fig. 7','nd l','#fig-7'),
 (90,270,150,'B1 · B2 · B3','energy · Fig. 3','nd u','#fig-3'),(250,270,150,'B5 · B7','energy · Fig. 4','nd u','#fig-4'),
 (410,270,150,'B6 · Folate','cells, DNA · Fig. 5','nd u','#fig-5'),(570,270,150,'B12','blood, nerves · Fig. 6','nd u','#fig-6'),(780,270,190,'Collagen','antioxidant · Fig. 7','nd u','#fig-7'),
 (90,390,150,'Beriberi','pellagra · Fig. 3','nd t','#fig-3'),(250,390,150,'Rarely short','in almost all foods · Fig. 4','nd t','#fig-4'),
 (410,390,150,'Anemia','neural tube defects · Fig. 5','nd t','#fig-5'),(570,390,150,'Anemia','nerve damage · Fig. 6','nd t','#fig-6'),(780,390,190,'Scurvy','bleeding gums · Fig. 7','nd t','#fig-7')]
WS_EDGES=[(450,52,330,128),(450,52,780,128)]+[(330,182,x,248) for x in (90,250,410,570)]+[(780,182,780,248)]+[(x,302,x,368) for x in (90,250,410,570,780)]
P1=('<!--noart-->'+ftree(WS_NODES,WS_EDGES,430,'Tree diagram: the water-soluble vitamins. B vitamins, which all become coenzymes: B1, B2 and B3 for energy (too little: beriberi, pellagra); B5 and B7 for energy (rarely short); B6 and folate for cells and DNA (too little: anemia, neural tube defects); B12 for blood and nerves (too little: anemia, nerve damage). Vitamin C: collagen and antioxidant (too little: scurvy).')
 +lblock('label','What they share',[('Covered in N and O','Their many oxygen and nitrogen atoms form hydrogen bonds with water, so they dissolve in it, unlike vitamins A, D, E and K.'),
   ('Little storage','Apart from B12, the body keeps only small reserves and passes extra in urine, so a steady supply from food matters.'),
   ('Easily lost in cooking','They leach into cooking water, and several (C, folate, thiamin) are damaged by heat; riboflavin is damaged by light (Figure 8).')]))
P2=('<!--noart-->'+flow('coenzyme','What a coenzyme is',[('Enzymes run your chemistry','proteins that speed up reactions, such as releasing energy from glucose and fat'),('Many need a helper','a small non-protein partner that carries electrons, carbon or other groups'),('B vitamins become those helpers','each is changed slightly in the body, often by adding phosphate'),('Reused, not burned','a little goes a long way, so needs are in milligrams or micrograms')])
 +table('table',['Vitamin','Becomes','Carries or does'],[
   ['B1 thiamin','thiamin pyrophosphate (TPP)','cuts carbon chains in carbohydrate breakdown'],['B2 riboflavin','FAD and FMN','carries electrons (hydrogens)'],
   ['B3 niacin','NAD and NADP','carries electrons; used in hundreds of reactions'],['B5 pantothenic acid','coenzyme A','carries two-carbon acetyl groups'],
   ['B6','pyridoxal phosphate (PLP)','moves amino groups between amino acids'],['B7 biotin','biotin bound to enzymes','adds CO<sub>2</sub> to molecules'],
   ['B9 folate','tetrahydrofolate (THF)','carries one-carbon units for DNA building blocks'],['B12','methylcobalamin, adenosylcobalamin','recycles folate; one step of fat and amino-acid breakdown']],'Each B vitamin and its coenzyme')
 +lblock('energy','The B vitamins don’t give energy',[('A common mix-up','B vitamins contain no usable calories. They are the tools that let your cells release the energy in carbohydrate, fat and protein, so a shortage makes you tired, but extra doesn’t make you more energetic.')]))
P3=('<!--noart-->'+molbox('b1','Thiamin (vitamin B1), '+_wf('thiamin'),[W2('thiamin','Thiamin: a six-membered ring with two nitrogens on the left joined by a CH2 bridge to a five-membered ring containing nitrogen and sulfur, with a CH2CH2OH arm; every hydrogen shown',[('pyr','1',A,A),('thz','2',A,A),('oh','3',A,A)],'Thiamin, C12H17N4OS+',eager=True)],
   [('1','A pyrimidine ring (two N atoms) with an NH<sub>2</sub>.',''),('2','A thiazole ring with sulfur (yellow); the positive N is part of the business end. Thiamin is one of only two vitamins with sulfur (biotin is the other).',''),('3','The OH is where two phosphates are added to make the coenzyme TPP.','')],
   fx=facts(body='As TPP, needed to break down glucose for energy and for nerve function. RDA 1.2 mg (men), 1.1 mg (women).',low='Beriberi: nerve damage, muscle weakness, heart failure. In heavy drinkers, a brain disorder (Wernicke-Korsakoff syndrome).',found='Pork, trout, black beans, lentils, whole grains, sunflower seeds.'),head='B1: thiamin')
 +molbox('b2','Riboflavin (vitamin B2), '+_wf('riboflavin'),[W2('riboflavin','Riboflavin: three fused rings (two with nitrogens) and a five-carbon sugar-alcohol chain with four OH groups; every hydrogen shown',[('rings','1',A,A),('chain','2',A,A)],'Riboflavin, C17H20N4O6')],
   [('1','Three flat rings that can take up and release two hydrogens: this is how FAD carries electrons. They make riboflavin bright yellow.',''),('2','A ribitol chain, a sugar alcohol with four OH groups.','')],
   fx=facts(body='As FAD and FMN, carries electrons in energy production. RDA 1.3 mg (men), 1.1 mg (women). Extra turns urine bright yellow, which is harmless.',low='Cracks at the corners of the mouth, sore red tongue, sore throat.',found='Milk, yogurt, eggs, liver, almonds, mushrooms. Light destroys it, which is why milk is sold in opaque containers.'),head='B2: riboflavin')
 +molbox('b3','Niacin (vitamin B3): two forms',[
   '<div class="mgrid">'+mcell(W2('niacin','Nicotinic acid: a pyridine ring with a COOH group; every hydrogen shown',[('cooh','1',A,A)],'Nicotinic acid, C6H5NO2'),'Nicotinic acid',_wf('niacin'))
   +mcell(W2('niacinamide','Nicotinamide: a pyridine ring with a CONH2 group; every hydrogen shown',[('amide','2',A,A)],'Nicotinamide, C6H6N2O'),'Nicotinamide',_wf('niacinamide'))+'</div>'],
   [('1','Nicotinic acid ends in COOH…',''),('2','…nicotinamide in CONH<sub>2</sub>. Both make NAD, the most widely used coenzyme in the body.','')],
   fx=facts(body='As NAD and NADP, used in hundreds of reactions. Your body can also make niacin from the amino acid tryptophan. RDA 16 mg (men), 14 mg (women).',low='Pellagra: rough, dark skin rash in sunlight, diarrhea, confusion.',high='Supplements of nicotinic acid above about 35 mg cause flushing; large doses can harm the liver. Food doesn’t cause this.',found='Tuna, chicken, turkey, salmon, peanuts, mushrooms, brown rice.'),head='B3: niacin')
 +legend('c h o n s'))
P4=('<!--noart-->'+molbox('b5','Pantothenic acid (vitamin B5), '+_wf('pantothenic'),[W2('pantothenic','Pantothenic acid: a branched chain with two OH groups joined by an amide link to a three-carbon acid; every hydrogen shown',[('amide','1',A,A),('cooh','2',A,A)],'Pantothenic acid, C9H17NO5',eager=True)],
   [('1','An amide link, like a peptide bond, joins two small pieces.',''),('2','The acid end. In the body it is built into coenzyme A, which carries two-carbon pieces in and out of the energy cycle.','')],
   fx=facts(what='Its name means “from everywhere”: almost every food has some.',body='Part of coenzyme A, needed to make and break down fats and to release energy. Adequate intake 5 mg a day.',low='Very rare; seen only in severe starvation or experiments: numbness and burning feet, fatigue.',found='Liver, chicken, mushrooms, avocado, eggs, sunflower seeds, whole grains.'),head='B5: pantothenic acid')
 +molbox('b7','Biotin (vitamin B7), '+_wf('biotin'),[W2('biotin','Biotin: two fused five-membered rings, one with sulfur and one with two NH groups and a C=O, and a five-carbon acid tail; every hydrogen shown',[('urea','1',A,A),('s','2',A,A),('cooh','3',A,A)],'Biotin, C10H16N2O3S')],
   [('1','The ring with two NH groups is where CO<sub>2</sub> is attached and handed on.',''),('2','The sulfur ring.',''),('3','The acid tail links biotin firmly to its enzymes.','')],
   fx=facts(body='Helps enzymes add CO<sub>2</sub> to molecules, in making fat, glucose and some amino acids. Adequate intake 30 µg a day.',low='Rare: thinning hair, red scaly rash. Avidin in raw egg white binds biotin, but only large amounts of raw whites over long periods cause a problem; cooking destroys avidin.',high='No harm known, but high-dose supplements can distort some blood tests, including thyroid and heart tests.',found='Egg yolks, liver, salmon, sunflower seeds, almonds, sweet potato.'),head='B7: biotin')
 +legend('c h o n s'))
P5=('<!--noart-->'+molbox('b6','Pyridoxine (vitamin B6), '+_wf('pyridoxine'),[W2('pyridoxine','Pyridoxine: a pyridine ring with a methyl, an OH and two CH2OH groups; every hydrogen shown',[('n','1',A,A),('ch2oh','2',A,A)],'Pyridoxine, C8H11NO3',eager=True)],
   [('1','A pyridine ring: a benzene-like ring with one nitrogen.',''),('2','In the body this CH<sub>2</sub>OH becomes an aldehyde and a phosphate is added, making pyridoxal phosphate (PLP), the working coenzyme.','')],
   fx=facts(body='As PLP, needed by over 100 enzymes, mostly in amino-acid metabolism; also for making neurotransmitters and hemoglobin. RDA 1.3 mg for adults up to 50, then 1.7 mg (men) and 1.5 mg (women).',low='Anemia, cracked lips, sore tongue, depression and confusion.',high='Long-term supplements above the upper limit (100 mg a day) can cause nerve damage in the hands and feet.',found='Chickpeas, tuna, salmon, chicken, potatoes, bananas.'),head='B6')
 +molbox('folate','Folic acid and food folate',[
   '<p class="mt">Folic acid (the form added to foods), '+_wf('folicacid')+'</p>'+W2('folicacid','Folic acid: a two-ring pterin unit on the left, joined through a CH2-NH to a benzene ring, then by an amide to glutamic acid on the right; every hydrogen shown',[('pter','1',A,A),('paba','2',A,A),('glu','3',A,A)],'Folic acid, C19H19N7O6')
   +'<p class="mt">5-Methyltetrahydrofolate (the main form in food and blood), '+_wf('mthf')+'</p>'+W2('mthf','5-Methyltetrahydrofolate: the same three parts, but the pterin unit has four extra hydrogens and a methyl group on one nitrogen; every hydrogen shown',[('h4','4',A,A),('me','5',A,A)],'5-Methyltetrahydrofolate, C20H25N7O6')],
   [('1','<b>Pterin</b>: two rings rich in nitrogen.',''),('2','<b>Para-aminobenzoic acid</b>: a benzene ring linking the two ends.',''),('3','<b>Glutamate</b>, an amino acid. Food folates usually carry a chain of several glutamates, trimmed off in the gut.',''),
    ('4','<b>Four more hydrogens</b> here (tetrahydro): this reduced ring is the active form that carries one-carbon units.',''),('5','<b>A methyl group</b>: the one-carbon unit, ready to hand on (to B12, Figure 6).','')],
   fx='<p class="mfact"><b>Folate vs folic acid:</b> “folate” covers all the natural forms. Folic acid is the synthetic, fully oxidized form: very stable and better absorbed (about 1.7 times as well as food folate), so it is used in supplements and fortified flour. The body must add the four hydrogens before it can use it.</p>'
   +facts(body='Carries one-carbon units to build DNA and to recycle the amino acid homocysteine; essential for cell division. RDA 400 µg DFE (dietary folate equivalents); 600 µg in pregnancy.',
     low='Megaloblastic anemia (large, immature red cells). Before and early in pregnancy, low folate raises the risk of neural tube defects such as spina bifida, which is why folic acid is recommended for anyone who could become pregnant.',
     high='No harm known from food folate. Folic acid above the upper limit (1,000 µg a day) can hide the anemia of B12 deficiency while its nerve damage continues.',
     found='Lentils, chickpeas, black-eyed peas, spinach, asparagus, Brussels sprouts, avocado, liver. Its name comes from Latin <i>folium</i>, leaf.'),head='B9: folate')
 +legend('c h o n'))
def _b12svg():
    cx,cy,R,sy=150,105,72,0.5
    o=['<line x1="150" y1="105" x2="150" y2="34" stroke="#8a8a8a" stroke-width="5"/><circle cx="150" cy="28" r="13" fill="#E39A3B" stroke="#8a5a10" stroke-width="2"/>',
       '<path d="M226 128 Q272 128 272 150 L272 172 Q272 192 245 192 L165 192 Q150 192 150 178" fill="none" stroke="#8a8a8a" stroke-width="5"/><line x1="150" y1="105" x2="150" y2="168" stroke="#8a8a8a" stroke-width="4"/>']
    ring=[];ns=[]
    for k in range(4):
        a=math.radians(45+90*k); px,py=cx+R*math.cos(a),cy+R*math.sin(a)*sy
        pts=[]
        for j in range(5):
            b=a+math.pi+math.radians(72*j); pts.append((px+26*math.cos(b),py+26*math.sin(b)*sy))
        ring.append(f'<polygon points="{" ".join(f"{x:.1f},{y:.1f}" for x,y in pts)}" fill="#bdbdbd" fill-opacity=".45" stroke="#8c8c8c" stroke-width="4" stroke-linejoin="round"/>')
        ns.append(pts[0])
    for k in range(4):
        a=math.radians(90*k+90); ring.append(f'<circle cx="{cx+R*0.72*math.cos(a):.1f}" cy="{cy+R*0.72*math.sin(a)*sy:.1f}" r="5" fill="#8c8c8c"/>')
    o=[o[1]]+ring+[f'<line x1="{cx}" y1="{cy}" x2="{x:.1f}" y2="{y:.1f}" stroke="#2F55F0" stroke-width="3"/><circle cx="{x:.1f}" cy="{y:.1f}" r="6" fill="#2F55F0"/>' for x,y in ns]+[o[0],'<circle cx="150" cy="105" r="15" fill="#E8A0C8" stroke="#8a3a6a" stroke-width="2"/><circle cx="150" cy="172" r="8" fill="#2F55F0"/>']
    return ''.join(o)
P6=('<!--noart-->'+stages('b12','Vitamin B12 (cobalamin)',[('A big molecule built around cobalt',svgd(_b12svg(),'50 8 240 196','Cartoon of vitamin B12: a pink cobalt atom at the centre held by four nitrogens of a ring made of four linked five-membered rings; an orange group above the cobalt; below, a blue nitrogen of a long looping tail',260),
   'B12 is the largest and most complex vitamin: about 180 atoms (cyanocobalamin is C<sub>63</sub>H<sub>88</sub>CoN<sub>14</sub>O<sub>14</sub>P), too big to draw atom by atom at this page’s scale. At its heart is a <b>cobalt</b> atom (pink) held by four nitrogens (blue) of a ring of four linked five-membered rings, the <b>corrin</b> ring (gray), seen here at a slant. Below, a long tail loops round so that a nitrogen at its end (blue, below) holds the cobalt from underneath. The group on top (orange) varies: methyl or adenosyl in the body’s two coenzymes, hydroxo in food, cyano in most supplements.')],cap='Cartoon, not to scale.')
 +flow('absorb','How B12 is absorbed',[('In food','B12 is bound to protein'),('Stomach','acid and enzymes release it'),('Intrinsic factor','a protein made by the stomach lining binds the B12'),('End of the small intestine','the pair is taken up together'),('Stored','the liver keeps a supply that can last several years')])
 +lblock('who','Who runs short',[('Vegans','Only bacteria make B12, and it reaches us through animal foods. Plant foods don’t provide reliable amounts, so vegans need fortified foods or a supplement.'),
   ('Older adults','Many have less stomach acid and absorb less B12 from food; the synthetic form in fortified foods and supplements is absorbed more easily.'),
   ('People without intrinsic factor','Pernicious anemia, an autoimmune condition, or stomach surgery stops absorption; treatment is by injection or high doses, under a doctor’s care.')])
 +'<div class="art mols" data-part="b12facts"><p class="mt">Vitamin B12 at a glance</p>'+facts(body='Works with folate to make DNA and red blood cells; keeps the nerves’ insulating sheath healthy. RDA 2.4 µg a day.',
   low='Megaloblastic anemia and fatigue; numbness, tingling, balance problems and memory changes that can become permanent.',
   high='No harm known from food or supplements, so there is no upper limit.',found='Clams, liver, sardines, salmon, beef, eggs, milk, yogurt, cheese.')+'</div>')
P7=('<!--noart-->'+molbox('c','Vitamin C: ascorbic acid and its oxidized form',[
   '<div class="mgrid">'+mcell(W2('ascorbic','Ascorbic acid: a five-membered ring containing an oxygen, with a C=C double bond carrying two OH groups, and a two-carbon side chain with two more OH groups; every hydrogen shown',[('enediol','1',A,A),('side','3',A,A)],'Ascorbic acid, C6H8O6',eager=True),'Ascorbic acid',_wf('ascorbic'))
   +mcell(W2('dehydroascorbic','Dehydroascorbic acid: the same ring with the two OH carbons now both C=O; every hydrogen shown',[('keto','2',A,A)],'Dehydroascorbic acid, C6H6O6'),'Dehydroascorbic acid',_wf('dehydroascorbic'))+'</div>'],
   [('1','<b>Two OH groups on a C=C</b>: they give up two hydrogens (with their electrons) very easily. That is what makes vitamin C an antioxidant and a helper for enzymes.',''),
    ('2','After giving them up, both carbons carry a C=O: <b>dehydroascorbic acid</b>. Your cells can take it up and turn it back into ascorbic acid.',''),
    ('3','Four OH groups in all: very water-soluble.','')],fx=facts(what='Humans, along with a few other animals such as guinea pigs, can’t make vitamin C, because the gene for the last enzyme of the pathway no longer works.',
   body='RDA 90 mg (men), 75 mg (women); smokers need 35 mg more.',
   low='Scurvy, after about a month of very low intake: tiredness, bleeding and swollen gums, easy bruising, slow wound healing.',
   high='Above the upper limit (2,000 mg a day, from supplements), diarrhea and stomach upset; possibly kidney stones in some people.',
   found='Bell peppers, kiwi, oranges and other citrus, strawberries, broccoli, Brussels sprouts, tomatoes, potatoes.'),head='Vitamin C')
 +lblock('jobs','What vitamin C does',[('Collagen','Enzymes that make collagen, the protein of skin, gums, tendons and blood vessels, need vitamin C to stay active.'),
   ('Iron','It turns plant (non-heme) iron into a form that is absorbed more easily when eaten in the same meal.'),
   ('Antioxidant','It mops up reactive molecules in water-based parts of the body and helps restore vitamin E.')])
 +legend('c h o'))
P8=('<!--noart-->'+table('losses',['Vitamin','Damaged by','To keep more'],[
   ['C, folate, thiamin','heat; also leach into cooking water','steam or microwave briefly; use less water; eat some fruit and vegetables raw'],
   ['Riboflavin','light','store milk and grains out of light'],['B12, niacin, biotin','fairly stable','—']],'Cooking and storage')
 +table('labelforms',['On the label or ingredient list','Vitamin'],[
   ['Thiamin mononitrate, thiamin hydrochloride','B1'],['Riboflavin','B2 (also a yellow color, E101)'],['Niacin, niacinamide (nicotinamide)','B3'],
   ['Calcium pantothenate','B5'],['Pyridoxine hydrochloride','B6'],['Biotin','B7'],['Folic acid; L-methylfolate','B9'],['Cyanocobalamin, methylcobalamin','B12'],
   ['Ascorbic acid, sodium ascorbate (E300, E301)','C; also used as an antioxidant to stop browning']],'Forms you will see')
 +lblock('enriched','Enriched and fortified',[('Enriched flour','In the US, refined wheat flour is usually enriched: thiamin, riboflavin, niacin and iron are added back after milling removes them, and folic acid has been required in enriched grain products since 1998.'),
   ('Folate on the label','Folate is listed in µg DFE; if folic acid is added, the label also shows the amount of folic acid in parentheses.'),
   ('Daily Values','Thiamin 1.2 mg, riboflavin 1.3 mg, niacin 16 mg, B6 1.7 mg, folate 400 µg DFE, B12 2.4 µg, biotin 30 µg, pantothenic acid 5 mg, vitamin C 90 mg.')]))
P9=('<!--noart-->'+table('table',['Vitamin','Main job','Too little','Whole-food sources'],[
  ['B1 thiamin','carbohydrate energy, nerves','beriberi','pork, beans, whole grains, sunflower seeds'],['B2 riboflavin','carries electrons','sore mouth and tongue','milk, eggs, almonds, mushrooms'],
  ['B3 niacin','NAD, hundreds of reactions','pellagra','tuna, chicken, peanuts, mushrooms'],['B5 pantothenic acid','coenzyme A','very rare','almost every food'],
  ['B6','amino acids, neurotransmitters','anemia, confusion','chickpeas, fish, poultry, potatoes, bananas'],['B7 biotin','adds CO<sub>2</sub>','rare: hair, skin','eggs, salmon, seeds, sweet potato'],
  ['B9 folate','DNA, cell division','anemia; neural tube defects','lentils, leafy greens, asparagus'],['B12 cobalamin','DNA, red cells, nerves','anemia, nerve damage','animal foods only: clams, fish, meat, eggs, dairy'],
  ['C ascorbic acid','collagen, iron, antioxidant','scurvy','peppers, kiwi, citrus, strawberries, broccoli']],'The nine water-soluble vitamins')
 +worth([('Bright yellow urine','After a B-complex supplement, the extra riboflavin passes into urine and colors it bright yellow. It’s harmless.'),
   ('Vitamin C and colds','Taking vitamin C regularly doesn’t prevent colds in most people; it may shorten them slightly.'),
   ('Lime-treated corn','Corn’s niacin is tightly bound. Traditional cooking of corn with lime (nixtamalization, as for tortillas) frees it, which protected people from pellagra.'),
   ('Choline','Choline is an essential nutrient grouped with the B vitamins, with an adequate intake of its own (550 mg men, 425 mg women); it is found in eggs, liver, meat, fish and soybeans.')]))
WS_LESSON=[('The Water-Soluble Vitamin Family Tree','Eight B vitamins and vitamin C.',P1),
 ('Coenzymes: What B Vitamins Do','Small helpers that let enzymes work.',P2),
 ('B1, B2 and B3','Thiamin, riboflavin and niacin: energy release.',P3),
 ('B5 and B7','Pantothenic acid and biotin.',P4),
 ('B6 and Folate','Amino acids, DNA, and folate versus folic acid.',P5),
 ('Vitamin B12','The cobalt vitamin, and who runs short.',P6),
 ('Vitamin C','Ascorbic acid: collagen, iron and antioxidant.',P7),
 ('Cooking and Labels','What destroys them, and the forms on labels.',P8),
 ('Putting It All Together','The whole lesson in one table, plus a few extras.',P9)]
WS_QUIZ=[('Why do the B vitamins and vitamin C dissolve in water?','They have many oxygen and nitrogen atoms that form hydrogen bonds with water (Figure 1).'),
 ('Which water-soluble vitamin is stored for years?','B12, in the liver (Figure 6).'),
 ('What is a coenzyme?','A small non-protein helper an enzyme needs to work; B vitamins become coenzymes (Figure 2).'),
 ('Do B vitamins provide energy?','No. They contain no usable calories; they help release energy from food (Figure 2).'),
 ('Which deficiency disease comes from too little thiamin? From too little niacin?','Beriberi; pellagra (Figure 3).'),
 ('Which two vitamins contain sulfur?','Thiamin (B1) and biotin (B7) (Figures 3 and 4).'),
 ('Why is milk sold in opaque containers?','Light destroys riboflavin (Figure 3).'),
 ('How does folic acid differ from the main food folate?','Folic acid lacks the four extra hydrogens and the methyl group; it is synthetic, stable and better absorbed (Figure 5).'),
 ('Why is folic acid recommended for anyone who could become pregnant?','It lowers the risk of neural tube defects such as spina bifida (Figure 5).'),
 ('What metal is at the center of vitamin B12?','Cobalt (Figure 6).'),
 ('Why do vegans need fortified foods or a B12 supplement?','Only bacteria make B12 and plant foods don’t provide reliable amounts (Figure 6).'),
 ('Name three things vitamin C does.','Keeps collagen-making enzymes working, helps absorb plant iron, acts as an antioxidant (Figure 7).')]
build_lesson('micronutrients-water-soluble-vitamins','Water-Soluble Vitamins','The second micronutrient lesson covers the nine water-soluble vitamins: the eight B vitamins and vitamin C. Unlike A, D, E and K, they dissolve in water, are stored only in small amounts (except B12) and are easily lost in cooking. The B vitamins all become coenzymes, small helpers that let enzymes release energy and build new cells. Each is shown as a ball-and-stick model with what it does, what happens with too little or too much, and where to find it in whole foods, including the difference between folate and folic acid. The figure is on the left and the lesson script on the right; the quiz is at the end.',WS_LESSON,WS_QUIZ,mols=W2)
