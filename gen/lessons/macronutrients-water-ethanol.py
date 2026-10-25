# ---------------- Module 1 · Water and Ethanol ----------------
W_=mk_lmol('macronutrients-water-ethanol')
def _wf(n): return fsub(W_.D[n]['formula'])
# Figure 1: family tree (Fats Figure 1 style)
WE_NODES=[(450,30,240,'Water and Ethanol','the last two','nd root',None),
 (240,150,230,'Water','0 kcal · Fig. 2','nd l','#fig-2'),(660,150,230,'Ethanol','7 kcal/g · Fig. 5','nd l','#fig-5'),
 (130,290,190,'The molecule','bent and polar · Fig. 2','nd u','#fig-2'),(350,290,190,'In your body','about 60% of you · Fig. 3','nd u','#fig-3'),
 (560,290,190,'Fermentation','sugar to alcohol · Fig. 5','nd t','#fig-5'),(780,290,190,'In the liver','broken down · Fig. 6','nd t','#fig-6'),
 (130,410,190,'Dissolves things','salt, sugar · Fig. 2','nd u','#fig-2'),(350,410,190,'Balance','in equals out · Fig. 4','nd u','#fig-4'),
 (560,410,190,'Methanol','its toxic cousin · Fig. 5','nd t','#fig-5'),(780,410,190,'Effects','short and long term · Fig. 6','nd t','#fig-6')]
WE_EDGES=[(450,52,240,128),(450,52,660,128),(240,182,130,268),(240,182,350,268),(660,182,560,268),(660,182,780,268),(130,322,130,388),(350,322,350,388),(560,322,560,388),(780,322,780,388)]
P1=('<!--noart-->'+ftree(WE_NODES,WE_EDGES,450,'Tree diagram: water (the molecule, which dissolves things; water in your body, kept in balance) and ethanol (made by fermentation, with methanol as its toxic cousin; broken down in the liver, with short- and long-term effects)')
 +lblock('label','Why these two',[('Water: the nutrient you need most','It gives no calories, but you can live only a few days without it. It is the main ingredient of your body and of most whole foods.'),
   ('Ethanol: calories, not a nutrient','The alcohol in drinks gives 7 kcal per gram, nearly as much as fat, but your body has no need for it and treats it as something to clear.'),
   ('On labels','Water appears only in ingredient lists. In the US most beer, wine and spirits are labeled under separate rules, so they show alcohol by volume rather than a Nutrition Facts panel.')]))
# Figure 2: the water molecule
def _hbonds():
    import math
    # O centres; donors: (i, j) = one H of molecule i points at the O of molecule j
    P=[(150,100),(70,60),(250,60),(80,170),(240,165),(160,20)]
    don={0:2,1:0,3:0,4:0,5:2}
    rot={2:200}
    out=[];lines=[]
    for i,(x,y) in enumerate(P):
        if i in don:
            jx,jy=P[don[i]]; a=math.degrees(math.atan2(jy-y,jx-x))
        else: a=rot[i]
        hs=[a,a+104.5]
        for k,h in enumerate(hs):
            hx=x+26*math.cos(math.radians(h)); hy=y+26*math.sin(math.radians(h))
            out.append(f'<line x1="{x}" y1="{y}" x2="{hx:.1f}" y2="{hy:.1f}" stroke="#888" stroke-width="5"/>')
            out.append(f'<circle cx="{hx:.1f}" cy="{hy:.1f}" r="9" fill="#f4f4f4" stroke="#777" stroke-width="2"/>')
            if k==0 and i in don:
                jx,jy=P[don[i]]; L=math.hypot(jx-hx,jy-hy); ux,uy=(jx-hx)/L,(jy-hy)/L
                lines.append(f'<line x1="{hx+ux*11:.1f}" y1="{hy+uy*11:.1f}" x2="{jx-ux*18:.1f}" y2="{jy-uy*18:.1f}" style="stroke:var(--acc)" stroke-width="3" stroke-dasharray="4 4"/>')
        out.append(f'<circle cx="{x}" cy="{y}" r="16" fill="#E02424" stroke="#8a1010" stroke-width="2"/>')
    return ''.join(lines)+''.join(out)
P2=('<!--noart-->'+molbox('water','Water, '+_wf('water'),[W_('water','Water: one oxygen in the middle bonded to two hydrogens, bent like a V; every hydrogen shown',[('c','1',0,-0.55),('h1','2',-0.35,0.3),('h2','2',0.35,0.3)],'Water, H2O',eager=True)],
   [('1','<b>Oxygen</b> makes two bonds. It pulls the shared electrons toward itself, so it carries a slight negative charge.',''),('2','<b>Hydrogens</b>: each is left slightly positive. The bonds meet at about 104.5°, so the molecule is bent, not straight.','')],
   fx='<p class="mfact">One end slightly negative, the other slightly positive: water is a <b>polar</b> molecule. That one fact explains most of what water does.</p>',head='Two hydrogens, one oxygen')
 +stages('hbonds','Hydrogen bonds',[('Water molecules hold on to each other',svgd(_hbonds(),'25 -15 270 225','Six water molecules, each red oxygen with two white hydrogens; dashed lines join the hydrogen of one molecule to the oxygen of the next',300),
   'The slightly positive H of one water is drawn to the slightly negative O of another: a <b>hydrogen bond</b> (dashed). Each one is weak and lasts a split second, but there are so many that water stays liquid at body temperature, takes a lot of heat to warm up, and carries heat away when sweat evaporates.')],cap='Cartoon, not to scale: red = oxygen, white = hydrogen.')
 +lblock('dissolve','What water dissolves, and what it doesn’t',[('Salts','Water pulls table salt apart into sodium and chloride ions, each wrapped in water molecules. Minerals travel around your body this way.'),
   ('Sugars and many vitamins','Molecules covered in OH groups, like glucose and vitamin C, form hydrogen bonds with water and dissolve easily.'),
   ('Not fats','Long carbon-hydrogen chains have no charge to grab, so oil and water separate. That is why fats need bile to be digested and carriers to travel in blood (see Fats).')])
 +legend('h o'))
# Figure 3: water in your body
P3=('<!--noart-->'+table('howmuch',['Who or what','Water content'],[
  ['Newborn baby','about 75% of body weight'],['Adult man','about 60%'],['Adult woman','about 50 to 55% (more body fat, which holds little water)'],['Older adult','lower, as muscle declines'],
  ['Muscle and other lean tissue','about three quarters water'],['Fat tissue','much less water']],'How much of you is water')
 +lblock('where','Where the water is',[('Inside cells','About two thirds of your body water.'),('Between cells','Most of the remaining third bathes the cells.'),('In blood','A smaller share is plasma, the liquid part of blood, which is over 90% water. Water moves freely between these spaces, following salts such as sodium and potassium.')])
 +lblock('jobs','What water does',[('Dissolves and carries','Blood carries nutrients, oxygen, hormones and waste in water; urine carries waste out.'),
   ('Keeps temperature steady','Sweat takes heat with it as it evaporates. Water also holds heat well, so body temperature changes slowly.'),
   ('Takes part in chemistry','Digestion adds water back into every peptide and glycosidic bond (hydrolysis). Water also cushions the brain and spinal cord, lubricates joints and keeps eyes and mouth moist.')]))
# Figure 4: balance and needs
P4=('<!--noart-->'+lblock('inout','Water in, water out',[('In: drinks','Most of your water: plain water, milk, tea, coffee and other drinks all count.'),
   ('In: food and your own cells','About a fifth comes from food; fruit and vegetables are mostly water. Your cells also make about a cup a day when they burn fuel (metabolic water).'),
   ('Out','Urine (the biggest share), sweat, the moisture in every breath, and a little in stool. Heat, exercise, fever, vomiting and diarrhea all raise losses.')])
 +flow('control','How your body keeps it level',[('Water runs low','blood becomes slightly more concentrated'),('Thirst','the brain senses it and you feel thirsty'),('Vasopressin','the pituitary releases this hormone (also called antidiuretic hormone, ADH)'),('Kidneys save water','urine becomes smaller in volume and darker'),('Balance restored','when you drink, the signals switch off')])
 +table('foods',['Whole food','Approximate water'],[['Cucumber, lettuce, celery','about 95%'],['Watermelon, strawberries, tomatoes','about 90 to 95%'],['Oranges, apples, milk','about 85 to 90%'],['Cooked oats, cooked rice','about 70 to 85%'],['Bread','about 35%'],['Nuts','under 10%']],'Water in whole foods')
 +lblock('need','How much you need',[('Adequate intake','The US Institute of Medicine set total water (from drinks and food together) at about 2.7 liters a day for women and 3.7 liters for men, roughly 80% from drinks. Needs rise with heat, exercise, pregnancy and breastfeeding.'),
   ('Too little','Dehydration: thirst, dark urine, headache, tiredness and dizziness; severe loss is dangerous, especially for babies and older adults, whose thirst signal is weaker.'),
   ('Too much','Drinking far more than the kidneys can clear in a short time dilutes blood sodium (hyponatremia), which can be dangerous; it is rare and mostly seen in long endurance events.')]))
# Figure 5: ethanol from atoms, fermentation, methanol
P5=('<!--noart-->'+molbox('build','From ethane to ethanol',[
   '<div class="mgrid">'+mcell(W_('ethane','Ethane, C2H6: two carbons, each with three hydrogens',[],'Ethane, C2H6'),'Ethane','C<sub>2</sub>H<sub>6</sub>, a gas')
   +mcell(W_('ethanol','Ethanol, C2H5OH: ethane with one hydrogen replaced by an OH group; every hydrogen shown',[('oh','1',0.1,-0.75)],'Ethanol, C2H6O'),'Ethanol','C<sub>2</sub>H<sub>5</sub>OH')+'</div>'],
   [('1','Swap one H of ethane for an <b>OH group</b> and you have ethanol. Any carbon chain carrying an OH like this is called an <b>alcohol</b>; ethanol is the one in drinks.','')],
   fx='<p class="mfact">The OH lets ethanol mix with water; the two-carbon end lets it slip through fatty cell membranes. So it spreads quickly into every tissue, including the brain.</p>'
   +facts(what='A two-carbon alcohol, C<sub>2</sub>H<sub>5</sub>OH, made by yeast from sugar.',body='Gives 7 kcal per gram but has no nutritional role; the liver breaks it down as a priority (Figure 6).',found='Beer, wine and spirits; tiny amounts in very ripe fruit, fruit juice and fermented foods such as kefir and kombucha.'),head='Ethanol')
 +'<div class="part">Fermentation: yeast turns sugar into alcohol</div><div class="art mols" data-part="ferment"><div class="pair rx">'
 +'<div class="pc"><p class="mt">Glucose</p>'+W_('glucose','Glucose ring drawn as a 3D model',[],'Glucose, C6H12O6')+'</div></div><div class="op" style="text-align:center;margin:6px 0">↓ <small style="font-size:.9rem">yeast, no oxygen</small></div><div class="pair rx">'
 +'<div class="pc"><p class="mt">2 × ethanol</p>'+W_('ethanol','Ethanol',[],'Ethanol')+'</div><div class="op">+</div>'
 +'<div class="pc"><p class="mt">2 × carbon dioxide</p>'+W_('co2','Carbon dioxide, CO2: a carbon with a double bond to an oxygen on each side',[],'Carbon dioxide, CO2')+'</div></div>'
 +'<p class="mfact">Without oxygen, yeast splits each glucose into two ethanols and two CO<sub>2</sub>: C<sub>6</sub>H<sub>12</sub>O<sub>6</sub> → 2 C<sub>2</sub>H<sub>5</sub>OH + 2 CO<sub>2</sub>. Count the atoms: nothing is lost. In bread the CO<sub>2</sub> makes the dough rise and the ethanol mostly bakes off; in wine and beer the ethanol stays.</p></div>'
 +molbox('methanol','Methanol, '+_wf('methanol')+' <small>one carbon fewer, far more dangerous</small>',[W_('methanol','Methanol: a single carbon with three hydrogens and an OH group; every hydrogen shown',[('oh','1',0.1,-0.75)],'Methanol, CH4O')],
   [('1','The same OH, on a one-carbon chain.','')],
   fx=facts(what='The simplest alcohol, CH<sub>3</sub>OH.',body='The liver turns it into formaldehyde and formic acid, which damage the optic nerve and other tissues.',
    high='Drinking even small amounts of pure methanol can cause blindness or death; it is a danger in illegally distilled spirits.',
    found='Tiny, harmless amounts in fruit and vegetable juices, formed from pectin.'),head='Methanol')
 +legend('c h o'))
# Figure 6: how the body handles ethanol
P6=('<!--noart-->'+flow('path','From glass to liver',[('Stomach','some ethanol is absorbed here; food in the stomach slows the rest'),('Small intestine','most is absorbed here, quickly'),('Blood','ethanol spreads through all body water, so the same drink gives a smaller body a higher blood level'),('Liver','breaks down roughly one standard drink an hour; it can’t be hurried'),('Lungs, urine, skin','a few percent leaves unchanged: the basis of breath tests')])
 +'<div class="part">Two steps in the liver</div><div class="art mols" data-part="steps"><div class="pair rx">'
 +'<div class="pc"><p class="mt">Ethanol</p>'+W_('ethanol','Ethanol',[('c2','1',0,0.65)],'Ethanol, C2H6O')+'</div><div class="op">→</div>'
 +'<div class="pc"><p class="mt">Acetaldehyde</p>'+W_('acetaldehyde','Acetaldehyde: two carbons, the second with a double-bonded oxygen and one hydrogen; every hydrogen shown',[('o','2',0.5,0.1)],'Acetaldehyde, C2H4O')+'</div></div><div class="op" style="text-align:center;margin:6px 0">↓ <small style="font-size:.9rem">aldehyde dehydrogenase</small></div><div class="pair rx">'
 +'<div class="pc"><p class="mt">Acetic acid (acetate)</p>'+W_('acetic','Acetic acid: two carbons, the second with a double-bonded oxygen and an OH group; every hydrogen shown',[('acid','3',0.65,0.1)],'Acetic acid, C2H4O2')+'</div></div>'
 +mleg([('1','<b>Alcohol dehydrogenase</b> takes two hydrogens off ethanol…',''),('2','…making <b>acetaldehyde</b>, a toxic, reactive molecule that causes much of alcohol’s damage.',''),('3','<b>Aldehyde dehydrogenase</b> adds an oxygen, making <b>acetate</b> (the same molecule as in vinegar), which cells burn for energy or turn into fat.','')])
 +'<p class="mfact">Many people of East Asian descent carry a slow version of the second enzyme, so acetaldehyde builds up and the face flushes after even a small drink.</p></div>'
 +table('drink',['US standard drink (14 g ethanol)','Typical serving'],[['Beer, about 5% alcohol','12 fl oz (355 ml)'],['Wine, about 12%','5 fl oz (148 ml)'],['Spirits, about 40%','1.5 fl oz (44 ml)']],'What counts as one drink')
 +lblock('effects','Effects on the body',[('Short term','Slower reactions and judgment, more urine (alcohol blocks vasopressin), poorer sleep; large amounts at once can cause alcohol poisoning, which can be fatal.'),
   ('Long term, heavy use','Fatty liver, alcoholic hepatitis and cirrhosis; high blood pressure and heart rhythm problems; dependence. Heavy drinkers often run short of thiamine (vitamin B1) and folate.'),
   ('Cancer and pregnancy','The WHO’s cancer agency classifies alcoholic drinks as a cause of cancer (mouth, throat, esophagus, liver, breast, bowel), with risk rising with amount. No amount is known to be safe in pregnancy. Less is better for health.')])
 +legend('c h o'))
# Figure 7: putting it all together
P7=('<!--noart-->'+table('table',['Molecule','Formula','Energy','In your body','Found in'],[
  ['Water','H<sub>2</sub>O','0 kcal','about 60% of you; solvent, temperature, chemistry','drinks, fruit, vegetables, milk'],
  ['Ethanol','C<sub>2</sub>H<sub>5</sub>OH','7 kcal/g','no role; cleared by the liver','beer, wine, spirits; traces in ripe fruit'],
  ['Methanol','CH<sub>3</sub>OH','—','toxic: becomes formaldehyde and formic acid','traces in fruit juices'],
  ['Acetaldehyde','C<sub>2</sub>H<sub>4</sub>O','—','toxic first breakdown product of ethanol','made in your liver'],
  ['Acetate','C<sub>2</sub>H<sub>3</sub>O<sub>2</sub><sup>−</sup>','burned for energy','second breakdown product; fuel','vinegar (as acetic acid); made by gut bacteria from fiber'],
  ['Carbon dioxide','CO<sub>2</sub>','—','breathed out as waste','made by yeast in bread and drinks']],'Every molecule in this lesson')
 +worth([('Coffee and tea count','Caffeine has only a mild effect on urine in regular drinkers, so coffee and tea still add to your daily water.'),
   ('Ice floats','Hydrogen bonds hold frozen water in an open lattice that is less dense than liquid water, so ice floats and lakes freeze from the top.'),
   ('Cooking doesn’t remove all the alcohol','A quick flambé or short simmer leaves most of it; long simmering or baking removes most, but rarely all.'),
   ('“Alcohol-free” isn’t always zero','In the US, “non-alcoholic” drinks can contain up to 0.5% alcohol; “alcohol-free” should contain none.')]))
WE_LESSON=[('The Water and Ethanol Family Tree','Two small molecules: one you can’t live without, one you don’t need.',P1),
 ('The Water Molecule','Bent, polar and sticky: why water dissolves so much.',P2),
 ('Water in Your Body','How much of you is water, where it is, and what it does.',P3),
 ('Water Balance','What comes in, what goes out, and how much you need.',P4),
 ('Ethanol','From ethane to ethanol, how yeast makes it, and its toxic cousin.',P5),
 ('How Your Body Handles Alcohol','Absorbed fast, cleared slowly, in two steps in the liver.',P6),
 ('Putting It All Together','The whole lesson in one table, plus a few extras.',P7)]
WE_QUIZ=[('How many kcal does a gram of ethanol give, and a gram of water?','About 7 for ethanol; 0 for water (Figure 1).'),
 ('Why is a water molecule polar?','Oxygen pulls the shared electrons toward itself, leaving the O slightly negative and the two H slightly positive, and the molecule is bent (Figure 2).'),
 ('What is a hydrogen bond?','A weak attraction between the slightly positive H of one molecule and the slightly negative O of another (Figure 2).'),
 ('Why don’t oil and water mix?','Fat chains have no charges or OH groups for water to grab, so they separate (Figure 2).'),
 ('Roughly how much of an adult’s body weight is water?','About 50 to 60%; more in babies (Figure 3).'),
 ('Where is most of your body water?','Inside cells, about two thirds of it (Figure 3).'),
 ('What hormone tells the kidneys to save water?','Vasopressin, also called antidiuretic hormone (Figure 4).'),
 ('What is the US adequate intake for total water?','About 2.7 L a day for women and 3.7 L for men, from drinks and food together (Figure 4).'),
 ('What does yeast make from one glucose during fermentation?','Two ethanols and two carbon dioxides (Figure 5).'),
 ('Why is methanol dangerous?','The liver turns it into formaldehyde and formic acid, which can cause blindness or death (Figure 5).'),
 ('What are the two steps that break down ethanol in the liver?','Ethanol to acetaldehyde (alcohol dehydrogenase), then acetaldehyde to acetate (aldehyde dehydrogenase) (Figure 6).'),
 ('How much pure ethanol is in a US standard drink?','14 g: about 12 fl oz of beer, 5 fl oz of wine or 1.5 fl oz of spirits (Figure 6).')]
build_lesson('macronutrients-water-ethanol','Water and Ethanol','The last two energy-related molecules of Module 1: water, which gives no calories but makes up most of your body, and ethanol, which gives calories but no nutrition. Built from the atoms up: why water is polar and sticky, how much of you is water and how the balance is kept, how yeast makes ethanol from sugar, and how your liver breaks it down. The figure is on the left and the lesson script on the right; the quiz is at the end.',WE_LESSON,WE_QUIZ,mols=W_,scale=8.5)
