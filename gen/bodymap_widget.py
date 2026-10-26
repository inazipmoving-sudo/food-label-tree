# Module 6 body map: parts, dives, nutrient routes and the widget HTML builder.
# exec'd after bodymap.py (needs P, sp, cr, ghost, organs, ... and json/_html from curriculum.py)
import json as _bj, html as _bh
LAYERS=[('skin','Skin'),('muscles','Muscles'),('bones','Bones'),('nerves','Nerves'),('organs','Organs'),('circulation','Circulation')]
LAYER_INTRO={
 'skin':'The outside of the statue: skin, the body’s largest organ, about 2 m² in an adult. It keeps water in and germs out, sweats to cool you, and makes vitamin D in sunlight. Tap the body to look at a slice.',
 'muscles':'About 600 skeletal muscles, roughly a third to two fifths of body weight. Muscle holds most of the body’s protein and burns glucose and fat. Tap a muscle to zoom in.',
 'bones':'206 bones in an adult. They hold about 99% of the body’s calcium, and the red marrow inside some of them makes every blood cell. Tap a bone to zoom in.',
 'nerves':'The brain, the spinal cord and the nerves that branch from it carry signals as tiny flows of sodium and potassium. The brain alone uses about a fifth of your resting energy. Tap a nerve to zoom in.',
 'organs':'The torso opened like a cutaway: the digestive tube and its helpers, the heart and lungs, and the kidneys behind the gut (dashed). Tap an organ to zoom in.',
 'circulation':'Arteries (terracotta) carry blood out from the heart; veins (blue) bring it back. Two special roads carry food: the portal vein (blue dashes, gut to liver) and the lymph (green dots, the road for fats). Tap a vessel to zoom in.'}
# key: (name, one-line job)
PARTS={
 'skin':('Skin','Barrier against water loss and germs; senses touch, heat and pain; makes vitamin D in sunlight.'),
 'epidermis':('Epidermis','The thin outer layer: cells form at its base, flatten and are shed about a month later.'),
 'dermis':('Dermis','Tough collagen layer holding blood vessels, nerves, sweat glands and hair roots.'),
 'subcutaneous-fat':('Fat under the skin','Stores energy as triglyceride, insulates and cushions. Most body fat is here.'),
 'hair-follicle':('Hair follicle','Grows a hair; its oil gland keeps skin supple.'),
 'sweat-gland':('Sweat gland','Releases salty water that cools you as it evaporates, taking some sodium with it.'),
 'skin-vessels':('Skin blood vessels','Widen to shed heat, narrow to save it; feed the skin.'),
 'neck':('Neck muscle','Turns and tilts the head (sternocleidomastoid).'),
 'trap':('Trapezius','Shrugs the shoulders and steadies the shoulder blade.'),
 'deltoid':('Deltoid','Lifts the arm out to the side and forward.'),
 'pecs':('Chest muscle','Pulls the arm forward and across the body (pectoralis major).'),
 'biceps':('Biceps','Bends the elbow and turns the palm up.'),
 'forearm':('Forearm muscles','Bend and straighten the wrist and fingers; your grip.'),
 'serratus':('Serratus','Holds the shoulder blade against the ribs.'),
 'obliques':('Obliques','Twist and bend the trunk; help you breathe out hard.'),
 'abs':('Abdominal muscle','Bends the trunk and holds the gut in (rectus abdominis).'),
 'hipflex':('Hip flexors','Lift the thigh when you walk or climb.'),
 'quads':('Thigh muscles','Straighten the knee; the biggest muscle group, with the largest glycogen store (quadriceps).'),
 'adductors':('Adductors','Pull the legs together.'),
 'sartorius':('Sartorius','The longest muscle in the body; crosses hip and knee.'),
 'shin':('Shin muscles','Lift the foot and toes.'),
 'calf':('Calf muscles','Push you up onto your toes with every step.'),
 'skull':('Skull','Protects the brain; the jaw chews food.'),
 'spine':('Spine','Holds the body upright and shelters the spinal cord; red marrow inside.'),
 'ribs':('Ribs','A cage around the heart and lungs that moves with each breath.'),
 'sternum':('Breastbone','Joins the ribs at the front; one of the places red marrow makes blood cells.'),
 'clavicle':('Collarbone','Braces the shoulder; the vein just under it is where lymph rejoins the blood.'),
 'shoulder':('Shoulder blade','The moving base of the arm.'),
 'humerus':('Upper arm bone','Lever for the shoulder and elbow muscles (humerus).'),
 'forearm-bones':('Forearm bones','Radius and ulna: two bones so the hand can turn over.'),
 'hand-bones':('Hand bones','27 bones each side for fine movement.'),
 'pelvis':('Pelvis','Carries the weight of the trunk to the legs and cradles the bladder and gut; rich in red marrow.'),
 'femur':('Thigh bone','The longest, strongest bone (femur); red marrow at its upper end.'),
 'kneecap':('Kneecap','Gives the thigh muscle better leverage on the knee (patella).'),
 'shin-bones':('Shin bones','Tibia carries the weight; the thin fibula anchors muscles.'),
 'foot-bones':('Foot bones','26 bones each side forming springy arches.'),
 'compact-bone':('Compact bone','The dense outer shell, built from calcium phosphate on a collagen frame.'),
 'spongy-bone':('Spongy bone','A light lattice at the ends; its spaces hold red marrow.'),
 'marrow':('Marrow','Red marrow makes red cells, white cells and platelets; yellow marrow is mostly fat.'),
 'cartilage':('Cartilage','Smooth caps where bones meet in a joint.'),
 'periosteum':('Periosteum','Living skin of the bone, with the nerves and vessels that feed it.'),
 'brain':('Brain','Thinks and controls the body; about 2% of body weight but about 20% of resting energy, mostly from glucose.'),
 'spinal-cord':('Spinal cord','The main cable between brain and body.'),
 'arm-nerves':('Arm nerves','Carry movement and touch signals to and from the hand (median, ulnar, radial).'),
 'intercostal':('Rib nerves','Run between the ribs to the breathing muscles and the skin of the chest.'),
 'femoral':('Femoral nerve','Works the front thigh muscles.'),
 'sciatic':('Sciatic nerve','The largest nerve, running down the back of the thigh (dashed: it lies behind).'),
 'vagus':('Vagus nerve','Links the brain with the heart and gut; carries fullness signals up and digestion signals down.'),
 'trachea':('Windpipe','Carries air to the lungs (trachea).'),
 'esophagus':('Esophagus','Muscular tube that squeezes food down to the stomach.'),
 'lungs':('Lungs','Take in oxygen and breathe out carbon dioxide; a little alcohol leaves this way too.'),
 'heart':('Heart','Pumps about 5 liters of blood a minute around the body.'),
 'diaphragm':('Diaphragm','Dome-shaped muscle under the lungs that does most of the work of breathing.'),
 'liver':('Liver','First stop for absorbed nutrients: stores glycogen, vitamins and iron, makes bile, clears alcohol and turns extra nitrogen into urea.'),
 'gallbladder':('Gallbladder','Stores bile and squeezes it into the small intestine when fat arrives.'),
 'stomach':('Stomach','Churns food with acid and pepsin; starts protein digestion; makes intrinsic factor for vitamin B12.'),
 'spleen':('Spleen','Filters blood and recycles iron from old red blood cells.'),
 'pancreas':('Pancreas','Sends digestive enzymes to the small intestine and releases insulin and glucagon into the blood.'),
 'small-intestine':('Small intestine','Several meters long: where almost all nutrients are absorbed, through millions of villi.'),
 'large-intestine':('Large intestine','Takes back water and salts; its bacteria ferment fiber (colon).'),
 'kidneys':('Kidneys','Filter about 180 liters of fluid from the blood a day and return nearly all of it, keeping water, sodium and calcium in balance and passing urea out in urine.'),
 'bladder':('Bladder','Stores urine until you empty it.'),
 'aorta':('Aorta','The body’s main artery, leaving the heart.'),
 'carotid':('Carotid arteries','Carry blood up the neck to the brain.'),
 'arm-artery':('Arm arteries','Feed the arm and hand (subclavian, then brachial).'),
 'leg-artery':('Leg arteries','Feed the thigh, leg and foot (iliac, then femoral).'),
 'vena-cava':('Vena cava','The two great veins returning blood to the heart.'),
 'jugular':('Jugular veins','Drain blood from the head.'),
 'arm-vein':('Arm veins','Return blood from the arm; the left one under the collarbone receives the lymph.'),
 'leg-vein':('Leg veins','Return blood from the leg, helped by the calf muscles.'),
 'portal-vein':('Portal vein','Carries blood from the stomach and intestines straight to the liver, so the liver sees most absorbed nutrients first.'),
 'thoracic-duct':('Thoracic duct','The main lymph vessel: carries absorbed fat up the chest into a vein near the left collarbone.'),
 'villus':('Villus','A finger-like fold about 1 mm tall; millions of them give the small intestine a huge absorbing surface.'),
 'enterocytes':('Absorbing cells','Take nutrients in from the gut and pass them on to the blood or lymph (enterocytes).'),
 'microvilli':('Brush border','Tiny folds on each absorbing cell, holding the enzymes that finish digestion.'),
 'villus-capillaries':('Capillaries','Pick up sugars, amino acids, minerals, water-soluble vitamins and water; drain to the portal vein.'),
 'lacteal':('Lacteal','A lymph vessel in the middle of each villus; takes in chylomicrons, which carry fat and fat-soluble vitamins.')}
# dive regions: key: (title, layer, viewBox, [parts], [(part,x,y) pin anchors], lead)
DIVES={
 'skin':('A slice of skin','skin','440 90 220 440',['epidermis','dermis','subcutaneous-fat','hair-follicle','sweat-gland','skin-vessels'],
   {'epidermis':(560,172),'dermis':(500,300),'subcutaneous-fat':(520,420),'hair-follicle':(516,240),'sweat-gland':(592,330),'skin-vessels':(570,214)},
   'Three layers, top to bottom. Not to scale: the epidermis is thinner than a sheet of paper.'),
 'muscles-trunk':('Muscles of the trunk and arm','muscles','110 120 220 440',['neck','trap','deltoid','pecs','biceps','forearm','serratus','abs','obliques','hipflex','sartorius'],
   {'neck':(222,126),'trap':(238,144),'deltoid':(287,190),'pecs':(232,192),'biceps':(306,262),'forearm':(326,330),'serratus':(259,248),'abs':(215,284),'obliques':(248,310),'hipflex':(262,420),'sartorius':(246,404)},
   'Each muscle is a bundle of long fibers, shown by the hatching; muscle pulls, it never pushes.'),
 'muscles-leg':('Muscles of the leg','muscles','150 380 180 360',['quads','adductors','sartorius','shin','calf'],
   {'quads':(255,480),'adductors':(215,470),'sartorius':(232,500),'shin':(246,640),'calf':(224,630)},
   'The thigh muscles are the body’s biggest glycogen store, a few hundred grams spread through muscle as a whole.'),
 'bones-trunk':('Skull, spine, ribs and pelvis','bones','100 20 200 400',['skull','spine','ribs','sternum','clavicle','shoulder','humerus','pelvis'],
   {'skull':(222,60),'spine':(200,300),'ribs':(236,214),'sternum':(200,196),'clavicle':(240,154),'shoulder':(276,172),'humerus':(296,230),'pelvis':(244,370)},
   'Red marrow in the skull, spine, ribs, breastbone and pelvis makes blood cells throughout life.'),
 'bones-limb':('Bones of the limbs','bones','170 380 180 360',['pelvis','femur','kneecap','shin-bones','foot-bones'],
   {'pelvis':(250,390),'femur':(245,480),'kneecap':(237,557),'shin-bones':(238,640),'foot-bones':(246,730)},
   'Long bones are hollow tubes of compact bone with spongy bone at each end.'),
 'bone':('Inside a long bone','bones','690 90 220 440',['compact-bone','spongy-bone','marrow','cartilage','periosteum'],
   {'compact-bone':(780,330),'spongy-bone':(800,172),'marrow':(800,280),'cartilage':(840,142),'periosteum':(772,250)},
   'Cut lengthwise, like a split bamboo cane. Bone is living tissue, rebuilt about every 10 years.'),
 'nerves-head':('Brain and spinal cord','nerves','130 20 140 280',['brain','spinal-cord','vagus','arm-nerves','intercostal'],
   {'brain':(214,58),'spinal-cord':(200,150),'vagus':(193,216),'arm-nerves':(250,164),'intercostal':(236,200)},
   'The brain and spinal cord form the central nervous system; everything else is the peripheral nerves.'),
 'nerves-leg':('Nerves of the leg','nerves','150 330 180 360',['spinal-cord','femoral','sciatic'],
   {'spinal-cord':(200,380),'femoral':(246,470),'sciatic':(236,560)},
   'The cord ends at about waist level; below it a bundle of nerve roots fans out to the legs.'),
 'torso':('Inside the torso','organs','110 130 180 360',['trachea','esophagus','lungs','heart','diaphragm','liver','gallbladder','stomach','spleen','pancreas','small-intestine','large-intestine','kidneys','bladder'],
   {'trachea':(200,132),'esophagus':(208,160),'lungs':(162,210),'heart':(222,226),'diaphragm':(252,264),'liver':(166,276),'gallbladder':(183,304),'stomach':(240,290),'spleen':(256,288),'pancreas':(244,316),'small-intestine':(200,366),'large-intestine':(156,358),'kidneys':(166,306),'bladder':(200,422)},
   'Front view with the skin and muscle wall removed. The kidneys lie behind the gut, against the back (dashed).'),
 'gut':('The digestive organs','organs','130 240 140 280',['esophagus','stomach','liver','gallbladder','pancreas','spleen','small-intestine','large-intestine','kidneys'],
   {'esophagus':(213,254),'stomach':(240,290),'liver':(166,276),'gallbladder':(183,304),'pancreas':(244,316),'spleen':(256,288),'small-intestine':(200,366),'large-intestine':(156,358),'kidneys':(166,306)},
   'Food goes mouth, esophagus, stomach, small intestine, large intestine. The liver, gallbladder and pancreas are helpers that food never passes through.'),
 'villus':('One villus, close up','organs','940 90 220 440',['villus','enterocytes','microvilli','villus-capillaries','lacteal'],
   {'villus':(1000,200),'enterocytes':(1060,120),'microvilli':(1142,168),'villus-capillaries':(1076,250),'lacteal':(1100,330)},
   'Magnified about 200 times. Everything you absorb crosses a single layer of cells like this one.'),
 'heart':('Heart and great vessels','circulation','140 100 120 240',['heart','aorta','vena-cava','carotid','jugular','arm-artery','arm-vein','thoracic-duct'],
   {'heart':(222,230),'aorta':(204,270),'vena-cava':(194,218),'carotid':(208,128),'jugular':(184,124),'arm-artery':(246,158),'arm-vein':(234,152),'thoracic-duct':(198,290)},
   'The heart is two pumps side by side: one to the lungs, one to the rest of the body.'),
 'gut-vessels':('The food roads','circulation','140 240 120 240',['portal-vein','thoracic-duct','aorta','vena-cava','leg-artery','leg-vein'],
   {'portal-vein':(190,304),'thoracic-duct':(197,276),'aorta':(204,318),'vena-cava':(196,290),'leg-artery':(224,402),'leg-vein':(214,410)},
   'Blood from the gut goes to the liver first (portal vein); fat goes the other way, up the lymph.'),
}
# which dive a tapped part opens, per layer (first dive in this list that holds the part)
DIVE_ORDER={'skin':['skin'],'muscles':['muscles-trunk','muscles-leg'],'bones':['bones-trunk','bones-limb','bone'],'nerves':['nerves-head','nerves-leg'],'organs':['torso','gut','villus'],'circulation':['heart','gut-vessels']}
CLOSER={'small-intestine':'villus','femur':'bone','marrow':'bone','skin':'skin','subcutaneous-fat':'skin','spongy-bone':'bone','pelvis':'bone','lacteal':'villus'}
# ---- nutrient routes ----
GUT=[(200,104),(206,130),(207,180),(210,232),(216,262),(236,280),(244,298),(228,314),(214,320),(222,332),(206,344),(184,352),(216,362),(188,372),(214,382),(180,392)]
STOM,DUO,SI,ILEUM=(238,288),(218,326),(200,362),(176,392)
COLON=[(176,392),(160,384),(156,362),(158,336),(178,330),(200,332),(226,330),(246,340),(248,370),(240,390),(222,400),(206,412)]
TD=[(200,352),(198,312),(197,280),(198,230),(200,190),(204,160),(214,148),(226,150)]
POR=[(200,356),(204,340),(200,322),(190,306),(176,288)]
LIV,IVC,HRT=(172,280),(194,240),(214,226)
TOP=[(214,226),(206,196),(206,176),(206,140),(204,100),(200,66)]
DOWN=[(214,226),(204,250),(203,300),(203,348),(218,384),(234,420),(244,480)]
KID=[(214,226),(204,250),(203,300),(222,314),(236,318)]
BLAD=[(236,318),(226,340),(214,380),(200,420)]
LUNG=[(214,226),(190,214),(164,212)]
FAT=[(214,226),(204,250),(203,330),(222,370),(250,396),(260,408)]
MARROW=[(214,226),(204,250),(203,340),(222,380),(244,416)]
BONE=[(214,226),(204,250),(203,348),(218,384),(234,420),(240,500),(240,610)]
NRV=[(214,226),(236,170),(266,174),(290,200),(306,250),(318,292)]
SKIN=[(214,226),(204,250),(203,330),(214,380),(176,420),(150,452),(140,470)]
SPLEEN=[(214,226),(204,250),(203,270),(232,280),(254,286)]
GB=[(182,304),(196,318),(214,322)]
def gut_to(i): return GUT[:i+1]
ROUTES={
 'glucose':dict(name='Glucose',lesson=('macronutrients-carbohydrates.html','Carbohydrates'),
   segs=[('gut',gut_to(12)),('blood portal',POR),('blood',[LIV,(186,262),IVC,HRT]),('blood',TOP),('blood',DOWN)],
   stops=[(200,104,'Mouth','Saliva starts breaking starch into shorter sugar chains.'),(SI[0],SI[1],'Small intestine','Enzymes finish the job; glucose is pumped into the cells of the villi and on into the capillaries.'),
     (LIV[0],LIV[1],'Liver, by the portal vein','The first stop. The liver stores some as glycogen (about 100 g when full) and releases glucose between meals.'),
     (HRT[0],HRT[1],'Heart','Pumped out to every cell; blood glucose is held in a narrow range, about 4 to 7 mmol/L.'),
     (200,66,'Brain','Uses about 120 g of glucose a day.'),(244,480,'Muscle','Takes glucose in, faster with insulin, and stores about 400 g as glycogen.')],
   end='Burned for energy in nearly every cell. Extra goes to glycogen in the liver and muscle, and once those are full the liver can turn it into fat.',
   simp='Drawn as one road to two places; really glucose reaches every cell. Fructose and galactose take the same road and the liver turns most of them into glucose.'),
 'fats':dict(name='Fats',lesson=('macronutrients-fats.html','Fats'),
   segs=[('gut',gut_to(12)),('bile',GB),('lymph',TD),('blood',[(226,150),(220,180),HRT]),('blood',FAT),('blood',DOWN),('blood',[HRT,IVC,(186,262),LIV])],
   stops=[(DUO[0],DUO[1],'Small intestine','Bile from the gallbladder breaks fat into tiny droplets; lipase from the pancreas cuts off fatty acids.'),
     (200,352,'Villus cells','Rebuild the pieces into triglycerides and pack them into chylomicrons.'),
     (198,250,'Lymph','Chylomicrons are too big for capillaries, so they enter the lacteals and ride the lymph up the chest (thoracic duct).'),
     (226,150,'Into the blood','The lymph empties into a vein near the left collarbone, then goes on to the heart.'),
     (260,408,'Fat tissue','An enzyme on the vessel walls (lipoprotein lipase) frees the fatty acids; fat cells store them as triglyceride.'),
     (244,480,'Muscle','Burns fatty acids for energy, especially at rest and in long exercise.'),
     (LIV[0],LIV[1],'Liver','Clears the leftover chylomicron remnants.')],
   end='Stored in fat tissue or burned by muscle and the heart. Chylomicrons are cleared from the blood within hours of a meal.',
   simp='Short- and medium-chain fatty acids (a small share of butter and coconut oil) skip the lymph and go straight to the liver by the portal vein, like glucose.'),
 'amino':dict(name='Amino acids',lesson=('macronutrients-protein.html','Protein'),
   segs=[('gut',gut_to(12)),('blood portal',POR),('blood',[LIV,(186,262),IVC,HRT]),('blood',DOWN),('out',[LIV,(196,300),(222,314),(236,318)]),('out',BLAD)],
   stops=[(STOM[0],STOM[1],'Stomach','Acid unfolds proteins and pepsin starts cutting them.'),(SI[0],SI[1],'Small intestine','Enzymes from the pancreas and the brush border finish the job; amino acids and very short peptides are absorbed.'),
     (LIV[0],LIV[1],'Liver','First stop: builds blood proteins such as albumin and sorts the amino acids.'),(HRT[0],HRT[1],'Heart','Pumped out to every cell.'),
     (244,480,'Muscle and every cell','Build new proteins: muscle, enzymes, antibodies, hormones.'),(236,318,'Kidneys','Extra amino acids lose their nitrogen in the liver as urea, which the kidneys pass out in urine.')],
   end='Built into the body’s proteins, which are always being broken down and rebuilt. Amino acids beyond that are burned for energy or turned into glucose or fat once their nitrogen has gone.',
   simp='There is no protein store like glycogen or fat; muscle is working tissue, though the body does break it down when food runs short.'),
 'water':dict(name='Water',lesson=('macronutrients-water-ethanol.html','Water and Ethanol'),
   segs=[('gut',GUT),('gut',COLON),('blood portal',POR),('blood',[LIV,(186,262),IVC,HRT]),('blood',KID),('out',BLAD),('out',LUNG),('out',SKIN)],
   stops=[(SI[0],SI[1],'Small intestine','Absorbs most of it, following the salts and sugars being absorbed.'),(156,362,'Large intestine','Takes back most of what is left, so stool holds only about 100 mL a day.'),
     (HRT[0],HRT[1],'Blood','Water moves freely between blood, the cells and the spaces between them.'),(236,318,'Kidneys','Adjust how much urine you make (vasopressin tells them to save water).'),
     (164,212,'Lungs','Some leaves as vapor in every breath.'),(140,470,'Skin','Some leaves as sweat, more in heat and exercise.')],
   end='About 60% of an adult’s weight, two thirds of it inside cells. Urine is the main way out.',
   simp='Drawn as a road, but water crosses nearly every membrane within minutes; it does not travel as a single stream.'),
 'alcohol':dict(name='Alcohol',lesson=('macronutrients-water-ethanol.html','Water and Ethanol'),
   segs=[('gut',gut_to(12)),('blood portal',[STOM,(226,304),(208,314),(190,306),(176,288)]),('blood portal',POR),('blood',[LIV,(186,262),IVC,HRT]),('blood',TOP),('out',LUNG),('out',KID),('out',BLAD)],
   stops=[(STOM[0],STOM[1],'Stomach','About a fifth is absorbed here. Food in the stomach slows it down.'),(SI[0],SI[1],'Small intestine','The rest is absorbed quickly.'),
     (LIV[0],LIV[1],'Liver','Alcohol dehydrogenase turns ethanol into acetaldehyde, then a second enzyme makes acetate: about one standard drink an hour.'),
     (200,66,'Brain','Alcohol the liver has not cleared yet spreads through all body water, brain included, causing its effects.'),
     (164,212,'Lungs and kidneys','A few percent leaves unchanged in breath (what breath tests measure) and urine.')],
   end='Burned as fuel, 7 kcal per gram, once the liver has converted it. The body cannot store alcohol, so the liver deals with it first.',
   simp='The stomach and intestine split is approximate and varies with food; the stomach lining also breaks down a little alcohol itself. Clearance rates vary from person to person.'),
 'fiber':dict(name='Fiber',lesson=('macronutrients-carbohydrates.html','Carbohydrates'),
   segs=[('gut',GUT),('gut',COLON)],
   stops=[(STOM[0],STOM[1],'Stomach','Soluble fiber thickens and slows emptying, so you feel full longer.'),(SI[0],SI[1],'Small intestine','Human enzymes cannot break it down, so it passes through.'),
     (158,336,'Large intestine','Gut bacteria ferment much of it into short-chain fatty acids, which feed the colon’s own cells.'),(206,412,'Out','What is left adds bulk and water to stool.')],
   end='Mostly not absorbed: it feeds the gut bacteria and leaves in stool.',
   simp='Fiber itself is not absorbed, but the short-chain fatty acids bacteria make from it are, giving about 2 kcal per gram.'),
 'fat-vitamins':dict(name='Vitamins A, D, E, K',lesson=('micronutrients-fat-soluble-vitamins.html','Fat-Soluble Vitamins'),
   segs=[('gut',gut_to(12)),('bile',GB),('lymph',TD),('blood',[(226,150),(220,180),HRT]),('blood',[HRT,IVC,(186,262),LIV]),('blood',FAT),('blood',[(292,206),(270,190),(240,180),HRT]),('blood',KID)],
   stops=[(SI[0],SI[1],'Small intestine','Absorbed along with fat, so a meal with some fat helps; bile is needed.'),(198,250,'Lymph','Packed into chylomicrons with the fat and carried up the lymph.'),
     (LIV[0],LIV[1],'Liver','Stores most of the body’s vitamin A, and some D, E and K.'),(260,408,'Fat tissue','Stores vitamins D and E.'),
     (292,206,'Skin','Makes vitamin D from sunlight (UVB).'),(236,318,'Kidneys','Vitamin D is activated in two steps: first in the liver, then in the kidneys.')],
   end='Stored for weeks to months, so you do not need them every day, and large supplement doses, of A and D especially, can build up to harmful levels.',
   simp='Vitamin K is stored only briefly. Vitamin D from sunlight skips the gut entirely.'),
 'water-vitamins':dict(name='B vitamins and C',lesson=('micronutrients-water-soluble-vitamins.html','Water-Soluble Vitamins'),
   segs=[('gut',GUT),('blood portal',POR),('blood',[LIV,(186,262),IVC,HRT]),('blood',DOWN),('blood',KID),('out',BLAD)],
   stops=[(STOM[0],STOM[1],'Stomach','Acid frees vitamin B12 from food, and the stomach makes intrinsic factor, the protein B12 needs.'),(SI[0],SI[1],'Small intestine','Most B vitamins and vitamin C are absorbed here, into the blood.'),
     (ILEUM[0],ILEUM[1],'End of the small intestine','B12, bound to intrinsic factor, is absorbed only here (the ileum).'),(LIV[0],LIV[1],'Liver','Stores B12 for years and folate for months.'),
     (244,480,'Every cell','Use them as helpers (coenzymes) for energy, DNA and collagen.'),(236,318,'Kidneys','Pass out any extra in urine.')],
   end='Mostly not stored, so you need a steady supply. B12 is the exception, with years in the liver.',
   simp='Grouped here as one route; each vitamin has its own carriers and limits.'),
 'iron':dict(name='Iron',lesson=('micronutrients-trace-minerals.html','Trace Minerals'),
   segs=[('gut',gut_to(9)),('blood portal',[DUO,(208,316),(190,306),(176,288)]),('blood',[LIV,(186,262),IVC,HRT]),('blood',MARROW),('blood',SPLEEN)],
   stops=[(STOM[0],STOM[1],'Stomach','Acid frees iron from food; vitamin C helps the body absorb iron from plants.'),(DUO[0],DUO[1],'Top of the small intestine','Iron is absorbed here (duodenum). How much depends on need, set by the liver hormone hepcidin.'),
     (LIV[0],LIV[1],'Liver','Carried in blood by transferrin; spare iron is stored here as ferritin.'),(244,416,'Red marrow','Builds iron into hemoglobin in new red blood cells.'),
     (254,286,'Spleen','Breaks down old red blood cells and recycles their iron.')],
   end='About two thirds of body iron is in hemoglobin. The body has no real way to get rid of iron, so it controls absorption instead.',
   simp='Only 1 to 2 mg is absorbed a day; most of the iron used to make blood each day (about 20 mg) is recycled from old cells.'),
 'calcium':dict(name='Calcium',lesson=('micronutrients-major-minerals.html','Major Minerals'),
   segs=[('gut',gut_to(12)),('blood portal',POR),('blood',[LIV,(186,262),IVC,HRT]),('blood',BONE),('blood',KID),('out',BLAD)],
   stops=[(SI[0],SI[1],'Small intestine','Absorbed mostly at its top; active vitamin D makes the carrier proteins. Roughly a quarter to a third of dietary calcium gets in.'),
     (HRT[0],HRT[1],'Blood','Held within a narrow range; muscle and nerves need it to work.'),(240,610,'Bones and teeth','Store 99% of the body’s calcium.'),
     (236,318,'Kidneys','When blood calcium dips, parathyroid hormone tells the kidneys to keep more and the bones to release some.')],
   end='Almost all in bones and teeth; the 1% in blood and cells runs muscle contraction, nerve signals and clotting.',
   simp='Bone is not a dead store: it is broken down and rebuilt all the time, which is how it lends calcium to the blood.'),
 'sodium':dict(name='Sodium',lesson=('micronutrients-major-minerals.html','Major Minerals'),
   segs=[('gut',gut_to(12)),('blood portal',POR),('blood',[LIV,(186,262),IVC,HRT]),('blood',NRV),('blood',KID),('out',BLAD),('out',SKIN)],
   stops=[(SI[0],SI[1],'Small intestine','Almost all the sodium you eat is absorbed.'),(HRT[0],HRT[1],'Blood','The main salt of blood and the fluid around cells; where sodium goes, water follows.'),
     (318,292,'Nerves and muscle','Sodium rushing into the cell is what fires each nerve signal and muscle contraction.'),(236,318,'Kidneys','Pass out the extra, so urine sodium tracks what you eat.'),(140,470,'Skin','Some is lost in sweat.')],
   end='Mostly in the fluid outside cells. The kidneys keep the total in balance; the body does not store extra.',
   simp='The heart and liver are on the road only because all blood from the gut passes through them; they do not process sodium.')}
# ROUTE_LINKS: show each route's lesson link (set to a URL prefix such as '../curriculum/' to enable; off while the courses stand alone)
ROUTE_LINKS=None
MACRO=['glucose','fats','amino','water','alcohol','fiber']
MICRO=['fat-vitamins','water-vitamins','iron','calcium','sodium']
RCLS={'gut':'rt-g','blood':'rt-b','blood portal':'rt-b rt-p','lymph':'rt-l','bile':'rt-x','out':'rt-o'}
def routes_svg(keys):
    o=''
    for k in keys:
        r=ROUTES[k]
        o+=f'<g class="bm-route" data-n="{k}">'+''.join(f'<path d="{sp(pts)}" class="rt {RCLS[c]}"/>' for c,pts in r['segs'])+''.join(f'<circle class="rt-stop" cx="{x}" cy="{y}" r="5"/>' for x,y,*_ in r['stops'])+'</g>'
    return o
def route_layer():
    org=organs().split('<g class="cut">',1)[1]
    return ghost()+'<g class="rlayer"><g class="cut">'+org+'</g></g>'
def _skin_layer(): return '<g data-k="skin">'+base()+silhouette()+skin_lines()+'</g>'
_LAYER_SVG=None
def layer_svg():
    global _LAYER_SVG
    if _LAYER_SVG is None:
        _LAYER_SVG={'skin':_skin_layer(),'muscles':muscles(),'bones':bones(),'nerves':nerves(),'organs':organs(),'circulation':circulation(),'route':route_layer()}
    return _LAYER_SVG
_BM_N=[0]
def bodymap(start_layer='skin',start_dive=None,chips=None,aria='',fig=None):
    """the interactive statue: layer tabs above, the figure with pins, and an HTML panel"""
    _BM_N[0]+=1;uid=f'bm{_BM_N[0]}'
    L=layer_svg()
    svg=(f'<svg class="bm-svg" viewBox="0 0 400 800" role="img" aria-label="{_bh.escape(aria)}"><rect class="bm-bg" x="-400" y="-200" width="2000" height="1200"/>'
         +''.join(f'<g class="bm-l" data-layer="{k}">{v}</g>' for k,v in L.items())
         +skin_close()+bone_close()+villus_close()+(routes_svg(chips) if chips else '')+'</svg>')
    tabs='<div class="bm-tabs" role="group" aria-label="Body layers">'+''.join(f'<button type="button" class="bm-tab" data-layer="{k}" data-part="layer-{k}" aria-pressed="false">{n}</button>' for k,n in LAYERS)+'</div>'
    dv='<div class="bm-dives" role="group" aria-label="Zoom in">'+''.join(f'<button type="button" class="bm-dv" data-dive="{k}" data-for="{d[1]}" data-part="dive-{k}">{d[0]}</button>' for k,d in DIVES.items())+'</div>'
    ch=''
    if chips:
        ch='<div class="bm-chips" role="group" aria-label="Follow a nutrient"><span class="bm-chl">Follow a nutrient</span>'+''.join(f'<button type="button" class="bm-chip" data-n="{k}" data-part="n-{k}" aria-pressed="false">{ROUTES[k]["name"]}</button>' for k in chips)+'</div>'
    data={'parts':{k:list(v) for k,v in PARTS.items()},'dives':{k:{'t':d[0],'layer':d[1],'vb':d[2],'parts':d[3],'pins':d[4],'lead':d[5]} for k,d in DIVES.items()},
          'order':DIVE_ORDER,'closer':CLOSER,'intro':LAYER_INTRO,'names':dict(LAYERS),
          'routes':{k:{'name':ROUTES[k]['name'],'lesson':([ROUTE_LINKS+ROUTES[k]['lesson'][0],ROUTES[k]['lesson'][1]] if ROUTE_LINKS else None),'stops':[list(s) for s in ROUTES[k]['stops']],'end':ROUTES[k]['end'],'simp':ROUTES[k]['simp']} for k in (chips or [])},
          'start':{'layer':start_layer,'dive':start_dive}}
    js=_bj.dumps(data,ensure_ascii=False).replace('</','<\\/')
    return (f'<div class="bm" id="{uid}" data-part="body" data-layer="{start_layer}" data-mode="layer">'+tabs+ch
            +'<div class="bm-stage"><div class="bm-figw"><div class="bm-fig">'+svg+'<div class="bm-pins" aria-hidden="true"></div></div>'
            +'<button type="button" class="bm-back" hidden>← Whole body</button></div>'
            +'<div class="bm-panel" aria-live="polite"></div></div>'+(('<p class="bm-key">'+''.join(f'<span><i style="border-color:var({c})"></i>{t}</span>' for c,t in (('--bm-hi','Through the gut'),('--bm-art','In the blood'),('--bm-vein','Portal vein, gut to liver'),('--bm-lym','Lymph'),('--bm-bile','Bile'),('--bm-line','Ways out')))+'</p>') if chips else '')+dv
            +f'<script type="application/json" class="bm-data">{js}</script></div>')
