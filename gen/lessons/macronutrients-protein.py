# ---------------- Module 1 · Protein ----------------
P_=mk_lmol('macronutrients-protein')
def _aa(n): return P_.D[n]['formula']
# Figure 1: family tree (Fats Figure 1 style), drawn as a build-up: amino acids -> peptide bonds -> peptide -> folded protein -> what proteins do.
# Food sits to the right as the SOURCE: its protein is digested (dashed arrow) back to amino acids, which feed the top of the chain.
PT_NODES=[(450,50,220,'Amino acids','20 building blocks · Fig. 2','nd l','#fig-2'),
 (150,150,190,'Essential','9 · must eat · Fig. 4','nd u','#fig-4'),(150,240,190,'Non-essential','11 · body makes','nd s','#fig-4'),(150,340,190,'Conditional','6 of the 11 · Fig. 4','nd s','#fig-4'),
 (450,190,220,'Peptide','short chain, 2 to ~50','nd l','#fig-3'),
 (450,330,240,'Protein','longer chain, folded · Fig. 5','nd root','#fig-5'),
 (780,50,200,'Food','the source · Fig. 7','nd l','#fig-7'),
 (790,150,170,'Complete','all 9 essentials','nd u','#fig-7'),(790,240,170,'Incomplete','low in 1 or more','nd t','#fig-7'),(790,340,170,'Combine them','beans + grains','nd t','#fig-7'),
 (120,460,180,'Muscle','structure · Fig. 6','nd l','#fig-6'),(340,460,180,'Enzymes','speed reactions · Fig. 5','nd l','#fig-5'),
 (560,460,180,'Antibodies','fight germs · Fig. 6','nd l','#fig-6'),(780,460,180,'Hemoglobin','carries oxygen · Fig. 5','nd l','#fig-5')]
PT_EDGES=[('side',340,50,245,150),('side',340,50,245,240),(150,272,150,318),
 ('line',700,82,700,240),('line',700,150,705,150),('line',700,240,705,240),(790,272,790,318),
 (450,362,120,438),(450,362,340,438),(450,362,560,438),(450,362,780,438)]
PT_EXTRA=['<path class="edge" d="M450,84 L450,164" marker-end="url(#lar)"/>',
 '<a class="tlk" href="#fig-3"><text class="lab hotl" x="464" y="130">peptide bonds · Fig. 3</text></a>',
 '<path class="edge" d="M450,224 L450,304" marker-end="url(#lar)"/>',
 '<a class="tlk" href="#fig-5"><text class="lab hotl" x="464" y="270">longer chain folds</text></a>',
 '<path class="edge dash" d="M678,50 L564,50" marker-end="url(#lar)"/>',
 '<a class="tlk" href="#fig-6"><text class="lab hotl" x="620" y="38" text-anchor="middle">digestion</text><text class="lab hotl" x="620" y="72" text-anchor="middle">Fig. 6</text></a>']
P1=('<!--noart-->'+ftree(PT_NODES,PT_EDGES,500,'Build-up diagram of protein. Amino acids, 20 in all (9 essential, 11 non-essential of which 6 are conditionally essential), are joined by peptide bonds into a chain. A short chain, up to about 50, is a peptide; a longer chain folds into a working protein: muscle, enzymes, antibodies, hemoglobin. Food is the source: its protein (complete, incomplete, or combined) is digested back down to amino acids, which feed the start of the chain.',PT_EXTRA)
 +lblock('label','Protein on a food label',[('Protein (grams)','Every gram gives about 4 kcal, the same as carbohydrate. The grams are total protein, whatever the source.'),
   ('%DV is often missing','In the US the % Daily Value for protein is optional unless the package makes a protein claim or the food is for young children; then it is adjusted for protein quality.'),
   ('Not listed: which amino acids','The label doesn’t say whether a protein is complete. Figure 7 shows how to tell from the food itself.')]))
# Figure 2: atoms to an amino acid
P2=('<!--noart-->'+molbox('atoms','Four atoms, four ways to bond',[
   mcell(P_('methane','Methane, CH4: one carbon with four hydrogens',[],'Methane, CH4'),'Carbon makes 4 bonds','methane, CH<sub>4</sub>'),
   mcell(P_('ammonia','Ammonia, NH3: one nitrogen with three hydrogens',[],'Ammonia, NH3'),'Nitrogen makes 3','ammonia, NH<sub>3</sub>'),
   mcell(P_('water','Water, H2O: one oxygen with two hydrogens',[],'Water, H2O'),'Oxygen makes 2','water, H<sub>2</sub>O'),
   mcell(P_('h2s','Hydrogen sulfide, H2S: one sulfur with two hydrogens',[],'Hydrogen sulfide, H2S'),'Sulfur makes 2','hydrogen sulfide, H<sub>2</sub>S')],
   fx='<p class="mfact">Hydrogen makes just 1 bond. Every amino acid is built from these few atoms: carbon, hydrogen, oxygen and nitrogen, plus sulfur in two of them. Nitrogen is the atom that fats and carbohydrates don’t have.</p>',head='The atoms').replace('<div class="art mols" data-part="atoms"><p class="mt">Four atoms, four ways to bond</p>','<div class="art mols" data-part="atoms"><p class="mt">Four atoms, four ways to bond</p><div class="mgrid">',1).replace('<p class="mfact">Hydrogen','</div><p class="mfact">Hydrogen',1)
 +molbox('glycine','Glycine, '+fsub(_aa('glycine'))+' <small>the simplest amino acid</small>',[P_('glycine','Glycine: an amine group (NH2) on the left, a central carbon with two hydrogens, and a carboxyl group (COOH) on the right; every hydrogen shown',
   [('amine','1',-0.85,-0.6),('alpha','2',0,1.0),('carboxyl','3',0.9,-0.9)],'Glycine, C2H5NO2',eager=True)],
   [('1','<b>Amine group</b> (NH<sub>2</sub>): a nitrogen with two hydrogens. This is the “amino” in amino acid.',''),('2','<b>Alpha carbon</b>: the centre that everything hangs on.',''),('3','<b>Carboxyl group</b> (COOH): the “acid”. Its OH can give up a hydrogen.','')],head='The amino acid')
 +molbox('alanine','Alanine, '+fsub(_aa('alanine')),[P_('alanine','Alanine: the same amine, alpha carbon and carboxyl as glycine, with a CH3 side chain pointing up; every hydrogen shown',
   [('amine','1',-0.6,0.45),('alpha','2',0.15,0.75),('carboxyl','3',0.9,-0.9),('r','4',0.95,0)],'Alanine, C3H7NO2')],
   [('1','<b>Amine group</b>, same as glycine.',''),('2','<b>Alpha carbon</b>, same as glycine.',''),('3','<b>Carboxyl group</b>, same as glycine.',''),('4','<b>Side chain</b> (R group): here a CH<sub>3</sub>. Glycine’s side chain is just one hydrogen. The side chain is the only part that differs between the 20 amino acids.','')])
 +legend('c h o n s'))
# Figure 3: peptide bond
P3=('<!--noart--><div class="part">Two amino acids join</div><div class="art mols" data-part="join"><div class="pair rx">'
 +'<div class="pc"><p class="mt">Glycine</p>'+P_('glycine','Glycine',[('carboxyl','1',0.9,-0.9)],'Glycine')+'</div><div class="op">+</div>'
 +'<div class="pc"><p class="mt">Alanine</p>'+P_('alanine','Alanine',[('amine','2',-0.2,-0.95)],'Alanine')+'</div></div><div class="pair rx"><div class="op">→</div>'
 +'<div class="pc"><p class="mt">Glycyl-alanine, '+fsub(_aa('glyala'))+'</p>'+P_('glyala','Glycyl-alanine dipeptide: glycine and alanine joined by a C(=O)-NH peptide bond in the middle; every hydrogen shown',[('peptide','3',0,-0.6)],'Glycyl-alanine dipeptide, C5H10N2O3')+'</div><div class="op">+</div>'
 +'<div class="pc"><p class="mt">Water</p>'+P_('water','Water, H2O, released when the bond forms',[],'Water, H2O')+'</div></div>'
 +mleg([('1','The OH of glycine’s carboxyl group…',''),('2','…and one H of alanine’s amine group leave together as a water molecule.',''),('3','<b>Peptide bond</b>: the carbon of one amino acid now bonds straight to the nitrogen of the next (C–N), next to its C=O. This bond is strong and flat.','')])
 +'</div>'+molbox('tripeptide','A tripeptide: Gly-Ala-Ser, '+fsub(_aa('glyalaser')),[P_('glyalaser','Tripeptide glycine-alanine-serine: three amino acids joined by two peptide bonds in a zigzag backbone, with the side chains alternating up and down; every hydrogen shown',
   [('amine','N',-0.4,-0.8,'tx'),('pep1','1',0,-0.6),('pep2','2',0,0.6),('carboxyl','C',0.95,-0.4,'tx')],'Tripeptide Gly-Ala-Ser, C8H15N3O5')],
   [('1','First peptide bond.',''),('2','Second peptide bond. Each new amino acid adds one more and releases one more water.',''),('N','<b>N-terminus</b>: a free amine group starts every chain.','tx'),('C','<b>C-terminus</b>: a free carboxyl group ends it.','tx')],
   fx='<p class="mfact">The repeating N–C–C, N–C–C pattern is the <b>backbone</b>. A chain of up to about 50 amino acids is usually called a peptide; longer ones are proteins. Most proteins are a few hundred amino acids long.</p>',head='A chain grows')
 +legend('c h o n'))
# Figure 4: the 20 amino acids
def _c(n,label,code,ess=False,sub=''):
    return mcell(P_(n,f'{label} ({code}), {_aa(n)}: amine and carboxyl at the bottom, side chain pointing up; every hydrogen shown',[('r','',0,0,'hid')] if False else [],f'{label} ({code}), {_aa(n)}'),f'{label}'+(' <span class="ess">essential</span>' if ess else ''),f'{code} · {sub}' if sub else code)
ESS=[('histidine','Histidine','His','ring with nitrogens'),('isoleucine','Isoleucine','Ile','branched'),('leucine','Leucine','Leu','branched'),('lysine','Lysine','Lys','ends in NH₂'),
 ('methionine','Methionine','Met','has sulfur'),('phenylalanine','Phenylalanine','Phe','benzene ring'),('threonine','Threonine','Thr','has OH'),('tryptophan','Tryptophan','Trp','double ring'),('valine','Valine','Val','branched')]
COND=[('arginine','Arginine','Arg'),('cysteine','Cysteine','Cys'),('glutamine','Glutamine','Gln'),('glycine','Glycine','Gly'),('proline','Proline','Pro'),('tyrosine','Tyrosine','Tyr')]
NON=[('alanine','Alanine','Ala'),('asparagine','Asparagine','Asn'),('aspartate','Aspartic acid','Asp'),('glutamate','Glutamic acid','Glu'),('serine','Serine','Ser')]
P4=('<!--noart--><div class="part">The 9 essential amino acids</div>'+mgrid('essential',[_c(n,l,c,True,s) for n,l,c,s in ESS])
 +'<div class="part">The 6 conditionally essential</div>'+mgrid('conditional',[_c(n,l,c,False,'conditional') for n,l,c in COND])
 +'<div class="part">The 5 non-essential</div>'+mgrid('nonessential',[_c(n,l,c) for n,l,c in NON])+legend('c h o n s')
 +table('esstable',['Essential','What its side chain does','In your body'],[
  ['Leucine, isoleucine, valine','Branched carbon chains (the BCAAs); oily, so they sit inside proteins','Plentiful in muscle protein; leucine also signals muscle to build protein'],
  ['Lysine','Long chain ending in NH<sub>2</sub>, charged','Collagen cross-links, carnitine; often the lowest essential amino acid in grains'],
  ['Methionine','Contains sulfur','Starts nearly every new protein chain; the body makes cysteine from it; often lowest in beans'],
  ['Phenylalanine','Benzene ring','The body makes tyrosine from it. People with PKU can’t, which is why aspartame labels warn about it'],
  ['Tryptophan','Largest: a double ring with nitrogen','Raw material for serotonin and melatonin, and some niacin (vitamin B3)'],
  ['Threonine','Has an OH group','Part of mucus proteins that line the gut; collagen'],
  ['Histidine','Ring with two nitrogens','Raw material for histamine; part of hemoglobin’s iron pocket']],'What the essential ones do'))
# Figure 5: structure (stages: small drawings, all text page HTML)
_BC=['#3E5C76','#7A8256','#A86B53','#5F7F99','#8E7A4A','#6E8C70']
_beads='<div class="beads" role="img" aria-label="A chain of amino acid beads: Gly, Ala, Ser, Leu, Lys, Glu, Phe, Val, His, Met, Trp">'+''.join(f'<span style="background:{_BC[k%6]}">{c}</span>' for k,c in enumerate(['Gly','Ala','Ser','Leu','Lys','Glu','Phe','Val','His','Met','Trp']))+'</div>'
_helix=''.join(f'<path d="M{20+k*26},40 q13,40 26,0" fill="none" style="stroke:var(--acc)" stroke-width="7" stroke-linecap="round"/><path d="M{33+k*26},40 q13,-40 26,0" fill="none" stroke="#9fb3c4" stroke-width="7" stroke-linecap="round"/>' for k in range(8))
_sheet=''.join(f'<path d="M{300},{14+k*28} h150 l0,-8 l22,14 l-22,14 l0,-8 h-150z" fill="#7A8256" opacity="{0.95-k*0.15:.2f}"/>' for k in range(3))
_sec=svgd(_helix+_sheet,'0 0 500 90','Alpha helix drawn as a spiral ribbon, and beta sheet drawn as three parallel arrows',420)+'<div class="sgl"><span>alpha helix (spiral)</span><span>beta sheet (strands side by side)</span></div>'
_ter=svgd('<path d="M60,90 C60,30 140,20 160,60 S230,120 250,70 S200,10 280,20 S360,90 320,120 S220,140 180,110 S110,150 90,120" fill="none" style="stroke:var(--acc)" stroke-width="8" stroke-linecap="round"/>','30 0 340 160','A single chain folded into a compact knot-like shape',300)
_qua=svgd(''.join(f'<ellipse cx="{x}" cy="{y}" rx="44" ry="34" fill="{c}"/><circle cx="{x}" cy="{y}" r="9" fill="#E06633" stroke="#7a2a0a" stroke-width="2"/>' for x,y,c in ((50,40,'#3E5C76'),(130,40,'#7A8256'),(50,102,'#7A8256'),(130,102,'#3E5C76'))),'0 0 180 142','Hemoglobin drawn as four chains packed together, each with an orange iron-containing heme',170)
P5=('<!--noart-->'+stages('levels','Four levels of structure',[
   ('1 · Primary: the order of amino acids',_beads,'Set by your genes. Change one amino acid and the whole protein can change: sickle-cell hemoglobin differs from normal hemoglobin by a single swap.'),
   ('2 · Secondary: local coils and sheets',_sec,'Held by hydrogen bonds between the C=O of one peptide bond and the N–H of another.'),
   ('3 · Tertiary: the whole chain folds',_ter,'Oily side chains tuck inside, water-loving ones face out, and sulfur cross-links between cysteines can hold the fold. The shape decides the job.'),
   ('4 · Quaternary: chains team up',_qua,'Hemoglobin is 4 chains, each holding one heme with an iron atom (orange) that carries oxygen.')],
   cap='Cartoons, not to scale: each bead is a whole amino acid, and each ribbon is a stretch of chain.')
 +note('denature','Cooking unfolds proteins','<p>Heat, acid, salt or whipping break the weak bonds that hold the folds, so the chain unravels: this is <b>denaturing</b>. Egg white turns from clear to white, milk curdles with lemon juice, meat firms up. The peptide bonds stay, so the amino acids are all still there; your stomach does the same thing with acid.</p>'))
# Figure 6: digestion and use
_st=[('Mouth','chewing only; no protein digestion'),('Stomach','acid unfolds proteins; pepsin cuts them into shorter pieces'),('Small intestine','trypsin and chymotrypsin from the pancreas, then enzymes on the gut wall, cut down to single amino acids and pairs or threes'),
 ('Into the blood','absorbed and carried to the liver first'),('The amino acid pool','your body’s supply, used to build proteins all day')]
P6=('<!--noart-->'+flow('path','From plate to amino acids',_st,cap='The small intestine also absorbs some pairs and threes of amino acids, which are split inside the gut-wall cells.')
 +lblock('uses','What the pool is used for',[('Building','Muscle, skin, hair, bone matrix (collagen) and the lining of the gut, all constantly broken down and rebuilt.'),
   ('Working proteins','Enzymes that run chemical reactions, antibodies, hemoglobin and other carriers, and hormones such as insulin.'),
   ('Fuel, last','Amino acids not needed for building are burned for energy (4 kcal per gram) or turned into glucose or fat. The body doesn’t store spare protein.')])
 +molbox('urea','Urea, '+fsub(_aa('urea'))+' <small>how the nitrogen leaves</small>',[P_('urea','Urea: a carbon with a C=O and two NH2 groups; every hydrogen shown',[('n1','1',-0.1,-0.95),('n2','1',0.1,-0.95)],'Urea, CH4N2O')],
   [('1','<b>Two nitrogens</b>: when an amino acid is burned, its amine group comes off as ammonia, which is toxic. The liver packs it into urea, and the kidneys send it out in urine.','')],
   fx=facts(body='Protein builds and repairs every tissue and makes enzymes, antibodies and many hormones.',
    low='Too little over time causes muscle loss, slow healing, weaker immunity, thin hair and, in severe shortage, swelling from fluid (kwashiorkor) and poor growth in children.',
    high='Extra protein is burned or stored as fat, and makes more urea to clear, so you need a little more water. Very high intakes are a concern mainly for people with kidney disease.'),head='Getting rid of the nitrogen')+legend('c h o n'))
# Figure 7: complete vs incomplete
P7=('<!--noart-->'+table('foods',['Food','Protein type','Lowest essential amino acid'],[
  ['Meat, poultry, fish','Complete','none'],['Eggs, milk, yogurt, cheese','Complete','none'],['Soybeans (tofu, tempeh, edamame)','Complete','none really (methionine a little low)'],
  ['Quinoa, buckwheat','Complete, or close','none really'],['Beans, lentils, peas, chickpeas','Incomplete','methionine (and cysteine)'],['Wheat, rice, oats, corn','Incomplete','lysine'],
  ['Nuts and seeds','Incomplete','lysine (most)']],'Complete and incomplete foods')
 +lblock('combine','Putting plant proteins together',[('Limiting amino acid','A protein is only as useful as its scarcest essential amino acid. Your body can’t build a protein when one is missing.'),
   ('Beans + grains','Beans are low in methionine but rich in lysine; grains are the opposite. Together they cover each other: rice and beans, hummus and pita, peanut butter on whole-wheat bread.'),
   ('Over the day is fine','The amino acid pool lasts for hours, so the foods don’t have to be eaten in the same meal, just over the course of the day.')])
 +lblock('need','How much you need',[('Adults: 0.8 g per kg','The US RDA is 0.8 grams of protein per kilogram of body weight per day: about 56 g for a 70 kg (154 lb) adult.'),
   ('More at some stages','Pregnancy and breastfeeding need more; growing children need more per kilogram; some research suggests older adults benefit from a little more.'),
   ('Found in','Meat, poultry, fish, eggs, dairy, beans, lentils, peas, soy, nuts, seeds and whole grains.')]))
# Figure 8: putting it all together
P8=('<!--noart-->'+table('table',['Idea','In one line','See'],[
  ['Atoms','C, H, O and N (plus S): nitrogen is what sets protein apart from fat and carbohydrate','<a href="#fig-2">Figure 2</a>'],
  ['Amino acid','Amine + alpha carbon + carboxyl + one side chain','<a href="#fig-2">Figure 2</a>'],
  ['Peptide bond','Carboxyl of one joins the amine of the next; one water released','<a href="#fig-3">Figure 3</a>'],
  ['20 amino acids','9 essential, 6 conditionally essential, 5 non-essential','<a href="#fig-4">Figure 4</a>'],
  ['Shape','Primary, secondary, tertiary, quaternary; cooking unfolds it','<a href="#fig-5">Figure 5</a>'],
  ['Digestion','Back to amino acids; nitrogen leaves as urea','<a href="#fig-6">Figure 6</a>'],
  ['Food','Animal foods and soy are complete; combine beans and grains','<a href="#fig-7">Figure 7</a>']],'The whole lesson in one table')
 +worth([('Protein powders are just protein','Whey and casein come from milk, and pea and soy powders from those plants. They give the same amino acids as the whole foods, without the fibre, vitamins and minerals that come along in the food.'),
   ('Collagen is incomplete','Collagen, the most common protein in your body, is rich in glycine and proline but has almost no tryptophan, so on its own it’s an incomplete protein.'),
   ('Gelatin is cooked collagen','Simmering bones and skin unfolds collagen into gelatin, which sets into a gel as it cools.'),
   ('Protein quality scores','PDCAAS and DIAAS score proteins by their essential amino acids and how well they are digested. Milk, eggs and soy score near the top.')]))
PROTEIN_LESSON=[('The Protein Family Tree','Amino acids build up into peptides and proteins; food supplies the amino acids.',P1),
 ('From Atoms to an Amino Acid','Four kinds of atom, one shared backbone, one side chain that changes.',P2),
 ('The Peptide Bond','Amino acids join head to tail and release water.',P3),
 ('The 20 Amino Acids','Same backbone, 20 side chains; 9 you must eat.',P4),
 ('From Chain to Shape','Four levels of structure, and why cooking changes protein.',P5),
 ('Digestion and Use','Back to amino acids, into the pool, and out as urea.',P6),
 ('Complete and Incomplete Protein','Which foods have all 9 essentials, and how to combine the rest.',P7),
 ('Putting It All Together','The whole lesson in one table, plus a few extras.',P8)]
PROTEIN_QUIZ=[('How many kcal does a gram of protein give?','About 4, the same as carbohydrate (Figure 1).'),
 ('Which atom do proteins have that fats and carbohydrates don’t?','Nitrogen, in the amine group of every amino acid (Figure 2).'),
 ('What three parts do all amino acids share, and what part differs?','An amine group, an alpha carbon and a carboxyl group are shared; the side chain (R group) differs (Figure 2).'),
 ('What is released when a peptide bond forms?','One water molecule: an OH from one amino acid’s carboxyl and an H from the next one’s amine (Figure 3).'),
 ('How many amino acids are essential? Name three.','Nine: histidine, isoleucine, leucine, lysine, methionine, phenylalanine, threonine, tryptophan, valine (Figure 4).'),
 ('Which essential amino acid contains sulfur?','Methionine (cysteine, a conditionally essential one, has sulfur too) (Figure 4).'),
 ('What does cooking an egg do to its proteins?','It denatures them: the folds unravel, but the peptide bonds and amino acids stay (Figure 5).'),
 ('Where does protein digestion start, and which enzyme begins it?','In the stomach, where acid unfolds proteins and pepsin starts cutting them (Figure 6).'),
 ('What happens to the nitrogen when amino acids are burned for energy?','It comes off as ammonia, the liver turns it into urea, and the kidneys remove it in urine (Figure 6).'),
 ('Why do rice and beans go well together?','Grains are low in lysine and beans in methionine; each supplies what the other lacks (Figure 7).'),
 ('What is the US RDA for protein for adults?','0.8 grams per kilogram of body weight per day, about 56 g for a 70 kg adult (Figure 7).'),
 ('Is collagen a complete protein?','No; it has almost no tryptophan (Figure 8).')]
build_lesson('macronutrients-protein','Protein','Protein from the atoms up: the four kinds of atom in an amino acid, the shared backbone and changing side chain, the peptide bond, all 20 amino acids drawn at one scale, how chains fold into working shapes, how you digest and use protein, and which foods give you all 9 essential amino acids. The figure is on the left and the lesson script on the right; the quiz is at the end.',PROTEIN_LESSON,PROTEIN_QUIZ,mols=P_)
