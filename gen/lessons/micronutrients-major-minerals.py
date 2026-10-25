# ---------------- Module 2 · Major Minerals ----------------
M3=mk_lmol('micronutrients-major-minerals')
A=None
def _cap(t): return f'<small style="font-size:.9rem">{t}</small>'
MM_NODES=[(450,30,280,'Major Minerals','over 100 mg a day, carried as ions · Fig. 2','nd root','#fig-2'),
 (190,150,250,'Electrolytes','charged ions in body fluids · Figs. 3–4','nd l','#fig-3'),(570,150,250,'Bone minerals','also in every cell · Figs. 5–6','nd l','#fig-5'),(830,150,130,'Sulfur','Fig. 7','nd l','#fig-7'),
 (70,270,112,'Sodium','Na⁺ · Fig. 3','nd u','#fig-3'),(190,270,112,'Chloride','Cl⁻ · Fig. 3','nd u','#fig-3'),(310,270,112,'Potassium','K⁺ · Fig. 4','nd u','#fig-4'),
 (450,270,112,'Calcium','Ca²⁺ · Fig. 5','nd u','#fig-5'),(570,270,112,'Phosphorus','phosphate · Fig. 6','nd u','#fig-6'),(690,270,112,'Magnesium','Mg²⁺ · Fig. 6','nd u','#fig-6'),
 (830,270,130,'In protein','amino acids · Fig. 7','nd u','#fig-7')]
MM_EDGES=[(450,52,190,128),(450,52,570,128),(450,52,830,128)]+[(190,182,x,248) for x in (70,190,310)]+[(570,182,x,248) for x in (450,570,690)]+[(830,182,830,248)]
P1=('<!--noart-->'+ftree(MM_NODES,MM_EDGES,300,'Tree diagram: the major minerals. Electrolytes: sodium, chloride and potassium (Figures 3 and 4). Bone minerals: calcium, phosphorus and magnesium (Figures 5 and 6). Sulfur, found in protein (Figure 7). All are carried as ions (Figure 2).')
 +lblock('label','What makes a mineral “major”',[('Amount, not importance','Major minerals are those you need in amounts over about 100 mg a day; trace minerals, such as iron and zinc, are needed in smaller amounts but are just as essential.'),
   ('Elements, not molecules','A mineral is a single element. It can’t be made or destroyed by the body, or by cooking, though some can be lost into cooking water.'),
   ('Carried as ions','In food and in your body, minerals are almost always charged atoms (ions) or parts of simple compounds, not neutral atoms (Figure 2).')]))
P2=('<!--noart-->'+molbox('ions','Atoms become ions',[
   '<div class="mgrid">'+mcell(M3('na','A sodium ion, Na+: a single purple ball',[],'Sodium ion, Na+',eager=True),'Sodium ion','Na → Na⁺: gives away one electron')
   +mcell(M3('cl','A chloride ion, Cl-: a single larger green ball',[],'Chloride ion, Cl-'),'Chloride ion','Cl → Cl⁻: takes one electron')+'</div>'],
   fx='<p class="mfact">An atom that loses an electron has one more proton than electrons: a positive ion. One that gains an electron becomes a negative ion. Opposite charges attract, and that attraction, an <b>ionic bond</b>, holds salt together. Chloride is drawn bigger than sodium because it is: the extra electron and fewer protons per electron let it spread out.</p>',head='Giving and taking electrons')
 +molbox('salt','Table salt: a sodium chloride crystal, NaCl',[M3('nacl','Part of a sodium chloride crystal: small purple sodium ions and large green chloride ions alternating in a square grid',[('a','1',A,A),('b','2',A,A)],'Sodium chloride crystal, NaCl')],
   [('1','Every sodium ion is surrounded by chloride ions…',''),('2','…and every chloride by sodium ions. The sticks show neighbors, not shared electrons. The real crystal continues in three dimensions.','')])
 +molbox('sizes','The ions of the major minerals, at the same scale',[
   '<div class="mgrid">'+mcell(M3('mg','Magnesium ion, Mg2+: a small light-green ball',[],'Magnesium ion, Mg2+'),'Magnesium','Mg²⁺')
   +mcell(M3('ca','Calcium ion, Ca2+: a medium dark-green ball',[],'Calcium ion, Ca2+'),'Calcium','Ca²⁺')
   +mcell(M3('k','Potassium ion, K+: a larger purple ball',[],'Potassium ion, K+'),'Potassium','K⁺')+'</div>'],
   fx='<p class="mfact">Magnesium and calcium give away two electrons each (2+); sodium and potassium one (1+). Potassium is bigger than sodium, and that difference in size is how cells tell them apart (Figure 4).</p>')
 +table('charges',['Mineral','Main form in the body','Charge'],[['Sodium','sodium ion, Na⁺','+1'],['Potassium','potassium ion, K⁺','+1'],['Calcium','calcium ion, Ca²⁺','+2'],['Magnesium','magnesium ion, Mg²⁺','+2'],['Chloride','chloride ion, Cl⁻','−1'],['Phosphorus','phosphate, PO₄³⁻ and HPO₄²⁻','−3, −2'],['Sulfur','in amino acids; sulfate, SO₄²⁻','−2 as sulfate']],'The seven major minerals')
 +legend('na cl kk ca mg',note='ions drawn to the same scale (relative ionic size) · tap one to enlarge it'))
P3=('<!--noart-->'+molbox('dissolve','Salt in water: ions surrounded by water',[
   '<div class="pair"><div class="pc">'+M3('na_aq','A sodium ion surrounded by six water molecules, each with its red oxygen facing the ion and its hydrogens pointing away; every hydrogen shown',[('c','1',A,A),('w','2',A,A)],'Sodium ion with six water molecules')+'</div><div class="pc">'
   +M3('cl_aq','A chloride ion surrounded by six water molecules, each with one white hydrogen pointing at the ion; every hydrogen shown',[('c','3',A,A)],'Chloride ion with six water molecules')+'</div></div>'],
   [('1','A sodium ion (+)…',''),('2','…attracts the slightly negative oxygen ends of water (Water and Ethanol, Figure 2).',''),('3','A chloride ion (−) attracts the slightly positive hydrogen ends instead. Surrounded this way, the ions drift apart: salt dissolves.','')],
   fx='<p class="mfact">This is how sodium and chloride travel in blood and the fluid around your cells. Where sodium goes, water follows, so sodium sets how much fluid is outside your cells.</p>',head='Sodium and chloride')
 +molbox('na','Sodium',[],fx=facts(body='The main positive ion in the fluid outside cells: keeps fluid volume and blood pressure steady, and carries nerve signals with potassium. Adequate intake 1,500 mg a day.',
    low='Rare from diet. Low blood sodium usually comes from illness, some medicines, or drinking very large amounts of water during endurance exercise.',
    high='Raises blood pressure in many people, which increases the risk of heart disease and stroke. US guidance is to reduce intake if above 2,300 mg a day; most Americans eat about 3,400 mg.',
    found='Small amounts in most foods: celery, beets, milk, eggs, shellfish. Most dietary sodium comes from salt added in processing, restaurants and cooking.'))
 +molbox('cl','Chloride, and stomach acid',[M3('hcl','Hydrogen chloride, HCl: a small white hydrogen bonded to a large green chlorine',[('cl','1',A,A)],'Hydrogen chloride, HCl')],
   [('1','Your stomach makes hydrochloric acid, HCl, from chloride in the blood. In water it splits into H⁺, which makes the stomach acidic, and Cl⁻.','')],
   fx=facts(body='The main negative ion outside cells, paired with sodium; needed for stomach acid. Adequate intake 2,300 mg a day.',low='Rare; can follow prolonged vomiting.',high='Comes with salt; the concern is the sodium.',found='Salt, seaweed, tomatoes, celery, olives.'))
 +legend('na cl h o'))
P4=('<!--noart-->'+molbox('kcl','Potassium chloride, KCl',[M3('kcl','Part of a potassium chloride crystal: purple potassium ions and green chloride ions alternating in a square grid',[('a','1',A,A)],'Potassium chloride crystal, KCl',eager=True)],
   [('1','The same grid as table salt, with larger potassium ions in place of sodium. Potassium chloride is the main ingredient of “salt substitutes”; it tastes salty with a bitter edge.','')],head='Potassium')
 +flow('pump','Sodium outside, potassium inside',[('Inside cells','about 98% of your potassium is inside cells'),('Outside cells','most sodium stays in the fluid around them'),('The sodium-potassium pump','a protein in every cell membrane pushes 3 Na⁺ out and brings 2 K⁺ in, using energy from ATP'),('Why it matters','the difference in charge across the membrane lets nerves fire, muscles contract and the heart beat steadily')])
 +molbox('k','Potassium',[],fx=facts(body='The main positive ion inside cells; helps control heartbeat, muscle and nerve signals, and blunts the effect of sodium on blood pressure. Adequate intake 3,400 mg (men), 2,600 mg (women).',
    low='Low intake is common and linked with higher blood pressure. Very low blood potassium, usually from vomiting, diarrhea or some diuretics, causes weakness and irregular heartbeat.',
    high='Healthy kidneys remove extra potassium from food. In kidney disease, or with some blood-pressure medicines, it can build up and disturb the heart rhythm, so salt substitutes and supplements need a doctor’s advice.',
    found='Beans, lentils, potatoes, sweet potatoes, squash, spinach, bananas, dried apricots, avocado, yogurt.'))
 +legend('kk cl'))
P5=('<!--noart-->'+molbox('ca','Calcium carbonate, CaCO₃',[
   '<div class="mgrid">'+mcell(M3('ca','Calcium ion, Ca2+',[],'Calcium ion, Ca2+',eager=True),'Calcium ion','Ca²⁺')
   +mcell(M3('caco3','Calcium carbonate: a calcium ion beside a carbonate ion, a carbon with three oxygens',[('x','1',A,A),('c','2',A,A)],'Calcium carbonate, CaCO3'),'Calcium carbonate','CaCO₃')+'</div>'],
   [('1','A calcium ion (2+)…',''),('2','…paired with carbonate, CO₃²⁻ (2−). Calcium carbonate is chalk, limestone, eggshell and seashell, and the most common calcium supplement. In the stomach, acid frees the calcium ion.','')],head='Calcium')
 +lblock('where','Where your calcium is',[('Bones and teeth: about 99%','Calcium and phosphate form hard crystals (hydroxyapatite) on a collagen frame.'),
   ('Blood and cells: about 1%','Used for muscle contraction, nerve signals, blood clotting and hormone release.'),
   ('Bone is a bank','Blood calcium is held in a narrow range. When intake is low, hormones (with active vitamin D) take calcium from bone, so low intake shows up years later as weak bones.')])
 +molbox('cafacts','Calcium',[],fx=facts(body='RDA 1,000 mg for adults 19–50 and men 51–70; 1,200 mg for women over 50 and men over 70. Vitamin D is needed to absorb it (Fat-Soluble Vitamins, Figure 4).',
    low='Over time, low bone mass and osteoporosis, with a higher risk of fractures.',
    high='Above the upper limit (2,500 mg a day up to age 50; 2,000 mg after), usually from supplements: constipation and kidney stones.',
    found='Yogurt, milk, cheese, sardines and canned salmon with the bones, tofu made with calcium sulfate, kale, bok choy, collard greens, almonds. Spinach is high in calcium but its oxalate binds most of it (Antinutrients).'))
 +legend('ca c o'))
P6=('<!--noart-->'+molbox('phos','Phosphate',[
   '<div class="mgrid">'+mcell(M3('phosphate','Phosphate ion: a phosphorus atom with four oxygens around it, one double-bonded',[('c','1',A,A)],'Phosphate ion, PO4 3-',eager=True),'Phosphate','PO₄³⁻')
   +mcell(M3('hpo4','Hydrogen phosphate ion: the same with a hydrogen on one oxygen',[('x','2',A,A)],'Hydrogen phosphate ion, HPO4 2-'),'Hydrogen phosphate','HPO₄²⁻')+'</div>'],
   [('1','Phosphorus (orange) with four oxygens. In the body, phosphorus is almost always found as phosphate.',''),('2','At the pH of blood, much of it carries one hydrogen.','')],
   fx=facts(body='About 85% is in bone, with calcium. Phosphate is also part of DNA, of the phospholipids in every cell membrane (Lipids) and of ATP, the cell’s energy carrier. RDA 700 mg.',
     low='Rare from diet; occurs in some illnesses and with long-term heavy antacid use: weakness, bone pain.',
     high='In kidney disease phosphate builds up and harms bones and blood vessels. Upper limit 4,000 mg (3,000 mg over 70).',
     found='Protein foods: dairy, meat, poultry, fish, eggs, beans, lentils, nuts. Whole grains and seeds contain it as phytate, which is less well absorbed (Antinutrients).'),head='Phosphorus')
 +molbox('mgaq','Magnesium ion in water, Mg(H₂O)₆²⁺',[M3('mg_aq','A small magnesium ion surrounded closely by six water molecules, oxygens facing in; every hydrogen shown',[('c','1',A,A),('w','2',A,A)],'Magnesium ion with six water molecules')],
   [('1','Magnesium is small and doubly charged…',''),('2','…so it holds its water molecules tightly, much more than sodium does (Figure 3).','')],
   fx=facts(body='About half is in bone. Needed by over 300 enzymes; ATP works mostly as a magnesium–ATP pair. Also for muscle and nerve function and heart rhythm. Magnesium sits at the center of chlorophyll, which is why green vegetables supply it. RDA 400–420 mg (men), 310–320 mg (women).',
     low='Many people eat less than the RDA; a true deficiency is uncommon but causes muscle cramps, weakness and irregular heartbeat.',
     high='No harm from food. Supplements above 350 mg a day can cause diarrhea; larger amounts are dangerous with kidney disease.',
     found='Pumpkin seeds, chia seeds, almonds, cashews, spinach, black beans, edamame, whole grains, dark chocolate.'),head='Magnesium')
 +legend('mg p o h'))
P7=('<!--noart-->'+molbox('samino','The sulfur amino acids',[
   '<div class="mgrid">'+mcell(M3('methionine','Methionine: an amino acid whose side chain contains a sulfur between two carbons; every hydrogen shown',[('s','1',A,A)],'Methionine, C5H11NO2S',eager=True),'Methionine','essential')
   +mcell(M3('cysteine','Cysteine: an amino acid whose side chain ends in a sulfur with a hydrogen (SH); every hydrogen shown',[('sh','2',A,A)],'Cysteine, C3H7NO2S'),'Cysteine','made from methionine')+'</div>'],
   [('1','<b>Methionine</b>: sulfur (yellow) in the middle of its side chain. It’s essential: you must eat it.',''),('2','<b>Cysteine</b>: an SH group at the end. Two cysteines in a protein can join S–S, a disulfide bridge that holds proteins such as keratin in shape (Protein, Figure 5).','')],head='Sulfur')
 +molbox('sulfate','Sulfate, SO₄²⁻',[M3('sulfate','Sulfate ion: a sulfur atom with four oxygens, two double-bonded',[('c','3',A,A)],'Sulfate ion, SO4 2-')],
   [('3','Your body turns extra sulfur from amino acids into sulfate, used to build cartilage and to help the liver clear some drugs, and passes the rest in urine.','')],
   fx=facts(what='The third most plentiful mineral in the body by weight, after calcium and phosphorus.',body='Part of methionine and cysteine, of glutathione (a major antioxidant inside cells), and of thiamin and biotin (Water-Soluble Vitamins).',
     low='There is no separate requirement: enough protein supplies enough sulfur.',found='Eggs, meat, fish, dairy, beans, nuts; garlic, onions and cabbage-family vegetables also contain sulfur compounds that give them their smell (Bioactives).'))
 +legend('c h o n s'))
P8=('<!--noart-->'+table('dv',['On the label','Daily Value','Notes'],[['Sodium','2,300 mg','required on every label'],['Potassium','4,700 mg','required since the 2016 update'],['Calcium','1,300 mg','required since the 2016 update'],['Phosphorus','1,250 mg','only if added or claimed'],['Magnesium','420 mg','only if added or claimed'],['Chloride','2,300 mg','only if added or claimed']],'Major minerals on the Nutrition Facts label')
 +lblock('salt','Salt and sodium',[('Salt is about 40% sodium','Sodium chloride is 39% sodium by weight. A teaspoon of salt (about 6 g) has about 2,300 mg of sodium, a whole day’s Daily Value.'),
   ('Sea salt, kosher salt, pink salt','All are mostly sodium chloride, with the same sodium per gram. Coarse crystals pack less tightly, so a teaspoon can hold less.'),
   ('Where it comes from','Most sodium in US diets comes from packaged and restaurant foods rather than the salt shaker; cooking from whole foods makes intake easier to control.')])
 +lblock('pct','Reading the % Daily Value',[('5% or less is low','A food with 5% DV or less of sodium is low in sodium; 20% or more is high.'),
   ('Potassium and calcium','The same 5% / 20% guide works the other way round for nutrients you want more of.')]))
P9=('<!--noart-->'+table('table',['Mineral','Main jobs','Too little / too much','Whole-food sources'],[
  ['Sodium (Na⁺)','fluid volume, nerve signals','rarely short / raises blood pressure','small amounts in many foods; mostly from added salt'],
  ['Chloride (Cl⁻)','fluid balance, stomach acid','rare / comes with sodium','salt, seaweed, tomatoes, celery'],
  ['Potassium (K⁺)','heartbeat, nerves, muscles, blood pressure','low intake common / risk only with kidney disease','beans, potatoes, squash, leafy greens, bananas'],
  ['Calcium (Ca²⁺)','bones, teeth, muscles, clotting','weak bones / kidney stones from supplements','dairy, sardines, tofu, kale, bok choy'],
  ['Phosphorus (phosphate)','bones, DNA, membranes, ATP','rare / harmful in kidney disease','dairy, meat, fish, beans, nuts'],
  ['Magnesium (Mg²⁺)','300+ enzymes, ATP, muscles','cramps, irregular heartbeat / diarrhea from supplements','seeds, nuts, greens, beans, whole grains'],
  ['Sulfur','sulfur amino acids, glutathione','covered by protein / —','eggs, meat, fish, beans, onions, garlic']],'The seven major minerals')
 +worth([('Minerals can’t be cooked away','Heat doesn’t destroy minerals, but boiling leaches potassium and some magnesium into the water; soups keep it.'),
   ('Hard water','Hard tap water carries dissolved calcium and magnesium, and can supply a useful share of them.'),
   ('Bones keep changing','Bone is living tissue, remodeled throughout life; weight-bearing exercise, calcium, vitamin D and protein all help keep it strong.')]))
MM_LESSON=[('The Major Mineral Family Tree','Seven minerals needed in amounts over 100 mg a day.',P1),
 ('From Atoms to Ions','How minerals get their charge, and the salt crystal.',P2),
 ('Sodium and Chloride','Salt in water, fluid balance and stomach acid.',P3),
 ('Potassium','The ion inside your cells.',P4),
 ('Calcium','Bones, teeth and a steady blood level.',P5),
 ('Phosphorus and Magnesium','Phosphate in bone and ATP; magnesium for enzymes.',P6),
 ('Sulfur','In protein: methionine, cysteine and sulfate.',P7),
 ('Salt and the Label','Daily Values, and salt versus sodium.',P8),
 ('Putting It All Together','The whole lesson in one table, plus a few extras.',P9)]
MM_QUIZ=[('What makes a mineral “major” rather than “trace”?','You need it in amounts over about 100 mg a day; it is not about importance (Figure 1).'),
 ('Why is a sodium ion positive?','It has given away one electron, so it has one more proton than electrons (Figure 2).'),
 ('Which is larger, a sodium ion or a chloride ion?','Chloride (Figure 2).'),
 ('Which end of a water molecule faces a sodium ion?','The slightly negative oxygen end (Figure 3).'),
 ('What acid does your stomach make from chloride?','Hydrochloric acid, HCl (Figure 3).'),
 ('Where is most of your potassium, inside or outside cells?','Inside, about 98% (Figure 4).'),
 ('What does the sodium-potassium pump do?','Pushes 3 sodium ions out and brings 2 potassium ions in, using ATP (Figure 4).'),
 ('What share of your calcium is in bones and teeth?','About 99% (Figure 5).'),
 ('Name three things phosphate is part of besides bone.','DNA, phospholipids in membranes, ATP (Figure 6).'),
 ('Why are green vegetables a good source of magnesium?','Magnesium is at the center of chlorophyll (Figure 6).'),
 ('Which two amino acids contain sulfur?','Methionine and cysteine (Figure 7).'),
 ('About how much sodium is in a teaspoon of salt?','About 2,300 mg, a full day’s Daily Value (Figure 8).')]
build_lesson('micronutrients-major-minerals','Major Minerals','The third micronutrient lesson covers the seven major minerals: sodium, chloride, potassium, calcium, phosphorus, magnesium and sulfur, which you need in amounts over 100 mg a day. It starts with how atoms become ions, then shows each mineral as an ion or simple compound in ball-and-stick form, with what it does in your body, what happens with too little or too much, and where to find it in whole foods. The figure is on the left and the lesson script on the right; the quiz is at the end.',MM_LESSON,MM_QUIZ,mols=M3,scale=13)
