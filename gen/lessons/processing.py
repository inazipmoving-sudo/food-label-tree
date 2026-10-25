# ---------------- Module 3 · Non-Nutrients · Processing ----------------
MP=mk_lmol('processing')
A=None
_L=[(50,'Solvents','Fig. 2','#fig-2','Hexane','oil extraction','#fig-2'),
    (150,'Browning','Fig. 3','#fig-3','Acrylamide','and AGEs','#fig-3'),(250,'Grill, smoke','Fig. 4','#fig-4','HCAs, PAHs','charred meat','#fig-4'),(350,'Cure','Fig. 5','#fig-5','NDMA','nitrosamines','#fig-5'),
    (450,'Ferment','Fig. 6','#fig-6','Yogurt','bread, vinegar','#fig-6'),(550,'Pasteurize','Fig. 6','#fig-6','Milk, juice','kills germs','#fig-6'),
    (650,'Hydrogenate','Fig. 7','#fig-7','Trans fat','if partial','#fig-7'),(750,'Refine','Fig. 7','#fig-7','White flour','bran removed','#fig-7'),(850,'Nixtamalize','Fig. 8','#fig-8','Tortillas','frees niacin','#fig-8')]
PR_NODES=[(450,30,300,'Processing','what happens to food between farm and plate','nd root','#fig-2'),
 (50,150,98,'Unlisted','processing aids','nd l','#fig-2'),(250,150,298,'Made by heat','Figs. 3–5','nd l','#fig-3'),(650,150,498,'Change the food itself','Figs. 6–8','nd l','#fig-6')]
PR_NODES+=[(x,270,98,t,s,'nd u',h) for x,t,s,h,_,_,_ in _L]+[(x,390,98,t,s,'nd t',h) for x,_,_,_,t,s,h in _L]
_P={50:50,150:250,250:250,350:250,450:650,550:650,650:650,750:650,850:650}
PR_EDGES=[(450,52,x,128) for x in (50,250,650)]+[(_P[x],182,x,248) for x in _P]+[(x,302,x,368) for x in _P]
P1=('<!--noart-->'+ftree(PR_NODES,PR_EDGES,420,'Tree diagram: food processing in three groups. Unlisted processing aids: solvents such as hexane, used to extract oil. Made by heat: browning makes acrylamide and AGEs; grilling and smoking make HCAs and PAHs on charred meat; curing makes nitrosamines such as NDMA. Change the food itself: fermenting (yogurt, bread, vinegar), pasteurizing (milk, juice; kills germs), hydrogenating (trans fat if partial), refining (white flour; bran removed) and nixtamalizing (tortillas; frees niacin).')
 +lblock('label','What the tree shows',[('Three kinds of change','Almost every food is processed somehow: washed, cut, heated, fermented, pressed or milled. This lesson follows three kinds of change: helpers used along the way that never reach the label, new compounds that form when food is heated hard, and methods that change the food itself.'),
   ('Good, bad and both','Processing is not good or bad as a whole. Pasteurizing and fermenting make food safer; nixtamalizing makes corn more nutritious; charring and partial hydrogenation make compounds worth limiting; refining trades nutrients for shelf life and texture.'),
   ('Mostly not on the label','Processing aids and the compounds that form during cooking are not listed as ingredients. A few methods show up in the wording, such as “partially hydrogenated”, “enriched”, “pasteurized”, “cured” or “nixtamalized corn”.')]))
P2=('<!--noart-->'+molbox('hex','Hexane, C₆H₁₄',[MP('hexane','Hexane: a straight chain of six carbons with fourteen hydrogens; every hydrogen shown',[('c','1',A,A)],'Hexane, C6H14',eager=True)],
   [('1','Six carbons in a row and nothing but hydrogens around them: no oxygen, so it mixes with oil, not water.','')],
   fx=facts(what='A petroleum solvent. Crushed soybeans, canola, corn or sunflower seeds are washed with hexane, which dissolves the oil out; the hexane is then boiled off and recycled.',
     body='Hexane is not a nutrient and has no role in the body. Breathing high levels for long periods at work can damage nerves, which is why it is a workplace hazard; the traces left in refined oil are very small.',
     high='The EU caps hexane residue in edible fats and oils at 1 mg per kg. If you would rather avoid it, oils labeled expeller-pressed, cold-pressed or USDA organic are pressed without hexane.',
     found='Used to make most soybean, canola, corn, cottonseed and sunflower oil, and soy protein ingredients. It is not listed on the label because it is a processing aid.'),head='A processing aid')
 +table('aids',['Processing aid','What it does','Ends up in the food?'],[
   ['Hexane','dissolves oil out of seeds','evaporated off; tiny traces'],
   ['Enzymes such as pectinase','clear fruit juice; break down starch in baking and brewing','inactivated by heat or filtered out'],
   ['Fining agents (gelatin, bentonite clay)','pull haze out of wine, beer and juice','settle out and are removed'],
   ['Anti-foaming agents','stop foam in fryers and tanks','trace amounts'],
   ['Carryover additives','a preservative in an ingredient (say, the dried fruit in a cereal) that does nothing in the final food','small amounts']],'Common processing aids')
 +lblock('rules','Why they are not listed',[('The labeling exemption','US rules (21 CFR 101.100) and EU rules (Regulation 1169/2011) let manufacturers leave off processing aids and carryover additives that are removed, inactive, or present only at insignificant levels with no effect in the finished food.'),
   ('Allergens are the exception','If a processing aid comes from a major allergen, such as a fining agent made from fish or milk, it must still be declared in both the US and the EU.')])
 +legend('c h'))
P3=('<!--noart-->'+molbox('acr','From asparagine to acrylamide',[
   '<div class="mgrid">'+mcell(MP('asparagine','Asparagine: an amino acid with an amide group on its side chain; every hydrogen shown',[('amide','1',A,A),('aa','2',A,A)],'Asparagine, C4H8N2O3',eager=True),'Asparagine','C₄H₈N₂O₃')
   +mcell(MP('acrylamide','Acrylamide: a carbon-carbon double bond next to an amide group; every hydrogen shown',[('vinyl','3',A,A),('amide','4',A,A)],'Acrylamide, C3H5NO'),'Acrylamide','C₃H₅NO')+'</div>'],
   [('1','Asparagine is an amino acid that potatoes and grains carry in large amounts. This end is the amide group…',''),('2','…and this is the amino-acid end. Heated above about 120°C with a sugar such as glucose, it loses this end as carbon dioxide and ammonia…',''),('3','…leaving a small molecule with a reactive double bond…',''),('4','…and the same amide group: acrylamide.','')],
   fx=facts(what='A small molecule that forms when starchy foods are fried, baked, roasted or toasted at high heat and low moisture. It is part of the Maillard reaction, the browning that gives crusts, chips and coffee their color and flavor. Swedish scientists found it in food in 2002.',
     body='The body turns acrylamide into glycidamide, which can damage DNA. It causes cancer in lab animals at high doses, and IARC classifies it as probably carcinogenic to humans (Group 2A). Studies in people have not shown a clear link at dietary levels, but regulators advise keeping intake as low as reasonably possible.',
     high='Very high exposure at work damages nerves. In the diet, the practical advice from the US FDA and others is to fry, bake and toast to a golden yellow rather than dark brown.',
     found='French fries, potato chips, crackers, cookies, toast, breakfast cereals, roasted coffee. Boiled and steamed foods have essentially none, and meat and dairy form little.'),head='Acrylamide')
 +molbox('age','AGEs: a sugar sticks to a protein',[
   '<div class="mgrid">'+mcell(MP('lysine','Lysine: an amino acid with a long side chain ending in an NH2 group; every hydrogen shown',[('n','5',A,A)],'Lysine, C6H14N2O2'),'Lysine','C₆H₁₄N₂O₂')
   +mcell(MP('cml','Carboxymethyl-lysine: lysine with a CH2-COOH group stuck onto its side-chain nitrogen; every hydrogen shown',[('add','6',A,A)],'Carboxymethyl-lysine (CML), C8H16N2O4'),'CML','C₈H₁₆N₂O₄')+'</div>'],
   [('5','Lysine’s side chain ends in a free NH₂ group, which reacts readily with sugars…',''),('6','…and after several steps it can carry this two-carbon acid group. The result, carboxymethyl-lysine (CML), is the most-measured AGE.','')],
   fx=facts(what='Advanced glycation end products (AGEs) are proteins or fats that have been permanently altered by sugars. They form in food during browning, and also slowly inside the body, faster when blood sugar is high.',
     body='AGEs build up in tissues with age and in diabetes, where they stiffen collagen and promote inflammation. How much the AGEs in food add to this is still debated; some trials of low-AGE diets show small improvements, but the evidence is not settled.',
     high='No official limit exists. Moist cooking (stewing, poaching, steaming) and acidic marinades make far fewer AGEs than dry high heat.',
     found='Highest in meat that is grilled, broiled, roasted or fried, especially fatty or processed meat; also browned cheeses, butter, and crisp baked snacks. Vegetables, fruit, grains and milk are low.'),head='AGEs')
 +legend('c h o n'))
P4=('<!--noart-->'+molbox('hca','PhIP, a heterocyclic amine (HCA)',[MP('phip','PhIP: two fused rings containing nitrogen, with an NH2 group, a methyl group and a benzene ring attached; every hydrogen shown',[('nh2','1',A,A),('ph','2',A,A)],'PhIP, C13H12N4',eager=True)],
   [('1','Rings that contain nitrogen, with an amino group: the “heterocyclic amine”. They form from creatine, amino acids and sugar in muscle meat…',''),('2','…when it is cooked very hot. PhIP is the HCA found in the largest amounts in cooked meat.','')],
   fx=facts(what='HCAs form when creatine (found in muscle), amino acids and sugars react at high temperature, mainly on the surface of meat, poultry and fish that is pan-fried or grilled well done.',
     body='Enzymes in the liver activate HCAs into forms that damage DNA. They cause cancer in animals at high doses; IARC lists PhIP as possibly carcinogenic to humans (Group 2B). Studies in people link eating a lot of well-done meat to some cancers, but cannot separate HCAs from other factors.',
     high='No set limit. The US National Cancer Institute suggests avoiding direct flame and long cooking at very high heat, turning meat often, and cutting off charred parts.',
     found='Well-done, pan-fried, grilled or barbecued beef, pork, chicken and fish, and gravy made from their drippings. Plant foods form essentially none.'),head='HCAs')
 +molbox('pah','Benzo[a]pyrene, a polycyclic aromatic hydrocarbon (PAH)',[MP('bap','Benzo[a]pyrene: five benzene rings fused into a flat sheet, with twelve hydrogens around the edge; every hydrogen shown',[('c','3',A,A)],'Benzo[a]pyrene, C20H12')],
   [('3','Five benzene rings fused into one flat sheet, with only carbon and hydrogen. Flat sheets like this can slip between the layers of DNA.','')],
   fx=facts(what='PAHs form when fat and juices drip onto flames or coals and burn; the smoke rises and coats the food. They also come from smoking food and from burning wood, coal, tobacco and fuel.',
     body='Like HCAs, PAHs are activated by liver enzymes into forms that bind DNA. Benzo[a]pyrene is classified by IARC as carcinogenic to humans (Group 1); the EU sets maximum levels for it in smoked meat, smoked fish, oils and baby foods.',
     high='Reduce it by trimming fat, avoiding flare-ups, not letting food touch flames, and scraping off charred bits.',
     found='Charcoal-grilled and barbecued meat, traditionally smoked meat and fish, and some smoke-dried foods. Smoking cigarettes is a far larger source than food.'),head='PAHs')
 +molbox('smoke','Guaiacol: the taste of smoke',[MP('guaiacol','Guaiacol: a benzene ring with an OH group and a methoxy group (O-CH3) side by side; every hydrogen shown',[('ome','4',A,A),('oh','5',A,A)],'Guaiacol, C7H8O2')],
   [('4','A methoxy group (oxygen plus methyl)…',''),('5','…next to an OH on a benzene ring. Guaiacol forms when the lignin in wood burns, and is a main source of smoky aroma.','')],
   fx=facts(what='Smoking dries food, adds flavor, and deposits compounds such as guaiacol and other phenols that slow the growth of bacteria and the spoiling of fat.',
     body='Guaiacol itself is a flavor, not a concern at food levels. The concern with smoking is the PAHs that come with the smoke.',
     found='Smoked meats, fish, cheese and paprika, whisky, coffee, and liquid smoke, which is filtered smoke condensate with most PAHs removed.'),head='Smoking')
 +legend('c h o n'))
P5=('<!--noart-->'+molbox('nit','Nitrite plus an amine makes a nitrosamine',[
   '<div class="mgrid">'+mcell(MP('nitrite','Nitrite ion: a blue nitrogen between two red oxygens, carrying a negative charge',[('n','1',A,A)],'Nitrite ion, NO2-',eager=True),'Nitrite','NO₂⁻')
   +mcell(MP('dma','Dimethylamine: a nitrogen holding two methyl groups and one hydrogen; every hydrogen shown',[('n','2',A,A)],'Dimethylamine, C2H7N'),'Dimethylamine','C₂H₇N')
   +mcell(MP('ndma','N-nitrosodimethylamine: dimethylamine whose N-H hydrogen has been replaced by an N=O group; every hydrogen shown',[('no','3',A,A)],'N-nitrosodimethylamine (NDMA), C2H6N2O'),'NDMA','C₂H₆N₂O')+'</div>'],
   [('1','Nitrite is the curing salt: it keeps cured meat pink, adds the cured flavor and stops the bacterium that causes botulism (see Additives).',''),('2','Amines like this one come from the breakdown of protein, and are plentiful in meat and fish.',''),('3','In high heat or stomach acid, nitrite puts an N=O group on the amine’s nitrogen: a nitrosamine. NDMA is the most common one.','')],
   fx=facts(what='Nitrosamines are compounds with an N–N=O group. They form when nitrite meets amines, especially with frying heat or in the acid of the stomach.',
     body='Liver enzymes activate nitrosamines into forms that damage DNA, and they cause cancer in many animal species. IARC classifies NDMA as probably carcinogenic to humans (Group 2A). Nitrosamines are thought to be one reason IARC lists processed meat as carcinogenic to humans (Group 1), mainly for colorectal cancer.',
     high='The main advice is to eat processed meat sparingly. Bacon fried crisp forms the most; cooking it more gently and avoiding burnt bits helps.',
     found='Fried cured bacon, cured and smoked meats and fish, some cheeses and beers (much lower now than in the past), and tobacco smoke.'),head='Nitrosamines')
 +lblock('block','How curing is made safer',[('Vitamin C blocks the reaction','Ascorbate and its mirror form erythorbate react with nitrite first, turning it into nitric oxide rather than letting it reach the amine. US rules for bacon limit the nitrite added and require ascorbate or erythorbate with it.'),
   ('“Uncured” still has nitrite','Meat labeled “uncured” or “no nitrites added” is usually cured with celery powder or juice, which is naturally rich in nitrate that bacteria turn into nitrite. The chemistry ends up the same.'),
   ('Vegetables are different','Most nitrate in the diet comes from vegetables such as spinach, beets and lettuce, which also bring vitamin C and polyphenols and are linked to lower, not higher, cancer risk.')])
 +legend('c h n o'))
P6=('<!--noart-->'+molbox('ferm','What microbes make',[
   '<div class="mgrid">'+mcell(MP('lactic','Lactic acid: a three-carbon acid with an OH on the middle carbon; every hydrogen shown',[('c','1',A,A)],'Lactic acid, C3H6O3',eager=True),'Lactic acid','C₃H₆O₃')
   +mcell(MP('ethanol','Ethanol: two carbons and an OH group; every hydrogen shown',[('oh','2',A,A)],'Ethanol, C2H6O'),'Ethanol','C₂H₆O')
   +mcell(MP('co2','Carbon dioxide: a carbon double-bonded to two oxygens in a straight line',[('c','3',A,A)],'Carbon dioxide, CO2'),'Carbon dioxide','CO₂')
   +mcell(MP('acetic','Acetic acid: a methyl group attached to a carboxylic acid; every hydrogen shown',[('acid','4',A,A)],'Acetic acid, C2H4O2'),'Acetic acid','C₂H₄O₂')+'</div>'],
   [('1','Lactic acid bacteria turn sugar into lactic acid, which sours and thickens milk into yogurt and preserves cabbage as sauerkraut and kimchi.',''),('2','Yeast turns sugar into ethanol…',''),('3','…and carbon dioxide. In bread the gas raises the dough and the alcohol bakes off; in beer and wine both stay.',''),('4','Acetobacter bacteria then turn ethanol into acetic acid: vinegar.','')],
   fx=facts(what='Fermentation is using microbes to change food. They eat sugars and leave behind acids, alcohol and gas, plus flavor compounds.',
     body='The acid keeps harmful bacteria from growing, which is how fermentation preserved food long before refrigerators. It can also predigest food: yogurt has less lactose than milk, and sourdough has less phytate (see Antinutrients). Foods with live cultures, like yogurt and kefir, add living bacteria; most baked, canned or pasteurized-after-fermenting foods do not.',
     high='Alcohol is the one fermentation product to limit. Very salty ferments such as soy sauce and some pickles add a lot of sodium.',
     found='Yogurt, kefir, cheese, sauerkraut, kimchi, miso, tempeh, soy sauce, sourdough and all yeast bread, vinegar, beer, wine, cocoa and coffee (both fermented during processing).'),head='Fermentation')
 +table('past',['Method','Temperature and time','Used for'],[
   ['Low-temperature, long time (vat)','63°C (145°F) for 30 minutes','small dairies'],
   ['High-temperature, short time (HTST)','72°C (161°F) for 15 seconds','most milk and juice'],
   ['Ultra-high temperature (UHT)','about 135–150°C for a few seconds','shelf-stable milk and cartons; sealed sterile']],'Pasteurization')
 +lblock('pnote','Why pasteurize',[('Kills germs, keeps nutrients','Heating just enough kills disease-causing bacteria such as Listeria, Salmonella, E. coli and Campylobacter while barely changing protein, calcium or flavor. Small losses of heat-sensitive vitamins such as vitamin C and some B vitamins are minor in milk.'),
   ('Raw milk','US health agencies warn that raw milk and raw-milk products can carry these germs and are riskier for children, pregnant women, older adults and people with weak immune systems.')])
 +legend('c h o'))
P7=('<!--noart-->'+molbox('hyd','Adding hydrogen to a double bond',[
   '<div class="mgrid">'+mcell(MP('h2','Hydrogen gas, H2: two hydrogens joined',[],'Hydrogen gas, H2',eager=True),'Hydrogen','H₂')
   +mcell(MP('cisbutene','cis-2-Butene: four carbons with a double bond in the middle and both end carbons on the same side; every hydrogen shown',[('db','1',A,A)],'cis-2-Butene, C4H8'),'cis double bond','C₄H₈')
   +mcell(MP('butane','Butane: four carbons joined by single bonds, each carbon full of hydrogens; every hydrogen shown',[('c','2',A,A)],'Butane, C4H10'),'Fully hydrogenated','C₄H₁₀')
   +mcell(MP('transbutene','trans-2-Butene: four carbons with a double bond in the middle and the end carbons on opposite sides; every hydrogen shown',[('db','3',A,A)],'trans-2-Butene, C4H8'),'Partial: trans','C₄H₈')+'</div>'],
   [('1','Hydrogen gas (first cell) is bubbled through hot oil with a nickel catalyst. Natural unsaturated fats have cis double bonds, which kink the chain. A four-carbon piece stands in for a whole fatty acid here…',''),('2','…and adding both hydrogens turns the double bond into a single one: a saturated chain, straight and solid.',''),('3','Stop partway and some double bonds just flip to trans instead: that is trans fat (see Fats, Figure 7).','')],
   fx=facts(what='Hydrogenation adds hydrogen to the double bonds of a liquid oil so it becomes firmer, more stable and slower to go rancid. Partial hydrogenation made margarine, shortening and frying fats from the 1950s on.',
     body='Partial hydrogenation forms industrial trans fat, which raises LDL cholesterol and lowers HDL, raising the risk of heart disease more than any other fat (see <a href="macronutrients-fats.html#fig-7">Fats, Figure 7</a>).',
     high='In 2015 the US FDA ruled that partially hydrogenated oils are no longer generally recognized as safe, and they were removed from the US food supply over the following years. Fully hydrogenated oil has almost no trans fat; it is saturated fat, often blended with liquid oils.',
     found='On older or imported labels: “partially hydrogenated soybean oil” in shortening, stick margarine, frosting, microwave popcorn and fried snacks. Small amounts of natural trans fat occur in dairy and beef.'),head='Hydrogenation')
 +table('refine',['','Whole grain','Refined (white)','Enriched refined'],[
   ['Parts kept','bran, germ and endosperm','endosperm only','endosperm only'],
   ['Fiber','high','low','low (not added back)'],
   ['B vitamins and iron','natural amounts','mostly lost','thiamin, riboflavin, niacin, folic acid and iron added back'],
   ['Magnesium, zinc, vitamin E, B6','natural amounts','mostly lost','not added back'],
   ['Shelf life','shorter (oily germ)','long','long']],'Refining grain')
 +lblock('oil','Refining oil',[('Refined, bleached, deodorized','After pressing or hexane extraction, most oils are degummed, neutralized, bleached with clay and deodorized with steam. The result is clear, mild and stable for frying, but loses much of its vitamin E, polyphenols and flavor. Extra-virgin olive oil and cold-pressed oils skip these steps.')])
 +legend('c h'))
P8=('<!--noart-->'+molbox('nix','Lime, and the vitamin it frees',[
   '<div class="mgrid">'+mcell(MP('ca','Calcium ion, Ca2+: a green ball',[],'Calcium ion, Ca2+',eager=True),'Calcium ion','Ca²⁺')
   +mcell(MP('hydroxide','Hydroxide ion, OH-: an oxygen with one hydrogen',[('o','1',A,A)],'Hydroxide ion, OH-'),'Hydroxide','OH⁻')
   +mcell(MP('niacin','Niacin (nicotinic acid): a pyridine ring with a carboxylic acid group; every hydrogen shown',[('acid','2',A,A),('n','3',A,A)],'Niacin, C6H5NO2'),'Niacin','C₆H₅NO₂')+'</div>'],
   [('1','Slaked lime, calcium hydroxide, breaks into calcium ions and hydroxide in water, making it strongly alkaline.',''),('2','In raw corn, niacin’s acid group is tied to other molecules, so the body cannot absorb it…',''),('3','…the alkaline soak cuts it free. Niacin is vitamin B3 (see Water-Soluble Vitamins).','')],
   fx=facts(what='Nixtamalization is cooking and soaking dried corn in water with lime (calcium hydroxide), then rinsing it and grinding it into masa. It was developed in Mesoamerica thousands of years ago.',
     body='It frees bound niacin, loosens the hull, adds calcium, improves the balance of available amino acids, lowers some mold toxins, and lets the dough hold together for tortillas.',
     low='Where corn became a staple without nixtamalization, as in parts of Europe and the US South in the 1700s to early 1900s, pellagra was common: the disease of niacin deficiency, with dermatitis, diarrhea and dementia.',
     found='Corn tortillas, tamales, tortilla chips, pozole and hominy, and masa harina; look for “corn treated with lime” or “nixtamalized corn” on the label. Cornmeal, grits and polenta usually are not nixtamalized.'),head='Nixtamalization')
 +flow('steps','From dried corn to tortilla',[('Cook','dried corn simmers in water with lime'),('Steep','it soaks overnight; the hull loosens and niacin is freed'),('Rinse','the loose hulls and extra lime wash away'),('Grind','the wet kernels become masa dough'),('Shape and cook','pressed into tortillas or tamales')])
 +legend('ca c h o n',note='every molecule and ion on this page is drawn at the same scale with every hydrogen shown · tap one to enlarge it'))
P9=('<!--noart-->'+table('table',['Process','What it does','What forms or changes','Main foods','Worth doing'],[
  ['Processing aids','help make the food, then are removed','tiny traces; not labeled','vegetable oils, juice, wine','choose expeller-pressed oil if you prefer'],
  ['Browning (dry heat)','Maillard reaction of sugar with amino acids','acrylamide, AGEs, flavor and color','fries, chips, toast, coffee, seared meat','cook to golden, not dark brown'],
  ['Grilling, smoking','burns fat and drips; smoke coats food','HCAs, PAHs, smoky flavor','charred meat and fish, smoked foods','avoid flare-ups; trim char'],
  ['Curing','nitrite preserves and colors meat','nitrosamines when fried hot','bacon, ham, hot dogs, salami','eat processed meat sparingly'],
  ['Fermenting','microbes turn sugar into acid, alcohol, gas','lactic acid, ethanol, CO₂, vinegar','yogurt, sauerkraut, bread, wine','a useful way to preserve and digest'],
  ['Pasteurizing','brief heat kills germs','few changes to nutrients','milk, juice, eggs','choose pasteurized dairy'],
  ['Partial hydrogenation','adds hydrogen to oil','trans fat','old shortening and margarine','avoid; banned in the US'],
  ['Refining','removes bran, germ or impurities','loses fiber, vitamins, minerals','white flour, white rice, refined oils','choose whole grains often'],
  ['Nixtamalizing','alkaline lime cook of corn','frees niacin; adds calcium','tortillas, hominy, masa','a traditional gain']],'Processing at a glance')
 +worth([('Ultra-processed food','A popular classification called NOVA groups foods by how much they are processed. Diets high in ultra-processed foods, made mostly from refined ingredients and additives, are linked in many studies to obesity and chronic disease, though researchers still debate which features are responsible.'),
   ('Frying oil','Oil reused many times for deep-frying breaks down into polar compounds and aldehydes; restaurants are told to change it when it darkens, smokes or foams.'),
   ('Microwaving and pressure-cooking','Fast, moist methods often keep more water-soluble vitamins than long boiling, and form few of the heat compounds in this lesson.')],
   note='General education, not medical advice. Facts follow mainstream sources (US FDA and USDA, EU regulations, IARC, US National Cancer Institute, NIH Office of Dietary Supplements, standard food-science texts).'))
PR_LESSON=[('The Processing Family Tree','What happens to food between farm and plate, in three groups.',P1),
 ('Processing Aids','Helpers like hexane that never reach the label.',P2),
 ('Browning: Acrylamide and AGEs','What forms when sugars meet amino acids in dry heat.',P3),
 ('Grilling and Smoking: HCAs and PAHs','Compounds made in charred meat and smoke.',P4),
 ('Curing and Nitrosamines','How curing salt can form nitrosamines, and how vitamin C stops it.',P5),
 ('Fermentation and Pasteurization','Microbes that preserve food, and heat that makes it safe.',P6),
 ('Hydrogenation and Refining','Firming oils, and stripping grains and oils down.',P7),
 ('Nixtamalization','The lime soak that makes corn more nutritious.',P8),
 ('Putting It All Together','The whole lesson in one table, plus a few extras.',P9)]
PR_QUIZ=[('What is a processing aid, and why is it usually not on the label?','A substance used during manufacturing that is removed or has no function in the finished food; US and EU rules exempt it, unless it comes from a major allergen (Figure 2).'),
 ('What is hexane used for?','Dissolving oil out of crushed seeds such as soybeans and canola; it is then evaporated off (Figure 2).'),
 ('Which two things react to form acrylamide?','The amino acid asparagine and a sugar, heated above about 120°C (Figure 3).'),
 ('How can you form less acrylamide when making fries or toast?','Cook to golden yellow rather than dark brown (Figure 3).'),
 ('What is an AGE?','A protein or fat permanently altered by a sugar, such as carboxymethyl-lysine; they form in browned food and in the body (Figure 3).'),
 ('Where do HCAs and PAHs come from?','HCAs form in muscle meat cooked very hot; PAHs form when fat drips on flames and the smoke coats the food (Figure 4).'),
 ('What gives smoked foods their smoky aroma?','Phenols such as guaiacol, made when wood lignin burns (Figure 4).'),
 ('What does nitrite react with to form a nitrosamine?','An amine from protein breakdown, especially in frying heat or stomach acid (Figure 5).'),
 ('Why is ascorbate or erythorbate added to cured bacon?','It reacts with nitrite first and blocks nitrosamine formation (Figure 5).'),
 ('What do lactic acid bacteria and yeast each make from sugar?','Lactic acid bacteria make lactic acid; yeast makes ethanol and carbon dioxide (Figure 6).'),
 ('What does partial hydrogenation create that full hydrogenation does not?','Trans fat, when some double bonds flip from cis to trans instead of being filled (Figure 7).'),
 ('Why did pellagra appear where corn was eaten without nixtamalization?','Corn’s niacin is bound and cannot be absorbed unless the corn is cooked with lime (Figure 8).')]
build_lesson('processing','Processing','Processing is everything that happens to food between the farm and your plate. This lesson follows processing aids that never reach the label; the compounds that form when food is browned, grilled, smoked or cured (acrylamide, AGEs, HCAs, PAHs and nitrosamines); and methods that change the food itself: fermenting, pasteurizing, hydrogenating, refining and nixtamalizing. Each molecule is shown in ball-and-stick form with what it does, the risks, and where it is found. The figure is on the left and the lesson script on the right; the quiz is at the end.',PR_LESSON,PR_QUIZ,mols=MP,scale=11)
