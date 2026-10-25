# ---------------- Module 7 · Flavorings ----------------
MF=mk_lmol('flavorings')
A=None
_X=[64,193,321,450,579,707,836]
_L=[('Sweet','Fig. 3','#fig-3','Sugars','and sweeteners'),('Bitter','Fig. 3','#fig-3','Coffee, greens','about 25 receptors'),
    ('Sour','Fig. 4','#fig-4','Citrus','vinegar, yogurt'),('Salty','Fig. 4','#fig-4','Salt','sodium ions'),('Umami','Fig. 5','#fig-5','Glutamate','tomato, cheese'),
    ('Aromas','Fig. 6','#fig-6','Vanilla, mint','citrus, cinnamon'),('Flavor labels','Figs. 7–8','#fig-7','Natural flavor','vs artificial')]
FL_NODES=[(450,30,320,'Flavor','taste on the tongue + smell in the nose','nd root','#fig-2'),
 (321,150,637,'Taste','five basic tastes, each with its own receptor · Figs. 3–5','nd l','#fig-3'),(707,150,122,'Smell','Fig. 6','nd l','#fig-6'),(836,150,122,'On the label','Figs. 7–8','nd l','#fig-7')]
FL_NODES+=[(x,270,122,t,s,'nd u',h) for x,(t,s,h,_,_) in zip(_X,_L)]+[(x,390,122,t,s,'nd t',h) for x,(_,_,h,t,s) in zip(_X,_L)]
_P=dict(zip(_X,[321,321,321,321,321,707,836]))
FL_EDGES=[(450,52,x,128) for x in (321,707,836)]+[(_P[x],182,x,248) for x in _X]+[(x,302,x,368) for x in _X]
P1=('<!--noart-->'+ftree(FL_NODES,FL_EDGES,420,'Tree diagram: flavor is taste on the tongue plus smell in the nose. Taste has five basic tastes, each with its own receptor: sweet (sugars and sweeteners), bitter (coffee, greens; about 25 receptors), sour (citrus, vinegar, yogurt), salty (salt; sodium ions) and umami (glutamate; tomato, cheese). Smell: aromas such as vanilla, mint, citrus and cinnamon. On the label: natural flavor versus artificial flavor.')
 +lblock('label','What the tree shows',[('Taste plus smell','What we call flavor is mostly two senses working together: a handful of tastes on the tongue and thousands of aromas sensed in the nose. Pinch your nose and a jelly bean tastes only sweet; the cherry or lemon comes back when you let go.'),
   ('Molecules meet receptors','Every taste and smell starts when a molecule fits a receptor protein on a sensory cell. This lesson shows the molecules and the receptors they fit.'),
   ('Flavorings on the label','Most added flavorings are aroma molecules, listed as “natural flavor” or “artificial flavor”; a few, such as MSG, act on taste. Figures 7 and 8 explain what those label lines do and do not tell you.')]))
P2=('<!--noart-->'+table('five',['Taste','What it signals','Receptor','Examples'],[
   ['Sweet','energy (sugars)','one receptor made of two parts, T1R2 + T1R3','sugar, fruit, honey, sweeteners'],
   ['Umami','protein (amino acids)','T1R1 + T1R3','tomato, cheese, broth, soy sauce'],
   ['Salty','sodium, a needed mineral','the sodium channel ENaC, plus others at high salt','salt, soy sauce, olives'],
   ['Sour','acid: unripe or spoiled food','OTOP1, a channel that lets hydrogen ions in','lemon, vinegar, yogurt'],
   ['Bitter','possible poison','about 25 different TAS2R receptors','coffee, dark greens, hops, tonic water']],'The five basic tastes')
 +lblock('smell','Smell does most of the work',[('Through the back of the mouth','As you chew, aroma molecules rise from the back of the mouth into the nose. Humans have about 400 kinds of smell receptor, and each aroma molecule switches on a pattern of them, so we can tell apart a huge number of smells.'),
   ('The tongue map is a myth','Every part of the tongue that has taste buds can sense all five tastes. Each taste bud holds 50 to 100 receptor cells, and they are replaced about every week or two.'),
   ('Hot, cool and tingling','Chili heat, mint cool and the fizz of carbonation are not tastes or smells but touch and pain nerves reacting to chemicals (see Bioactives, Figure 7).')]))
P3=('<!--noart-->'+molbox('sweet','Sweet: a sugar fits the sweet receptor',[MF('sucrose','Sucrose: a glucose ring and a fructose ring joined through an oxygen; every hydrogen shown',[('link','1',A,A)],'Sucrose, C12H22O11',eager=True)],
   [('1','Table sugar, sucrose: glucose and fructose joined through one oxygen (see Carbohydrates). Its OH groups grip the sweet receptor’s clamp-like pocket.','')],
   fx=facts(what='Sweet taste is sensed by one receptor built from two proteins, T1R2 and T1R3. Sugars, sugar alcohols, artificial sweeteners and even a few plant proteins all fit it, in different spots.',
     body='Sweetness signals energy, and babies prefer it from birth. The same receptor sits in the gut, where it helps control sugar absorption and hormone release. Sweeteners such as sucralose fit it hundreds of times more tightly than sugar, so a tiny amount tastes as sweet (see Additives).',
     high='Liking for sweetness falls when people eat less sugar for a few weeks. The WHO advises keeping free sugars below 10% of calories.',
     found='Sugars in fruit, honey, milk and added sugar; sweeteners such as sucralose, aspartame, stevia and monk fruit.'),head='Sweet')
 +molbox('bitter','Bitter: many receptors for many molecules',[MF('caffeine','Caffeine: two fused rings with four nitrogens, two C=O groups and three methyl groups; every hydrogen shown',[('m1','2',A,A)],'Caffeine, C8H10N4O2')],
   [('2','Caffeine (see Bioactives) fits several bitter receptors. Bitter compounds share no single shape, which is why we need about 25 kinds of receptor to catch them.','')],
   fx=facts(what='Bitter taste is sensed by about 25 different TAS2R receptors, each tuned to a range of molecules. It is the most sensitive taste, because many plant poisons are bitter.',
     body='Bitterness warns us, and it can trigger gagging at high levels. People differ genetically: about a quarter of people are strong tasters of certain bitter compounds, through a variant of the TAS2R38 receptor, and often find broccoli, kale and grapefruit harsher.',
     high='Bitterness is often a sign of something valuable as well, since many polyphenols are bitter; cooking, salt, fat and sweetness all soften it.',
     found='Coffee, tea, cocoa, beer hops, dark leafy greens and brassicas, grapefruit (naringin), olives, tonic water (quinine).'),head='Bitter')
 +legend('c h o n'))
P4=('<!--noart-->'+molbox('sour','Sour: hydrogen ions',[
   '<div class="mgrid">'+mcell(MF('hydronium','Hydronium ion, H3O+: an oxygen holding three hydrogens',[('o','1',A,A)],'Hydronium ion, H3O+',eager=True),'Hydronium','H₃O⁺')
   +mcell(MF('citric','Citric acid: a six-carbon molecule with three carboxylic acid groups and one OH; every hydrogen shown',[('c','2',A,A)],'Citric acid, C6H8O7'),'Citric acid','C₆H₈O₇')+'</div>'],
   [('1','Acids release hydrogen ions, which in water ride on a water molecule as hydronium. Sour cells sense them through a channel called OTOP1 that lets them in.',''),('2','Citric acid, the sour of lemons, has three acid groups, each able to release a hydrogen ion.','')],
   fx=facts(what='Sour is the taste of acid. It is detected by hydrogen ions flowing into sour-sensing cells through the OTOP1 channel.',
     body='Sourness warns of unripe fruit and spoiled food, yet in moderation it is refreshing. Acids such as citric, lactic, malic and acetic acid are added to foods for tartness and to preserve them (see Additives).',
     high='Frequent acidic drinks, including sodas, juices and sports drinks, can erode tooth enamel; rinsing with water helps.',
     found='Lemons, limes and other citrus (citric acid), apples (malic), grapes (tartaric), yogurt and sauerkraut (lactic), vinegar (acetic), sodas (phosphoric and citric).'),head='Sour')
 +molbox('salty','Salty: sodium ions',[
   '<div class="mgrid">'+mcell(MF('na','Sodium ion, Na+: a purple ball',[],'Sodium ion, Na+'),'Sodium','Na⁺')
   +mcell(MF('cl','Chloride ion, Cl-: a larger green ball',[],'Chloride ion, Cl-'),'Chloride','Cl⁻')
   +mcell(MF('k','Potassium ion, K+: a larger purple ball',[],'Potassium ion, K+'),'Potassium','K⁺')+'</div>'],
   fx=facts(what='Salt taste is mainly the taste of sodium ions. At normal levels they enter salt cells through a sodium channel called ENaC; very high salt also switches on bitter and sour cells, which is why heavily salted food tastes harsh.',
     body='Sodium is needed for nerves, muscles and fluid balance (see Major Minerals), and salt taste helps us seek it. Most people eat far more than they need. Potassium chloride, used in salt substitutes, tastes salty but also bitter and metallic, because potassium does not fit the sodium channel as well.',
     high='The FDA Daily Value for sodium is 2,300 mg, about one teaspoon of salt. Taste for salt adapts: after a few weeks of eating less, lightly salted food tastes right.',
     found='Table salt, and above all processed and restaurant food: bread, cured meats, cheese, soups, sauces and snacks supply most dietary sodium.'),head='Salty')
 +legend('c h o na cl kk',note='every molecule and ion on this page is drawn at the same scale with every hydrogen shown · tap one to enlarge it'))
P5=('<!--noart-->'+molbox('glu','Glutamate and inosinate',[
   '<div class="mgrid">'+mcell(MF('glutamate','Glutamate ion: an amino acid with a positive NH3 group and two negative carboxylate groups; every hydrogen shown',[('n','1',A,A),('side','2',A,A)],'Glutamate ion, C5H8NO4-',eager=True),'Glutamate','C₅H₈NO₄⁻')
   +mcell(MF('imp','Inosine monophosphate: a double ring with nitrogens, joined to a ribose sugar that carries a phosphate group; every hydrogen shown',[('p','3',A,A)],'Inosine monophosphate (IMP), C10H13N4O8P'),'Inosinate (IMP)','C₁₀H₁₃N₄O₈P')+'</div>'],
   [('1','Glutamate is one of the amino acids in every protein (see Protein). Free, unattached glutamate is what tastes savory…',''),('2','…and this second acid group is what the umami receptor grips. MSG is just glutamate paired with a sodium ion.',''),('3','Inosinate, from meat and fish, binds the same receptor at a different spot and multiplies glutamate’s effect.','')],
   fx=facts(what='Umami is the savory taste of free glutamate, sensed by the T1R1 + T1R3 receptor. The Japanese chemist Kikunae Ikeda named it in 1908 after finding glutamate in kombu seaweed broth, and he went on to make monosodium glutamate (MSG, E621).',
     body='Umami signals protein. Inosinate (E631) and guanylate (E627) strongly boost it, which is why dashi made from kombu and bonito flakes, or tomato with parmesan, tastes so rich. Your body handles glutamate from MSG the same way as glutamate from tomatoes or cheese; most is used as fuel by the gut itself.',
     high='The US FDA lists MSG as generally recognized as safe, and controlled studies have not consistently reproduced the headaches and flushing some people attribute to it; a few may react to large doses on an empty stomach. MSG has about a third as much sodium as table salt, so it can help cut sodium.',
     found='Naturally high in parmesan and aged cheeses, tomatoes, mushrooms, soy sauce, miso, fish sauce, kombu, cured ham, yeast extract and broths. On labels: monosodium glutamate, yeast extract, hydrolyzed protein, disodium inosinate and guanylate.'),head='Umami')
 +legend('c h o n p'))
P6=('<!--noart-->'+molbox('van','Vanillin',[MF('vanillin','Vanillin: a benzene ring with an aldehyde group, a methoxy group and an OH; every hydrogen shown',[('cho','1',A,A),('oh','2',A,A)],'Vanillin, C8H8O3',eager=True)],
   [('1','An aldehyde group (C=O with H) on a ring…',''),('2','…plus the methoxy and OH pair of guaiacol, the smoke molecule in Processing. Vanillin is the main flavor of cured vanilla beans.','')],
   fx=facts(what='The most widely used flavor molecule in the world. Vanilla beans develop it during weeks of curing, but less than 1% of the vanillin used comes from vanilla beans; the rest is made from other sources (Figure 7).',
     body='No nutritional role; used at tiny levels. Real vanilla contains hundreds of other aroma compounds, which is why it tastes rounder than pure vanillin.',
     found='Vanilla beans and extract, chocolate, ice cream, baked goods, soft drinks; small amounts form naturally in oak-aged wine and whisky.'),head='Four aroma molecules')
 +molbox('cin','Cinnamaldehyde',[MF('cinnamaldehyde','Cinnamaldehyde: a benzene ring attached to a three-carbon chain with a double bond and an aldehyde at the end; every hydrogen shown',[('cho','3',A,A)],'Cinnamaldehyde, C9H8O')],
   [('3','A ring, a double bond and an aldehyde. Besides its smell, cinnamaldehyde switches on TRPA1, the nerve receptor behind cinnamon’s warm sting.','')],
   fx=facts(what='The main aroma compound of cinnamon bark, making up most of its essential oil.',
     body='Food amounts are safe. Cinnamon supplements for blood sugar have shown small and inconsistent effects.',
     high='Cassia, the common cinnamon in North America, also contains coumarin, which can harm the liver in large amounts; EFSA set a tolerable intake of 0.1 mg per kg of body weight a day. Ceylon cinnamon has very little. Inhaling dry ground cinnamon can damage the lungs.',
     found='Cinnamon (cassia and Ceylon), cinnamon gum and candy, baked goods, colas, chai.'))
 +molbox('men','Menthol',[MF('menthol','Menthol: a ring of six carbons with an OH, a methyl group and an isopropyl group; every hydrogen shown',[('oh','4',A,A)],'Menthol, C10H20O')],
   [('4','A carbon ring with one OH. Menthol switches on TRPM8, the receptor that senses cold, so mint feels cool at room temperature.','')],
   fx=facts(what='The cooling compound of peppermint and corn mint.',
     body='Enteric-coated peppermint oil can ease symptoms of irritable bowel syndrome in some studies. Menthol is also used in cough drops and rubs for its cool feeling.',
     high='Concentrated peppermint oil can worsen heartburn and is toxic if swallowed in large amounts; it should not be put on the faces of young children.',
     found='Peppermint, mint tea, gum, candy, toothpaste, cough drops. Spearmint gets its flavor mainly from a different molecule, carvone.'))
 +molbox('lim','Limonene',[MF('limonene','Limonene: a ring of six carbons with one double bond and a methyl group, joined to a three-carbon group with a double bond; every hydrogen shown',[('ring','5',A,A)],'Limonene, C10H16')],
   [('5','Ten carbons and only hydrogens: a terpene, built from two isoprene units (see Bioactives, Figure 4). Its mirror-image twins smell different: one of oranges, one more of pine.','')],
   fx=facts(what='The main compound of citrus peel oil, released when you peel or zest an orange.',
     body='Food amounts are safe and it is generally recognized as safe by the US FDA. It is also widely used in cleaners and fragrances.',
     high='Concentrated limonene can irritate skin, and it reacts with ozone in indoor air to form other compounds.',
     found='Orange, lemon, lime and grapefruit peel and zest, marmalade, citrus sodas and candies, dill, caraway.'))
 +legend('c h o'))
P7=('<!--noart-->'+molbox('nat','Same molecule, different label',[
   '<div class="mgrid">'+mcell(MF('ferulic','Ferulic acid: a benzene ring with methoxy and OH groups and a three-carbon chain ending in a carboxylic acid; every hydrogen shown',[('chain','1',A,A)],'Ferulic acid, C10H10O4',eager=True),'Ferulic acid','C₁₀H₁₀O₄ · from rice bran')
   +mcell(MF('guaiacol','Guaiacol: a benzene ring with an OH and a methoxy group; every hydrogen shown',[('oh','2',A,A)],'Guaiacol, C7H8O2'),'Guaiacol','C₇H₈O₂ · from petroleum')
   +mcell(MF('ethylvanillin','Ethyl vanillin: vanillin with an ethyl group in place of the methyl on its oxygen; every hydrogen shown',[('et','3',A,A)],'Ethyl vanillin, C9H10O3'),'Ethyl vanillin','C₉H₁₀O₃ · made only by chemists')+'</div>'],
   [('1','Microbes can trim ferulic acid’s three-carbon chain down to vanillin’s aldehyde. Because it starts from a plant and uses fermentation, the result can be called natural.',''),('2','Most vanillin is built from guaiacol made from petroleum. The vanillin is identical, molecule for molecule, but it must be called artificial.',''),('3','Ethyl vanillin has one extra carbon, does not occur in vanilla, and tastes two to four times stronger. It is always an artificial flavor.','')],
   fx=facts(what='In US rules (21 CFR 101.22), a natural flavor is one whose flavor compounds come from a plant or animal source, such as a spice, fruit, vegetable, meat or fermentation; an artificial flavor is any flavoring substance not from those sources. EU rules (Regulation 1334/2008) draw a similar line.',
     body='Natural and artificial versions of the same molecule act the same in the body. “Natural” describes the source, not the nutrition or the safety; both kinds are used in tiny amounts and are reviewed for safety, in the US often through an industry expert panel (FEMA GRAS) and in the EU by EFSA.',
     high='A “natural flavor” can be a complex mixture of dozens of compounds plus solvents and carriers, and the recipe does not have to be disclosed, although major allergens must be.',
     found='Natural or artificial flavors are in most packaged drinks, snacks, cereals, yogurts, candy and sauces.'),head='Natural vs artificial')
 +legend('c h o'))
P8=('<!--noart-->'+table('lines',['Label line','What it means'],[
   ['Natural flavor(s)','flavor compounds from a plant, animal or fermentation source; may be one compound or a blend'],
   ['Artificial flavor(s)','flavor compounds made by chemical synthesis; must be stated, and the front label must say “artificially flavored” when it supplies the main flavor'],
   ['Natural and artificial flavors','a mix of both'],
   ['Vanilla extract','by US standard, vanilla beans extracted in at least 35% alcohol at a set strength'],
   ['Vanillin','artificial unless stated as natural; ethyl vanillin is always artificial'],
   ['Spices','may be listed as a group without naming each one; paprika, turmeric and saffron add color, so they must also be declared as coloring'],
   ['Monosodium glutamate, disodium inosinate, guanylate','umami flavor enhancers; MSG must be named'],
   ['Yeast extract, hydrolyzed protein','natural sources of free glutamate; a food containing them cannot claim “No MSG”'],
   ['Smoke flavoring','filtered smoke condensate (see Processing, Figure 4)']],'Reading the flavor lines')
 +lblock('front','On the front of the pack',[('“Strawberry yogurt” vs “strawberry flavored”','A name like “strawberry yogurt” suggests the fruit is there. “Strawberry flavored” or “naturally flavored” can mean the taste comes mostly or entirely from flavorings. Check the ingredient list for the fruit itself.'),
   ('Natural vanilla in the EU','In the EU, “natural vanilla flavouring” must get at least 95% of its flavor from vanilla.')]))
P9=('<!--noart-->'+table('table',['Sense or flavoring','Molecule','Receptor','Main sources','Good to know'],[
  ['Sweet','sucrose and other sugars, sweeteners','T1R2 + T1R3','fruit, honey, added sugar','liking falls when you eat less'],
  ['Bitter','caffeine, quinine, polyphenols','about 25 TAS2Rs','coffee, greens, hops, grapefruit','strong tasters vary genetically'],
  ['Sour','hydrogen ions from acids such as citric acid','OTOP1 channel','citrus, vinegar, yogurt','acid drinks erode enamel'],
  ['Salty','sodium ions','ENaC and others','salt, processed food','Daily Value 2,300 mg sodium'],
  ['Umami','glutamate, inosinate, guanylate','T1R1 + T1R3','cheese, tomato, soy sauce, broth','MSG has a third of salt’s sodium'],
  ['Aroma','vanillin, cinnamaldehyde, menthol, limonene','about 400 smell receptors','vanilla, cinnamon, mint, citrus','most of what we call flavor'],
  ['Flavor labels','natural or artificial versions of aroma molecules','—','most packaged food','“natural” is about the source, not safety']],'Flavor at a glance')
 +worth([('Losing smell','Colds, COVID-19, head injuries, some medicines and aging can dull smell, which makes food seem tasteless even though taste itself works. People with smell loss often add more salt and sugar; herbs, spices, acidity and texture can help instead.'),
   ('Kokumi','Some researchers propose a sixth sensation, kokumi, a richness and mouthfulness from certain small peptides sensed by the calcium-sensing receptor. Fat taste is another candidate under study.'),
   ('Sensory-specific satiety','The pleasure of one flavor fades as you eat it, while a new flavor still appeals, which is one reason there is always room for dessert, and why very varied buffets lead people to eat more.')],
   note='General education, not medical advice. Facts follow mainstream sources (US FDA, EFSA and EU regulations, NIH, standard food-science and sensory-science texts).'))
FL_LESSON=[('The Flavorings Family Tree','Flavor is taste plus smell: five tastes, many aromas, and the label lines.',P1),
 ('How Flavor Works','The five basic tastes, their receptors, and why smell does most of the work.',P2),
 ('Sweet and Bitter','One receptor for sweet, about 25 for bitter.',P3),
 ('Sour and Salty','Tastes made by ions: hydrogen and sodium.',P4),
 ('Umami and Glutamate','The savory taste, and the facts about MSG.',P5),
 ('Four Aroma Molecules','Vanillin, cinnamaldehyde, menthol and limonene.',P6),
 ('Natural vs Artificial Flavors','Identical molecules from different sources, and what the words mean.',P7),
 ('Reading Flavor Lines on a Label','What each flavor-related ingredient line tells you.',P8),
 ('Putting It All Together','The whole lesson in one table, plus a few extras.',P9)]
FL_QUIZ=[('Which two senses make up most of what we call flavor?','Taste on the tongue and smell in the nose (Figure 1).'),
 ('Name the five basic tastes.','Sweet, sour, salty, bitter and umami (Figure 2).'),
 ('Is the tongue map, with sweet at the tip and bitter at the back, correct?','No; every area with taste buds senses all five tastes (Figure 2).'),
 ('How many receptors sense sweet, and how many sense bitter?','One sweet receptor (T1R2 + T1R3) and about 25 bitter receptors (Figure 3).'),
 ('Why do some people find broccoli and grapefruit very bitter?','They carry a receptor variant (TAS2R38) that makes them strong bitter tasters (Figure 3).'),
 ('What do sour cells actually detect?','Hydrogen ions released by acids, entering through the OTOP1 channel (Figure 4).'),
 ('Why do potassium chloride salt substitutes taste bitter?','Potassium does not fit the sodium channel well and also activates bitter cells (Figure 4).'),
 ('What molecule causes umami taste, and what boosts it?','Free glutamate; inosinate and guanylate boost it strongly (Figure 5).'),
 ('How does the sodium in MSG compare with table salt?','MSG has about a third as much sodium (Figure 5).'),
 ('Which receptor does menthol switch on, and what does it normally sense?','TRPM8, the cold receptor (Figure 6).'),
 ('Can the same vanillin molecule be natural or artificial?','Yes; the label depends on the source: from a plant via fermentation it can be natural, from petroleum guaiacol it is artificial (Figure 7).'),
 ('Can a food containing yeast extract claim “No MSG”?','No; yeast extract is a natural source of free glutamate (Figure 8).')]
build_lesson('flavorings','Flavorings','Flavor is taste plus smell. This lesson covers the five basic tastes and the receptors that sense them, the umami molecules glutamate and inosinate, four common aroma molecules (vanillin, cinnamaldehyde, menthol and limonene), and what natural and artificial flavor mean on a label. Each molecule is shown in ball-and-stick form with what it does, the cautions, and where it is found. The figure is on the left and the lesson script on the right; the quiz is at the end.',FL_LESSON,FL_QUIZ,mols=MF,scale=11)
