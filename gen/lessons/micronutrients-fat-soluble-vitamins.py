# ---------------- Module 2 · Fat-Soluble Vitamins ----------------
V_=mk_lmol('micronutrients-fat-soluble-vitamins')
def _vf(n): return fsub(V_.D[n]['formula'])
FS_NODES=[(450,30,260,'Fat-Soluble Vitamins','A, D, E and K','nd root',None),
 (120,150,190,'Vitamin A','vision, growth · Fig. 3','nd l','#fig-3'),(340,150,190,'Vitamin D','calcium, bone · Fig. 4','nd l','#fig-4'),
 (560,150,190,'Vitamin E','antioxidant · Fig. 5','nd l','#fig-5'),(780,150,190,'Vitamin K','blood clotting · Fig. 6','nd l','#fig-6'),
 (120,270,190,'Retinol, retinal','preformed · Fig. 3','nd u','#fig-3'),(340,270,190,'D3 (cholecalciferol)','from skin or animals · Fig. 4','nd u','#fig-4'),
 (560,270,190,'Alpha-tocopherol','the form you need · Fig. 5','nd u','#fig-5'),(780,270,190,'K1 (phylloquinone)','from plants · Fig. 6','nd u','#fig-6'),
 (120,390,190,'Beta-carotene','provitamin A · Fig. 3','nd t','#fig-3'),(340,390,190,'D2 (ergocalciferol)','from fungi · Fig. 4','nd t','#fig-4'),
 (560,390,190,'Other tocopherols','gamma, delta · Fig. 5','nd t','#fig-5'),(780,390,190,'K2 (menaquinones)','from bacteria · Fig. 6','nd t','#fig-6')]
FS_EDGES=[(450,52,x,128) for x in (120,340,560,780)]+[(x,182,x,248) for x in (120,340,560,780)]+[(x,302,x,368) for x in (120,340,560,780)]
P1=('<!--noart-->'+ftree(FS_NODES,FS_EDGES,430,'Tree diagram: the four fat-soluble vitamins. Vitamin A: retinol and retinal (preformed) and beta-carotene (provitamin A). Vitamin D: D3 cholecalciferol and D2 ergocalciferol. Vitamin E: alpha-tocopherol and other tocopherols. Vitamin K: K1 phylloquinone and K2 menaquinones.')
 +lblock('label','What they share',[('Built mostly of carbon and hydrogen','All four are lipids, assembled from five-carbon isoprene units (Figure 2), so they dissolve in fat, not water.'),
   ('Absorbed with fat, stored in the body','They need fat and bile to be absorbed and are stored in the liver and fat tissue (Figure 7). Stores last weeks to months, so you don’t need them every day.'),
   ('Storage cuts both ways','Because they build up, large supplement doses of A and D can be harmful. Food sources almost never cause too much.')]))
P2=('<!--noart-->'+molbox('isoprene','Isoprene, '+_vf('isoprene'),[V_('isoprene','Isoprene: a four-carbon chain with two double bonds and a methyl branch on the second carbon; every hydrogen shown',[('me','1',None,None)],'Isoprene, C5H8',eager=True)],
   [('1','Five carbons: a four-carbon chain with a one-carbon branch. Plants and animals join these units head to tail to build long, oily molecules.','')],head='The building block')
 +molbox('retinol','Retinol (vitamin A), '+_vf('retinol'),[V_('retinol','Retinol: a six-carbon ring on the left and a chain of alternating double bonds ending in CH2OH on the right; every hydrogen shown',[('u1','1',None,None),('chain','2',None,None),('end','3',None,None)],'Retinol, C20H30O')],
   [('1','The ring and its first branches come from isoprene units, folded around.',''),('2','Four isoprene units in all: 20 carbons, with alternating single and double bonds along the chain.',''),('3','Just one OH group: too small a water-loving patch for 30 hydrogens of oily chain.','')],
   fx='<p class="mfact">Compare glucose, with an OH on almost every carbon (Carbohydrates, Figure 3). Retinol is mostly C–H, like a fat, so it dissolves in oil, not water.</p>',head='Isoprene units, joined')
 +table('compare',['','Fat-soluble (A, D, E, K)','Water-soluble (B group, C)'],[
  ['Made mostly of','carbon and hydrogen','many O and N atoms, OH groups'],['Absorbed','with fat, via bile, into lymph','directly into blood'],
  ['Stored','liver and fat tissue, for weeks to months','little storage (except B12); extra leaves in urine'],['Too much','possible with supplements (especially A and D)','less common, but possible for some (B6, niacin)']],'Fat-soluble versus water-soluble')
 +legend('c h o'))
P3=('<!--noart-->'+molbox('retinal','Retinol and retinal',[
   '<div class="mgrid">'+mcell(V_('retinol','Retinol',[('end','1',None,None)],'Retinol, C20H30O'),'Retinol','the form stored and carried')
   +mcell(V_('retinal','Retinal: the same as retinol but the last carbon carries a double-bonded oxygen (an aldehyde) instead of an OH; every hydrogen shown',[('cho','2',None,None)],'Retinal, C20H28O'),'Retinal','the form used in the eye')+'</div>'],
   [('1','Retinol ends in CH<sub>2</sub>OH.',''),('2','Remove two hydrogens and it becomes retinal, ending in CH=O. Retinal can be turned into retinoic acid, which switches genes on and off for cell growth.','')],
   fx='<p class="mfact">Drawn straight (all-trans). In the eye, retinal sits bent at one double bond (11-cis) inside a protein; light straightens it, and that change is the first step of seeing.</p>'
   +facts(what='Preformed vitamin A: retinol and the forms made from it (retinal, retinoic acid, and retinyl esters for storage).',
    body='Vision, especially in dim light; healthy skin and the linings of the eyes, gut and lungs; immune defense; growth and development.',
    low='Night blindness, then dry, damaged eyes; more infections. A leading cause of preventable blindness in children worldwide, though rare in the US.',
    high='Preformed vitamin A builds up in the liver. Large supplement doses can cause liver damage and, in pregnancy, birth defects. Adult upper limit: 3,000 µg a day of preformed vitamin A.',
    found='Liver (very high), fish liver oils, oily fish, eggs, butter, milk and cheese.'),head='Vitamin A')
 +molbox('bc','Beta-carotene, '+_vf('betacarotene'),[V_('betacarotene','Beta-carotene: a long chain of alternating double bonds with a six-carbon ring at each end; every hydrogen shown',[('center','1',None,None),('ring1','2',None,None)],'Beta-carotene, C40H56')],
   [('1','<b>The middle</b>: a gut enzyme cuts here, and each half becomes retinal. So beta-carotene is <b>provitamin A</b>.',''),('2','<b>Rings</b>: the same ring as retinol, one at each end.','')],
   fx=facts(what='An orange plant pigment (a carotenoid) made of eight isoprene units.',
    body='Converted to vitamin A only as needed, so food sources don’t cause vitamin A poisoning. It takes about 12 µg of beta-carotene from food to make 1 µg of retinol activity (RAE).',
    high='Very large intakes turn the skin yellow-orange, which is harmless. High-dose supplements raised lung cancer risk in smokers in two large trials.',
    found='Carrots, sweet potato, pumpkin and squash, spinach and kale, cantaloupe, mango, apricots.'))
 +legend('c h o'))
P4=('<!--noart-->'+'<div class="part">Vitamin D: made in your skin</div><div class="art mols" data-part="skin">'
 +'<p class="mt">7-Dehydrocholesterol</p>'+V_('dhc7','7-Dehydrocholesterol: the four-ring cholesterol skeleton with two double bonds in the second ring; every hydrogen shown',[('b9','2',0,0),('db78','1',None,None)],'7-Dehydrocholesterol, C27H44O')
 +'<div class="op" style="text-align:center;margin:6px 0">↓ <small style="font-size:.9rem">UVB sunlight, then body heat</small></div>'
 +'<p class="mt">Vitamin D3 (cholecalciferol), '+_vf('vitd3')+'</p>'+V_('vitd3','Vitamin D3: the same atoms with the second ring broken open, leaving a chain of double bonds joining the first ring to the last two; every hydrogen shown',[('opened','3',None,None),('oh','4',None,None)],'Vitamin D3, C27H44O')
 +mleg([('1','7-Dehydrocholesterol is cholesterol with one extra double bond, here. Your skin has plenty of it.',''),('2','UVB light breaks the ring at this bond.',''),('3','The ring is now open: D3 is a <b>secosteroid</b>, a steroid with a broken ring. Same formula, C<sub>27</sub>H<sub>44</sub>O, nothing added.',''),('4','The OH from cholesterol survives. Two more OH groups are added later to make the active hormone.','')])+'</div>'
 +molbox('d2','Vitamin D2 (ergocalciferol), '+_vf('vitd2'),[V_('vitd2','Vitamin D2: like D3 but with a double bond and an extra methyl group in the tail; every hydrogen shown',[('db','1',None,None),('me','2',None,None)],'Vitamin D2, C28H44O')],
   [('1','A double bond in the tail…',''),('2','…and one extra carbon. Otherwise the same as D3. Fungi and yeast make D2 from ergosterol when exposed to UV light.','')])
 +flow('activate','From vitamin D to hormone',[('Skin or food','D3 or D2 reaches the liver'),('Liver','adds an OH: 25-hydroxyvitamin D, the form blood tests measure'),('Kidney','adds a second OH: calcitriol, the active hormone'),('Gut and bone','calcitriol raises calcium and phosphate absorption and keeps bone mineralized')])
 +lblock('dfacts','Vitamin D in brief',[('Needs','RDA 15 µg (600 IU) a day for ages 1 to 70, 20 µg (800 IU) over 70. Sunlight supplies a variable amount, depending on season, latitude, skin color and sunscreen.'),
   ('Too little','Soft, weak bones: rickets in children, osteomalacia in adults; more risk of fractures in later life.'),
   ('Too much','Only from supplements, not sunlight: high blood calcium, nausea, kidney stones. Adult upper limit 100 µg (4,000 IU) a day.')])
 +'<div class="art mols" data-part="dfound">'+facts(found='Oily fish (salmon, trout, sardines, mackerel), cod liver oil, egg yolks, beef liver, and mushrooms exposed to UV light (D2). Few foods have much naturally, which is why milk and some other foods are fortified.')+'</div>'
 +legend('c h o'))
P5=('<!--noart-->'+molbox('toc','Alpha- and gamma-tocopherol',[
   '<div class="mgrid">'+mcell(V_('tocopherol','Alpha-tocopherol: a two-ring head carrying an OH and three methyl groups, with a long 16-carbon tail; every hydrogen shown',[('oh','1',None,None),('me5','2',None,None),('tail','3',None,None)],'Alpha-tocopherol, C29H50O2'),'Alpha-tocopherol',_vf('tocopherol'))
   +mcell(V_('gtocopherol','Gamma-tocopherol: the same, but with a hydrogen instead of one of the three methyl groups on the head; every hydrogen shown',[('h5','2',None,None)],'Gamma-tocopherol, C28H48O2'),'Gamma-tocopherol',_vf('gtocopherol'))+'</div>'],
   [('1','<b>The OH</b> on the ring head is the working part: it gives up its hydrogen to stop a chain reaction of damage.',''),
    ('2','<b>One methyl group</b>: alpha has it, gamma has a plain H here. Only the alpha form is kept in the blood by the liver and counts toward your vitamin E needs.',''),
    ('3','<b>The tail</b> anchors the molecule inside fatty cell membranes, right where it is needed.','')],head='Vitamin E')
 +flow('antiox','How vitamin E protects membranes',[('Damage starts','a reactive oxygen molecule steals a hydrogen from a polyunsaturated fatty acid in a membrane'),('Chain reaction','the damaged fatty acid attacks its neighbor, and so on'),('Vitamin E steps in','its ring OH hands over a hydrogen and stops the chain'),('Recycled','vitamin C and other antioxidants restore vitamin E')])
 +'<div class="art mols" data-part="efacts">'+facts(what='A family of eight related compounds (four tocopherols, four tocotrienols); alpha-tocopherol is the one your body uses to meet its needs.',
    body='The main fat-soluble antioxidant, protecting the polyunsaturated fats in cell membranes and in blood lipoproteins.',
    low='Rare, and mostly in people who can’t absorb fat: nerve and muscle damage, poor balance, weakened immunity.',
    high='Not from food. Supplements above the adult upper limit (1,000 mg a day) raise the risk of bleeding.',
    found='Sunflower seeds, almonds, hazelnuts, peanuts, wheat germ, sunflower and safflower oils, spinach. RDA 15 mg a day of alpha-tocopherol.')+'</div>'
 +legend('c h o'))
P6=('<!--noart-->'+molbox('k','Vitamins K1 and K2',[
   '<p class="mt">K1 (phylloquinone), '+_vf('vitk1')+'</p>'+V_('vitk1','Vitamin K1: a two-ring head with two double-bonded oxygens, and a long, mostly saturated 20-carbon tail; every hydrogen shown',[('o1','1',None,None),('tail','2',None,None)],'Vitamin K1, C31H46O2')
   +'<p class="mt">K2, menaquinone-4 (MK-4), '+_vf('mk4')+'</p>'+V_('mk4','Vitamin K2 menaquinone-4: the same head with a tail of four isoprene units, each keeping its double bond; every hydrogen shown',[('dbs','3',None,None)],'Vitamin K2 MK-4, C31H40O2')],
   [('1','<b>The head</b>: a double ring with two C=O groups (a naphthoquinone). It is the same in every form of vitamin K and does the chemistry.',''),
    ('2','<b>K1’s tail</b>: four isoprene units, only the first with a double bond. Plants make it in their leaves.',''),
    ('3','<b>K2’s tail</b>: isoprene units that keep their double bonds. MK-4 has four; bacteria make longer ones, such as MK-7.','')],head='Vitamin K')
 +flow('clot','What vitamin K does',[('Clotting proteins are made','the liver makes several clotting factors in an inactive form'),('Vitamin K activates them','it helps add an extra carboxyl group to certain amino acids'),('Now they hold calcium','and can gather at a wound to form a clot'),('Also in bone','the same change activates proteins that bind calcium in bone')])
 +'<div class="art mols" data-part="kfacts">'+facts(what='A family of naphthoquinones: K1 from plants and K2 (menaquinones) from bacteria and animal foods.',
    body='Needed to activate clotting proteins and some bone proteins. Adequate intake 120 µg a day for men, 90 µg for women.',
    low='Easy bleeding and bruising. Rare in adults; newborns get a vitamin K injection at birth because little crosses the placenta and breast milk is low in it.',
    high='No harm known from food or supplements, so there is no upper limit. People taking the blood thinner warfarin are advised to keep their vitamin K intake steady, because it counteracts the drug.',
    found='K1: kale, spinach, collards, broccoli, Brussels sprouts, lettuce, soybean and canola oils. K2: natto (fermented soybeans), cheese, egg yolks, chicken, liver.')+'</div>'
 +legend('c h o'))
P7=('<!--noart-->'+flow('absorb','From food to storage',[('Eaten with fat','a little fat in the same meal greatly improves absorption'),('Bile','mixes the vitamins with fats into tiny droplets (micelles)'),('Gut wall','they are packed into chylomicrons with the fat'),('Lymph, then blood','carried around the body, then to the liver'),('Stored','vitamin A mainly in the liver; D and E in fat tissue and liver; K is used up fastest')])
 +table('labelforms',['On the label or ingredient list','What it is','Notes'],[
   ['Retinyl palmitate, retinyl acetate','vitamin A esters','stable forms used in fortified milk and supplements'],
   ['Beta-carotene (E160a)','provitamin A','also used as a yellow-orange color'],
   ['Cholecalciferol, ergocalciferol','vitamin D3, vitamin D2','D3 is from animals (often lanolin); D2 from UV-treated yeast or mushrooms'],
   ['d-alpha-tocopherol','natural vitamin E','full activity'],['dl-alpha-tocopheryl acetate','synthetic vitamin E','about half the activity of the natural form'],
   ['Tocopherols (E306–E309)','vitamin E family','often added as antioxidants to stop oils going rancid'],
   ['Phylloquinone (phytonadione), menaquinone-7','vitamin K1, K2','K2 as MK-7 is common in supplements']],'Forms you will see')
 +table('dv',['Vitamin','Daily Value','Unit used'],[['A','900 µg','µg RAE (retinol activity equivalents)'],['D','20 µg','µg; IU may also appear (1 µg = 40 IU)'],['E','15 mg','mg alpha-tocopherol'],['K','120 µg','µg']],'Nutrition Facts Daily Values (adults)')
 +lblock('labels','Reading the label',[('Only vitamin D is required','Since the 2016 update, US labels must list vitamin D (with calcium, iron and potassium). Vitamins A, E and K are listed only when added or when a claim is made.'),
   ('% Daily Value','The DV is a single reference amount for labels; your own needs may be higher or lower.')]))
P8=('<!--noart-->'+table('table',['Vitamin','Main forms','Main job','Too little','Too much','Whole-food sources'],[
  ['A','retinol, retinal; beta-carotene','vision, skin and linings, immunity','night blindness','liver damage, birth defects (preformed A)','liver, eggs, dairy; orange and green vegetables'],
  ['D','D3, D2','calcium absorption, bone','rickets, osteomalacia','high blood calcium (supplements)','oily fish, egg yolks, UV mushrooms; sunlight'],
  ['E','alpha-tocopherol','antioxidant in membranes','nerve damage (rare)','bleeding risk (supplements)','seeds, nuts, wheat germ, plant oils'],
  ['K','K1, K2','activates clotting and bone proteins','bleeding','none known','leafy greens; natto, cheese, eggs']],'The four fat-soluble vitamins')
 +worth([('Eat colorful vegetables with a little fat','Carotenoids and vitamin K from vegetables are absorbed much better with some oil, nuts or other fat in the meal.'),
   ('Liver is the richest source of vitamin A','A typical serving of beef liver has several times the adult RDA, so it is best eaten occasionally, especially in pregnancy.'),
   ('Sun and vitamin D','Skin stops making more vitamin D once enough has formed, so sunlight can’t cause vitamin D poisoning; supplements can.'),
   ('Cholesterol’s relatives','Vitamin D is made from a cholesterol precursor, and A, E and K are built from the same isoprene units as cholesterol (Lipids, Figure 3).')]))
FS_LESSON=[('The Fat-Soluble Vitamin Family Tree','A, D, E and K: four lipids you can’t make enough of.',P1),
 ('Built from Isoprene','Why these four vitamins dissolve in fat, not water.',P2),
 ('Vitamin A','Retinol, retinal and beta-carotene.',P3),
 ('Vitamin D','Made in your skin from a cholesterol relative, then activated.',P4),
 ('Vitamin E','The tocopherols, and how they protect cell membranes.',P5),
 ('Vitamin K','Two forms, one working head: clotting and bone.',P6),
 ('Absorption, Storage and Labels','How they get in, where they are kept, and the forms on labels.',P7),
 ('Putting It All Together','The whole lesson in one table, plus a few extras.',P8)]
FS_QUIZ=[('Why do vitamins A, D, E and K dissolve in fat rather than water?','They are made mostly of carbon and hydrogen (built from isoprene units), with few OH groups (Figure 2).'),
 ('What is isoprene?','A five-carbon building block, C5H8, that plants and animals join to make molecules like retinol and carotenoids (Figure 2).'),
 ('What is the difference between retinol and retinal?','Retinol ends in CH2OH; retinal ends in CH=O (two hydrogens fewer) (Figure 3).'),
 ('Why is beta-carotene called provitamin A?','The body can cut it in the middle and turn each half into retinal (Figure 3).'),
 ('Why is preformed vitamin A a concern in pregnancy?','Large amounts, mainly from supplements or lots of liver, can cause birth defects (Figure 3).'),
 ('What does UVB light do to 7-dehydrocholesterol in the skin?','It breaks open the second ring, forming vitamin D3 (Figure 4).'),
 ('Where is vitamin D activated?','An OH is added in the liver, then a second in the kidney, making calcitriol (Figure 4).'),
 ('Name two deficiency diseases of vitamin D.','Rickets in children, osteomalacia in adults (Figure 4).'),
 ('What part of vitamin E does the antioxidant work?','The OH on its ring head, which gives up a hydrogen to stop a chain reaction (Figure 5).'),
 ('How do alpha- and gamma-tocopherol differ?','Gamma lacks one methyl group on the ring; only alpha counts toward vitamin E needs (Figure 5).'),
 ('Why do newborns get a vitamin K injection?','Little vitamin K crosses the placenta and breast milk is low in it, so babies risk bleeding (Figure 6).'),
 ('Which vitamin must be listed on every US Nutrition Facts label?','Vitamin D (Figure 7).')]
build_lesson('micronutrients-fat-soluble-vitamins','Fat-Soluble Vitamins','Module 2 begins with the micronutrients: substances you need in milligrams or micrograms rather than grams. This lesson covers the four fat-soluble vitamins, A, D, E and K. All four are lipids built from five-carbon isoprene units, which is why they are absorbed with fat and stored in the body. Each is shown as a ball-and-stick model, with what it does, what happens with too little or too much, and where to find it in whole foods. The figure is on the left and the lesson script on the right; the quiz is at the end.',FS_LESSON,FS_QUIZ,mols=V_)
