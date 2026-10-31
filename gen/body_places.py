# "Everywhere else in the body": for each Nutrition 101 body-uses figure (Modules 1-3), every place outside the cell where the lesson's
# items are found or used, and what they do there. Pure data, read by gen/cell_panel.py (places_list). Grouped by item.
# PLACES[slug] = [(item, [(place, function), ...]), ...]
PLACES={}
PLACES['macronutrients-fats']=[
 ('Stored fat (triglycerides)',[
  ('Fat under the skin','The main energy store, packed into fat cells; it also insulates and cushions.'),
  ('Fat around the organs','Around the gut (omentum and mesentery) and the kidneys: a smaller store that cushions them; a lot of it is linked to heart disease and type 2 diabetes.'),
  ('Fat pads','In the heels, soles, palms and behind the eyes: cushions that take pressure.'),
  ('Brown fat','In the neck, upper back and along the spine: burns fat to make heat, more active in the cold.'),
  ('Yellow bone marrow','Fills the hollow of the long bones in adults: a fat store.'),
  ('Breasts','Mostly fat tissue around the milk glands.'),
  ('Around the heart','A layer of fat on the heart surface that it can use as fuel.'),
  ('Liver','Packs fat into VLDL to send out; if it keeps too much, that is fatty liver.'),
  ('Muscle','Keeps small fat droplets inside its fibers, ready to burn.')]),
 ('Digesting and carrying fat',[
  ('Mouth and stomach','Lipases from the tongue and the stomach start splitting a little fat.'),
  ('Liver and gallbladder','The liver makes bile and the gallbladder stores it; bile breaks fat into tiny droplets.'),
  ('Pancreas','Sends lipase into the small intestine, which does most of the splitting.'),
  ('Small intestine','Absorbs fatty acids and rebuilds them into triglycerides packed in chylomicrons.'),
  ('Lymph','Chylomicrons travel in the lymph first, then join the blood near the neck.'),
  ('Blood','Carries fat in chylomicrons after meals, in VLDL from the liver, and as fatty acids on albumin.'),
  ('Breast milk','About half its energy comes from fat.')]),
 ('Fatty acids as fuel',[
  ('Heart','Gets most of its energy from burning fatty acids.'),
  ('Skeletal muscle','Burns fat at rest and in long, easy exercise.'),
  ('Kidneys','Their outer layer runs mostly on fatty acids.'),
  ('Liver','Burns fatty acids and, in a long fast, turns them into ketones.'),
  ('Brain','Cannot burn fatty acids, but uses the ketones the liver makes from them in a long fast.')]),
 ('Omega-3 and omega-6 fats',[
  ('Brain','DHA, an omega-3, is concentrated in the membranes of nerve cells.'),
  ('Retina','DHA makes up a large share of the fats in the light-sensing cells.'),
  ('Sperm','DHA in their membranes.'),
  ('Skin','Linoleic acid, an omega-6, is built into the lipids that seal its water barrier.'),
  ('Placenta and breast milk','Pass DHA and arachidonic acid to the baby.')]),
 ('Nerve myelin',[
  ('Brain white matter, spinal cord and nerves','Myelin, the fatty wrapping that speeds nerve signals, is about three quarters lipid by dry weight.')]),
 ('Eicosanoids (signals made from fatty acids)',[
  ('Stomach lining','Prostaglandins protect it, which is why aspirin and ibuprofen can irritate it.'),
  ('Platelets','Make thromboxane to start a blood clot.'),
  ('Blood vessel walls','Make prostacyclin, which relaxes vessels and stops clots.'),
  ('Uterus','Prostaglandins trigger contractions in labor and period cramps.'),
  ('Injured tissue and immune cells','Prostaglandins and leukotrienes drive inflammation, swelling and pain.'),
  ('Brain','A prostaglandin raises the body temperature set point in a fever.'),
  ('Airways','Leukotrienes narrow them in asthma.'),
  ('Kidneys','Prostaglandins help keep their blood flow up.')]),
]
PLACES['macronutrients-lipids']=[
 ('Phospholipids',[
  ('Lungs','Surfactant, mostly a phospholipid film, coats the air sacs so they do not collapse when you breathe out.'),
  ('Blood','Form the outer coat of every lipoprotein (chylomicrons, VLDL, LDL, HDL).'),
  ('Bile','Lecithin keeps cholesterol dissolved; too little helps gallstones form.'),
  ('Liver','Makes most of the phospholipids for lipoproteins and bile.'),
  ('Joints','Phospholipids in the joint fluid help the cartilage surfaces slide.'),
  ('Platelets','Turn a phospholipid (phosphatidylserine) to their outer surface to speed clotting.')]),
 ('Cholesterol',[
  ('Liver','Makes most of your cholesterol, sends it out in VLDL and takes it back from LDL and HDL.'),
  ('Small intestine','Absorbs cholesterol from food and bile, and makes some of its own.'),
  ('Blood','LDL carries cholesterol out to the tissues; HDL brings extra back to the liver.'),
  ('Artery walls','LDL that builds up there starts the plaque of atherosclerosis.'),
  ('Brain','Makes its own; it holds about a quarter of the body\u2019s cholesterol, much of it in myelin.'),
  ('Skin','Part of the barrier lipids; a close relative, 7-dehydrocholesterol, is turned into vitamin D by sunlight.'),
  ('Gallbladder','Most gallstones are made of cholesterol.')]),
 ('Steroid hormones (made from cholesterol)',[
  ('Adrenal glands','Make cortisol (stress and blood sugar), aldosterone (salt and blood pressure) and some androgens.'),
  ('Testes','Make testosterone.'),
  ('Ovaries','Make estrogen and progesterone.'),
  ('Placenta','Makes progesterone and estrogens in pregnancy.'),
  ('Fat tissue','Turns some androgens into estrogen.'),
  ('Brain','Makes small amounts of its own steroids that act on nerve cells.')]),
 ('Bile acids (made from cholesterol)',[
  ('Liver','Turns cholesterol into bile acids, its main way of getting rid of cholesterol.'),
  ('Gallbladder','Stores and concentrates bile between meals.'),
  ('Small intestine','Bile acids break fat into tiny droplets; at the far end, about 95% are absorbed and go back to the liver.'),
  ('Large intestine','Bacteria change the rest into secondary bile acids, and some leave in stool.')]),
 ('Vitamin D (from a cholesterol relative)',[
  ('Skin','Makes it in sunlight.'),
  ('Liver and kidneys','Turn it into its active hormone, which helps absorb calcium.')]),
 ('Sphingolipids',[
  ('Nerve myelin','Rich in sphingomyelin and galactocerebroside.'),
  ('Skin','Ceramides in the outer layer seal its water barrier.'),
  ('Brain','Gangliosides on the surface of nerve cells.'),
  ('Red blood cells','The A, B and O blood groups are sugar chains carried partly on sphingolipids.'),
  ('Blood','Sphingosine-1-phosphate signals tell immune cells when to leave the lymph nodes.')]),
 ('Eicosanoids',[
  ('Platelets','Thromboxane starts a clot.'),
  ('Stomach lining, uterus, kidneys and injured tissue','Prostaglandins protect, contract, keep blood flow and drive inflammation.')]),
 ('Waxes',[
  ('Skin and hair','Sebum from the oil glands contains wax esters that keep them supple.'),
  ('Ear canal','Earwax traps dust and protects the canal.')]),
]
PLACES['macronutrients-carbohydrates']=[
 ('Digesting carbohydrates',[
  ('Mouth','Saliva amylase starts breaking starch down as you chew.'),
  ('Pancreas','Sends amylase into the small intestine.'),
  ('Small intestine','Its lining finishes the job (maltase, sucrase, lactase) and absorbs glucose, fructose and galactose.')]),
 ('Glucose',[
  ('Blood','Carries only about a teaspoon (4 to 5 grams) at a time, kept in range day and night.'),
  ('Brain','Burns about 120 grams a day, its main fuel.'),
  ('Red blood cells','Have no mitochondria, so glucose is the only fuel they can use.'),
  ('Retina, lens and kidney medulla','Also depend heavily on glucose.'),
  ('Muscle','Takes glucose up with insulin and burns it fast in hard exercise.'),
  ('Fat tissue','Takes glucose up with insulin and turns extra into fat.'),
  ('Pancreas','Beta cells release insulin when blood sugar rises; alpha cells release glucagon when it falls.'),
  ('Liver','Takes glucose in after meals and releases it between them; in a fast it makes new glucose.'),
  ('Kidneys','Take back all filtered glucose until blood sugar is very high (about 180 mg/dL), then it spills into urine; they also make glucose in a fast.'),
  ('Placenta','Glucose is the main fuel passed to the growing baby.')]),
 ('Glycogen (stored glucose)',[
  ('Liver','About 100 grams, broken down to keep blood sugar steady between meals.'),
  ('Muscle','About 400 grams in total, kept for its own use in exercise.'),
  ('Kidneys and brain','Small amounts.')]),
 ('Fructose and galactose',[
  ('Liver','Handles most fructose and galactose, turning them into glucose, glycogen or fat.'),
  ('Seminal vesicles','Put fructose in semen as fuel for sperm.'),
  ('Breasts','Make lactose (glucose + galactose) for milk.'),
  ('Brain and nerves','Galactose is built into the lipids of myelin.')]),
 ('Fiber',[
  ('Small intestine','Soluble fiber slows sugar absorption and binds bile acids, which lowers LDL cholesterol a little.'),
  ('Large intestine','Bacteria ferment fiber into short-chain fatty acids; butyrate feeds the cells of the colon wall; gas is a by-product.'),
  ('Stool','Insoluble fiber adds bulk and keeps it moving.')]),
 ('Sugar chains on proteins and in tissues',[
  ('Joint cartilage','Long sugar chains (chondroitin, keratan sulfate) hold water so cartilage can take pressure.'),
  ('Joint fluid, eyes and skin','Hyaluronic acid makes joint fluid slippery, fills the eye\u2019s vitreous gel and holds water in the skin.'),
  ('Mucus (gut, airways)','Mucins, proteins heavy with sugar chains, make mucus slippery and protective.'),
  ('Red blood cells','The A, B and O blood groups are sugar chains on their surface.'),
  ('Kidneys','Sugar chains in the filter help hold proteins back in the blood.')]),
 ('Sugar and the teeth',[
  ('Teeth','Mouth bacteria ferment sugar into acid that dissolves enamel and causes cavities.')]),
]
PLACES['macronutrients-water-ethanol']=[
 ('Water: where it is',[
  ('Inside cells','About two thirds of body water.'),
  ('Between cells','The fluid that bathes every cell and carries nutrients to it.'),
  ('Blood plasma','About 90% water; carries nutrients, heat, hormones and wastes.'),
  ('Muscle and brain','About three quarters water.'),
  ('Fat tissue and bone','Low in water, so lean people hold a larger share of body water.'),
  ('Eyes','The fluid and gel inside the eye are almost all water.'),
  ('Brain and spinal cord','Cerebrospinal fluid cushions them.'),
  ('Joints','A watery fluid lubricates them.'),
  ('Saliva, tears and mucus','Wet the mouth, eyes and airways.'),
  ('Womb','Amniotic fluid cushions the baby.'),
  ('Breast milk','About 87% water.')]),
 ('Water: keeping the balance',[
  ('Brain (hypothalamus)','Senses salty blood, makes you thirsty and triggers ADH.'),
  ('Pituitary gland','Releases ADH, which tells the kidneys to keep water.'),
  ('Kidneys','Filter about 180 liters a day and return nearly all of it, keeping 1 to 2 liters as urine.'),
  ('Adrenal glands','Aldosterone makes the kidneys keep salt, and water follows.'),
  ('Heart','Releases ANP when overfilled, so the kidneys let out more salt and water.'),
  ('Skin','Sweat cools you by evaporating.'),
  ('Lungs','Breath carries out a few hundred milliliters a day.'),
  ('Small intestine','Absorbs most of the water you drink and the gut\u2019s own juices.'),
  ('Large intestine','Takes back most of what is left.')]),
 ('Ethanol',[
  ('Stomach','Absorbs about a fifth; its own enzyme breaks a little down; food slows it.'),
  ('Small intestine','Absorbs most of it.'),
  ('Blood','Spreads it through all body water.'),
  ('Liver','Breaks most of it down, to acetaldehyde and then acetate, at about one drink an hour; heavy drinking causes fatty liver, hepatitis and cirrhosis.'),
  ('Brain','Boosts the calming signal GABA and blocks glutamate, so nerve signals slow; the cerebellum\u2019s balance goes first.'),
  ('Pituitary gland','Alcohol blocks ADH, so you pass more urine.'),
  ('Skin','Blood vessels widen: flushing and heat loss.'),
  ('Lungs','A little leaves in the breath, which is what a breath test measures.'),
  ('Kidneys and sweat','A little leaves unchanged.'),
  ('Pancreas and heart','Heavy drinking can inflame the pancreas and weaken the heart muscle.'),
  ('Placenta and breast milk','Alcohol crosses to the baby; in pregnancy it can cause fetal alcohol spectrum disorders.')]),
]
PLACES['micronutrients-fat-soluble-vitamins']=[
 ('Absorbing them',[
  ('Small intestine','Absorbs A, D, E and K with fat, packed into chylomicrons.'),
  ('Lymph','Chylomicrons carry them through the lymph before they reach the blood.')]),
 ('Vitamin A',[
  ('Retina','Becomes retinal, the light-catching part of rhodopsin and the cone pigments; a shortage causes night blindness first.'),
  ('Eye surface','Keeps the cornea moist and healthy; a severe shortage can scar it and cause blindness.'),
  ('Liver','Stores most of it, in its stellate cells.'),
  ('Blood','Carried on retinol-binding protein.'),
  ('Skin and linings','Keeps the skin and the linings of the gut, lungs and urinary tract renewing.'),
  ('Immune system','Needed for immune cells, especially in the gut.'),
  ('Bones','Needed for growth; too much raises fracture risk.'),
  ('Embryo','Guides how the body is laid out; too much in pregnancy causes birth defects.'),
  ('Testes and ovaries','Needed to make sperm and for reproduction.')]),
 ('Vitamin D',[
  ('Skin','Makes it in UVB sunlight.'),
  ('Liver','Turns it into 25-hydroxyvitamin D, the form measured in a blood test.'),
  ('Kidneys','Turn that into calcitriol, the active hormone.'),
  ('Small intestine','Calcitriol makes it absorb calcium and phosphate.'),
  ('Bones','Need it to harden; in a shortage, bones soften (rickets in children).'),
  ('Parathyroid glands','Calcitriol tones down their hormone, PTH.'),
  ('Fat tissue','Stores it.'),
  ('Immune cells and muscle','Have vitamin D receptors; immune cells make some of their own calcitriol.')]),
 ('Vitamin E',[
  ('Fat tissue','Holds most of the store.'),
  ('Liver','Picks out alpha-tocopherol and sends it out in VLDL; other forms are cleared.'),
  ('Blood','Carried in lipoproteins, where it protects LDL from oxidation.'),
  ('Nerves','A long shortage damages nerves and balance.'),
  ('Red blood cells','Protects their membranes from bursting.'),
  ('Adrenal glands, pituitary and testes','Hold high levels.')]),
 ('Vitamin K',[
  ('Liver','Makes clotting factors II, VII, IX and X, and proteins C and S.'),
  ('Blood','Clots properly only with enough vitamin K; warfarin works by blocking it.'),
  ('Bones','Activates osteocalcin, a bone protein that binds calcium.'),
  ('Artery walls','Activates a protein (matrix Gla protein) that keeps calcium out of them.'),
  ('Large intestine','Bacteria make vitamin K2.'),
  ('Newborns','Born with little, so they get a vitamin K shot at birth.')]),
]
PLACES['micronutrients-water-soluble-vitamins']=[
 ('Absorbing and clearing them',[
  ('Small intestine','Absorbs most B vitamins and vitamin C through their own carriers.'),
  ('Blood','Carries them to every tissue.'),
  ('Kidneys','Send extra out in urine; riboflavin turns it bright yellow.')]),
 ('Thiamin (B1)',[
  ('Brain and nerves','Need it to burn glucose; a shortage causes beriberi and, in heavy drinkers, Wernicke-Korsakoff syndrome.'),
  ('Heart','A shortage can cause heart failure (wet beriberi).'),
  ('Muscle','Holds about half the body\u2019s thiamin.')]),
 ('Riboflavin (B2) and niacin (B3)',[
  ('Mouth and skin','A riboflavin shortage cracks the corners of the mouth and makes the tongue sore.'),
  ('Skin, gut and brain','A niacin shortage causes pellagra: rash on sun-exposed skin, diarrhea and confusion.'),
  ('Liver','Makes some niacin from the amino acid tryptophan.'),
  ('Skin blood vessels','High-dose niacin widens them: a hot flush.')]),
 ('Pantothenic acid (B5) and biotin (B7)',[
  ('Every tissue','Pantothenic acid is part of coenzyme A, used to burn and build fats.'),
  ('Liver','Biotin enzymes help make glucose and fatty acids.'),
  ('Skin and hair','A biotin shortage causes rash and hair loss.'),
  ('Large intestine','Bacteria make some biotin.')]),
 ('Vitamin B6',[
  ('Brain','Needed to make serotonin, dopamine and GABA.'),
  ('Bone marrow','Needed to make heme for new red blood cells.'),
  ('Liver','Needed to process amino acids.'),
  ('Muscle','Holds most of the body\u2019s B6, in its glycogen enzyme.'),
  ('Nerves','Very high supplement doses can damage them.')]),
 ('Folate',[
  ('Bone marrow','Needed to make new red blood cells; a shortage causes large, immature red cells (megaloblastic anemia).'),
  ('Embryo','Early in pregnancy it helps the neural tube close, preventing spina bifida.'),
  ('Gut lining','Its fast-renewing cells need folate to copy DNA.'),
  ('Liver','Stores some.'),
  ('Blood','With B12 and B6 it keeps homocysteine low.')]),
 ('Vitamin B12',[
  ('Stomach','Acid frees B12 from food, and the stomach lining makes intrinsic factor, which B12 needs to be absorbed.'),
  ('Small intestine (ileum)','Absorbs B12 bound to intrinsic factor at its far end.'),
  ('Liver','Stores a few years\u2019 supply.'),
  ('Bone marrow','Needed to make red blood cells.'),
  ('Nerves and spinal cord','Needed to keep myelin healthy; a shortage causes numbness and memory problems.'),
  ('Large intestine','Bacteria make B12, but too far down to be absorbed.')]),
 ('Vitamin C',[
  ('Skin, gums, blood vessels, tendons, bone and scars','Needed to make collagen; a shortage (scurvy) causes bleeding gums, bruising and poor wound healing.'),
  ('Adrenal glands','Hold some of the highest levels; needed to make noradrenaline.'),
  ('Brain','Also high; used to make noradrenaline.'),
  ('Eyes','High in the lens and the fluid in front of it.'),
  ('White blood cells','Concentrate it.'),
  ('Small intestine','Helps absorb iron from plant foods.'),
  ('Muscle','Needed to make carnitine, which carries fat into mitochondria.'),
  ('Kidneys','Remove extra; very high doses can raise the risk of oxalate kidney stones.')]),
 ('Choline',[
  ('Brain and nerves','Make acetylcholine, the messenger for memory and muscle control.'),
  ('Muscle','Nerves signal muscles to contract with acetylcholine.'),
  ('Liver','Makes some choline (PEMT) and needs it to send fat out as VLDL; too little causes fatty liver.'),
  ('Every cell membrane','Phosphatidylcholine and sphingomyelin.')])
]
PLACES['micronutrients-major-minerals']=[
 ('Calcium',[
  ('Bones and teeth','Hold about 99%, as calcium phosphate (hydroxyapatite); bone is also a bank the blood draws on.'),
  ('Blood','Kept in a narrow range; also needed for clotting.'),
  ('Parathyroid glands','Sense blood calcium and release PTH when it falls.'),
  ('Thyroid gland','Its C cells release calcitonin, which lowers it a little.'),
  ('Muscle','Triggers every contraction.'),
  ('Heart','Each beat starts with calcium flowing in.'),
  ('Nerves','Calcium lets nerve endings release their signals.'),
  ('Small intestine','Absorbs calcium with help from vitamin D.'),
  ('Kidneys','Take back most filtered calcium; calcium is part of most kidney stones.'),
  ('Breast milk','Carries calcium to the baby.')]),
 ('Phosphorus',[
  ('Bones and teeth','Hold about 85%, in calcium phosphate.'),
  ('Blood','Phosphate helps buffer acid.'),
  ('Red blood cells','A phosphate compound (2,3-BPG) helps hemoglobin let go of oxygen.'),
  ('Kidneys','Keep the level steady, guided by FGF23 from bone and PTH.')]),
 ('Magnesium',[
  ('Bones','Hold over half.'),
  ('Muscle and soft tissue','Hold most of the rest; needed for relaxing after contraction.'),
  ('Heart','Helps keep a steady rhythm.'),
  ('Nerves','Calms nerve excitability.'),
  ('Parathyroid glands','Need magnesium to release PTH.'),
  ('Kidneys','Keep the blood level steady.')]),
 ('Sodium',[
  ('Blood and the fluid between cells','The main positive ion outside cells: holds water there and sets blood volume and pressure.'),
  ('Nerves and muscle','Sodium rushing in starts every nerve signal and muscle contraction.'),
  ('Kidneys','Adjust how much they keep, guided by aldosterone from the adrenal glands.'),
  ('Small intestine','Sodium and glucose are absorbed together, which is how oral rehydration solution works.'),
  ('Bone','Holds a store of sodium.'),
  ('Skin','Sweat carries sodium out.')]),
 ('Potassium',[
  ('Muscle','Holds most of the body\u2019s potassium.'),
  ('Heart','Both too little and too much in the blood disturb its rhythm.'),
  ('Nerves','Potassium flowing out resets each signal.'),
  ('Kidneys','Send extra out; aldosterone speeds this.'),
  ('Blood','Kept in a narrow range; only about 2% of body potassium is outside cells.')]),
 ('Chloride',[
  ('Stomach','Its lining makes hydrochloric acid.'),
  ('Blood','The main negative ion outside cells.'),
  ('Red blood cells','Swap chloride for bicarbonate to help carry carbon dioxide.'),
  ('Airways and gut','Chloride channels keep mucus watery; when they fail, mucus thickens (cystic fibrosis).'),
  ('Skin','Sweat carries chloride out with sodium.')]),
 ('Sulfur',[
  ('Hair, nails and outer skin','Keratin is held together by sulfur bridges.'),
  ('Cartilage','Chondroitin sulfate holds water.'),
  ('Liver','Uses sulfur in glutathione and to tag drugs and wastes for removal.'),
  ('Bile','Taurine, a sulfur compound, is joined to bile acids.'),
  ('Pancreas','Insulin is held in shape by sulfur bridges.')]),
]
PLACES['micronutrients-trace-minerals']=[
 ('Iron',[
  ('Red blood cells','About two thirds of body iron, in hemoglobin, which carries oxygen.'),
  ('Muscle','Myoglobin, another iron protein, holds oxygen.'),
  ('Bone marrow','Builds iron into new red blood cells.'),
  ('Spleen','Recycles iron from old red cells.'),
  ('Liver','Stores iron as ferritin and makes hepcidin, the hormone that sets how much is absorbed.'),
  ('Small intestine (duodenum)','Absorbs iron; heme iron from meat best.'),
  ('Blood','Transferrin carries iron between tissues.'),
  ('Brain','Needed for myelin and to make dopamine.'),
  ('Placenta','Passes iron to the baby; needs rise in pregnancy.'),
  ('Uterus','Periods lose iron each month.')]),
 ('Zinc',[
  ('Muscle and bone','Hold most of the body\u2019s zinc.'),
  ('Skin','Needed for wound healing.'),
  ('Immune system','Needed for immune cells, including in the thymus.'),
  ('Eyes','High levels in the retina.'),
  ('Prostate and semen','Some of the highest levels.'),
  ('Pancreas','Insulin is stored packed with zinc.'),
  ('Tongue and nose','A shortage dulls taste and smell.'),
  ('Small intestine','Absorbs zinc; phytate in grains and beans reduces it.')]),
 ('Copper',[
  ('Liver','Stores copper, makes ceruloplasmin and sends extra out in bile.'),
  ('Blood','Ceruloplasmin helps load iron onto transferrin.'),
  ('Brain','Needed to make noradrenaline and for myelin.'),
  ('Skin and hair','Needed to make melanin, the pigment.'),
  ('Blood vessels, skin and bone','A copper enzyme links collagen and elastin fibers.')]),
 ('Selenium',[
  ('Thyroid','Holds the most per gram; selenium enzymes switch thyroid hormone on and off.'),
  ('Muscle','Holds the largest share of the total.'),
  ('Testes and sperm','Needed for healthy sperm.'),
  ('Blood','Selenoprotein P carries it to tissues.'),
  ('Immune system','Needed for immune cells.')]),
 ('Iodine',[
  ('Thyroid','Holds most of the body\u2019s iodine and builds it into the hormones T4 and T3, which set how fast you use energy.'),
  ('Fetal brain','Needs the mother\u2019s thyroid hormone, so iodine matters in pregnancy.'),
  ('Breasts, salivary glands and stomach','Also take iodide up; breast milk passes it to the baby.'),
  ('Kidneys','Send most iodine out in urine.')]),
 ('Fluoride',[
  ('Teeth','Turns enamel into harder, acid-resistant fluorapatite; saliva fluoride helps repair it.'),
  ('Bones','Hold nearly all body fluoride; too much over years causes skeletal fluorosis.')]),
 ('Manganese, chromium and molybdenum',[
  ('Bone','Manganese helps build bone and cartilage.'),
  ('Liver, kidneys and pancreas','Hold the most manganese.'),
  ('Brain','Too much manganese, usually breathed in at work, damages it.'),
  ('Blood','Chromium may help insulin work; the evidence is weak.'),
  ('Liver and kidneys','Molybdenum enzymes break down sulfites and make uric acid.')]),
]
PLACES['additives']=[
 ('Sweeteners',[
  ('Tongue','Fit the sweet receptor; many are hundreds of times sweeter than sugar.'),
  ('Small intestine','Aspartame is digested to phenylalanine, aspartic acid and a little methanol, which is why labels warn people with PKU.'),
  ('Large intestine','Sucralose mostly passes through; bacteria strip stevia\u2019s sugars off before it is absorbed.'),
  ('Liver','Clears absorbed steviol.'),
  ('Kidneys','Sucralose, acesulfame K and saccharin that are absorbed leave mostly unchanged in urine.')]),
 ('Sugar alcohols',[
  ('Teeth','Mouth bacteria can\u2019t ferment them well, so they don\u2019t cause cavities.'),
  ('Small intestine','Absorbed only partly.'),
  ('Large intestine','Bacteria ferment the rest: gas, and loose stools in large amounts.'),
  ('Kidneys','Erythritol is mostly absorbed and leaves in urine.')]),
 ('MSG and flavor enhancers',[
  ('Tongue','Glutamate fits the umami receptor.'),
  ('Small intestine','Its cells burn most of the glutamate you eat as their own fuel.')]),
 ('Preservatives',[
  ('Stomach','Nitrite can react with amines to form nitrosamines, which is why vitamin C is added to cured meat.'),
  ('Blood','Very large amounts of nitrite turn hemoglobin into a form that can\u2019t carry oxygen; babies are most at risk.'),
  ('Liver','Joins benzoate to glycine; sorbate and propionate are burned like fats.'),
  ('Kidneys','Pass the benzoate product (hippuric acid) out in urine.'),
  ('Airways','Sulfites can trigger asthma in sensitive people.')]),
 ('Acids and antioxidants',[
  ('Teeth','Citric and phosphoric acid in drinks can wear enamel.'),
  ('Stomach','Food acids simply add to stomach acid.'),
  ('Every tissue','Ascorbic acid and tocopherols work as vitamins C and E.')]),
 ('Colors',[
  ('Small intestine','Many synthetic colors are poorly absorbed.'),
  ('Large intestine','Bacteria split azo dyes into smaller parts.'),
  ('Liver','Clears absorbed colors into bile or urine.'),
  ('Brain and behavior','A UK study linked some colors to more hyperactivity in some children, so the EU requires a warning.')]),
 ('Thickeners and emulsifiers',[
  ('Large intestine','Gums are fermented by bacteria, like fiber.'),
  ('Gut lining','In mice, the emulsifiers carboxymethylcellulose and polysorbate 80 thinned the mucus layer; human evidence is early.')]),
 ('Phosphates and minerals',[
  ('Small intestine','Absorbs phosphate additives more fully than the phosphorus in whole foods.'),
  ('Kidneys','Clear the extra; people with kidney disease are told to limit them.'),
  ('Bones','Phosphorus is balanced with calcium in bone.'),
  ('Gut immune patches','Some tiny titanium dioxide particles are taken up there; most pass through.')]),
]
PLACES['antinutrients']=[
 ('Phytate',[
  ('Small intestine','Binds iron, zinc, calcium and magnesium so less is absorbed.'),
  ('Large intestine','Bacteria break some down.'),
  ('Kidneys','The little that is absorbed may help prevent calcium kidney stones.')]),
 ('Oxalate',[
  ('Small intestine','Binds calcium in the meal.'),
  ('Large intestine','Some bacteria break oxalate down.'),
  ('Kidneys','Absorbed oxalate leaves in urine, where it can join calcium in kidney stones, the most common kind.')]),
 ('Tannins',[
  ('Mouth','Bind saliva proteins: the dry, puckering feel of strong tea or red wine.'),
  ('Small intestine','Bind iron from plant foods, proteins and digestive enzymes.'),
  ('Large intestine','Bacteria break them into smaller compounds.')]),
 ('Lectins',[
  ('Small intestine','Raw kidney-bean lectin binds the gut lining and causes vomiting and diarrhea; cooking destroys it.'),
  ('Blood','Some lectins clump red blood cells in the lab, which gave them their name (agglutinins).')]),
 ('Trypsin inhibitors',[
  ('Small intestine','Block trypsin and chymotrypsin, so protein is digested less.'),
  ('Pancreas','In animals fed raw soy, the pancreas works harder and grows.')]),
 ('Goitrogens',[
  ('Thyroid','Thiocyanate blocks iodine uptake and goitrin blocks hormone making, mainly a problem when iodine is low.')]),
 ('Cyanogenic glycosides',[
  ('Gut','Release cyanide from raw cassava, bitter almonds and apricot kernels.'),
  ('Liver','Turns cyanide into thiocyanate.'),
  ('Thyroid','That thiocyanate competes with iodine.'),
  ('Nerves','Long exposure from badly processed cassava causes konzo, a paralysis of the legs.')]),
]
PLACES['processing']=[
 ('Cooking in general',[
  ('Stomach and small intestine','Cooked starch and protein are digested faster; heat also kills germs.')]),
 ('Acrylamide',[
  ('Small intestine','Absorbs it.'),
  ('Liver','Turns some into glycidamide, which can damage DNA, and clears the rest with glutathione.'),
  ('Blood','Binds hemoglobin, which is how exposure is measured.'),
  ('Nerves','High exposure at work damages nerves.'),
  ('Placenta and breast milk','Pass small amounts.')]),
 ('AGEs (browning products)',[
  ('Small intestine','Absorbs a share of those in food.'),
  ('Blood vessels','Link collagen fibers so vessels stiffen, and trigger inflammation through the RAGE receptor.'),
  ('Kidneys','Clear AGEs; they build up in kidney disease.'),
  ('Eye lens and skin','Build up with age in long-lived proteins.'),
  ('Blood','The body makes its own when sugar is high; HbA1c, the diabetes test, measures an early step of the same reaction.')]),
 ('HCAs and PAHs (charring and smoke)',[
  ('Liver','Activates them, and some products can damage DNA.'),
  ('Colon, prostate and breast','Where HCA damage has been studied in animals.'),
  ('Lungs','PAHs from smoke reach them directly.')]),
 ('Nitrite and nitrosamines',[
  ('Stomach','Nitrite and amines can form nitrosamines in its acid.'),
  ('Liver','Activates nitrosamines.'),
  ('Large intestine','Eating a lot of processed meat is linked to colon cancer.')]),
 ('Trans fats',[
  ('Blood','Raise LDL and lower HDL cholesterol.'),
  ('Artery walls and heart','Raise the risk of plaque and heart disease.')]),
 ('Fermentation and pasteurization',[
  ('Large intestine','Live cultures from yogurt and other fermented foods meet the gut bacteria.'),
  ('Small intestine','Yogurt bacteria break down part of the lactose.'),
  ('Whole body','Pasteurization kills germs such as Listeria and Salmonella.')]),
 ('Refining, fortification and nixtamalization',[
  ('Skin, gut and brain','Nixtamalized corn frees niacin, preventing pellagra.'),
  ('Bones','Lime-treated corn adds calcium.'),
  ('Bone marrow and embryo','Fortified flour adds iron for red blood cells and folic acid for the neural tube.')]),
]
PLACES['bioactives']=[
 ('Carotenoids',[
  ('Retina','Lutein and zeaxanthin collect in the macula and filter blue light.'),
  ('Eye lens and brain','Also hold lutein.'),
  ('Skin','Beta-carotene and lycopene tint it slightly.'),
  ('Fat tissue','Stores carotenoids.'),
  ('Liver','Turns beta-carotene into vitamin A.'),
  ('Blood','Carried in lipoproteins.'),
  ('Prostate, adrenal glands and testes','Concentrate lycopene.')]),
 ('Caffeine',[
  ('Brain','Blocks adenosine, the signal that builds up as you get tired.'),
  ('Heart','Can raise heart rate a little.'),
  ('Stomach','Increases acid.'),
  ('Kidneys','Mild extra urine in people not used to it.'),
  ('Liver','Clears it (CYP1A2); its half-life is about 3 to 7 hours.'),
  ('Placenta and breast milk','Pass it to the baby.')]),
 ('Capsaicin',[
  ('Mouth, skin and gut','Opens the heat-pain receptor (TRPV1): the burn of chili.'),
  ('Nerves','Repeated use dulls pain nerves, which is why it is used in pain creams.')]),
 ('Polyphenols (flavonoids and others)',[
  ('Small intestine','Absorbs only a small share.'),
  ('Large intestine','Bacteria break most into smaller molecules, which are absorbed.'),
  ('Liver','Tags them for removal.'),
  ('Blood vessels','Cocoa and tea flavanols can help vessel walls relax.'),
  ('Kidneys','Send the products out in urine.')]),
 ('Phytosterols',[
  ('Small intestine','Block some cholesterol from being absorbed; about 2 grams a day lowers LDL by roughly 6 to 12%.')]),
 ('Glucosinolates and sulforaphane',[
  ('Mouth','Chewing broccoli mixes its enzyme with glucosinolates to make sulforaphane.'),
  ('Large intestine','Bacteria make some when the vegetable is cooked.'),
  ('Liver','Sulforaphane switches on detox and antioxidant enzymes.'),
  ('Bladder','The products concentrate in urine.')]),
]
PLACES['flavorings']=[
 ('Taste molecules',[
  ('Tongue','Taste buds sense sweet, bitter, sour, salty and umami.'),
  ('Soft palate and throat','Also have taste buds.'),
  ('Gut','Has sweet and bitter receptors that help release gut hormones.'),
  ('Airways','Bitter receptors there help sweep out mucus.'),
  ('Brain','The taste area (in the insula) receives the signals.')]),
 ('Aroma molecules',[
  ('Nose','About 400 kinds of smell receptor in the roof of the nose.'),
  ('Mouth to nose','Aromas rise from the back of the mouth as you chew, which is most of flavor.'),
  ('Brain','Smell goes straight to areas for emotion and memory.')]),
 ('Feel: heat, cold, bite and fizz',[
  ('Mouth, nose and eyes','The trigeminal nerve feels chili (TRPV1), menthol\u2019s cool (TRPM8), mustard and wasabi (TRPA1) and the fizz of carbonation.'),
  ('Eyes','An onion compound reaches them and makes them water.')]),
 ('Flavor in the brain',[
  ('Brain','Combines taste, smell, texture and heat into one flavor; that\u2019s why food tastes flat with a blocked nose.')]),
 ('Digesting and clearing them',[
  ('Stomach and small intestine','Absorb flavor molecules like the rest of the food.'),
  ('Liver','Breaks most of them down; vanillin becomes vanillic acid.'),
  ('Kidneys','Send the products out in urine; asparagus gives urine its smell this way.'),
  ('Lungs and skin','Garlic compounds leave in the breath and sweat.')]),
]
PLACES['macronutrients-protein']=[
 ('Digesting protein',[
  ('Stomach','Acid unfolds proteins and pepsin starts cutting them.'),
  ('Pancreas','Sends trypsin, chymotrypsin and other enzymes into the small intestine.'),
  ('Small intestine','Its lining finishes the job and absorbs amino acids and small peptides into the blood.')]),
 ('Proteins that move you',[
  ('Skeletal muscle','Holds about 40% of body protein; actin and myosin slide past each other to contract.'),
  ('Heart','Its muscle uses the same proteins for every beat.'),
  ('Gut and blood vessel walls','Smooth muscle squeezes food along and sets vessel width.')]),
 ('Proteins that hold you together',[
  ('Skin','Collagen gives it strength and elastin lets it stretch back.'),
  ('Bones and teeth','A collagen framework holds the minerals.'),
  ('Tendons, ligaments and cartilage','Mostly collagen.'),
  ('Arteries and lungs','Elastin lets them stretch and recoil.'),
  ('Hair, nails and outer skin','Made of keratin.'),
  ('Eyes','Collagen keeps the cornea clear; crystallin proteins make the lens.')]),
 ('Proteins in the blood',[
  ('Liver','Makes albumin, which holds water in the blood and carries things, and the clotting factors such as fibrinogen.'),
  ('Red blood cells','Hemoglobin carries oxygen.'),
  ('Blood','Carrier proteins move iron, fats and hormones.')]),
 ('Defense',[
  ('Bone marrow, lymph nodes, spleen and gut lining','Plasma cells there make antibodies that tag germs.'),
  ('Skin and mucus','Protein barriers and germ-killing enzymes such as lysozyme in tears and saliva.')]),
 ('Protein hormones',[
  ('Pancreas','Insulin and glucagon.'),
  ('Pituitary gland','Growth hormone, ADH and oxytocin.'),
  ('Parathyroid glands','PTH, which raises blood calcium.'),
  ('Kidneys','EPO, which tells the marrow to make red blood cells.'),
  ('Fat tissue','Leptin, which signals how much fat is stored.'),
  ('Gut','Gastrin, CCK and other digestion signals.')]),
 ('Amino acids made into other things',[
  ('Brain','Serotonin from tryptophan, dopamine from tyrosine, and GABA and glutamate.'),
  ('Adrenal glands','Adrenaline from tyrosine.'),
  ('Thyroid','Thyroid hormones are built on tyrosine.'),
  ('Skin and hair','Melanin, the pigment, from tyrosine.'),
  ('Bone marrow','Heme is built from glycine.'),
  ('Liver, kidneys and muscle','Creatine is made in the kidneys and liver and stored in muscle for quick energy.'),
  ('Breast milk','Casein and whey proteins feed the baby.')]),
 ('Spare amino acids',[
  ('Liver','Removes their nitrogen as urea and turns the rest into glucose, fat or energy.'),
  ('Kidneys','Send urea out in urine and use glutamine to balance acid.'),
  ('Muscle','In a fast, breaks some protein down to supply amino acids.')]),
]
