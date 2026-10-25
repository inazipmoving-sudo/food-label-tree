# ---------------- Module 2 · Trace Minerals ----------------
M4=mk_lmol('micronutrients-trace-minerals')
A=None
_L2=[(50,'Iron','Fe · Figs. 2–3','#fig-2','Anemia','Fig. 3','#fig-3'),(145,'Copper','Cu · Fig. 4','#fig-4','Anemia (rare)','Fig. 4','#fig-4'),
     (250,'Zinc','Zn · Fig. 4','#fig-4','Slow healing','Fig. 4','#fig-4'),(345,'Selenium','Se · Fig. 5','#fig-5','Rare in US','Fig. 5','#fig-5'),
     (450,'Iodine','I · Fig. 6','#fig-6','Goiter','Fig. 6','#fig-6'),(560,'Fluoride','F · Fig. 7','#fig-7','Tooth decay','Fig. 7','#fig-7'),
     (655,'Manganese','Mn · Fig. 7','#fig-7','Rare','Fig. 7','#fig-7'),(750,'Chromium','Cr · Fig. 7','#fig-7','Rare','Fig. 7','#fig-7'),(845,'Molybdenum','Mo · Fig. 7','#fig-7','Unknown','Fig. 7','#fig-7')]
TM_NODES=[(450,30,300,'Trace Minerals','needed in amounts under 20 mg a day','nd root',None),
 (97,150,180,'Blood and oxygen','Figs. 2–4','nd l','#fig-2'),(297,150,180,'Enzymes and defense','Figs. 4–5','nd l','#fig-4'),(450,150,110,'Thyroid','Fig. 6','nd l','#fig-6'),(702,150,330,'Teeth, bones and enzymes','Fig. 7','nd l','#fig-7')]
TM_NODES+=[(x,270,88,t,s,'nd u',h) for x,t,s,h,_,_,_ in _L2]+[(x,390,88,t,s,'nd t',h) for x,_,_,_,t,s,h in _L2]
_P={50:97,145:97,250:297,345:297,450:450,560:702,655:702,750:702,845:702}
TM_EDGES=[(450,52,x,128) for x in (97,297,450,702)]+[(_P[x],182,x,248) for x in _P]+[(x,302,x,368) for x in _P]
P1=('<!--noart-->'+ftree(TM_NODES,TM_EDGES,420,'Tree diagram: the trace minerals. Blood and oxygen: iron (too little: anemia) and copper. Enzymes and defense: zinc and selenium. Thyroid: iodine (too little: goiter). Teeth, bones and enzymes: fluoride, manganese, chromium and molybdenum.')
 +lblock('label','Small amounts, big jobs',[('Under 20 mg a day','Trace minerals are needed in milligrams or micrograms, but each is essential: most sit at the active center of enzymes or other proteins.'),
   ('A narrow window','The gap between enough and too much is small for several of them, notably iron, selenium and fluoride, so food is safer than high-dose supplements.'),
   ('Soil and food choice matter','The selenium and iodine in plant foods depend on the soil where they grew; iron and zinc absorption depends on what else is in the meal (Figure 8).')]))
P2=('<!--noart-->'+molbox('fe','Two forms of iron ion',[
   '<div class="mgrid">'+mcell(M4('fe2','Ferrous iron ion, Fe2+: an orange ball',[],'Ferrous iron, Fe2+',eager=True),'Ferrous iron','Fe²⁺')
   +mcell(M4('fe3','Ferric iron ion, Fe3+: a slightly smaller orange ball',[],'Ferric iron, Fe3+'),'Ferric iron','Fe³⁺')
   +mcell(M4('na','Sodium ion, Na+, for comparison',[],'Sodium ion, Na+'),'Sodium, for scale','Na⁺')+'</div>'],
   fx='<p class="mfact">Iron switches easily between Fe²⁺ and Fe³⁺ by gaining or losing one electron. That is what makes it useful for carrying oxygen and electrons, and also why loose iron can be harmful: it can spark damaging reactions, so the body keeps it bound to proteins.</p>',head='Iron')
 +molbox('heme','Heme, C₃₄H₃₂FeN₄O₄',[M4('heme','Heme: an iron atom at the center of a large flat ring made of four five-membered rings, each with a nitrogen bonded to the iron, with methyl, vinyl and two propionic acid side groups; every hydrogen shown',[('fe','1',A,A),('ring','2',A,A),('acid','3',A,A)],'Heme, C34H32FeN4O4')],
   [('1','An iron atom held at the center…',''),('2','…by four nitrogens of a porphyrin ring, four linked five-membered rings, the same plan as the corrin ring of vitamin B12 and the ring around magnesium in chlorophyll.',''),('3','Two acid side chains. In hemoglobin, oxygen binds to the iron from above.','')],
   fx='<p class="mfact"><b>Heme iron</b> comes only from animal foods (meat, poultry, fish), inside hemoglobin and myoglobin; it is absorbed well. <b>Nonheme iron</b>, mostly Fe³⁺, is the form in plants, eggs, dairy and fortified foods; it is absorbed less well and depends on the rest of the meal.</p>')
 +legend('fe c h o n',note='every molecule and ion on this page is drawn at the same scale with every hydrogen shown · tap one to enlarge it'))
P3=('<!--noart-->'+flow('path','How your body handles iron',[('Absorbed in the upper small intestine','heme iron is taken up whole; nonheme Fe³⁺ must first be changed to Fe²⁺, which vitamin C helps with'),
   ('Carried by transferrin','a blood protein that holds iron safely'),('Used','about 70% of body iron is in hemoglobin, carrying oxygen in red blood cells, and myoglobin in muscle; a little is in enzymes'),
   ('Stored as ferritin','in the liver, spleen and bone marrow'),('Recycled, not excreted','old red cells are broken down and their iron reused; the body has no active way to get rid of extra iron, so it controls how much it absorbs')])
 +molbox('fefacts','Iron',[],fx=facts(body='RDA 8 mg for men and for women over 50; 18 mg for women 19–50, because of menstrual losses; 27 mg in pregnancy. Vegetarians may need about 1.8 times as much, because nonheme iron is less well absorbed.',
   low='The most common nutrient deficiency in the world. Stores run down first, then iron-deficiency anemia: tiredness, pale skin, shortness of breath, poor concentration.',
   high='Upper limit 45 mg a day for adults; supplements above it often upset the stomach. Accidental overdose of iron supplements is dangerous for young children, so keep them out of reach. Some people inherit a tendency to absorb too much (hemochromatosis).',
   found='Heme: beef, lamb, oysters, clams, sardines, dark-meat poultry. Nonheme: lentils, beans, tofu, spinach, pumpkin seeds, dried apricots.')))
P4=('<!--noart-->'+molbox('zn','Zinc ion, Zn²⁺',[M4('zn','Zinc ion, Zn2+: a blue-gray ball',[],'Zinc ion, Zn2+',eager=True)],
   fx='<p class="mfact">Zinc gives up two electrons and, unlike iron and copper, never changes charge. It is used to hold proteins in shape (“zinc fingers” that grip DNA) and as the working part of many enzymes.</p>'
   +facts(body='Needed by about 100 enzymes; for immune function, wound healing, growth, DNA and protein making, and taste and smell. RDA 11 mg (men), 8 mg (women).',
     low='Slow growth in children, loss of appetite, poor wound healing, more infections, hair loss, loss of taste.',
     high='Upper limit 40 mg a day. Long-term high-dose supplements cause copper deficiency.',
     found='Oysters (by far the richest), beef, crab, lobster, pork, chicken, pumpkin seeds, beans, chickpeas, cashews, yogurt. Phytate in whole grains and beans lowers absorption (Figure 8).'),head='Zinc')
 +molbox('cu','Copper ion, Cu²⁺',[M4('cu','Copper ion, Cu2+: a copper-brown ball',[],'Copper ion, Cu2+')],
   fx='<p class="mfact">Like iron, copper switches between two charges (Cu⁺ and Cu²⁺), so it works in enzymes that move electrons.</p>'
   +facts(body='Helps make energy, connective tissue and the pigment melanin; needed to move iron out of storage, so a shortage can cause anemia. RDA 900 µg.',
     low='Rare: anemia, low white cells, nerve problems; often linked to high-dose zinc supplements or stomach surgery.',high='Upper limit 10 mg a day; very high doses damage the liver.',
     found='Oysters, liver, crab, cashews, sunflower seeds, lentils, mushrooms, dark chocolate, whole grains.'),head='Copper')
 +legend('zn cu',note='ions drawn to the same scale as Figure 2 · tap one to enlarge it'))
P5=('<!--noart-->'+molbox('se','Selenium in amino acids',[
   '<div class="mgrid">'+mcell(M4('cysteine','Cysteine: an amino acid whose side chain ends in SH; every hydrogen shown',[('x','1',A,A)],'Cysteine, C3H7NO2S',eager=True),'Cysteine','with sulfur')
   +mcell(M4('selenocysteine','Selenocysteine: the same amino acid with selenium in place of sulfur; every hydrogen shown',[('x','2',A,A)],'Selenocysteine, C3H7NO2Se'),'Selenocysteine','with selenium')+'</div>'
   +'<p class="mt">Selenomethionine, the main form in plant foods</p>'+M4('selenomethionine','Selenomethionine: methionine with selenium in place of sulfur; every hydrogen shown',[('x','3',A,A)],'Selenomethionine, C5H11NO2Se')],
   [('1','Cysteine has sulfur (yellow)…',''),('2','…selenocysteine has selenium (orange), the element just below sulfur in the periodic table. It is called the 21st amino acid and is built into about 25 human selenoproteins.',''),('3','Plants take up selenium from soil and build it into selenomethionine in place of methionine.','')],
   fx=facts(body='Selenoproteins include antioxidant enzymes (glutathione peroxidases) and enzymes that activate thyroid hormone. RDA 55 µg.',
     low='Rare in the US, where soils and a varied food supply provide enough; in low-selenium regions it has caused a heart disease (Keshan disease).',
     high='Upper limit 400 µg a day. Too much (selenosis) causes garlic-smelling breath, brittle hair and nails, and skin rashes. One Brazil nut can contain more than a day’s needs, so eat them only occasionally.',
     found='Brazil nuts, tuna, sardines, shrimp, eggs, chicken, turkey, beef, whole grains; plant content depends on the soil.'),head='Selenium')
 +legend('c h o n s se'))
P6=('<!--noart-->'+molbox('iodide','Iodide, I⁻',[M4('iodide','Iodide ion, I-: a large purple ball',[],'Iodide ion, I-',eager=True)],
   fx='<p class="mfact">Iodine is taken in as iodide, a large negative ion. The thyroid gland traps it from the blood and builds it into thyroid hormones.</p>',head='Iodine')
 +molbox('thyroid','The thyroid hormones',[
   '<p class="mt">Thyroxine (T4), C₁₅H₁₁I₄NO₄</p>'+M4('thyroxine','Thyroxine: two benzene rings joined by an oxygen, with two iodines on each ring, an OH on the outer ring and an amino-acid end; every hydrogen shown',[('i1','1',A,A),('i2','2',A,A),('aa','3',A,A)],'Thyroxine, C15H11I4NO4')
   +'<p class="mt">Triiodothyronine (T3), C₁₅H₁₂I₃NO₄</p>'+M4('t3','Triiodothyronine: the same as thyroxine with one iodine on the outer ring replaced by hydrogen; every hydrogen shown',[('i2','4',A,A)],'Triiodothyronine, C15H12I3NO4')],
   [('1','Two iodines (purple) on the inner ring…',''),('2','…and two on the outer ring: four in all, so thyroxine is called T4.',''),('3','It is built from the amino acid tyrosine.',''),('4','In body tissues one outer iodine is removed (by a selenium enzyme), giving T3, the active hormone.','')],
   fx=facts(body='Thyroid hormones set the body’s metabolic rate and are essential for brain and bone development before birth and in infancy. RDA 150 µg; 220 µg in pregnancy.',
     low='Goiter (an enlarged thyroid) and hypothyroidism. In pregnancy, deficiency can impair the baby’s brain development; worldwide it is a leading preventable cause of intellectual disability.',
     high='Upper limit 1,100 µg a day. Too much can also disturb the thyroid, causing goiter or an over- or underactive thyroid.',
     found='Seaweed (amounts vary widely), cod, shrimp, tuna, milk, yogurt, cheese, eggs, and iodized salt. Sea salt, kosher salt and most salt in processed foods are not usually iodized.'))
 +legend('i c h o n'))
P7=('<!--noart-->'+molbox('four','Four more trace minerals',[
   '<div class="mgrid">'+mcell(M4('fluoride','Fluoride ion, F-: a pale green ball',[],'Fluoride ion, F-',eager=True),'Fluoride','F⁻')
   +mcell(M4('mn','Manganese ion, Mn2+: a lilac ball',[],'Manganese ion, Mn2+'),'Manganese','Mn²⁺')
   +mcell(M4('cr','Chromium ion, Cr3+: a small gray-blue ball',[],'Chromium ion, Cr3+'),'Chromium','Cr³⁺')
   +mcell(M4('molybdate','Molybdate: a molybdenum atom with four oxygens',[('c','1',A,A)],'Molybdate, MoO4 2-'),'Molybdate','MoO₄²⁻')+'</div>'],
   [('1','Molybdenum (teal) arrives mostly as molybdate; the body builds it into a cofactor for four enzymes.','')],head='Fluoride, manganese, chromium, molybdenum')
 +table('table4',['Mineral','In your body','Intake (adults)','Too little / too much','Whole-food sources'],[
   ['Fluoride','replaces OH in tooth enamel to form fluorapatite, which resists acid','AI 4 mg (men), 3 mg (women); upper limit 10 mg','more tooth decay / white flecks on teeth (fluorosis) if too much while teeth form','fluoridated water, tea, seafood'],
   ['Manganese','enzymes for bone, carbohydrate and amino-acid use, and an antioxidant enzyme (MnSOD)','AI 2.3 mg (men), 1.8 mg (women); upper limit 11 mg','rare / nerve damage, mostly from breathing it in at work or from well water','whole grains, nuts, beans, tea, leafy greens, pineapple'],
   ['Chromium','may help insulin work; supplements show little clear benefit','AI 35 µg (men), 25 µg (women)','rare / no harm known from food','broccoli, potatoes, whole grains, beef, green beans'],
   ['Molybdenum','cofactor for four enzymes, including sulfite oxidase','RDA 45 µg; upper limit 2,000 µg','essentially unknown / rare','beans, lentils, peas, whole grains, nuts']],'At a glance')
 +legend('f mn cr mo o'))
P8=('<!--noart-->'+table('help',['In the same meal','Effect'],[
   ['Vitamin C (peppers, citrus, tomatoes, broccoli)','increases nonheme iron absorption'],['Meat, poultry or fish','increases nonheme iron absorption from the rest of the meal'],
   ['Phytate (whole grains, beans, nuts, seeds)','lowers iron and zinc absorption (Antinutrients)'],['Polyphenols (tea, coffee)','lower nonheme iron absorption; drink them between meals if iron is low'],
   ['Calcium (dairy, supplements)','lowers iron absorption a little'],['High-dose zinc supplements','lower copper absorption']],'Helpers and blockers')
 +lblock('soak','Making minerals easier to absorb',[('Soaking, sprouting, fermenting','Soaking beans, sprouting grains and leavening bread with yeast or sourdough break down phytate and free more iron and zinc.'),
   ('Cast-iron pans','Cooking acidic foods such as tomato sauce in cast iron adds some iron to the food.')])
 +table('dv',['On the label','Daily Value'],[['Iron (required)','18 mg'],['Zinc','11 mg'],['Copper','0.9 mg'],['Selenium','55 µg'],['Iodine','150 µg'],['Manganese','2.3 mg'],['Chromium','35 µg'],['Molybdenum','45 µg']],'Daily Values')
 +lblock('labelnote','On the label',[('Iron is required','Iron must appear on every Nutrition Facts label; the other trace minerals appear only if added or a claim is made. Fluoride has no Daily Value.')]))
P9=('<!--noart-->'+table('table',['Mineral','Main job','Too little','Whole-food sources'],[
  ['Iron','carries oxygen (hemoglobin)','anemia, fatigue','red meat, shellfish, lentils, beans, spinach'],['Copper','iron use, energy, connective tissue','anemia (rare)','oysters, liver, nuts, seeds, cocoa'],
  ['Zinc','enzymes, immunity, healing','slow growth and healing, infections','oysters, beef, crab, pumpkin seeds, beans'],['Selenium','antioxidant enzymes, thyroid','rare in US','Brazil nuts, fish, eggs, poultry'],
  ['Iodine','thyroid hormones','goiter; brain development in pregnancy','seaweed, fish, dairy, eggs, iodized salt'],['Fluoride','strong tooth enamel','tooth decay','fluoridated water, tea'],
  ['Manganese','enzymes, bone','rare','whole grains, nuts, tea'],['Chromium','may help insulin','rare','broccoli, whole grains'],['Molybdenum','four enzymes','unknown','beans, lentils, grains']],'The nine trace minerals')
 +worth([('The same ring, three times','Heme, the corrin ring of vitamin B12 and chlorophyll all hold a metal (iron, cobalt, magnesium) at the center of a ring of four nitrogen-containing rings.'),
   ('Blood donors and iron','Each blood donation removes about 200–250 mg of iron, which is why donors are screened for anemia.'),
   ('Iodized salt','Adding iodine to salt, started in the US in 1924, all but eliminated goiter in the country.')]))
TM_LESSON=[('The Trace Mineral Family Tree','Nine minerals needed in amounts under 20 mg a day.',P1),
 ('Iron and Heme','Two charges, and iron held in a ring.',P2),
 ('Iron in Your Body','Absorption, use, storage and recycling.',P3),
 ('Zinc and Copper','Enzyme metals that compete with each other.',P4),
 ('Selenium','The 21st amino acid.',P5),
 ('Iodine and the Thyroid','Iodide, T4 and T3.',P6),
 ('Fluoride, Manganese, Chromium, Molybdenum','Four more, in brief.',P7),
 ('Absorption and Labels','What helps and blocks absorption, and Daily Values.',P8),
 ('Putting It All Together','The whole lesson in one table, plus a few extras.',P9)]
TM_QUIZ=[('What makes a mineral a trace mineral?','You need it in amounts under about 20 mg a day (Figure 1).'),
 ('What are the two charges iron switches between?','Fe²⁺ (ferrous) and Fe³⁺ (ferric) (Figure 2).'),
 ('What holds the iron in heme?','Four nitrogens of a porphyrin ring (Figure 2).'),
 ('Which foods supply heme iron?','Animal foods: meat, poultry and fish (Figure 2).'),
 ('How does the body get rid of extra iron?','It has no active way; it controls how much it absorbs and recycles iron from old red cells (Figure 3).'),
 ('Why do women 19–50 need more iron than men?','To replace menstrual losses (Figure 3).'),
 ('What can long-term high-dose zinc supplements cause?','Copper deficiency (Figure 4).'),
 ('Which food is by far the richest in zinc?','Oysters (Figure 4).'),
 ('What is selenocysteine?','Cysteine with selenium in place of sulfur, the 21st amino acid (Figure 5).'),
 ('Why eat Brazil nuts only occasionally?','One nut can exceed a day’s selenium needs; too much causes selenosis (Figure 5).'),
 ('How many iodine atoms are in thyroxine (T4)? In T3?','Four; three (Figure 6).'),
 ('Name one thing that helps and one that hinders nonheme iron absorption.','Helps: vitamin C or meat in the meal. Hinders: phytate, tea or coffee polyphenols, calcium (Figure 8).')]
build_lesson('micronutrients-trace-minerals','Trace Minerals','The last micronutrient lesson covers the nine trace minerals, needed in amounts under 20 mg a day: iron, copper, zinc, selenium, iodine, fluoride, manganese, chromium and molybdenum. Each is shown as an ion or in a molecule that carries it, such as heme, selenocysteine and thyroxine, in ball-and-stick form, with what it does, what happens with too little or too much, and where to find it in whole foods. The figure is on the left and the lesson script on the right; the quiz is at the end.',TM_LESSON,TM_QUIZ,mols=M4,scale=13)
