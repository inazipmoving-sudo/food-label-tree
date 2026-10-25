# ---------------- Module 4 · Final Review ----------------
# Whole-site family tree, then five whole-food labels read line by line. Label numbers are TYPICAL values (USDA FoodData Central-style
# averages, rounded the way FDA labels round); they are illustrative, not any brand's label. Every molecule is reused from the lesson that teaches it.
MR=mk_lmol('final-review')
A=None
def L(slug,fig,txt=None):
    t=txt or next(r[3] for r in REG if r[0]==slug)
    return f'<a href="{slug}.html#fig-{fig}">{t}, Fig. {fig}</a>'
def nflabel(part,food,serving,cal,rows,ingred,extra=''):
    """Nutrition Facts-style label as page HTML (white card, dark text in both themes). rows: (name, amount, %DV, cls) cls in '', 'i', 'ii', 'b'"""
    R=''.join(f'<div class="nfr {c}"><span class="nfn">{n}</span><span class="nfa">{a}</span><span class="nfp">{p}</span></div>' for n,a,p,c in rows)
    return (f'<div class="art nflw" data-part="{part}"><div class="nfl" role="group" aria-label="Typical Nutrition Facts for {_html.escape(food)}">'
            f'<p class="nfh">Nutrition Facts</p><p class="nft">{food} · typical values, illustrative, not a specific brand</p>'
            f'<p class="nfs"><b>Serving size</b><span>{serving}</span></p><p class="nfc"><b>Calories</b><b>{cal}</b></p><p class="nfdv">% Daily Value</p>{R}'
            f'<p class="nfi"><b>Ingredients:</b> {ingred}</p>{extra}</div></div>')
MAPH=['Label line','Branch','What it is here','Lesson']
# ---- Figure 1: the whole-site tree ----
_C=[150,450,750]
_HD=[('Macronutrients','Module 1 · grams','nd s','macronutrients-fats.html'),('Micronutrients','Module 2 · mg and µg','nd u','micronutrients-fat-soluble-vitamins.html'),
     ('Non-Nutrients','Module 3 · not nutrients','nd t','additives.html')]
_KIDS=[[('Fats','9 kcal/g','macronutrients-fats.html'),('Lipids','cholesterol, sterols','macronutrients-lipids.html'),
        ('Protein','4 kcal/g','macronutrients-protein.html'),('Carbohydrates','4 kcal/g · fiber','macronutrients-carbohydrates.html'),
        ('Water and Ethanol','alcohol 7 kcal/g','macronutrients-water-ethanol.html')],
       [('Vitamins A, D, E, K','fat-soluble','micronutrients-fat-soluble-vitamins.html'),('B Vitamins and C','water-soluble','micronutrients-water-soluble-vitamins.html'),
        ('Major Minerals','sodium, calcium','micronutrients-major-minerals.html'),('Trace Minerals','iron, zinc, iodine','micronutrients-trace-minerals.html')],
       [('Additives','E-numbers','additives.html'),('Antinutrients','phytate, lectins','antinutrients.html'),('Processing','heat, microbes','processing.html'),
        ('Bioactives','polyphenols','bioactives.html'),('Flavorings','taste and smell','flavorings.html')]]
_Y0=150; _DY=84; _W=196
FR_NODES=[(450,30,330,'What’s in Food','every label line belongs to one branch','nd root','#fig-2')]
FR_EDGES=[]
for cx,(t,s,c,h),kids in zip(_C,_HD,_KIDS):
    FR_NODES.append((cx,_Y0,212,t,s,c,h)); FR_EDGES.append((450,52,cx,128))
    tx=cx-96; ys=[_Y0+_DY*(k+1) for k in range(len(kids))]
    FR_EDGES.append(('line',tx,_Y0+32,tx,ys[-1]+5))
    for y,(kt,ks,kh) in zip(ys,kids):
        FR_NODES.append((cx+12,y,_W-24,kt,ks,c,kh)); FR_EDGES.append(('line',tx,y+5,cx+12-(_W-24)/2,y+5))
P1=('<!--noart-->'+ftree(FR_NODES,FR_EDGES,_Y0+_DY*5+50,'Tree diagram of the whole curriculum. What’s in food splits into three branches, one per module. Macronutrients, needed in grams: Fats, Lipids, Protein, Carbohydrates, Water and Ethanol. Micronutrients, needed in milligrams and micrograms: vitamins A, D, E and K; B vitamins and C; major minerals; trace minerals. Non-nutrients, things in food or done to food that are not nutrients: Additives, Antinutrients, Processing, Bioactives, Flavorings. Each box links to its lesson.')
 +lblock('label','What the tree shows',[('Two branches are on the Nutrition Facts panel','Macronutrients and micronutrients are the nutrients the panel counts: grams of fat, carbohydrate and protein, and milligrams or micrograms of a few vitamins and minerals.'),
   ('Part of the third branch is in the ingredient list','Additives, processing words and flavorings show up in the ingredient list, and sometimes in words like “cultured”, “enriched” or “pasteurized”.'),
   ('The rest of the third branch is never printed','Antinutrients and bioactives, such as phytate and polyphenols, come with the whole food but have no label line. You find them by knowing the food, which is what the next five figures practise.')]))
# ---- Figure 2: the method ----
P2=('<!--noart-->'+table('panel',['Label line','Branch','Lesson'],[
   ['Calories','energy from protein and carbohydrate (4 kcal per gram), fat (9) and alcohol (7)',L('macronutrients-fats',1)+' · '+L('macronutrients-water-ethanol',5)],
   ['Total Fat, Saturated Fat, Trans Fat','fats: triglycerides grouped by their fatty acid chains',L('macronutrients-fats',4)],
   ['Cholesterol','a sterol, not a fat; listed in milligrams',L('macronutrients-lipids',3)],
   ['Sodium','a major mineral; salt is about 2.5 times the sodium figure',L('micronutrients-major-minerals',8)],
   ['Total Carbohydrate, Dietary Fiber, Total Sugars, Added Sugars','carbohydrates: starch, fiber and sugars',L('macronutrients-carbohydrates',8)],
   ['Protein','chains of amino acids',L('macronutrients-protein',7)],
   ['Vitamin D, Calcium, Iron, Potassium','the four micronutrients every US label must list',L('micronutrients-fat-soluble-vitamins',7)+' · '+L('micronutrients-major-minerals',8)+' · '+L('micronutrients-trace-minerals',8)],
   ['% Daily Value','how much of a day’s reference amount one serving gives; 5% or less is low, 20% or more is high','—']],'The Nutrition Facts panel')
 +lblock('list','The ingredient list',[('Order by weight','Ingredients are listed from most to least by weight, so the first one or two make up most of the food.'),
   ('Additives and flavor lines','Additives appear by name or, in the EU, by E-number, and flavorings as “natural flavor” or “artificial flavor” (Additives; Flavorings).'),
   ('Processing words','“Cultured”, “pasteurized”, “enriched”, “rolled” and “hydrogenated” each name a process from the Processing lesson.'),
   ('What is not printed','Antinutrients and bioactives have no line. A single-ingredient food can carry several of them.')]))
# ---- Figures 3-7: five labels ----
P3=('<!--noart-->'+nflabel('label','Plain whole-milk yogurt','1 cup (245 g)','150',[
   ('Total Fat','8 g','10%','b'),('Saturated Fat','5 g','25%','i'),('Trans Fat','0 g','','i'),('Cholesterol','30 mg','10%','b'),('Sodium','115 mg','5%','b'),
   ('Total Carbohydrate','11 g','4%','b'),('Dietary Fiber','0 g','0%','i'),('Total Sugars','11 g','','i'),('Includes 0 g Added Sugars','','0%','ii'),('Protein','9 g','','b'),
   ('Vitamin D','0 mcg','0%',''),('Calcium','300 mg','23%',''),('Iron','0 mg','0%',''),('Potassium','380 mg','8%','')],
   'Cultured pasteurized whole milk. Contains live and active cultures.')
 +table('map',MAPH,[['Total Sugars 11 g, Added 0 g','Carbohydrates','all of it is lactose, the sugar already in milk',L('macronutrients-carbohydrates',4)],
   ['Cultured','Processing · Flavorings','bacteria turn some lactose into lactic acid, which thickens the milk protein and tastes sour',L('processing',6)+' · '+L('flavorings',4)],
   ['Pasteurized','Processing','milk heated to kill harmful microbes before the cultures are added',L('processing',6)],
   ['Saturated Fat, Cholesterol','Fats · Lipids','milk fat is mostly saturated; cholesterol is a separate sterol',L('macronutrients-fats',4)+' · '+L('macronutrients-lipids',3)],
   ['Protein 9 g','Protein','casein and whey, a complete protein rich in leucine',L('macronutrients-protein',7)],
   ['Calcium 300 mg','Major minerals','calcium ions, about a quarter of the Daily Value',L('micronutrients-major-minerals',5)]],'Line by line')
 +molbox('mols','Key molecules in yogurt',['<div class="mgrid">'
   +mcell(MR('lactose','Lactose: a galactose ring joined to a glucose ring through one oxygen; every hydrogen shown',[('link','1',A,A)],'Lactose, C12H22O11',eager=True),'Lactose','C₁₂H₂₂O₁₁ · milk sugar')
   +mcell(MR('lactic','Lactic acid: three carbons with an OH group and a carboxylic acid; every hydrogen shown',[('c','2',A,A)],'Lactic acid, C3H6O3'),'Lactic acid','C₃H₆O₃ · made by the cultures')
   +mcell(MR('leucine','Leucine: an amino acid with a branched side chain; every hydrogen shown',[('r','3',A,A)],'Leucine, C6H13NO2'),'Leucine','C₆H₁₃NO₂ · in milk protein')
   +mcell(MR('ca','Calcium ion, Ca2+, drawn at its ionic size',[],'Calcium ion, Ca2+'),'4 · Calcium ion','Ca²⁺')+'</div>'],
   [('1','Lactose is a double sugar. The cultures use some of it up, and live cultures help digest the rest, so many people who are lactose intolerant manage yogurt better than milk.',''),
    ('2','Lactic acid is what the cultures make from lactose. Its acid sets the milk proteins into a soft gel and gives yogurt its tang.',''),
    ('3','Milk protein is rich in leucine, the amino acid that most strongly switches on muscle building.',''),
    ('4','Calcium in yogurt is well absorbed, and one cup gives about a quarter of the Daily Value.','')])
 +legend('c h o n ca'))
P4=('<!--noart-->'+nflabel('label','Canned black beans, drained','½ cup (130 g)','110',[
   ('Total Fat','0.5 g','1%','b'),('Saturated Fat','0 g','0%','i'),('Trans Fat','0 g','','i'),('Cholesterol','0 mg','0%','b'),('Sodium','400 mg','17%','b'),
   ('Total Carbohydrate','20 g','7%','b'),('Dietary Fiber','7 g','25%','i'),('Total Sugars','0 g','','i'),('Includes 0 g Added Sugars','','0%','ii'),('Protein','7 g','','b'),
   ('Vitamin D','0 mcg','0%',''),('Calcium','40 mg','3%',''),('Iron','1.8 mg','10%',''),('Potassium','350 mg','7%','')],
   'Black beans, water, salt, calcium chloride.')
 +table('map',MAPH,[['Sodium 400 mg, from salt','Major minerals','about 1 g of salt; draining and rinsing washes some away, and “no salt added” cans have far less',L('micronutrients-major-minerals',8)],
   ['Calcium chloride','Additives','a firming agent (E509) that keeps the beans from going mushy',L('additives',2)],
   ['Dietary Fiber 7 g','Carbohydrates','soluble and insoluble fiber, a quarter of the Daily Value',L('macronutrients-carbohydrates',6)],
   ['Protein 7 g','Protein','rich in lysine, low in methionine, so beans pair well with grains',L('macronutrients-protein',7)],
   ['Iron 1.8 mg','Trace minerals','nonheme iron, better absorbed with vitamin C in the same meal',L('micronutrients-trace-minerals',3)],
   ['Not printed: phytate, lectins','Antinutrients','phytate binds some iron and zinc; the canning heat destroys the lectins that make raw beans unsafe',L('antinutrients',3)+' · '+L('antinutrients',6)]],'Line by line')
 +molbox('mols','Key molecules in canned beans',['<div class="mgrid">'
   +mcell(MR('na','Sodium ion, Na+, drawn at its ionic size',[],'Sodium ion, Na+',eager=True),'1 · Sodium ion','Na⁺')
   +mcell(MR('cl','Chloride ion, Cl-, drawn at its ionic size',[],'Chloride ion, Cl-'),'1 · Chloride ion','Cl⁻')
   +mcell(MR('lysine','Lysine: an amino acid with a long side chain ending in an amine group; every hydrogen shown',[('r','2',A,A)],'Lysine, C6H14N2O2'),'Lysine','C₆H₁₄N₂O₂')
   +mcell(MR('phytic','Phytic acid: a six-carbon ring carrying six phosphate groups; every hydrogen shown',[('p','3',A,A)],'Phytic acid, C6H18O24P6'),'Phytic acid','C₆H₁₈O₂₄P₆')
   +mcell(MR('fe2','Iron ion, Fe2+, drawn at its ionic size',[],'Iron ion, Fe2+'),'4 · Iron ion','Fe²⁺')+'</div>'],
   [('1','Salt dissolves into sodium and chloride ions. The sodium line counts only the sodium.',''),
    ('2','Beans are rich in lysine, the amino acid grains are short of, which is why beans and rice or bread make a complete protein together.',''),
    ('3','Phytic acid’s six phosphate groups grip iron, zinc and calcium ions. Soaking and cooking lower it somewhat.',''),
    ('4','Plant iron is absorbed as Fe²⁺. Vitamin C turns more of it into this form, and phytate and tea tannins hold it back.','')])
 +legend('c h o n p na cl fe'))
P5=('<!--noart-->'+nflabel('label','Rolled oats, dry','½ cup (40 g)','150',[
   ('Total Fat','3 g','4%','b'),('Saturated Fat','0.5 g','3%','i'),('Trans Fat','0 g','','i'),('Cholesterol','0 mg','0%','b'),('Sodium','0 mg','0%','b'),
   ('Total Carbohydrate','27 g','10%','b'),('Dietary Fiber','4 g','14%','i'),('Total Sugars','1 g','','i'),('Includes 0 g Added Sugars','','0%','ii'),('Protein','5 g','','b'),
   ('Vitamin D','0 mcg','0%',''),('Calcium','20 mg','2%',''),('Iron','1.7 mg','10%',''),('Potassium','150 mg','3%','')],
   'Whole grain rolled oats.')
 +table('map',MAPH,[['Total Carbohydrate 27 g','Carbohydrates','mostly starch: long chains of alpha-glucose that your enzymes break down',L('macronutrients-carbohydrates',5)],
   ['Dietary Fiber 4 g','Carbohydrates','includes beta-glucan, a soluble fiber made of beta-glucose',L('macronutrients-carbohydrates',6)],
   ['Rolled','Processing','oats are steamed to stop a fat-splitting enzyme that would turn them rancid, then flattened between rollers',L('processing',2)],
   ['Iron 1.7 mg','Trace minerals','nonheme plant iron',L('micronutrients-trace-minerals',3)],
   ['Protein 5 g','Protein','grain protein: low in lysine, so oats pair well with milk, yogurt or beans',L('macronutrients-protein',7)],
   ['Not printed: phytate','Antinutrients','whole grains keep the phytate-rich outer layers; soaking overnight lowers it a little',L('antinutrients',8)]],'Line by line')
 +molbox('mols','Starch and fiber: the same sugar, a different link',['<div class="mgrid">'
   +mcell(MR('glucose_a','Alpha-glucose ring with every hydrogen shown; the OH on carbon 1 points down',[('oh1','1',A,A)],'Alpha-glucose, C6H12O6',eager=True),'Alpha-glucose','builds starch')
   +mcell(MR('glucose_b','Beta-glucose ring with every hydrogen shown; the OH on carbon 1 points up',[('oh1','2',A,A)],'Beta-glucose, C6H12O6'),'Beta-glucose','builds beta-glucan')
   +mcell(MR('cellobiose','Two beta-glucose rings joined by a beta link through one oxygen; every hydrogen shown',[('link','3',A,A)],'Two beta-glucose units joined by a beta link, C12H22O11'),'Beta link','two beta-glucose units')+'</div>'],
   [('1','Starch is chains of alpha-glucose. Your amylase enzymes cut those links, so starch becomes blood glucose.',''),
    ('2','Beta-glucose differs only in which way one OH group points.',''),
    ('3','Beta links like this one resist your enzymes, so oat beta-glucan reaches the gut as soluble fiber. It thickens into a gel, and about 3 g a day from oats, in a diet low in saturated fat, can lower LDL cholesterol; the US FDA allows a heart-health claim on that basis.','')])
 +legend('c h o'))
P6=('<!--noart-->'+nflabel('label','Extra virgin olive oil','1 tbsp (14 g)','120',[
   ('Total Fat','14 g','18%','b'),('Saturated Fat','2 g','10%','i'),('Trans Fat','0 g','','i'),('Polyunsaturated Fat','1.5 g','','i'),('Monounsaturated Fat','10 g','','i'),
   ('Cholesterol','0 mg','0%','b'),('Sodium','0 mg','0%','b'),('Total Carbohydrate','0 g','0%','b'),('Protein','0 g','','b'),
   ('Vitamin E (optional line)','2 mg','13%','')],
   'Extra virgin olive oil.')
 +table('map',MAPH,[['Calories 120','Fats','14 g of fat × 9 kcal per gram is 126; labels round to the nearest 10',L('macronutrients-fats',1)],
   ['Monounsaturated Fat 10 g','Fats','mostly oleic acid, the omega-9 fatty acid with one cis double bond',L('macronutrients-fats',5)+' · '+L('macronutrients-fats',6)],
   ['Cholesterol 0 mg','Lipids','plants make no cholesterol; olive oil has plant sterols instead',L('macronutrients-lipids',3)],
   ['Vitamin E','Fat-soluble vitamins','alpha-tocopherol, an antioxidant that protects the oil and your cell membranes',L('micronutrients-fat-soluble-vitamins',5)],
   ['Extra virgin','Processing','pressed from olives with no heat-and-solvent refining, so it keeps more polyphenols',L('processing',7)],
   ['Not printed: polyphenols','Bioactives · Flavorings','hydroxytyrosol and related polyphenols, also behind the peppery, bitter taste of fresh oil',L('bioactives',3)+' · '+L('flavorings',3)]],'Line by line')
 +molbox('mols','Key molecules in olive oil',[
   MR('triglyceride','A triglyceride: a glycerol backbone holding three fatty acid chains by ester links, one saturated, one with one cis double bond and one with two; every hydrogen shown',[((10.0,40.0),'1',A,A),((56.0,47.0),'2',A,A)],'A triglyceride, C55H100O6',eager=True),
   '<div class="mgrid">'+mcell(MR('tocopherol','Alpha-tocopherol: a ring with an OH group and a long saturated tail; every hydrogen shown',[('oh','3',A,A)],'Alpha-tocopherol, C29H50O2'),'Alpha-tocopherol','C₂₉H₅₀O₂ · vitamin E')
   +mcell(MR('hydroxytyrosol','Hydroxytyrosol: a benzene ring with two neighbouring OH groups and a two-carbon chain ending in OH; every hydrogen shown',[('cat','4',A,A)],'Hydroxytyrosol, C8H10O3'),'Hydroxytyrosol','C₈H₁₀O₃ · polyphenol')+'</div>'],
   [('1','Every fat and oil is triglycerides: glycerol, shaded, holding three fatty acids (Fats, Figure 3).',''),
    ('2','One cis double bond, drawn in orange, kinks the chain. In olive oil most chains are oleic acid, which is why it stays liquid.',''),
    ('3','Vitamin E dissolves in the oil. Its OH group gives up a hydrogen to stop fats from going rancid.',''),
    ('4','Hydroxytyrosol’s two neighbouring OH groups make it an antioxidant. The EU allows a claim that olive oil polyphenols help protect blood lipids from oxidation, at about 5 mg a day in 20 g of oil with enough of them.','')])
 +legend('c h o'))
P7=('<!--noart-->'+nflabel('label','Simple white sandwich bread','1 slice (30 g)','80',[
   ('Total Fat','1 g','1%','b'),('Saturated Fat','0 g','0%','i'),('Trans Fat','0 g','','i'),('Cholesterol','0 mg','0%','b'),('Sodium','150 mg','7%','b'),
   ('Total Carbohydrate','15 g','5%','b'),('Dietary Fiber','1 g','4%','i'),('Total Sugars','1 g','','i'),('Includes 0 g Added Sugars','','0%','ii'),('Protein','3 g','','b'),
   ('Vitamin D','0 mcg','0%',''),('Calcium','20 mg','2%',''),('Iron','1 mg','6%',''),('Potassium','30 mg','0%','')],
   'Enriched wheat flour (wheat flour, niacin, reduced iron, thiamin mononitrate, riboflavin, folic acid), water, yeast, salt.',
   '<p class="nfi"><b>Contains:</b> wheat.</p>')
 +table('map',MAPH,[['Enriched wheat flour','Micronutrients','milling removes the bran and germ, so B vitamins and iron are added back',L('micronutrients-water-soluble-vitamins',8)],
   ['Folic acid','Water-soluble vitamins','required in US enriched grain since 1998 to help prevent neural tube defects',L('micronutrients-water-soluble-vitamins',5)],
   ['Reduced iron','Trace minerals','fine iron powder added to the flour',L('micronutrients-trace-minerals',8)],
   ['Yeast','Water and Ethanol · Processing','yeast ferments sugar into carbon dioxide, which raises the dough, and ethanol, which bakes off',L('macronutrients-water-ethanol',5)],
   ['Crust','Processing','browning makes flavor and a little acrylamide; toast to golden, not dark brown',L('processing',3)],
   ['Salt, Sodium 150 mg','Major minerals','bread is one of the biggest sources of sodium in many diets because people eat it often',L('micronutrients-major-minerals',8)],
   ['Contains: wheat','Protein','wheat is a major allergen; its gluten proteins form the stretchy network that traps the gas',L('macronutrients-protein',5)]],'Line by line')
 +molbox('mols','Key molecules in bread',[
   MR('folicacid','Folic acid: a two-ring pteridine joined to a benzene ring and the amino acid glutamate; every hydrogen shown',[('pter','1',A,A)],'Folic acid, C19H19N7O6',eager=True),
   '<div class="mgrid">'+mcell(MR('ethanol','Ethanol: two carbons and an OH group; every hydrogen shown',[('oh','2',A,A)],'Ethanol, C2H6O'),'Ethanol','C₂H₆O')
   +mcell(MR('co2','Carbon dioxide: a carbon double-bonded to two oxygens',[('c','2',A,A)],'Carbon dioxide, CO2'),'Carbon dioxide','CO₂')
   +mcell(MR('acrylamide','Acrylamide: a C=C double bond next to an amide group; every hydrogen shown',[('vinyl','3',A,A)],'Acrylamide, C3H5NO'),'Acrylamide','C₃H₅NO · in the crust')+'</div>'],
   [('1','Folic acid is the stable, added form of folate. Your body converts it to the active form.',''),
    ('2','Yeast turns each glucose into two ethanol and two carbon dioxide. The gas makes the holes; the ethanol evaporates in the oven.',''),
    ('3','Acrylamide forms when the amino acid asparagine meets sugar in dry heat. Most of it is in the crust and in dark toast.','')])
 +legend('c h o n'))
P8=('<!--noart-->'+table('table',['Food','Lines that tell the story','Branches it touches','Not on the label'],[
   ['Plain yogurt','11 g sugars, 0 g added; calcium 23%','Carbohydrates, Fats, Lipids, Protein, Major minerals, Processing, Flavorings','live cultures'],
   ['Canned beans','sodium 17%, fiber 25%, calcium chloride','Carbohydrates, Protein, Major and Trace minerals, Additives','phytate; lectins destroyed by canning'],
   ['Rolled oats','fiber 4 g, no sodium, one ingredient','Carbohydrates, Protein, Trace minerals, Processing','beta-glucan amount, phytate'],
   ['Olive oil','14 g fat, 10 g of it monounsaturated','Fats, Lipids, Fat-soluble vitamins, Processing','polyphenols such as hydroxytyrosol'],
   ['White bread','enriched flour, folic acid, salt','Carbohydrates, Protein, Water-soluble vitamins, Trace and Major minerals, Water and Ethanol, Processing','acrylamide in the crust']],'Five foods at a glance')
 +worth([('Labels round','A nutrient under 0.5 g per serving can be listed as 0 g, so “0 g trans fat” can still mean a little. Calories above 50 are rounded to the nearest 10, and sodium above 140 mg to the nearest 10 mg.'),
   ('Serving sizes are reference amounts','The serving is based on how much people typically eat at one time, not on how much you should eat. Compare foods per 100 g when servings differ.'),
   ('Whole foods often have no label','Fresh fruit, vegetables and raw single-ingredient meat and fish do not need a Nutrition Facts panel. Databases such as USDA FoodData Central list typical values.'),
   ('Every number here is typical','Brands and batches differ. The labels in this lesson are illustrative averages, so always read the one on the package in your hand.')],
   note='General education, not medical advice. Typical values are rounded averages in the style of USDA FoodData Central and US FDA label rules (21 CFR 101.9), not any brand’s label.'))
FR_LESSON=[('The Whole Curriculum Family Tree','Every lesson on one chart, grouped the way a label is read.',P1),
 ('Reading a Label Line by Line','Which branch each line of the Nutrition Facts panel and ingredient list belongs to.',P2),
 ('Plain Yogurt','Milk sugar, fermentation and calcium.',P3),
 ('Canned Beans','Salt, an additive, fiber and the antinutrients the can deals with.',P4),
 ('Rolled Oats','One ingredient: starch, beta-glucan fiber and a processing step.',P5),
 ('Olive Oil','Almost pure fat, plus vitamin E and polyphenols.',P6),
 ('Simple Bread','Enriched flour, yeast, salt and the crust.',P7),
 ('Putting It All Together','The five foods in one table, plus a few things worth knowing.',P8)]
FR_QUIZ=[('How many calories does a gram of protein, carbohydrate, fat and alcohol give?','About 4, 4, 9 and 7 (Figure 2; Fats, Water and Ethanol).'),
 ('A tablespoon of olive oil has 14 g of fat. Why does the label say about 120 calories?','14 g × 9 kcal per gram is 126, and labels round calories above 50 to the nearest 10 (Figure 6).'),
 ('Plain yogurt lists 11 g of total sugars but 0 g added sugars. Where does the sugar come from?','Lactose, the sugar naturally in milk (Figure 3; Carbohydrates, Figure 8).'),
 ('What makes yogurt thick and tangy?','Cultures turn lactose into lactic acid, which sets the milk proteins into a gel and tastes sour (Figure 3; Processing, Figure 6).'),
 ('Why is cholesterol a separate line in milligrams rather than part of Total Fat?','Cholesterol is a sterol built from four rings, not a triglyceride, and it has no calories (Lipids, Figure 3).'),
 ('A can of beans lists 400 mg of sodium per serving. Roughly how much salt is that?','About 1 g, since salt is about 2.5 times the sodium figure (Figure 4; Major Minerals, Figure 8).'),
 ('What is calcium chloride doing in canned beans?','It is a firming agent, an additive (E509) that keeps the beans from going soft (Figure 4; Additives).'),
 ('Why can you eat canned kidney beans straight from the can but not raw or undercooked ones?','The canning heat destroys the lectins that cause illness (Figure 4; Antinutrients, Figure 6).'),
 ('Why do beans and grains make a good protein pair?','Beans are rich in lysine but low in methionine, and grains are the reverse (Figure 4; Protein, Figure 7).'),
 ('Starch and oat beta-glucan are both made of glucose. Why is one fiber?','Beta-glucan uses beta links that human enzymes cannot cut, while starch uses alpha links that amylase breaks (Figure 5; Carbohydrates, Figure 6).'),
 ('Why are oats steamed before they are rolled?','To stop a fat-splitting enzyme that would make them go rancid (Figure 5; Processing).'),
 ('What does “enriched” mean on flour, and which added vitamin helps prevent neural tube defects?','B vitamins and iron are added back after milling; folic acid prevents neural tube defects (Figure 7; Water-Soluble Vitamins).'),
 ('Where do the holes in bread come from?','Yeast ferments sugar into carbon dioxide gas, which the gluten network traps; the ethanol bakes off (Figure 7; Water and Ethanol, Figure 5).'),
 ('Why toast bread to golden rather than dark brown?','Browning forms acrylamide, and darker toast has more of it (Figure 7; Processing, Figure 3).'),
 ('Which fat-soluble vitamin does olive oil supply, and what does it protect?','Vitamin E, alpha-tocopherol, which protects fats in the oil and in your cell membranes from oxidation (Figure 6; Fat-Soluble Vitamins, Figure 5).'),
 ('Which two Non-Nutrients lessons cover compounds that never get their own label line?','Antinutrients and bioactives, such as phytate and polyphenols (Figures 1 and 2).'),
 ('Does “0 g trans fat” guarantee there is none?','No. Less than 0.5 g per serving can be listed as 0 g (Figure 8).'),
 ('On the % Daily Value column, what counts as low and what counts as high?','5% or less is low and 20% or more is high (Figure 2).')]
NFL_CSS=('<style>.nflw{padding:4px}.nfl{max-width:430px;margin:0 auto;background:#fff;color:#1f1f1f;border:2px solid #1f1f1f;padding:10px 12px;font-family:var(--sans);line-height:1.35}'
 '.nfh{margin:0;font:800 1.9rem/1.05 var(--sans);letter-spacing:-.01em}.nft{margin:2px 0 6px;font-size:.85rem;color:#55534E}'
 '.nfs{display:flex;justify-content:space-between;gap:10px;margin:0;padding:4px 0 6px;border-top:1px solid #1f1f1f;border-bottom:8px solid #1f1f1f}'
 '.nfc{display:flex;justify-content:space-between;margin:0;padding:4px 0;font-size:1.45rem;border-bottom:4px solid #1f1f1f}'
 '.nfdv{margin:0;padding:3px 0;text-align:right;font-weight:700;font-size:.9rem;border-bottom:1px solid #1f1f1f}'
 '.nfr{display:grid;grid-template-columns:1fr auto 3.2em;gap:6px;padding:3px 0;border-bottom:1px solid #9a9893;font-size:1rem}'
 '.nfr.b .nfn{font-weight:700}.nfr.i .nfn{padding-left:1em}.nfr.ii .nfn{padding-left:2em}.nfa{text-align:right}.nfp{text-align:right;font-weight:700}'
 '.nfr:not(.b):not(.i):not(.ii){font-size:.95rem}.nfr.b+.nfr:not(.b):not(.i):not(.ii){border-top:6px solid #1f1f1f}'
 '.nfi{margin:8px 0 0;font-size:.95rem}</style>')
build_lesson('final-review','Final Review','The whole curriculum on one chart, then five whole foods read label line by line: plain yogurt, canned beans, rolled oats, olive oil and a simple bread. Each label line is matched to its branch and lesson, and the key molecules behind it are shown in ball-and-stick form. The labels use typical values for illustration; they are not any brand’s label. The figure is on the left and the lesson script on the right; the mixed quiz at the end covers every module.',FR_LESSON,FR_QUIZ,after_extra=NFL_CSS,mols=MR)
