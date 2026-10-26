# Module 6 · The Human Body: the interactive marble statue (gen/bodymap*.py, bodymap.css, bodymap.js) and where each nutrient goes.
exec(open(os.path.join(GEN,'bodymap_geo.py'),encoding='utf-8').read())
exec(open(os.path.join(GEN,'bodymap.py'),encoding='utf-8').read())
exec(open(os.path.join(GEN,'bodymap_widget.py'),encoding='utf-8').read())
# Figure 1: the body-map family tree (Fats Figure 1 style), food at the top, destinations at the bottom
HB_NODES=[(450,30,170,'Food','what you eat','nd root','#fig-4'),
 (450,140,190,'Digestion','mouth to gut','nd','#fig-3'),
 (180,250,200,'Blood road','sugars · amino','nd s','#fig-4'),
 (450,250,200,'Lymph road','fats · A D E K','nd u','#fig-4'),
 (720,250,200,'Large intestine','fiber · water','nd t','#fig-4'),
 (180,360,200,'Liver','first stop','nd s','#fig-3'),
 (720,360,200,'Gut bacteria','ferment fiber','nd t','#fig-4'),
 (450,470,210,'Bloodstream','heart pumps it','nd','#fig-2')]+[
 (x,590,136,t,s,'nd',h) for x,(t,s,h) in zip((80,228,376,524,672,820),(
  ('Brain','glucose · Fig. 4','#fig-4'),('Muscle','protein · Fig. 4','#fig-4'),('Fat tissue','fats · Fig. 4','#fig-4'),
  ('Bones','calcium · Fig. 5','#fig-5'),('Marrow','iron · Fig. 5','#fig-5'),('Kidneys','waste · Fig. 3','#fig-3')))]
HB_EDGES=[(450,62,450,118),(450,172,180,228),(450,172,450,228),(450,172,720,228),(180,282,180,338),(720,282,720,338),
 (180,392,450,448),(450,282,450,448)]+[(450,502,x,568) for x in (80,228,376,524,672,820)]
P1=('<!--noart-->'+ftree(HB_NODES,HB_EDGES,640,'Family tree of where food goes in the body. Food is digested from mouth to gut. Then three roads: the blood road (sugars and amino acids) goes to the liver first; the lymph road carries fats and vitamins A, D, E and K; and what is not absorbed, such as fiber, goes to the large intestine, where gut bacteria ferment it. The liver and the lymph both feed the bloodstream, which the heart pumps to the brain (glucose), muscle (protein), fat tissue (fats), bones (calcium), red marrow (iron) and the kidneys (waste).')
 +lblock('ideas','Three ideas to carry through',[('Broken down first','Food is cut into small pieces, mostly glucose, fatty acids and amino acids, before almost anything is absorbed.'),
   ('The liver sees it first','Blood from the gut runs straight to the liver by the portal vein. Only fats and fat-soluble vitamins bypass it, by the lymph.'),
   ('What stays in the gut','Most fiber is never absorbed. Gut bacteria feed on it in the large intestine; what is left leaves as stool.')]))
def BMW(html,cap): return '<!--noart--><div class="art bmw">'+html+f'<p class="ccap">{cap}</p></div>'
SIMP='A teaching statue, not an anatomy atlas: organs are simplified, the left and right of the drawing are the statue’s right and left (you are facing it), and the kidneys are dashed because they sit behind the gut.'
P2=BMW(bodymap('skin',aria='Marble statue of a human body with six layer buttons above it: skin, muscles, bones, nerves, organs and circulation. Tap a part of the body to zoom in and see its name and job.'),
 'Tap a layer above the statue, then tap any part of the body to zoom in. '+SIMP)
P3=BMW(bodymap('organs','torso',aria='The torso of the marble statue opened as a cutaway: windpipe, lungs, heart, diaphragm, liver, gallbladder, stomach, spleen, pancreas, small and large intestine, kidneys and bladder. Buttons below zoom into the gut, one villus of the small intestine, and the heart.'),
 'The organs layer, zoomed into the torso. Use the buttons under the statue to zoom further, down to one villus of the small intestine. '+SIMP)
P4=BMW(bodymap('organs',chips=MACRO,aria='The marble statue with its organs shown faintly and six nutrient buttons: glucose, fats, amino acids, water, alcohol and fiber. Tapping one draws its road through the body with numbered stops.'),
 'Tap a nutrient to light up its road. The numbered stops match the steps in the panel, and each nutrient links to its lesson. Roads are drawn as single lines; blood really reaches every cell.')
P5=BMW(bodymap('organs',chips=MICRO,aria='The marble statue with its organs shown faintly and five buttons: vitamins A, D, E and K; B vitamins and C; iron; calcium; and sodium. Tapping one draws its road through the body with numbered stops.'),
 'The same roads for vitamins and minerals. Watch for the stores (liver, fat tissue, bone, marrow) and for the one-way door: the body can’t get rid of extra iron.')
_HL=lambda h,t:f'<a href="{h}">{t}</a>'
P6=('<!--noart-->'+table('table',['Nutrient','Absorbed','Road','Ends up','Lesson'],[
  ['Glucose','Small intestine','Portal vein to liver','Every cell, brain especially; glycogen in liver and muscle',_HL('macronutrients-carbohydrates.html','Carbohydrates')],
  ['Fats','Small intestine, with bile','Lymph, as chylomicrons','Fat tissue (stored), muscle (burned)',_HL('macronutrients-fats.html','Fats')],
  ['Amino acids','Small intestine','Portal vein to liver','Proteins in every cell; extra nitrogen leaves as urea',_HL('macronutrients-protein.html','Protein')],
  ['Water','Small and large intestine','Blood, then everywhere','Inside cells (two thirds); out as urine, breath, sweat',_HL('macronutrients-water-ethanol.html','Water and Ethanol')],
  ['Alcohol','Stomach and small intestine','Portal vein to liver','Cleared by the liver at about one drink an hour',_HL('macronutrients-water-ethanol.html','Water and Ethanol')],
  ['Fiber','Not absorbed','Stays in the gut','Gut bacteria in the large intestine; stool',_HL('macronutrients-carbohydrates.html','Carbohydrates')],
  ['Vitamins A, D, E, K','Small intestine, with fat','Lymph, as chylomicrons','Stored in liver and fat tissue',_HL('micronutrients-fat-soluble-vitamins.html','Fat-Soluble Vitamins')],
  ['B vitamins and C','Small intestine (B12 at its end)','Portal vein to liver','Used in every cell; extra in urine (B12 stored in liver)',_HL('micronutrients-water-soluble-vitamins.html','Water-Soluble Vitamins')],
  ['Iron','Top of the small intestine','Blood, on transferrin','Hemoglobin from red marrow; stored as ferritin',_HL('micronutrients-trace-minerals.html','Trace Minerals')],
  ['Calcium','Small intestine, with vitamin D','Blood','Bones and teeth (99%)',_HL('micronutrients-major-minerals.html','Major Minerals')],
  ['Sodium','Small intestine','Blood','Fluid outside cells; extra out by the kidneys and sweat',_HL('micronutrients-major-minerals.html','Major Minerals')]],
  title='Every route in one table')
 +worth([('Your gut lining is replaced every few days','The cells covering the villi live only about three to five days before they are shed and replaced, one of the fastest turnovers in the body.'),
   ('The liver can regrow','Even after much of it is removed, the liver grows back to nearly its full size within months.'),
   ('Most body fat is under the skin','Only a minority sits deep around the organs (visceral fat), but that share is the one most linked to heart disease and diabetes.'),
   ('Bone is alive','Your skeleton is broken down and rebuilt all the time; roughly a tenth of it is renewed each year in adults.')]))
HB_LESSON=[('The Body Map Family Tree','Where food goes: digestion, two roads into the blood, and what stays in the gut.',P1),
 ('The Statue in Six Layers','Skin, muscles, bones, nerves, organs and circulation on one marble figure.',P2),
 ('Diving In: The Organs','The torso opened up, then one villus of the small intestine close up.',P3),
 ('Following the Macronutrients','Glucose, fats, amino acids, water, alcohol and fiber, each on its road.',P4),
 ('Following the Vitamins and Minerals','Fat- and water-soluble vitamins, iron, calcium and sodium.',P5),
 ('Putting It All Together','Every route in one table, plus a few things worth knowing.',P6)]
HB_QUIZ=[('Where in the body is almost all of your food absorbed?','The small intestine, through millions of villi (Figure 3).'),
 ('Why does the liver get first pick of glucose and amino acids?','Blood from the gut drains into the portal vein, which runs straight to the liver before the rest of the body (Figures 1 and 4).'),
 ('Which nutrients skip the liver at first, and how?','Fats and vitamins A, D, E and K: they are packed into chylomicrons and travel up the lymph, joining the blood near the left collarbone (Figure 4).'),
 ('What is a lacteal?','The lymph vessel in the middle of each villus, which takes in fat in chylomicrons (Figure 3).'),
 ('What does bile do, and where is it made and stored?','It breaks fat into tiny droplets so enzymes can reach it. The liver makes it and the gallbladder stores it (Figure 3).'),
 ('What happens to amino acids your body doesn’t need for building?','The liver strips off their nitrogen as urea, which the kidneys pass out in urine, and the rest is burned or stored as glucose or fat (Figure 4).'),
 ('About how much of your resting energy does the brain use, and what is its main fuel?','About a fifth, mostly glucose (Figures 2 and 4).'),
 ('How can a breath test measure the alcohol in your blood?','A few percent of alcohol leaves the blood unchanged through the lungs, so breath alcohol tracks blood alcohol (Figure 4).'),
 ('What happens to fiber in your body?','Your enzymes can’t break it down. In the large intestine, gut bacteria ferment much of it into short-chain fatty acids; the rest adds bulk to stool (Figure 4).'),
 ('Why is vitamin B12 absorbed differently from the other B vitamins?','It needs intrinsic factor from the stomach and is absorbed only at the end of the small intestine; the liver stores years of it (Figure 5).'),
 ('Where does most of the iron for new red blood cells come from each day?','Recycled from old red cells broken down in the spleen. Only 1 to 2 mg a day is absorbed from food (Figure 5).'),
 ('Where is 99% of your calcium, and what raises blood calcium when it dips?','In bones and teeth. Parathyroid hormone tells the kidneys to keep more and the bones to release some (Figure 5).')]
build_lesson('human-body','The Human Body','Where everything you eat goes. A marble statue of the body in six layers you can switch between and zoom into: skin, muscles, bones, nerves, organs and circulation. Then tap a nutrient to follow its road from the plate to where it is used or stored, with a link back to its lesson. Every route is simplified, and each says how. The figure is on the left and the lesson script on the right; the quiz is at the end.',
 HB_LESSON,HB_QUIZ,after_extra=f'<link rel="stylesheet" href="{_asset("bodymap.css")}">'+BM_DEFS+f'<script src="{_asset("bodymap.js")}"></script>')
