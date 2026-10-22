# Micronutrients: vitamins & mineral forms (EU Reg 1925/2006 Annex II; US 21 CFR 184 GRAS forms), plus trace elements
FORT='Not naturally in foods as this form; fortified foods, supplements. '
V=[ # vitamin, role, natural sources, forms [(name, what, naturalfound or None)]
('Vitamin A (fat-soluble)','Vision, immune function, skin and cell growth','Liver, eggs, dairy fat; provitamin in orange/green vegetables',[
 ('Retinol','Preformed vitamin A alcohol','Liver, cod liver oil, egg yolks, butter'),
 ('Retinyl acetate','Synthetic acetate ester of retinol',None),
 ('Retinyl palmitate','Palmitate ester of retinol (main storage form)','Liver, dairy fat; added to fortified milk'),
 ('Beta-carotene (provitamin A)','Orange carotenoid split into two retinal molecules','Carrots, sweet potatoes, spinach, pumpkin')]),
('Vitamin D (fat-soluble)','Calcium absorption, bone health, immune function','Oily fish, egg yolks, UV-exposed mushrooms; skin makes it from sunlight',[
 ('Cholecalciferol (D3)','Animal form of vitamin D','Salmon, sardines, cod liver oil, egg yolks'),
 ('Ergocalciferol (D2)','Plant/fungal form of vitamin D','UV-exposed mushrooms'),
 ('Calcifediol (25-hydroxyvitamin D3)','Liver metabolite of D3 (authorized in EU supplements)','Meat, eggs (small amounts)')]),
('Vitamin E (fat-soluble)','Antioxidant protecting cell membranes','Nuts, seeds, vegetable oils, leafy greens',[
 ('D-alpha-tocopherol','Natural, most active vitamin E form','Sunflower seeds, almonds, wheat germ oil'),
 ('DL-alpha-tocopherol','Synthetic mix of eight stereoisomers',None),
 ('D-alpha-tocopheryl acetate','Natural-source vitamin E ester',None),
 ('DL-alpha-tocopheryl acetate','Synthetic vitamin E ester',None),
 ('D-alpha-tocopheryl acid succinate','Vitamin E succinate ester',None),
 ('Gamma-tocopherol','Main tocopherol in the US diet','Soybean and corn oils, walnuts, pecans'),
 ('Delta-tocopherol','Tocopherol with lower vitamin activity','Soybean oil, wheat germ'),
 ('Tocotrienols','Unsaturated vitamin E family','Palm oil, rice bran, annatto, barley')]),
('Vitamin K (fat-soluble)','Blood clotting; bone and vascular calcium regulation','Leafy greens, fermented foods, eggs',[
 ('Phylloquinone (K1, phytomenadione)','Plant form of vitamin K','Kale, spinach, broccoli, collards'),
 ('Menaquinone-4 (K2 MK-4)','Animal-tissue form of K2','Egg yolks, chicken, butter, liver'),
 ('Menaquinone-7 (K2 MK-7)','Bacterial long-chain K2','Natto, some aged cheeses')]),
('Vitamin B1 (thiamin)','Carbohydrate metabolism, nerve function','Pork, whole grains, legumes, sunflower seeds',[
 ('Thiamin (natural)','Thiamin and thiamin pyrophosphate in foods','Pork, whole grains, beans'),
 ('Thiamin hydrochloride','Salt form of B1',None),('Thiamin mononitrate','Stable salt form of B1',None)]),
('Vitamin B2 (riboflavin)','Energy metabolism (FAD/FMN coenzymes)','Milk, eggs, liver, almonds, mushrooms',[
 ('Riboflavin','Yellow B2 vitamin','Milk, eggs, liver, almonds'),
 ("Riboflavin 5'-phosphate sodium",'Soluble phosphate form (FMN)',None)]),
('Vitamin B3 (niacin)','Energy metabolism (NAD/NADP)','Tuna, chicken, peanuts, mushrooms; made from tryptophan',[
 ('Nicotinic acid','Niacin acid form; causes flushing at high doses','Grains (bound form), coffee'),
 ('Nicotinamide (niacinamide)','Amide form of niacin','Meat, fish, poultry'),
 ('Inositol hexanicotinate','"No-flush" niacin ester (EU supplements)',None)]),
('Vitamin B5 (pantothenic acid)','Part of coenzyme A (fat and energy metabolism)','Liver, mushrooms, eggs, avocado, sunflower seeds',[
 ('Pantothenic acid (natural)','Free and bound pantothenate in foods','Liver, mushrooms, eggs'),
 ('Calcium D-pantothenate','Calcium salt of B5',None),('Sodium D-pantothenate','Sodium salt of B5',None),
 ('Dexpanthenol (D-panthenol)','Alcohol form converted to B5',None)]),
('Vitamin B6','Amino acid metabolism, neurotransmitters, hemoglobin','Chickpeas, tuna, salmon, poultry, potatoes, bananas',[
 ('Pyridoxine hydrochloride','Common salt form of B6',None),
 ("Pyridoxine 5'-phosphate",'Phosphorylated pyridoxine',None),
 ("Pyridoxal 5'-phosphate (P5P)",'Active coenzyme form','Meat, fish, poultry'),
 ('Pyridoxamine','Natural B6 vitamer','Meat, fish')]),
('Vitamin B7 (biotin)','Fat, carbohydrate and amino acid metabolism','Egg yolks, liver, nuts, seeds',[
 ('D-biotin','Biotin','Egg yolks, liver, nuts, seeds, sweet potato')]),
('Vitamin B9 (folate)','DNA synthesis, cell division; prevents neural tube defects','Leafy greens, legumes, asparagus, liver',[
 ('Food folates (polyglutamates)','Natural folate forms','Leafy greens, lentils, chickpeas, asparagus, liver'),
 ('Folic acid (pteroylmonoglutamic acid)','Synthetic, very stable folate',None),
 ('Calcium L-methylfolate (5-MTHF)','Salt of the main active folate','Leafy greens, legumes, liver (as 5-MTHF)'),
 ('(6S)-5-methyltetrahydrofolic acid glucosamine salt','Active folate salt (EU-authorized)',None)]),
('Vitamin B12 (cobalamin)','Nerve function, red blood cells, DNA synthesis','Meat, fish, shellfish, eggs, dairy (not in plants)',[
 ('Cyanocobalamin','Stable synthetic B12',None),
 ('Hydroxocobalamin','Natural and injection form','Meat, fish, dairy'),
 ("5'-deoxyadenosylcobalamin",'Mitochondrial coenzyme form','Liver, meat, fish'),
 ('Methylcobalamin','Cytosolic coenzyme form','Meat, fish, eggs, dairy')]),
('Vitamin C','Antioxidant, collagen synthesis, iron absorption, immunity','Citrus, bell peppers, kiwi, strawberries, broccoli',[
 ('L-ascorbic acid','Vitamin C','Citrus, bell peppers, kiwi, strawberries'),
 ('Sodium L-ascorbate','Sodium salt of vitamin C',None),('Calcium L-ascorbate','Calcium salt of vitamin C',None),
 ('Potassium L-ascorbate','Potassium salt of vitamin C',None),('Magnesium L-ascorbate','Magnesium salt of vitamin C',None),
 ('Zinc L-ascorbate','Zinc salt of vitamin C',None),('L-ascorbyl 6-palmitate','Fat-soluble vitamin C ester',None)]),
]
VL=[('Choline','Essential nutrient (vitamin-like)','Acetylcholine, cell membranes, liver fat export','Eggs, liver, beef, fish, soybeans'),
 ('Choline bitartrate','Salt form of choline','Choline source',FORT+'Choline is natural in eggs, liver'),
 ('Citicoline (CDP-choline)','Choline-cytidine compound','Choline and phospholipid source',FORT+'Small amounts in organ meats'),
 ('Inositol','Sugar-alcohol-like compound','Cell signaling (phosphoinositides)','Citrus, beans, whole grains, nuts'),
 ('L-carnitine','Compound made from lysine and methionine','Shuttles fatty acids into mitochondria','Beef, lamb, pork, dairy'),
 ('Coenzyme Q10 (ubiquinone)','Fat-soluble quinone','Mitochondrial energy, antioxidant','Organ meats, beef, sardines, peanuts'),
 ('Alpha-lipoic acid','Sulfur-containing fatty acid','Mitochondrial enzyme cofactor, antioxidant','Organ meats, spinach, broccoli (small amounts)'),
 ('Pyrroloquinoline quinone (PQQ)','Redox cofactor','Studied for mitochondrial function; essentiality unproven','Natto, parsley, green tea, kiwi (traces)')]
MIN=[ # mineral, role, natural sources, forms
('Calcium','Bones, teeth, muscle contraction, nerve signaling, clotting','Dairy, sardines with bones, tofu set with calcium, kale, almonds',
 ['Calcium carbonate','Calcium chloride','Calcium citrate malate','Calcium citrate','Calcium gluconate','Calcium glycerophosphate','Calcium lactate','Calcium phosphates (mono-, di-, tricalcium)','Calcium hydroxide','Calcium malate','Calcium oxide','Calcium sulphate','Calcium bisglycinate','Calcium L-lysinate','Calcium pyruvate','Calcium succinate']),
('Magnesium','300+ enzymes, muscle and nerve function, energy, bones','Pumpkin seeds, almonds, spinach, black beans, whole grains, dark chocolate',
 ['Magnesium acetate','Magnesium L-ascorbate','Magnesium bisglycinate','Magnesium carbonate','Magnesium chloride','Magnesium citrate','Magnesium citrate malate','Magnesium gluconate','Magnesium glycerophosphate','Magnesium phosphates','Magnesium lactate','Magnesium L-lysinate','Magnesium hydroxide','Magnesium malate','Magnesium oxide','Magnesium L-pidolate','Potassium magnesium citrate','Magnesium pyruvate','Magnesium succinate','Magnesium sulphate','Magnesium taurate','Magnesium acetyl taurate']),
('Iron','Hemoglobin, oxygen transport, energy metabolism','Red meat, liver, clams, lentils, spinach, fortified cereals',
 ['Ferrous bisglycinate','Ferrous carbonate','Ferrous citrate','Ferric ammonium citrate','Ferrous gluconate','Ferrous fumarate','Ferric sodium diphosphate','Ferrous lactate','Ferrous sulphate','Ferrous ammonium phosphate','Ferric sodium EDTA','Ferric diphosphate (ferric pyrophosphate)','Ferric saccharate','Elemental iron (carbonyl, electrolytic, hydrogen-reduced)','Ferrous L-pidolate','Ferrous phosphate','Iron(II) taurate']),
('Copper','Iron metabolism, connective tissue, antioxidant enzymes','Liver, oysters, cashews, sesame, dark chocolate',
 ['Cupric carbonate','Cupric citrate','Cupric gluconate','Cupric sulphate','Copper L-aspartate','Copper bisglycinate','Copper lysine complex']),
('Iodine','Thyroid hormones (metabolism, brain development)','Seaweed, cod, dairy, eggs, iodized salt',
 ['Sodium iodide','Sodium iodate','Potassium iodide','Potassium iodate']),
('Zinc','Immunity, wound healing, taste, DNA synthesis, 300+ enzymes','Oysters, beef, crab, pumpkin seeds, chickpeas',
 ['Zinc acetate','Zinc L-ascorbate','Zinc L-aspartate','Zinc bisglycinate','Zinc chloride','Zinc citrate','Zinc gluconate','Zinc lactate','Zinc L-lysinate','Zinc malate','Zinc mono-L-methionine sulphate','Zinc oxide','Zinc carbonate','Zinc L-pidolate','Zinc picolinate','Zinc sulphate']),
('Manganese','Bone formation, antioxidant enzymes (MnSOD), metabolism','Oats, brown rice, nuts, tea, mussels',
 ['Manganese ascorbate','Manganese L-aspartate','Manganese bisglycinate','Manganese carbonate','Manganese chloride','Manganese citrate','Manganese gluconate','Manganese glycerophosphate','Manganese pidolate','Manganese sulphate']),
('Sodium','Fluid balance, nerve signals, muscle contraction','Salt, cheese, olives, cured meats, bread',
 ['Sodium bicarbonate','Sodium carbonate','Sodium chloride','Sodium citrate','Sodium gluconate','Sodium lactate','Sodium hydroxide','Sodium phosphates']),
('Potassium','Fluid balance, heart rhythm, blood pressure, nerve signals','Potatoes, beans, bananas, spinach, avocado, yogurt',
 ['Potassium bicarbonate','Potassium carbonate','Potassium chloride','Potassium citrate','Potassium gluconate','Potassium glycerophosphate','Potassium lactate','Potassium hydroxide','Potassium L-pidolate','Potassium malate','Potassium phosphates']),
('Selenium','Antioxidant enzymes (glutathione peroxidase), thyroid hormone activation','Brazil nuts, tuna, sardines, eggs, whole wheat',
 ['L-selenomethionine','Selenium-enriched yeast','Selenious acid','Sodium selenate','Sodium hydrogen selenite','Sodium selenite']),
('Chromium','Enhances insulin action (modest evidence)','Broccoli, grape juice, whole grains, meat',
 ['Chromium(III) chloride','Chromium(III) lactate tri-hydrate','Chromium picolinate','Chromium(III) sulphate']),
('Molybdenum','Cofactor for enzymes that break down sulfites and purines','Legumes, grains, nuts, liver',
 ['Ammonium molybdate','Potassium molybdate','Sodium molybdate']),
('Fluoride','Strengthens tooth enamel','Fluoridated water, tea, sardines with bones',
 ['Calcium fluoride','Potassium fluoride','Sodium fluoride','Sodium monofluorophosphate']),
('Phosphorus','Bones, ATP energy, DNA, cell membranes','Dairy, meat, fish, legumes, nuts',
 ['Phosphoric acid','Calcium phosphates (as P source)','Magnesium phosphates (as P source)','Potassium phosphates (as P source)','Sodium phosphates (as P source)']),
('Chloride','Stomach acid (HCl), fluid balance','Table salt, seaweed, tomatoes, celery, olives',['Sodium chloride (as Cl source)','Potassium chloride (as Cl source)','Calcium chloride (as Cl source)','Magnesium chloride (as Cl source)']),
('Boron','Bone and mineral metabolism (not established as essential)','Avocados, prunes, raisins, peanuts, wine',['Boric acid','Sodium borate']),
('Silicon','Connective tissue and bone (not established as essential)','Whole grains (oats, barley), beer, green beans, bananas',['Choline-stabilised orthosilicic acid','Silicon dioxide','Silicic acid']),
]
NAT={'Calcium carbonate':'Eggshells, limestone; tofu, fortified juices','Calcium phosphates (mono-, di-, tricalcium)':'Milk, bones (hydroxyapatite)','Sodium chloride':'Table salt, sea salt; cheese, olives','Sodium bicarbonate':'Baking soda; some mineral waters','Potassium chloride':'Seaweed, potatoes; salt substitutes','Potassium citrate':'Citrus fruit','Magnesium chloride':'Sea salt, nigari (tofu coagulant)','Calcium sulphate':'Mineral gypsum; tofu','L-selenomethionine':'Brazil nuts, grains, eggs','Selenium-enriched yeast':None,'Silicon dioxide':'Sand/quartz; spices (anti-caking)','Phosphoric acid':'Colas','Calcium lactate':'Aged cheese crystals','Magnesium sulphate':'Epsom salt; mineral waters','Calcium malate':'Apples (as malate)','Calcium hydroxide':'Pickling lime; corn tortillas','Sodium lactate':'Meat (formed from lactic acid)'}
TRACE=[('Vanadium','Ultratrace element','Insulin-like effects in studies; essentiality unproven','Mushrooms, shellfish, black pepper, parsley'),
 ('Nickel','Ultratrace element','Possible role in some enzymes; essentiality unproven in humans','Cocoa, nuts, legumes, oats'),
 ('Cobalt','Trace element (center of vitamin B12)','Needed only as part of B12','Meat, fish, dairy (as B12)'),
 ('Lithium','Ultratrace element','Possible mood effects at trace levels; essentiality unproven','Grains, vegetables, mineral waters'),
 ('Strontium','Ultratrace element chemically similar to calcium','Incorporated into bone; no known essential role','Seafood, whole grains, root vegetables'),
 ('Germanium','Ultratrace element','No proven role; organic supplements linked to kidney harm','Garlic, ginseng, mushrooms (traces)'),
 ('Sulfur','Element in methionine, cysteine, taurine','Protein structure, glutathione','Eggs, meat, garlic, onions, broccoli')]
def lines():
    o=[' Vitamins']
    fat=[v for v in V if 'fat-soluble' in v[0]];wat=[v for v in V if 'fat-soluble' not in v[0]]
    for title,grp in (('Fat-soluble vitamins',fat),('Water-soluble vitamins',wat)):
        o.append('  '+title)
        for v,role,src,forms in grp:
            o.append('   '+v.replace(' (fat-soluble)',''))
            for n,w,f in forms: o.append(f'    {n}|{w}|{role}|{f if f else FORT+"Natural sources: "+src}')
    o.append('  Vitamin-like nutrients')
    for n,w,d,f in VL:o.append(f'   {n}|{w}|{d}|{f}')
    o.append(' Minerals');o.append('  Elements and their permitted forms')
    for m,role,src,forms in MIN:
        o.append('   '+m)
        for f in forms:
            nf=NAT.get(f.replace(' (as P source)','').replace(' (as Cl source)',''))
            o.append(f'    {f}|Compound used to add {m.lower()} to foods or supplements|{role}|{nf+". " if nf else FORT}Natural sources of {m.lower()}: {src}')
    o.append('  Other trace and ultratrace elements')
    for n,w,d,f in TRACE:o.append(f'   {n}|{w}|{d}|{f}')
    return o
