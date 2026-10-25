import math
# ---------------- Module 3 · Non-Nutrients · Additives and E-Numbers ----------------
MA=mk_lmol('additives')
A=None
_C=[(50,'Colors','E100s · Fig. 3','#fig-3','Curcumin','E100','#fig-3'),
    (150,'Preservatives','E200s · Fig. 4','#fig-4','Benzoate','E211','#fig-4'),(250,'Antioxidants','E300s · Fig. 5','#fig-5','Vitamin C','E300','#fig-5'),
    (350,'Thickeners','E400s · Fig. 6','#fig-6','Pectin','E440','#fig-6'),(450,'Emulsifiers','E400s · Fig. 6','#fig-6','Lecithin','E322','#fig-6'),(550,'Anti-caking','E500s · Fig. 7','#fig-7','Silica','E551','#fig-7'),
    (650,'Acids','Fig. 5','#fig-5','Citric acid','E330','#fig-2'),(750,'Enhancers','E600s · Fig. 7','#fig-7','MSG','E621','#fig-7'),(850,'Sweeteners','E900s · Fig. 8','#fig-8','Aspartame','E951','#fig-8')]
AD_NODES=[(450,30,300,'Food Additives','added on purpose to do a job','nd root','#fig-2'),
 (50,150,96,'Appearance','Fig. 3','nd l','#fig-3'),(200,150,196,'Shelf life','Figs. 4–5','nd l','#fig-4'),(450,150,296,'Texture','Figs. 6–7','nd l','#fig-6'),(750,150,296,'Taste','Figs. 5, 7, 8','nd l','#fig-7')]
AD_NODES+=[(x,270,94,t,s,'nd u',h) for x,t,s,h,_,_,_ in _C]+[(x,390,94,t,s,'nd t',h) for x,_,_,_,t,s,h in _C]
_P={50:50,150:200,250:200,350:450,450:450,550:450,650:750,750:750,850:750}
AD_EDGES=[(450,52,x,128) for x in (50,200,450,750)]+[(_P[x],182,x,248) for x in _P]+[(x,302,x,368) for x in _P]
P1=('<!--noart-->'+ftree(AD_NODES,AD_EDGES,420,'Tree diagram: food additives grouped by job. Appearance: colors (E100s, e.g. curcumin E100). Shelf life: preservatives (E200s, e.g. benzoate E211) and antioxidants (E300s, e.g. vitamin C E300). Texture: thickeners (E400s, e.g. pectin E440), emulsifiers (e.g. lecithin E322) and anti-caking agents (E500s, e.g. silica E551). Taste: acids (e.g. citric acid E330), flavor enhancers (E600s, e.g. MSG E621) and sweeteners (E900s, e.g. aspartame E951).')
 +lblock('label','Reading the numbers',[('E for Europe','An E-number is the code an additive gets once it has passed an EU safety review. The hundreds digit roughly tells you the job: 1 colors, 2 preservatives, 3 antioxidants and acids, 4 thickeners and emulsifiers, 5 acidity regulators and anti-caking agents, 6 flavor enhancers, 9 sweeteners and glazes.'),
   ('Grouped by job','Some additives break the pattern: lecithin (E322) is an emulsifier, and acids turn up in both the 300s and 500s. That is why this lesson groups them by what they do.'),
   ('Not all synthetic','Many additives are ordinary food compounds: vitamin C (E300), citric acid (E330), pectin (E440), lecithin from egg yolk or soy (E322).')]))
P2=('<!--noart-->'+lblock('what','What counts as an additive',[('Added on purpose','An additive is a substance added to food to do a technical job: color it, keep it from spoiling, thicken it, sweeten it, or stop it from clumping. Ordinary ingredients such as flour, salt and sugar are not usually called additives.'),
   ('Listed by weight','The ingredient list runs from most to least by weight, so additives, used in small amounts, are usually near the end.'),
   ('Same molecule, either source','An additive is the same molecule whether it was squeezed from a fruit or made in a factory; what matters is the amount and the food it is in.')])
 +molbox('citric','Citric acid, E330, C₆H₈O₇',[MA('citric','Citric acid: a three-carbon backbone with a central OH and three carboxylic acid groups; every hydrogen shown',[('acid','1',A,A),('acid2','1',A,A),('acid3','1',A,A),('oh','2',A,A)],'Citric acid, C6H8O7',eager=True)],
   [('1','Three acid (COOH) groups give the sour taste…',''),('2','…around a central carbon with an OH.','')],
   fx=facts(what='The acid that makes lemons and limes sour. Added to drinks, jams and canned foods for tartness, to adjust acidity, and to help stop color and flavor changes.',
     body='Your cells make and use it every day: it is the first compound in the citric acid cycle, the main route for releasing energy from food.',
     high='Safe at the levels in food. Like any acid, frequent sour drinks can wear tooth enamel.',
     found='Lemons, limes, oranges, grapefruit, berries, tomatoes. Most added citric acid is made by fermenting sugar with a mold (Aspergillus niger).'))
 +table('rules',['Topic','United States','European Union'],[
   ['Approval','FDA review as a food or color additive, or “generally recognized as safe” (GRAS)','EFSA safety review, then an E-number'],
   ['On the label','by name, such as “sodium benzoate” or “Red 40”','by job plus name or E-number, such as “preservative: E211”'],
   ['Numbers','not used on labels','E-numbers; the worldwide Codex INS number is the same digits without the E (citric acid is INS 330)']],'Rules and labels')
 +legend('c h o'))
P3=('<!--noart-->'+molbox('natural','Curcumin, E100, C₂₁H₂₀O₆',[MA('curcumin','Curcumin: two benzene rings, each with an OH and a methoxy group, joined by a seven-carbon chain with two C=O groups; every hydrogen shown',[('ring','1',A,A),('mid','2',A,A)],'Curcumin, C21H20O6',eager=True)],
   [('1','Two rings at the ends…',''),('2','…joined by a long chain of alternating single and double bonds, which absorbs blue light, so it looks yellow.','')],
   fx=facts(what='The yellow pigment of turmeric, used to color mustard, cheese, butter and drinks.',body='Poorly absorbed from food; it gives color, not a nutrient.',
     found='Turmeric root. Other colors from whole foods include beet red (betanin, E162), paprika (E160c) and beta-carotene (E160a).'),head='Colors from plants')
 +molbox('synthetic','Allura Red AC, Red 40, E129',[MA('allura','Allura Red: two ring systems joined by an N=N azo bond, each carrying a sulfonate group; every hydrogen shown',[('azo','1',A,A),('so3','2',A,A),('so3b','2',A,A)],'Allura Red ion, C18H14N2O8S2 2-')],
   [('1','An N=N “azo” bond joins two ring systems; azo dyes are the largest group of synthetic food colors.',''),('2','Charged sulfonate groups make it dissolve in water.','')],
   fx=facts(what='A synthetic red dye made from petroleum, used in candy, drinks, cereals and snacks; sold as the sodium salt.',
     high='In the EU, foods with Red 40 or five other synthetic colors must carry the warning “may have an adverse effect on activity and attention in children.” In 2025 the FDA said it plans to phase out petroleum-based dyes, and it revoked the use of Red 3 in food from 2027.',
     found='Not in whole foods; ultra-processed foods only.'),head='Synthetic colors')
 +molbox('tio2','Titanium dioxide, E171, TiO₂',[MA('tio2','Titanium dioxide: a gray titanium atom between two red oxygens',[],'Titanium dioxide, TiO2')],
   fx=facts(what='A bright white mineral pigment, used to whiten candy coatings, frostings and chewing gum. In food it is a fine powder of tiny crystals; one unit is shown.',
     high='Banned as a food additive in the EU from 2022, after EFSA concluded it could no longer be considered safe because harm to DNA could not be ruled out. The US still permits it, up to 1% of a food’s weight.',
     found='Not in whole foods.'))
 +legend('c h o n s ti'))
P4=('<!--noart-->'+molbox('acids','Sorbic acid and benzoic acid',[
   '<div class="mgrid">'+mcell(MA('sorbic','Sorbic acid: a six-carbon chain with two C=C double bonds ending in a carboxylic acid; every hydrogen shown',[('acid','1',A,A)],'Sorbic acid, C6H8O2',eager=True),'Sorbic acid','E200; potassium sorbate E202')
   +mcell(MA('benzoic','Benzoic acid: a benzene ring with a carboxylic acid group; every hydrogen shown',[('acid','1',A,A)],'Benzoic acid, C7H6O2'),'Benzoic acid','E210; sodium benzoate E211')+'</div>'],
   [('1','Both are weak acids. In acidic foods they stay uncharged, slip into mold and yeast cells and stop them growing.','')],
   fx=facts(what='The most common preservatives against molds and yeasts. Sorbates are used in cheese, baked goods and wine; benzoates in soft drinks, pickles and sauces.',
     body='Sorbic acid is broken down like a fatty acid; benzoic acid is joined to glycine in the liver and passed in urine.',
     high='Low toxicity at permitted levels. With vitamin C, heat and light, benzoate can form traces of benzene in drinks, so manufacturers reformulated many drinks after FDA testing in 2006–2007.',
     found='Sorbic acid was first found in rowan berries; benzoic acid occurs naturally in cranberries, cinnamon and cloves.'),head='Against molds and yeasts')
 +molbox('nitrite','Nitrite, NO₂⁻',[MA('nitrite','Nitrite ion: a blue nitrogen bonded to two red oxygens in a bent shape',[('n','1',A,A)],'Nitrite ion, NO2-')],
   [('1','A nitrogen with two oxygens. Sodium nitrite is E250; nitrates (E251, E252) turn into nitrite.','')],
   fx=facts(what='The curing agent in bacon, ham, hot dogs and salami. It stops Clostridium botulinum, the bacterium that causes botulism, and gives cured meat its pink color and flavor.',
     high='Nitrite can react with amines in meat to form nitrosamines, especially at high heat such as frying bacon (see Processing). The WHO’s cancer agency classes processed meat as a cause of colorectal cancer.',
     found='Most nitrate in the diet comes from vegetables such as spinach, beets, celery and lettuce, where it comes packaged with vitamin C and other protective compounds. Meats labeled “uncured” are usually cured with celery powder, a natural source of nitrate.'),head='Curing meat')
 +molbox('sulfite','Sulfur dioxide, SO₂, E220',[MA('so2','Sulfur dioxide: a yellow sulfur bonded to two red oxygens in a bent shape',[('s','1',A,A)],'Sulfur dioxide, SO2')],
   [('1','Sulfur dioxide and sulfite salts (E220–E228) release the same active form.','')],
   fx=facts(what='Preservatives and antibrowning agents in wine, dried fruit such as apricots, and some potato products.',
     high='Can trigger asthma attacks in sensitive people. The US requires sulfites to be declared at 10 parts per million or more and bans them on fresh fruit and vegetables meant to be eaten raw. Sulfites also destroy thiamin (vitamin B1).',
     found='Formed in small amounts naturally during wine fermentation.'),head='Sulfites')
 +legend('c h o n s'))
P5=('<!--noart-->'+molbox('vitc','Ascorbic acid, vitamin C, E300',[MA('ascorbic','Ascorbic acid: a five-membered ring with a C=C double bond carrying two OH groups, and a two-carbon side chain; every hydrogen shown',[('ene','1',A,A)],'Ascorbic acid, C6H8O6',eager=True)],
   [('1','The two OH groups on the double bond give up electrons, so vitamin C is oxidized first and the food is protected.','')],
   fx=facts(what='Added to stop cut fruit, juices and wine from browning, to help bread dough, and to cured meats, where it speeds curing and reduces nitrosamine formation.',
     found='Citrus, peppers, kiwi, strawberries, broccoli. Tocopherols (vitamin E, E306–E309) and rosemary extract (E392) are other antioxidants from plants.'),head='Antioxidants from plants')
 +molbox('bht','BHA and BHT',[
   '<div class="mgrid">'+mcell(MA('bha','BHA: a benzene ring with an OH, a methoxy group and a bulky tert-butyl group; every hydrogen shown',[('oh','1',A,A),('tb','2',A,A)],'BHA, C11H16O2'),'BHA','E320')
   +mcell(MA('bht','BHT: a benzene ring with an OH between two bulky tert-butyl groups; every hydrogen shown',[('oh','1',A,A),('tb','2',A,A)],'BHT, C15H24O'),'BHT','E321')+'</div>'],
   [('1','An OH on a ring gives up a hydrogen to stop the chain reaction that turns fats rancid…',''),('2','…and the bulky tert-butyl groups keep the leftover molecule stable.','')],
   fx=facts(what='Synthetic antioxidants that keep fats and oils from going rancid, used in cereals, chewing gum, snack foods and fats.',
     high='Permitted in small amounts. The US National Toxicology Program lists BHA as “reasonably anticipated to be a human carcinogen,” based on high doses in animals; evidence in people is lacking.',
     found='Not in whole foods.'),head='Synthetic antioxidants')
 +molbox('acid','Phosphoric acid, E338',[MA('phosphoric','Phosphoric acid: an orange phosphorus atom with one double-bonded oxygen and three OH groups',[('p','1',A,A)],'Phosphoric acid, H3PO4')],
   [('1','A phosphorus with four oxygens, three of them carrying a hydrogen.','')],
   fx=facts(what='Gives colas their sharp tang. Related phosphates (E339–E343, E450–E452) are used in processed meats, cheese and baking powder.',
     high='Phosphate additives are absorbed more completely than the phosphorus in whole foods, which matters for people with kidney disease (see Major Minerals). Other acids from foods: acetic acid (vinegar, E260), lactic acid (yogurt, E270), malic acid (apples, E296).',
     found='Phosphate is in every cell: meat, fish, dairy, beans, nuts and whole grains.'),head='Acids')
 +legend('c h o p'))
P6=('<!--noart-->'+molbox('gums','Galacturonic acid, the building block of pectin',[MA('galacturonic','Galacturonic acid: a six-membered sugar ring with a carboxylic acid group; every hydrogen shown',[('acid','1',A,A)],'Galacturonic acid, C6H10O7',eager=True)],
   [('1','A sugar ring with an acid group. Pectin is long chains of these, which trap water and, with sugar and acid, set jam.','')],
   fx=facts(what='Pectin (E440) is a soluble fiber from plant cell walls, used to set jams and thicken yogurts and fillings.',body='Not digested; gut bacteria ferment it in the large intestine like other soluble fiber.',
     found='Apples, citrus peel, quince, plums, berries.'),head='Thickeners')
 +table('gumtbl',['Thickener','E-number','Source'],[['Agar','E406','red seaweed'],['Carrageenan','E407','red seaweed'],['Locust bean gum','E410','carob seeds'],['Guar gum','E412','guar beans'],
   ['Xanthan gum','E415','made by bacteria fermenting sugar'],['Cellulose gum (CMC)','E466','chemically modified plant cellulose']],'Gums and their sources')
 +molbox('emul','A monoglyceride, E471',[MA('monostearin','Glyceryl monostearate: a glycerol head with two OH groups joined to one long 18-carbon fatty acid tail; every hydrogen shown',[('head','1',A,A),('tail','2',A,A)],'Glyceryl monostearate, C21H42O4')],
   [('1','A water-loving head: glycerol with two free OH groups…',''),('2','…and a fat-loving tail: one fatty acid instead of a fat’s three. The head sits in water and the tail in oil, so droplets of one stay spread through the other.','')],
   fx=facts(what='Mono- and diglycerides (E471) keep bread soft and stop spreads and ice cream from separating. Lecithin (E322), from soy, sunflower or egg yolk, works the same way; egg yolk lecithin is what holds mayonnaise together.',
     body='Monoglycerides are digested like ordinary fat; your gut makes them itself when it digests a meal’s fat.',
     high='Early research in mice suggests some emulsifiers, such as cellulose gum (E466) and polysorbate 80 (E433), may disturb gut bacteria; evidence in people is limited.',
     found='Egg yolk, soybeans, sunflower seeds (lecithin).'),head='Emulsifiers')
 +legend('c h o'))
P7=('<!--noart-->'+molbox('soda','Bicarbonate, HCO₃⁻',[MA('bicarbonate','Bicarbonate ion: a carbon with three oxygens, one carrying a hydrogen',[('c','1',A,A)],'Bicarbonate ion, HCO3-',eager=True)],
   [('1','Baking soda is sodium bicarbonate (E500). With an acid it gives off carbon dioxide gas, which makes batter rise.','')],
   fx=facts(what='A leavening agent and acidity regulator. Baking powder is baking soda already mixed with a dry acid.',body='Your pancreas releases bicarbonate to neutralize stomach acid as food enters the small intestine.',
     found='Made from mineral sources; buttermilk and yogurt supply the acid in many recipes.'),head='Acidity regulators')
 +lblock('cake','Anti-caking agents',[('Keeping powders flowing','Silicon dioxide (silica, E551) and calcium silicate (E552) soak up moisture so salt, spice mixes and powdered drinks do not clump. Silica is the same compound as quartz sand, in a fine powder.')])
 +molbox('msg','Monosodium glutamate, MSG, E621',[
   '<div class="mgrid">'+mcell(MA('glutamate','Glutamate ion: the amino acid glutamic acid with one acid group carrying a negative charge; every hydrogen shown',[('aa','1',A,A),('coo','2',A,A)],'Glutamate ion, C5H8NO4-'),'Glutamate','C₅H₈NO₄⁻')
   +mcell(MA('na','Sodium ion, Na+: a purple ball',[],'Sodium ion, Na+'),'Sodium','Na⁺')+'</div>'],
   [('1','Glutamate is the amino acid glutamic acid (see Protein)…',''),('2','…with one acid group charged. In water MSG splits into glutamate and a sodium ion.','')],
   fx=facts(what='A flavor enhancer that tastes savory, or umami. It was first isolated from kombu seaweed in Japan in 1908.',
     body='Your body handles glutamate from MSG the same way as glutamate from tomatoes or cheese; most is used for energy by the gut itself.',
     high='The FDA classes it as GRAS and requires it to be listed by name. Blinded studies have not consistently reproduced the symptoms some people report. MSG has about a third of the sodium of table salt.',
     found='Free glutamate is high in tomatoes, parmesan, mushrooms, soy sauce, kombu and anchovies. Inosinate (E631) and guanylate (E627), from meat, fish and mushrooms, boost umami further.'),head='Flavor enhancers')
 +legend('c h o n na'))
P8=('<!--noart-->'+molbox('aspartame','Aspartame, E951, C₁₄H₁₈N₂O₅',[MA('aspartame','Aspartame: aspartic acid joined to phenylalanine, whose acid end is capped with a methyl group; every hydrogen shown',[('asp','1',A,A),('phe','2',A,A),('ome','3',A,A)],'Aspartame, C14H18N2O5',eager=True)],
   [('1','Aspartic acid…',''),('2','…joined to phenylalanine, two ordinary amino acids…',''),('3','…with a methyl ester cap that is released as methanol, in amounts smaller than from fruit juice.','')],
   fx=facts(what='About 200 times sweeter than sugar, used in diet drinks, yogurt and tabletop sweeteners. It breaks down with heat, so it is not used for baking.',
     body='Digested into its two amino acids and methanol. People with phenylketonuria (PKU) cannot break down phenylalanine, so labels must warn “Phenylketonurics: contains phenylalanine.”',
     high='In 2023 the WHO’s cancer agency classed it as “possibly carcinogenic” (the lowest level, based on limited evidence), while the WHO/FAO expert committee kept its acceptable daily intake at 40 mg per kg of body weight. The FDA’s is 50 mg per kg.',
     found='Not in whole foods.'),head='Sweeteners')
 +molbox('sucralose','Sucrose and sucralose, E955',[
   '<div class="mgrid">'+mcell(MA('sucrose','Sucrose: a six-membered glucose ring joined through an oxygen to a five-membered fructose ring; every hydrogen shown',[('o','1',A,A),('o2','1',A,A),('o3','1',A,A)],'Sucrose, C12H22O11'),'Sucrose','table sugar')
   +mcell(MA('sucralose','Sucralose: the same two rings as sucrose with three OH groups replaced by green chlorine atoms; every hydrogen shown',[('cl','2',A,A),('cl2','2',A,A),('cl3','2',A,A)],'Sucralose, C12H19Cl3O8'),'Sucralose','E955')+'</div>'],
   [('1','Three OH groups in sugar…',''),('2','…are swapped for chlorine. The result is about 600 times sweeter, heat-stable, and mostly passes through without being absorbed.','')],
   fx='<p class="mfact">Steviol glycosides (E960), from the leaves of the stevia plant, are 200–300 times sweeter than sugar.</p>')
 +molbox('polyol','Erythritol, a sugar alcohol, E968',[MA('erythritol','Erythritol: a four-carbon chain with an OH on every carbon; every hydrogen shown',[('c','1',A,A)],'Erythritol, C4H10O4')],
   [('1','A short chain with an OH on every carbon: a sugar alcohol, or polyol.','')],
   fx=facts(what='About 60–70% as sweet as sugar with almost no calories: it is absorbed and passed unchanged in urine.',
     high='A 2023 observational study linked high blood erythritol to heart attack and stroke; it does not show cause. Other polyols, such as sorbitol (E420) and xylitol (E967), cause gas and diarrhea in large amounts. Xylitol is poisonous to dogs.',
     found='Small amounts in pears, melons, grapes, mushrooms and fermented foods.'))
 +lblock('adi','Acceptable daily intake',[('ADI','The amount per kilogram of body weight that can be eaten every day for a lifetime without appreciable risk, usually set at one hundredth of the highest dose that caused no harm in animal studies. A 70 kg adult would need roughly 9 to 14 cans of diet soda a day to reach aspartame’s ADI.')])
 +legend('c h o n cl'))
P9=('<!--noart-->'+table('table',['Range','Main job','Examples','Also found in whole foods'],[
  ['E100s','colors','curcumin E100, Red 40 E129, titanium dioxide E171 (banned in the EU)','turmeric, beets (E162), paprika (E160c)'],
  ['E200s','preservatives','sorbates E200–E203, benzoates E210–E213, sulfites E220–E228, nitrite E250','rowan berries, cranberries, vegetables (nitrate)'],
  ['E300s','antioxidants and acids','vitamin C E300, tocopherols E306, citric acid E330, lecithin E322, BHA E320, BHT E321','citrus, nuts and seeds, egg yolk'],
  ['E400s','thickeners, gels and emulsifiers','pectin E440, guar E412, xanthan E415, carrageenan E407, mono- and diglycerides E471','apples, citrus peel, seaweed, beans'],
  ['E500s','acidity regulators and anti-caking agents','baking soda E500, silica E551','—'],
  ['E600s','flavor enhancers','MSG E621, guanylate E627, inosinate E631','tomatoes, parmesan, mushrooms, kombu'],
  ['E900s','sweeteners and glazes','aspartame E951, sucralose E955, steviol glycosides E960, erythritol E968, beeswax E901, carnauba wax E903','stevia leaves, pears and grapes, honeycomb']],'The E-number ranges')
 +worth([('An E-number is an approval, not a warning','It only means the additive passed an EU safety review; many are compounds also found in whole foods, such as vitamin C (E300) and pectin (E440).'),
   ('“Uncured” is still cured','Meats labeled “uncured” or “no nitrites added” are usually cured with celery powder, whose natural nitrate bacteria turn into nitrite.'),
   ('Additives cluster in ultra-processed foods','Whole foods need almost none; a long list of additives is one sign that a food is highly processed.')],
   note='General education, not medical advice. Facts follow regulators and mainstream sources (US FDA, European Food Safety Authority, WHO/FAO JECFA, standard food-science texts).'))
AD_LESSON=[('The Additive Family Tree','Additives grouped by the job they do.',P1),
 ('What Counts as an Additive','Definition, labels and approval, with citric acid as the first example.',P2),
 ('Colors','From turmeric to azo dyes and titanium dioxide.',P3),
 ('Preservatives','Stopping molds, yeasts and bacteria.',P4),
 ('Antioxidants and Acids','Stopping browning and rancidity, and adding tang.',P5),
 ('Thickeners and Emulsifiers','Gels, gums and molecules with two ends.',P6),
 ('Leavening, Anti-Caking and Flavor Enhancers','Baking soda, silica and MSG.',P7),
 ('Sweeteners','Intense sweeteners, sugar alcohols and the ADI.',P8),
 ('Putting It All Together','The whole lesson in one table, plus a few extras.',P9)]
AD_QUIZ=[('What does an E-number tell you?','That the additive has passed an EU safety review; the hundreds digit roughly gives its job (Figure 1).'),
 ('How are additives shown on a US label?','By name, such as “sodium benzoate,” not by E-number (Figure 2).'),
 ('Where does most added citric acid come from?','Fermenting sugar with a mold, Aspergillus niger (Figure 2).'),
 ('Which additive did the EU ban in 2022, and why?','Titanium dioxide, E171, because harm to DNA could not be ruled out (Figure 3).'),
 ('What does the E200 range do?','Preserves food against microbes (Figure 4).'),
 ('Why is sodium nitrite (E250) in cured meat?','It stops the botulism bacterium and gives the pink color and cured flavor (Figure 4).'),
 ('Who needs to watch for sulfites?','People with sulfite-sensitive asthma; US labels must declare 10 ppm or more (Figure 4).'),
 ('What do BHA and BHT do?','They stop fats from going rancid (Figure 5).'),
 ('What is pectin made of, and where does it come from?','Chains of galacturonic acid, from apples and citrus peel (Figure 6).'),
 ('How does an emulsifier keep oil and water mixed?','It has a water-loving head and a fat-loving tail (Figure 6).'),
 ('What is E621, and which whole foods are rich in the same compound?','Monosodium glutamate; tomatoes, parmesan, mushrooms, soy sauce, kombu (Figure 7).'),
 ('How does sucralose differ from sugar?','Three OH groups of sucrose are replaced by chlorine, making it about 600 times sweeter (Figure 8).')]
build_lesson('additives','Additives and E-Numbers','Additives are substances added to food to do a job: color, preserve, thicken, emulsify, sweeten or season. This lesson groups them by job and shows the key molecules, from citric acid to sucralose, with how they are labeled and regulated in the US and EU. Ultra-processed foods appear here because that is where most additives are used.',AD_LESSON,AD_QUIZ,mols=MA,scale=16)
