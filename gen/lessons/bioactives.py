# ---------------- Module 3 · Non-Nutrients · Bioactives ----------------
MB=mk_lmol('bioactives')
A=None
_X=[64,193,321,450,579,707,836]
_L=[('Flavonoids','Fig. 2','#fig-2','Berries, tea','onions, soy'),('Other phenols','Fig. 3','#fig-3','Coffee, grapes','olive oil'),
    ('Carotenoids','Fig. 4','#fig-4','Carrots','tomatoes, greens'),('Phytosterols','Fig. 5','#fig-5','Nuts, seeds','plant oils'),
    ('Sulforaphane','Fig. 6 · allicin','#fig-6','Broccoli','garlic, onions'),('Capsaicin','Fig. 7 · piperine','#fig-7','Chili','pepper, ginger'),('Caffeine','Fig. 8','#fig-8','Coffee, tea','cocoa')]
BI_NODES=[(450,30,320,'Bioactives','plant compounds that are not essential nutrients','nd root','#fig-2'),
 (128,150,251,'Polyphenols','rings with OH groups · Figs. 2–3','nd l','#fig-2'),(385,150,251,'Terpenoids','built from isoprene · Figs. 4–5','nd l','#fig-4'),
 (579,150,122,'Sulfur','compounds · Fig. 6','nd l','#fig-6'),(771,150,251,'Spice and stimulants','Figs. 7–8','nd l','#fig-7')]
BI_NODES+=[(x,270,122,t,s,'nd u',h) for x,(t,s,h,_,_) in zip(_X,_L)]+[(x,390,122,t,s,'nd t',h) for x,(_,_,h,t,s) in zip(_X,_L)]
_P=dict(zip(_X,[128,128,385,385,579,771,771]))
BI_EDGES=[(450,52,x,128) for x in (128,385,579,771)]+[(_P[x],182,x,248) for x in _X]+[(x,302,x,368) for x in _X]
P1=('<!--noart-->'+ftree(BI_NODES,BI_EDGES,420,'Tree diagram: bioactives, plant compounds that are not essential nutrients, in four groups. Polyphenols: flavonoids (berries, tea, onions, soy) and other phenols (coffee, grapes, olive oil). Terpenoids, built from isoprene: carotenoids (carrots, tomatoes, greens) and phytosterols (nuts, seeds, plant oils). Sulfur compounds: sulforaphane and allicin (broccoli, garlic, onions). Spice and stimulants: capsaicin and piperine (chili, pepper, ginger) and caffeine (coffee, tea, cocoa).')
 +lblock('label','What the tree shows',[('Not nutrients, but active','Bioactives are compounds in food that are not essential nutrients, so there is no deficiency disease and usually no recommended intake, but they still act on the body. Most come from plants, which make them as pigments, defenses or signals.'),
   ('Four chemical families','Polyphenols are built on rings with OH groups. Terpenoids are built from five-carbon isoprene units. The sulfur compounds give the cabbage and onion families their bite. And the spice and stimulant compounds act on nerve receptors.'),
   ('Whole foods first','Diets rich in fruit, vegetables, tea, coffee, whole grains and legumes are consistently linked to better health. Isolated bioactives in pills have mostly not matched those results, and a few have backfired.')]))
P2=('<!--noart-->'+molbox('phenol','What “phenol” means',[MB('phenol','Phenol: a benzene ring with one OH group; every hydrogen shown',[('oh','1',A,A)],'Phenol, C6H6O',eager=True)],
   [('1','A phenol is an OH group on a benzene ring. A polyphenol has several of them. That OH easily gives up its hydrogen to quench a reactive molecule, which is why polyphenols are antioxidants in a test tube.','')],head='Starting point')
 +molbox('quer','Quercetin, a flavonol',[MB('quercetin','Quercetin: two benzene rings joined through a ring containing oxygen, with five OH groups and a C=O; every hydrogen shown',[('a','2',A,A),('b','3',A,A),('cat','4',A,A)],'Quercetin, C15H10O7')],
   [('2','Every flavonoid has the same fifteen-carbon skeleton: a ring here…',''),('3','…a ring here, and a middle ring with an oxygen joining them.',''),('4','Two neighboring OH groups on this ring make it a strong antioxidant and metal binder.','')],
   fx=facts(what='Flavonoids are the largest group of polyphenols, with thousands of kinds; quercetin is the most common flavonol in food.',
     body='Little is absorbed intact; most is changed by the liver and gut bacteria, and the products may calm inflammation and help blood vessels relax. Diets high in flavonoid-rich foods are linked to lower risk of heart disease and stroke, though effects of single flavonoids are unproven.',
     high='There is no deficiency. Food amounts are safe; high-dose supplements can interact with some medicines.',
     found='Onions (especially red), kale, apples with the skin, capers, berries, broccoli, tea, red wine. Cocoa, tea and apples are rich in the related flavanols (catechins; see Antinutrients).'),head='Flavonoids')
 +molbox('cyan','Cyanidin, an anthocyanin color',[MB('cyanidin','Cyanidin: the flavonoid skeleton with a positively charged oxygen in the middle ring and five OH groups; every hydrogen shown',[('oplus','5',A,A),('c3','6',A,A)],'Cyanidin, C15H11O6+')],
   [('5','In anthocyanins the middle ring’s oxygen carries a positive charge, making the whole ring system a pigment.',''),('6','In food a sugar is attached here; the sugar-bound form is an anthocyanin.','')],
   fx=facts(what='Anthocyanins are the red, purple and blue pigments of berries, red cabbage and grapes. Their color changes with acidity: red in acid, purple near neutral, blue-green in alkali, which is why red cabbage turns blue when cooked with baking soda.',
     body='Studies link berry-rich diets to better blood vessel function and blood pressure; anthocyanins are thought to be part of the reason.',
     found='Blueberries, blackberries, black currants, cherries, red grapes, red cabbage, purple sweet potatoes, eggplant skin, black beans. The EU allows them as a natural coloring (E163).'))
 +molbox('gen','Genistein, an isoflavone',[MB('genistein','Genistein: the flavonoid skeleton with the second ring moved to the middle carbon, and three OH groups; every hydrogen shown',[('b','7',A,A),('oh','8',A,A)],'Genistein, C15H10O5')],
   [('7','In isoflavones the second ring is attached one carbon over…',''),('8','…which puts its OH about as far from the other end as in estrogen, so genistein weakly fits estrogen receptors.','')],
   fx=facts(what='Isoflavones are the main phytoestrogens: plant compounds that act like a weak estrogen.',
     body='In Asian populations that eat soy often, soy intake is linked to lower rates of some cancers and heart disease, and soy foods may modestly ease hot flashes. Normal intake of soy foods is considered safe, including for breast cancer survivors, by major cancer organizations.',
     high='High-dose isoflavone supplements are less studied than soy foods; anyone with a hormone-sensitive condition should ask a clinician.',
     found='Soybeans, edamame, tofu, tempeh, miso and soy milk; small amounts in chickpeas and other legumes.'))
 +legend('c h o'))
P3=('<!--noart-->'+molbox('res','Resveratrol, a stilbene',[MB('resveratrol','Resveratrol: two benzene rings joined by a two-carbon double bond, with three OH groups; every hydrogen shown',[('db','1',A,A)],'Resveratrol, C14H12O3',eager=True)],
   [('1','Two phenol rings joined by a double bond. Grapes make it in their skins to fight fungal infection.','')],
   fx=facts(what='A polyphenol made by grapes, peanuts and some berries in response to stress or infection.',
     body='It extended lifespan in yeast and some animals and drew attention as a reason for the “French paradox”, but human trials have been disappointing, and the amount in a glass of red wine is tiny, far below the doses used in research.',
     high='No deficiency. High-dose supplements can cause digestive upset and may interact with blood thinners.',
     found='Red grape skins and red wine, peanuts, pistachios, blueberries, cranberries, cocoa.'),head='Resveratrol')
 +molbox('cga','Chlorogenic acid',[MB('chlorogenic','Chlorogenic acid: a ring of carbons with OH groups (quinic acid) joined through an ester to caffeic acid, a phenol ring with two OH groups; every hydrogen shown',[('quinic','2',A,A),('ester','3',A,A),('caffeic','4',A,A)],'Chlorogenic acid, C16H18O9')],
   [('2','A ring of carbons with OH groups (quinic acid)…',''),('3','…joined through an ester link…',''),('4','…to caffeic acid, the phenol part, with two OH groups side by side.','')],
   fx=facts(what='A phenolic acid; the main polyphenol in coffee, where it adds bitterness and acidity.',
     body='Coffee is the largest source of polyphenols for many adults, and moderate coffee drinking is linked to lower risk of type 2 diabetes and liver disease; chlorogenic acid may contribute by slowing sugar absorption. Roasting breaks much of it down, so light roasts keep more.',
     found='Coffee (green beans have the most), apples, pears, blueberries, eggplant, potatoes, artichokes, sunflower seeds.'),head='Chlorogenic acid')
 +molbox('htyr','Hydroxytyrosol',[MB('hydroxytyrosol','Hydroxytyrosol: a benzene ring with two neighboring OH groups and a two-carbon chain ending in OH; every hydrogen shown',[('cat','5',A,A)],'Hydroxytyrosol, C8H10O3')],
   [('5','Two neighboring OH groups on one ring, the same strong antioxidant grip as quercetin and caffeic acid.','')],
   fx=facts(what='The main polyphenol of olives and extra-virgin olive oil, along with its relatives tyrosol and oleuropein; part of the bitter, peppery bite of fresh oil.',
     body='The EU allows the claim that olive oil polyphenols help protect blood lipids from oxidation, for oils providing at least 5 mg of hydroxytyrosol and its relatives per 20 g of oil. It is one reason extra-virgin oil is thought to do more than refined olive oil.',
     found='Extra-virgin olive oil (refining removes most of it), table olives, olive leaves.'),head='Hydroxytyrosol')
 +legend('c h o'))
P4=('<!--noart-->'+molbox('iso','The building block',[MB('isoprene','Isoprene: a five-carbon unit with two double bonds and a methyl branch; every hydrogen shown',[('me','1',A,A)],'Isoprene, C5H8',eager=True)],
   [('1','Terpenoids are built from isoprene, a five-carbon unit with one branch. Eight of them make a carotenoid; six make squalene, which cells fold into the sterols in Figure 5.','')],head='Starting point')
 +molbox('bc','β-Carotene, C₄₀H₅₆',[MB('betacarotene','Beta-carotene: a long zigzag chain of alternating double bonds with a six-carbon ring at each end; every hydrogen shown',[('ring1','2',A,A),('chain','3',A,A),('center','4',A,A)],'Beta-carotene, C40H56')],
   [('2','A ring at each end…',''),('3','…joined by a long chain of alternating double and single bonds. That chain absorbs blue light, so it looks orange.',''),('4','Cut in the middle, it makes two molecules of vitamin A (see Fat-Soluble Vitamins).','')],
   fx=facts(what='The best-known carotenoid and the main provitamin A in plants.',
     body='Your gut turns some of it into vitamin A, as needed, so it does not cause vitamin A poisoning. It is also an antioxidant in the fat of cell membranes. It is absorbed far better from cooked food eaten with some fat.',
     high='Eating a lot can turn the skin yellow-orange (carotenemia), which is harmless and fades. High-dose beta-carotene supplements raised lung cancer risk in smokers in two large trials, so smokers should avoid them.',
     found='Carrots, sweet potatoes, pumpkin and winter squash, spinach, kale, cantaloupe, mangoes, apricots, red palm oil.'),head='Carotenoids')
 +molbox('lyc','Lycopene, C₄₀H₅₆',[MB('lycopene','Lycopene: the same forty carbons as beta-carotene but with no rings, an open chain of alternating double bonds; every hydrogen shown',[('end1','5',A,A),('chain','6',A,A)],'Lycopene, C40H56')],
   [('5','Lycopene has the same formula as beta-carotene, but its ends stay open instead of closing into rings…',''),('6','…and its chain of alternating double bonds lies flat from end to end, which shifts its color to red.','')],
   fx=facts(what='The red pigment of tomatoes and watermelon. It is not turned into vitamin A.',
     body='One of the strongest carotenoid antioxidants. Diets high in tomato products are linked to lower prostate cancer risk in some studies, though the evidence is mixed. Cooking and a little fat make it several times more available, so tomato sauce supplies more than raw tomatoes.',
     found='Tomatoes and tomato products (paste, sauce, ketchup), watermelon, pink grapefruit, guava, papaya.'))
 +lblock('eyes','Two more carotenoids',[('Lutein and zeaxanthin','These yellow carotenoids collect in the macula of the eye, where they filter blue light. In a large US trial (AREDS2), they helped slow advanced age-related macular degeneration in people who already had it. Kale, spinach, corn and egg yolk are good sources.')])
 +legend('c h',note='every molecule on this page is drawn at the same scale with every hydrogen shown · tap one to enlarge it'))
P5=('<!--noart-->'+molbox('ster','Cholesterol and its plant twin',[
   '<div class="mgrid">'+mcell(MB('cholesterol','Cholesterol: four fused rings with an OH at one end and a branched carbon tail at the other; every hydrogen shown',[('tail','1',A,A)],'Cholesterol, C27H46O',eager=True),'Cholesterol','C₂₇H₄₆O · animals')
   +mcell(MB('sitosterol','Beta-sitosterol: the same four rings and OH, with an extra two-carbon ethyl group on the tail; every hydrogen shown',[('ethyl','2',A,A)],'Beta-sitosterol, C29H50O'),'β-Sitosterol','C₂₉H₅₀O · plants')+'</div>'],
   [('1','Cholesterol, the animal sterol: four fused rings, an OH, and a carbon tail (see Lipids).',''),('2','β-Sitosterol, the main plant sterol, is the same molecule with two extra carbons on the tail.','')],
   fx=facts(what='Phytosterols are the plant versions of cholesterol; plant stanols are the same with no double bond in the ring.',
     body='They look enough like cholesterol to crowd it out of the bile mixtures that carry it into gut cells, so less cholesterol is absorbed, both from food and from the cholesterol your liver sends into the gut. About 2 g a day lowers LDL cholesterol by roughly 8–10% within a few weeks; the US FDA and EU allow heart-health claims on foods with added sterols or stanols.',
     high='Very little is absorbed. People with the rare inherited disorder sitosterolemia absorb them and should avoid them. Large amounts can slightly lower beta-carotene absorption.',
     found='Vegetable oils (corn, canola, sesame), nuts, seeds, wheat germ, legumes. A normal diet supplies about 0.2–0.5 g a day; reaching 2 g needs fortified spreads, yogurts or drinks.'),head='Phytosterols')
 +legend('c h o'))
P6=('<!--noart-->'+molbox('gluc','From glucosinolate to sulforaphane',[
   '<div class="mgrid">'+mcell(MB('glucoraphanin','Glucoraphanin: a sulfur chain attached to a glucose ring and a sulfate group; every hydrogen shown',[('glc','1',A,A),('so','2',A,A)],'Glucoraphanin, C12H23NO10S3',eager=True),'Glucoraphanin','C₁₂H₂₃NO₁₀S₃')
   +mcell(MB('sulforaphane','Sulforaphane: a four-carbon chain with a sulfoxide group at one end and an N=C=S isothiocyanate group at the other; every hydrogen shown',[('ncs','3',A,A)],'Sulforaphane, C6H11NOS2'),'Sulforaphane','C₆H₁₁NOS₂')+'</div>'],
   [('1','Broccoli stores glucoraphanin, a glucosinolate: a sulfur chain parked on a glucose…',''),('2','…with this sulfur-oxygen end that sulforaphane keeps.',''),('3','When the plant is cut or chewed, the enzyme myrosinase cuts off the glucose and the molecule rearranges into an N=C=S group: an isothiocyanate.','')],
   fx=facts(what='Glucosinolates are the sulfur defense compounds of the cabbage family; sulforaphane is the isothiocyanate made from broccoli’s main one. The sharp taste of mustard, horseradish, wasabi and radish comes from related isothiocyanates.',
     body='Sulforaphane switches on Nrf2, a cell signal that raises the body’s own detoxifying and antioxidant enzymes. Diets high in brassicas are linked to lower risk of some cancers; human trials of sulforaphane itself are small and early.',
     high='Normal amounts are safe; very large raw amounts can act as goitrogens when iodine is low (see Antinutrients).',
     found='Broccoli sprouts (by far the most), broccoli, Brussels sprouts, cabbage, kale, cauliflower, arugula, watercress.'),head='Sulforaphane')
 +flow('myro','Getting the most sulforaphane',[('Chop or chew','cutting brings glucosinolate and myrosinase together'),('Wait or eat raw','raw or lightly steamed broccoli keeps the enzyme working'),('Boil hard','destroys myrosinase; gut bacteria then convert only a little'),('Rescue','a pinch of mustard powder on cooked broccoli adds fresh myrosinase')])
 +molbox('all','Allicin, from garlic',[MB('allicin','Allicin: two three-carbon allyl groups joined through two sulfurs, one of which carries an oxygen; every hydrogen shown',[('ss','4',A,A)],'Allicin, C6H10OS2')],
   [('4','Two sulfurs side by side, one with an oxygen. Allicin is made in seconds when garlic is crushed, as the enzyme alliinase meets its precursor alliin.','')],
   fx=facts(what='The pungent compound of freshly crushed garlic. It is unstable and soon breaks down into other sulfur compounds that carry garlic’s smell.',
     body='Garlic’s sulfur compounds kill microbes in the lab and may slightly lower blood pressure and cholesterol; the evidence for garlic supplements is modest and mixed. Letting crushed garlic stand a few minutes before heating is often advised, since heat stops alliinase.',
     high='Large amounts can upset the stomach, cause garlic breath and body odor, and add to the effect of blood thinners.',
     found='Garlic; onions, leeks, shallots and chives make related compounds, including the one that makes you cry when you cut onions.'))
 +legend('c h o n s'))
P7=('<!--noart-->'+molbox('cap','Capsaicin',[MB('capsaicin','Capsaicin: a benzene ring with OH and methoxy groups joined through an amide to a long branched carbon tail; every hydrogen shown',[('van','1',A,A),('amide','2',A,A),('tail','3',A,A)],'Capsaicin, C18H27NO3',eager=True)],
   [('1','A vanilla-like head: a ring with OH and methoxy groups, like the vanillin in Flavorings…',''),('2','…an amide link…',''),('3','…and a fatty tail, which is why capsaicin dissolves in fat and milk, not water.','')],
   fx=facts(what='The compound that makes chili peppers hot; the Scoville scale measures it. Plants make it to deter mammals, while birds, which spread the seeds, cannot taste it.',
     body='Capsaicin switches on TRPV1, the nerve receptor that senses dangerous heat, so the mouth feels burning without any real burn. With repeated exposure the nerves become less sensitive, which is why capsaicin creams are used for pain. It slightly raises energy use, too little to matter for weight.',
     high='Very hot peppers can cause pain, vomiting and, rarely, chest pain. Milk and other fatty foods relieve the burn better than water.',
     found='Chili peppers, from mild jalapeños to habaneros and hotter; concentrated in the white ribs, not the seeds themselves. Bell peppers have essentially none.'),head='Capsaicin')
 +molbox('pip','Piperine and gingerol',[
   '<div class="mgrid">'+mcell(MB('piperine','Piperine: a ring of five carbons and a nitrogen joined through an amide to a chain of two double bonds ending in a benzene ring with a methylenedioxy group; every hydrogen shown',[('pip','4',A,A)],'Piperine, C17H19NO3'),'Piperine','C₁₇H₁₉NO₃ · black pepper')
   +mcell(MB('gingerol','6-Gingerol: the same vanilla-like ring as capsaicin with a carbon chain carrying a ketone and an OH; every hydrogen shown',[('keto','5',A,A)],'6-Gingerol, C17H26O4'),'6-Gingerol','C₁₇H₂₆O₄ · ginger')+'</div>'],
   [('4','Piperine also has an amide and also triggers heat receptors, more mildly. It slows the breakdown of some compounds, which is why it is paired with turmeric to raise curcumin absorption.',''),('5','Gingerol has capsaicin’s head but a ketone and OH in its chain. Drying or cooking ginger turns it into shogaol, which is even more pungent.','')],
   fx=facts(what='The pungent compounds of black pepper (piperine) and fresh ginger (gingerol).',
     body='Ginger is one of the better-studied food remedies: it modestly relieves nausea, including morning sickness, in several trials. Piperine’s effect on absorption can also raise blood levels of some medicines.',
     found='Black and white pepper; fresh, dried and candied ginger, ginger tea.'))
 +legend('c h o n'))
P8=('<!--noart-->'+molbox('caf','Caffeine and theobromine',[
   '<div class="mgrid">'+mcell(MB('caffeine','Caffeine: two fused rings containing four nitrogens, two C=O groups and three methyl groups; every hydrogen shown',[('m1','1',A,A)],'Caffeine, C8H10N4O2',eager=True),'Caffeine','C₈H₁₀N₄O₂')
   +mcell(MB('theobromine','Theobromine: the same two rings with two methyl groups and an N-H where caffeine has its third methyl; every hydrogen shown',[('nh','2',A,A)],'Theobromine, C7H8N4O2'),'Theobromine','C₇H₈N₄O₂')+'</div>'],
   [('1','Caffeine is a purine, related to the A and G of DNA, with three methyl groups.',''),('2','Theobromine, from cocoa, has an N-H here instead of the third methyl. The liver turns some caffeine into theobromine.','')],
   fx=facts(what='Alkaloids: bitter, nitrogen-containing plant compounds, here made to deter insects. Caffeine is the most widely used stimulant in the world.',
     body='Caffeine blocks adenosine, the brain signal that builds up sleepiness, so you feel more alert; it takes effect in 15–45 minutes and its half-life is about 5 hours in adults. Theobromine is a much milder stimulant. Moderate coffee and tea drinking are linked to lower risk of several diseases.',
     high='The US FDA says up to 400 mg a day is generally not linked to harmful effects in healthy adults; pregnancy guidance is 200 mg a day or less. Too much causes jitters, fast heartbeat, anxiety and poor sleep; concentrated powders can be deadly. Theobromine is toxic to dogs, which clear it slowly, so keep chocolate away from them.',
     found='Coffee, tea, yerba mate, cola and energy drinks, cocoa and chocolate (mostly theobromine, some caffeine), guarana.'),head='Alkaloids')
 +table('amt',['Drink or food','Typical caffeine'],[
   ['Brewed coffee, 8 oz (240 mL)','80–100 mg'],['Espresso, 1 shot','about 60–75 mg'],['Black tea, 8 oz','about 40–50 mg'],['Green tea, 8 oz','about 30–50 mg'],
   ['Cola, 12 oz (355 mL)','about 30–40 mg'],['Energy drink, 8 oz','about 70–100 mg'],['Dark chocolate, 1 oz (28 g)','about 12–25 mg']],'How much caffeine')
 +legend('c h n o'))
P9=('<!--noart-->'+table('table',['Bioactive','Family','What it may do','Main sources','Good to know'],[
  ['Flavonoids (quercetin, anthocyanins)','polyphenols','support blood vessels; linked to lower heart risk','onions, berries, apples, tea, cocoa','color tells you: red, purple, blue'],
  ['Isoflavones (genistein)','polyphenols','weak estrogen effects','soy foods','soy foods are considered safe'],
  ['Resveratrol, chlorogenic acid, hydroxytyrosol','polyphenols','antioxidant; linked with coffee and olive oil benefits','grapes, coffee, extra-virgin olive oil','wine has too little resveratrol to matter'],
  ['Carotenoids (β-carotene, lycopene, lutein)','terpenoids','provitamin A, antioxidants, eye pigments','orange, red and dark green produce','cook with a little fat; smokers avoid β-carotene pills'],
  ['Phytosterols','terpenoids','block cholesterol absorption','oils, nuts, fortified spreads','about 2 g a day lowers LDL 8–10%'],
  ['Sulforaphane, allicin','sulfur compounds','switch on the body’s own defenses','broccoli, cabbage, garlic, onions','chop, wait, do not overboil'],
  ['Capsaicin, piperine, gingerol','pungent compounds','trigger heat receptors; ginger eases nausea','chili, pepper, ginger','fat, not water, cools chili heat'],
  ['Caffeine, theobromine','alkaloids','block adenosine; alertness','coffee, tea, cocoa','up to 400 mg caffeine a day for most adults']],'The bioactives at a glance')
 +worth([('Antioxidant claims','Test-tube antioxidant scores do not predict effects in the body, and the USDA withdrew its antioxidant (ORAC) database in 2012 for that reason. Many polyphenols probably work by signaling rather than by mopping up free radicals directly.'),
   ('Grapefruit and medicines','Grapefruit contains furanocoumarins, bioactives that block an enzyme in the gut that breaks down many drugs, raising their blood levels. Many statins, blood pressure drugs and others carry a grapefruit warning.'),
   ('Same compound, two sides','Tannins, phytate and glucosinolates appear in Antinutrients too: whether a compound helps or hinders depends on the dose, the rest of the diet and how the food is prepared.')],
   note='General education, not medical advice. Facts follow mainstream sources (NIH Office of Dietary Supplements and National Center for Complementary and Integrative Health, US FDA, EFSA, Linus Pauling Institute, standard food-science texts).'))
BI_LESSON=[('The Bioactives Family Tree','Plant compounds that are not essential nutrients, in four families.',P1),
 ('Flavonoids','What a phenol is, and three flavonoids: quercetin, anthocyanins and isoflavones.',P2),
 ('Other Polyphenols','Resveratrol, chlorogenic acid in coffee, and hydroxytyrosol in olive oil.',P3),
 ('Carotenoids','Isoprene chains that color food orange and red.',P4),
 ('Phytosterols','The plant twin of cholesterol, which blocks its absorption.',P5),
 ('Sulforaphane and Allicin','The sulfur compounds of broccoli and garlic, made when you cut them.',P6),
 ('Capsaicin and Other Pungent Compounds','Chili, black pepper and ginger, and why they feel hot.',P7),
 ('Caffeine and Theobromine','The stimulants of coffee, tea and chocolate.',P8),
 ('Putting It All Together','The whole lesson in one table, plus a few extras.',P9)]
BI_QUIZ=[('What makes a compound a bioactive rather than a nutrient?','It acts on the body but is not essential, so there is no deficiency disease (Figure 1).'),
 ('What is a phenol, and what makes a polyphenol?','An OH group on a benzene ring; a polyphenol has several (Figure 2).'),
 ('Why does red cabbage turn blue when cooked with baking soda?','Its anthocyanins change color with acidity: red in acid, blue-green in alkali (Figure 2).'),
 ('Which food is the main source of isoflavones, and how do they act?','Soy; they act like a weak estrogen (Figure 2).'),
 ('Which polyphenol is the main one in coffee?','Chlorogenic acid (Figure 3).'),
 ('What five-carbon unit are carotenoids and sterols built from?','Isoprene (Figure 4).'),
 ('How do beta-carotene and lycopene differ?','Beta-carotene has a ring at each end and is provitamin A; lycopene is an open chain, red, and not made into vitamin A (Figure 4).'),
 ('How do phytosterols lower LDL cholesterol?','They crowd cholesterol out of the bile mixtures that carry it into gut cells, so less is absorbed (Figure 5).'),
 ('What enzyme makes sulforaphane, and when does it act?','Myrosinase, when broccoli is cut or chewed; hard boiling destroys it (Figure 6).'),
 ('Which receptor does capsaicin switch on, and what cools the burn best?','TRPV1, the heat receptor; milk or other fatty foods (Figure 7).'),
 ('How does caffeine make you feel alert?','It blocks adenosine, the brain signal for sleepiness (Figure 8).'),
 ('What daily caffeine amount does the FDA say is generally safe for healthy adults?','Up to 400 mg, about four cups of brewed coffee (Figure 8).')]
build_lesson('bioactives','Bioactives','Bioactives are compounds in food that are not essential nutrients but still act on the body: polyphenols such as flavonoids, carotenoids, phytosterols, the sulfur compounds of broccoli and garlic, the pungent compounds of chili, pepper and ginger, and the stimulants caffeine and theobromine. Each is shown in ball-and-stick form with what it does, the cautions, and where it is found. The figure is on the left and the lesson script on the right; the quiz is at the end.',BI_LESSON,BI_QUIZ,mols=MB,scale=18.5)
