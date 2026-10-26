# ---------------- Module 6 · The statue body map: original SVG drawing + data ----------------
# One front-facing marble statue (400 x 800 user units, centre x=200), drawn once and reused by every figure widget.
# Layers: skin, muscles, bones, nerves, organs, circulation; close-ups (skin section, bone section, villus) sit to the right of x=420
# and are reached by zooming the viewBox. All text is HTML (markers + panel), never SVG text.
import math, json, os
exec(open(os.path.join(GEN,'bodymap_geo.py'),encoding='utf-8').read())
def P(d,cls='',k=None,extra=''):
    return f'<path d="{d}"'+(f' class="{cls}"' if cls else '')+(f' data-k="{k}"' if k else '')+(f' {extra}' if extra else '')+'/>'
def both(fn):
    """call fn(side) for side=+1 (viewer's right) and -1 (mirrored)"""
    return fn(1)+fn(-1)
def M(pts,s): return pts if s>0 else mx(pts)
def Mx(x,s): return x if s>0 else 400-x
def capM(s,x1,y1,r1,x2,y2,r2): return capsule(Mx(x1,s),y1,r1,Mx(x2,s),y2,r2)
# ---- silhouette ----
HEAD=sym([(200,30),(216,33),(228,44),(233,62),(233,80),(230,96),(224,108),(214,117),(204,121),(200,121)])
NECK=sym([(200,96),(214,98),(216,124),(226,142),(200,150)])
TORSO=sym([(200,136),(222,138),(248,146),(272,154),(286,166),(290,184),(282,206),(268,222),(267,250),(262,290),(252,330),(256,360),(264,392),(266,418),(250,432),(226,444),(210,452),(200,454)])
HAND_L=[(0,-10),(14,-12),(30,-12.5),(46,-11),(60,-9),(72,-6),(79,-1),(78,5),(70,8),(56,9),(42,9),(36,11),(30,20),(24,23),(17,17),(9,11),(0,10)]
WRIST=(362,396);TIPS=(390,467)
FOOT=[(232,706),(250,706),(256,728),(266,750),(269,763),(256,770),(236,770),(225,761),(227,734)]
ARM=[(268,151),(290,162),(303,181),(307,204),(312,228),(320,258),(329,284),(341,303),(353,330),(363,361),(369,391),(362,402),(355,401),(343,374),(330,346),(315,315),(305,297),(296,271),(288,246),(280,226),(268,214),(262,190)]
LEG=[(262,396),(268,424),(273,455),(269,495),(259,530),(255,552),(257,576),(261,602),(259,636),(253,670),(248,700),(247,713),(232,713),(230,690),(226,662),(220,632),(218,602),(222,578),(219,556),(215,534),(209,505),(204,476),(201,456),(212,430),(236,404)]
def body_shapes():
    o=[cr(HEAD),cr(NECK),cr(TORSO)]
    for s in (1,-1):
        o+=[cr(M([(229,74),(234,72),(236,82),(234,93),(229,94)],s)),cr(M(ARM,s)),cr(M(frame(WRIST,TIPS,HAND_L),s)),cr(M(LEG,s)),cr(M(FOOT,s))]
    return o
BODY=body_shapes()
BODY_D=''.join(BODY)
# ---- shared defs (one hidden SVG per page; widgets reference these ids) ----
def _hatch(a): return (f'<pattern id="bm-h{a}" width="5" height="5" patternUnits="userSpaceOnUse" patternTransform="rotate({a})">'
                       '<line x1="0" y1="0" x2="0" y2="5" class="bm-hl"/></pattern>')
HATCH_ANGLES=(0,20,40,60,80,100,120,140,160)
BM_DEFS=('<svg class="bm-defs" width="0" height="0" aria-hidden="true" focusable="false"><defs>'
 '<radialGradient id="bm-marble" gradientUnits="userSpaceOnUse" cx="175" cy="240" r="560" fx="165" fy="200">'
 '<stop offset="0" class="s1"/><stop offset=".45" class="s2"/><stop offset="1" class="s3"/></radialGradient>'
 '<radialGradient id="bm-marble2" gradientUnits="userSpaceOnUse" cx="175" cy="240" r="560" fx="165" fy="200">'
 '<stop offset="0" class="t1"/><stop offset=".5" class="t2"/><stop offset="1" class="t3"/></radialGradient>'
 '<radialGradient id="bm-stage" cx=".5" cy=".42" r=".75"><stop offset="0" class="g1"/><stop offset="1" class="g2"/></radialGradient>'
 '<linearGradient id="bm-base" x1="0" y1="0" x2="1" y2="0"><stop offset="0" class="s3"/><stop offset=".35" class="s1"/><stop offset="1" class="s3"/></linearGradient>'
 # inner shadow (light from upper left): darkens the lower-right inside edge and lifts the upper-left one -> rounded, carved look
 '<filter id="bm-carve" x="-5%" y="-5%" width="110%" height="110%" color-interpolation-filters="sRGB">'
 '<feGaussianBlur in="SourceAlpha" stdDeviation="4" result="b"/>'
 '<feOffset in="b" dx="-4" dy="-4" result="o1"/><feComposite in="SourceAlpha" in2="o1" operator="out" result="e1"/>'
 '<feFlood class="bm-fsh" result="c1"/><feComposite in="c1" in2="e1" operator="in" result="sh"/>'
 '<feOffset in="b" dx="2.5" dy="2.5" result="o2"/><feComposite in="SourceAlpha" in2="o2" operator="out" result="e2"/>'
 '<feFlood class="bm-fhl" result="c2"/><feComposite in="c2" in2="e2" operator="in" result="hl"/>'
 '<feMerge><feMergeNode in="SourceGraphic"/><feMergeNode in="sh"/><feMergeNode in="hl"/></feMerge></filter>'
 '<filter id="bm-carve-s" x="-10%" y="-10%" width="120%" height="120%" color-interpolation-filters="sRGB">'
 '<feGaussianBlur in="SourceAlpha" stdDeviation="1.6" result="b"/>'
 '<feOffset in="b" dx="-1.6" dy="-1.6" result="o1"/><feComposite in="SourceAlpha" in2="o1" operator="out" result="e1"/>'
 '<feFlood class="bm-fsh" result="c1"/><feComposite in="c1" in2="e1" operator="in" result="sh"/>'
 '<feMerge><feMergeNode in="SourceGraphic"/><feMergeNode in="sh"/></feMerge></filter>'
 '<filter id="bm-soft" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="3.5"/></filter>'
 '<filter id="bm-glow" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="2.5" result="g"/><feMerge><feMergeNode in="g"/><feMergeNode in="SourceGraphic"/></feMerge></filter>'
 '<clipPath id="bm-clip">'+''.join(f'<path d="{d}"/>' for d in BODY)+'</clipPath>'
 +''.join(_hatch(a) for a in HATCH_ANGLES)+
 '<marker id="bm-ar" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path d="M0,0L10,5L0,10z" class="bm-arh"/></marker>'
 '</defs></svg>')
def silhouette(fill_cls='sk',carve=True,outline=True):
    """the whole body: outlines first (thick), fills on top -> one clean union outline"""
    o=''
    if outline: o+='<g class="bm-ol">'+''.join(P(d) for d in BODY)+'</g>'
    o+=f'<g class="{fill_cls}"'+(' filter="url(#bm-carve)"' if carve else '')+'>'+''.join(P(d) for d in BODY)+'</g>'
    return o
def base():
    return ('<g class="bm-base"><path d="M75,776 L75,792 A125,20 0 0 0 325,792 L325,776 Z" class="bm-bs"/>'
            '<ellipse cx="200" cy="776" rx="125" ry="20" class="bm-bt"/><ellipse cx="200" cy="776" rx="118" ry="17" class="bm-bt2"/></g>')
# ---- skin layer line work ----
def skin_lines():
    L=[];S=[]  # L = carved lines, S = soft blurred shading
    def sl(pts,c='ln'): L.append(P(sp(pts),c))
    for s in (1,-1):
        m=lambda pts:M(pts,s)
        sl(m([(206,150),(226,153),(248,151),(270,157)]))                         # clavicle
        sl(m([(205,229),(228,236),(250,231),(266,215),(275,196)]))               # pectoral
        sl(m([(266,163),(272,190),(283,216)]),'ln f')                            # deltoid front
        sl(m([(226,242),(228,282),(225,330),(214,392)]),'ln f')                  # rectus edge
        for y in (268,298,326): sl(m([(203,y),(214,y-2),(225,y)]),'ln ff')       # tendinous lines
        sl(m([(250,330),(257,364),(246,398),(224,425),(209,446)]))               # iliac crest / inguinal line
        sl(m([(258,238),(250,247)]),'ln ff');sl(m([(257,257),(249,264)]),'ln ff');sl(m([(255,276),(248,282)]),'ln ff')
        sl(m([(222,104),(214,124),(206,146)]),'ln f')                            # neck (sternocleidomastoid)
        sl(m([(295,214),(305,250),(313,284)]),'ln f');sl(m([(281,222),(297,284)]),'ln ff')   # biceps
        sl(m([(326,300),(343,340),(357,386)]),'ln ff')                           # forearm
        for v in (-5.5,-0.5,4.5): sl(m(frame(WRIST,TIPS,[(48,v),(62,v),(74,v*.9)])),'ln f')  # fingers
        sl(m(frame(WRIST,TIPS,[(14,9),(24,4),(34,-2)])),'ln ff')                 # palm crease
        sl(m([(256,440),(259,490),(251,540)]),'ln f');sl(m([(224,474),(221,516),(226,546)]),'ln f')   # quads
        sl(m([(254,398),(240,452),(224,520),(220,552)]),'ln ff')                 # sartorius
        L.append(f'<ellipse class="ln" cx="{Mx(236,s)}" cy="561" rx="11" ry="14"/>')                  # kneecap
        sl(m([(241,588),(243,640),(242,700)]),'ln f');sl(m([(222,600),(220,628),(226,652)]),'ln ff')
        sl(m([(236,712),(239,718)]),'ln ff');sl(m([(250,752),(252,766)]),'ln ff');sl(m([(243,754),(244,768)]),'ln ff');sl(m([(236,756),(236,768)]),'ln ff')
        sl(m([(204,70),(213,66),(223,70)]),'ln')                                 # brow
        sl(m([(206,80),(213,77),(221,80)]),'ln');sl(m([(207,81),(214,83),(220,81)]),'ln ff')   # eyelids
        sl(m([(230,80),(232,88)]),'ln ff')
        for pts,w in ((m([(263,232),(259,300),(252,340)]),10),(m([(207,452),(214,520),(222,556)]),8),(m([(277,214),(299,272)]),7),
                      (m([(206,232),(230,240),(252,234),(268,214)]),5),(m([(256,392),(246,420),(228,440)]),6),(m([(244,580),(246,700)]),5),
                      (m([(282,212),(296,214)]),6)):
            S.append(f'<path d="{sp(pts)}" class="bm-shd" style="stroke-width:{w}"/>')
    L+= [P(line([(200,238),(200,334)]),'ln f'),'<ellipse class="ln" cx="200" cy="340" rx="2.6" ry="3.6"/>',
         P(sp([(203,72),(205,90),(207,97)]),'ln f'),P(sp([(195,100),(200,102.5),(205,100)]),'ln'),
         P(sp([(191,108),(196,107),(200,107.8),(204,107),(209,108)]),'ln'),P(sp([(194,111),(200,112),(206,111)]),'ln ff'),P(sp([(193,116),(200,118),(207,116)]),'ln ff')]
    S.append(f'<path d="{sp([(212,121),(200,128),(188,121)])}" class="bm-shd" style="stroke-width:9"/>')
    return '<g clip-path="url(#bm-clip)"><g filter="url(#bm-soft)">'+''.join(S)+'</g>'+''.join(L)+'</g>'
PREVIEW0=[base()+silhouette()+skin_lines()]

# ---- muscles layer (ecorche) ----
MUSCLES=[ # key, right-side outline, fibre angle
 ('neck',[(226,100),(231,108),(215,140),(207,151),(203,147),(218,112)],150),
 ('trap',[(218,124),(234,138),(266,151),(240,151),(222,143)],70),
 ('deltoid',[(258,150),(276,151),(294,162),(304,182),(307,206),(300,228),(291,242),(282,222),(274,196),(266,170)],160),
 ('pecs',[(203,152),(230,154),(258,153),(270,166),(278,192),(285,214),(270,224),(246,236),(222,237),(204,233),(202,196)],100),
 ('biceps',[(285,228),(296,223),(307,240),(315,262),(321,284),(313,293),(302,277),(292,253)],160),
 ('biceps',[(305,214),(311,232),(319,258),(327,282),(322,288),(315,262),(307,240)],160),
 ('forearm',[(322,288),(335,298),(348,322),(360,352),(367,388),(361,393),(349,361),(335,327),(323,303)],158),
 ('forearm',[(309,298),(322,303),(334,327),(348,361),(358,395),(352,399),(340,373),(326,345),(314,319)],158),
 ('serratus',[(257,224),(266,229),(263,236),(252,234)],60),('serratus',[(258,242),(266,247),(263,254),(252,252)],60),('serratus',[(258,260),(265,265),(262,272),(251,270)],60),
 ('obliques',[(250,240),(265,250),(263,290),(257,330),(259,362),(247,381),(230,373),(234,330),(236,290),(240,256)],30),
 ('abs',[(204,238),(225,240),(227,264),(204,266)],0),('abs',[(204,270),(227,268),(227,296),(204,297)],0),('abs',[(204,301),(227,300),(226,326),(204,326)],0),
 ('abs',[(204,330),(226,330),(224,370),(214,402),(204,412)],0),
 ('hipflex',[(258,372),(266,392),(271,420),(267,452),(259,442),(256,404)],10),
 ('quads',[(241,420),(251,430),(257,470),(255,510),(247,541),(239,537),(237,500),(235,460)],2),
 ('quads',[(259,440),(270,452),(273,482),(269,512),(259,541),(251,549),(255,510),(257,470)],4),
 ('quads',[(226,486),(234,500),(238,530),(232,551),(222,549),(218,526),(220,500)],170),
 ('adductors',[(204,440),(226,436),(239,426),(233,460),(223,496),(212,512),(205,480)],20),
 ('sartorius',[(250,384),(258,389),(248,430),(236,480),(226,525),(222,557),(216,555),(218,520),(228,476),(240,426)],25),
 ('shin',[(238,582),(246,586),(249,620),(247,660),(242,701),(237,701),(240,660),(240,620)],2),
 ('shin',[(250,590),(258,601),(258,640),(252,681),(247,701),(246,660),(250,620)],2),
 ('calf',[(222,584),(230,590),(232,620),(230,650),(224,663),(219,640),(218,606)],176),
 ('calf',[(226,662),(232,668),(234,700),(230,709),(227,690)],178)]
def muscles():
    o=[base(),silhouette('sk2',carve=True)]
    o.append('<g clip-path="url(#bm-clip)">')
    for s in (1,-1):
        for k,pts,a in MUSCLES:
            d=cr(M(pts,s));aa=a if s>0 else (180-a)%180;aa=min(HATCH_ANGLES,key=lambda h:abs(h-aa))
            o.append(f'<g class="ms" data-k="{k}"><path d="{d}" class="msf" filter="url(#bm-carve-s)"/><path d="{d}" class="msh" style="fill:url(#bm-h{aa})"/><path d="{d}" class="mso"/></g>')
        o.append(f'<ellipse class="ms-pat" cx="{Mx(236,s)}" cy="560" rx="10" ry="13"/>')
        o.append(P(sp(M([(206,150),(226,153),(248,151),(268,156)],s)),'ln'))
    o.append(P(line([(200,236),(200,412)]),'ln'))
    o.append('</g>')
    # statue head stays smooth marble, as on the reference: face lines only
    o.append('<g clip-path="url(#bm-clip)">'+''.join(P(sp(M(p,s)),'ln') for s in (1,-1) for p in ([(204,70),(213,66),(223,70)],[(206,80),(213,77),(221,80)]))
             +P(sp([(203,72),(205,90),(207,97)]),'ln f')+P(sp([(195,100),(200,102.5),(205,100)]),'ln')+P(sp([(191,108),(196,107),(200,107.8),(204,107),(209,108)]),'ln')+'</g>')
    return ''.join(o)

# ---- ghost body for the inner layers ----
def ghost():
    return base()+'<g class="ghostg">'+silhouette('sk',False,True)+'</g>'
def fing(pts): return P(sp(pts),'fing')+P(sp(pts),'fing-in')
def bone(d,k=None,extra=''): return P(d,'bn',k,extra)
def bones():
    o=[ghost(),'<g class="bones" filter="url(#bm-carve-s)">']
    # skull
    o.append(f'<g data-k="skull">'+bone(cr(sym([(200,36),(215,38),(226,48),(230,64),(229,84),(224,98),(220,104),(214,108),(212,118),(204,123),(200,124)])))
             +''.join(P(cr(M([(193,72),(181,70),(176,79),(181,88),(193,86),(196,79)],s)),'bn-h') for s in (1,-1))
             +P(cr([(200,88),(205,97),(203,102),(197,102),(195,97)]),'bn-h')+P(line([(188,110),(212,110)]),'bn-l')+P(line([(190,114),(210,114)]),'bn-l')+'</g>')
    # spine (neck + lower back; the chest part sits behind the breastbone)
    sp_=''.join(bone(cr([(193,y),(207,y),(208,y+8),(192,y+8)]),None) for y in range(124,150,9))
    sp_+=''.join(bone(cr([(190,y),(210,y),(212,y+12),(188,y+12)])) for y in range(266,350,16))
    o.append(f'<g data-k="spine">{sp_}</g>')
    # ribcage
    rc=''
    for i in range(10):
        y=164+i*10.5;w=40+min(i,5)*7-max(0,i-6)*3;drop=18+i*1.6
        for s in (1,-1):
            pts=M([(205,y),(218,y-3),(200+w*.75,y+2),(200+w,y+drop*.55),(200+w*.98,y+drop)],s)
            rc+=P(sp(pts),'rib')+P(sp(pts),'rib-in')
    o.append(f'<g data-k="ribs">{rc}</g>')
    o.append('<g data-k="sternum">'+bone(cr([(194,154),(206,154),(207,166),(204,170),(205,222),(200,234),(195,222),(196,170),(193,166)]))+'</g>')
    for s in (1,-1):
        o.append('<g data-k="clavicle">'+bone(capsule(Mx(205,s),152,4,Mx(268,s),156,4.5))+'</g>')
        o.append('<g data-k="shoulder">'+bone(cr(M([(262,150),(282,154),(286,166),(276,186),(266,200),(262,178)],s)))+'</g>')
        # arm
        o.append('<g data-k="humerus">'+bone(cr(M([(278,168),(291,170),(293,184),(288,196)],s)))+bone(capM(s,287,186,6.5,316,286,6))+bone(cr(M([(306,282),(322,280),(327,292),(318,298),(308,296)],s)))+'</g>')
        o.append('<g data-k="forearm-bones">'+bone(capM(s,322,296,4.5,366,392,5.5))+bone(capM(s,311,297,4.5,354,397,4))+'</g>')
        o.append('<g data-k="hand-bones">'+bone(cr(M(frame(WRIST,TIPS,[(2,-9),(14,-11),(16,9),(4,10)]),s)))
                 +''.join(fing(M(frame(WRIST,TIPS,[(16,v0),(46,v),(62,v*1.05),(76,v*.95)]),s)) for v0,v in ((-8,-7),(-3,-2.5),(2,2),(6,6.5)))
                 +fing(M(frame(WRIST,TIPS,[(14,9),(24,15),(30,20)]),s))+'</g>')
        # pelvis
        o.append('<g data-k="pelvis">'+bone(cr(M([(210,352),(232,338),(254,342),(264,362),(258,388),(244,402),(236,416),(222,430),(204,434),(203,422),(214,408),(212,384)],s)))
                 +P(cr(M([(214,418),(226,412),(230,424),(220,430)],s)),'bn-h')+'</g>')
        o.append('<g data-k="femur">'+bone(cr(M([(232,404),(243,402),(258,410),(262,422),(252,430)],s)))+bone(capM(s,252,424,7.5,238,544,7))+bone(cr(M([(222,542),(240,538),(252,548),(248,566),(224,566)],s)))+'</g>')
        o.append(f'<g data-k="kneecap"><ellipse class="bn" cx="{Mx(237,s)}" cy="557" rx="9" ry="11"/></g>')
        o.append('<g data-k="shin-bones">'+bone(cr(M([(222,568),(250,568),(246,584),(240,700),(244,708),(230,710),(232,700),(228,584)],s)))+bone(capM(s,253,578,3.5,250,706,3.5))+'</g>')
        o.append('<g data-k="foot-bones">'+bone(cr(M([(232,708),(248,708),(252,724),(236,726)],s)))+''.join(fing(M([(238+i*4,724),(240+i*6,746),(242+i*7.5,764)],s)) for i in range(4))+'</g>')
    o.append('<g data-k="pelvis">'+bone(cr([(190,352),(210,352),(212,384),(206,404),(200,410),(194,404),(188,384)]))+'</g>')
    o.append('</g>')
    return ''.join(o)

# ---- organs (torso cutaway) ----
CAV=cr(sym([(200,142),(214,143),(238,150),(256,160),(262,182),(260,232),(256,290),(248,330),(250,368),(254,398),(244,420),(222,430),(200,434)]))
HEART=cr([(192,206),(202,198),(216,198),(230,204),(240,216),(240,230),(232,242),(220,252),(210,258),(200,250),(190,236),(186,220)])
def og(k,d,cls='og',extra=''): return f'<g class="ogk" data-k="{k}">'+P(d,cls,None,extra)+'</g>'
def tube(pts,w=''): return P(sp(pts),'tb'+w)+P(sp(pts),'tb-in'+w)
BRAIN=cr([(200,42),(219,46),(226,60),(223,76),(212,84),(200,82),(188,84),(177,76),(174,60),(181,46)])
def brain():
    gy=''.join(P(sp(pts),'gy') for pts in ([(186,52),(194,58),(190,66),(198,72)],[(214,52),(206,58),(210,66),(202,74)],[(180,66),(186,72),(182,78)],[(220,66),(214,72),(218,78)],[(200,44),(200,80)]))
    return f'<g class="ogk" data-k="brain">{P(BRAIN,"og")}{gy}</g>'
LI=[(204,414),(198,402),(180,398),(162,392),(156,374),(156,352),(158,336),(170,328),(200,332),(230,328),(244,334),(248,354),(248,374),(242,390),(226,398),(212,402)]
def organs():
    o=[base(),silhouette('sk',True,True),'<g class="cut">',P(CAV,'cav'),P(cr([(200,40),(222,44),(228,62),(222,82),(200,88),(178,82),(172,62),(178,44)]),'cav'),brain()]
    o.append('<g class="org-in" filter="url(#bm-carve-s)">')
    # lungs: right lung (viewer left) has three lobes, left lung two and a notch for the heart
    RL=[(194,166),(184,156),(168,164),(154,186),(146,220),(144,256),(160,262),(180,258),(194,252),(196,210)]
    LL=[(206,166),(216,156),(232,164),(246,186),(254,220),(256,258),(240,264),(226,262),(238,246),(236,224),(222,208),(206,204)]
    o.append('<g class="ogk" data-k="lungs">'+P(cr(RL),'og')+P(cr(LL),'og')+P(sp([(192,190),(170,214),(148,236)]),'gy')+P(sp([(180,214),(160,222),(146,224)]),'gy')+P(sp([(208,186),(232,210),(252,238)]),'gy')+'</g>')
    o.append('<g class="ogk" data-k="trachea">'+P(capsule(200,110,5,200,172,5),'og')+''.join(P(line([(196,y),(204,y)]),'gy') for y in range(116,170,6))+tube([(200,170),(190,176),(178,186)],' s')+tube([(200,170),(210,176),(222,186)],' s')+'</g>')
    o.append('<g class="ogk" data-k="esophagus">'+tube([(206,112),(207,172),(210,232),(216,262)],' e')+'</g>')
    o.append('<g class="ogk" data-k="heart">'+P(HEART,'og')+P(sp([(206,200),(214,228),(224,250)]),'gy')+tube([(206,204),(205,188),(213,182),(220,190),(219,204)],' e')+'</g>')
    o.append('<g class="ogk" data-k="diaphragm">'+P(sp([(142,272),(160,258),(184,254),(200,262),(216,258),(240,256),(258,270)]),'dia')+'</g>')
    # pancreas sits behind the stomach
    o.append(og('pancreas',cr([(196,314),(212,316),(232,312),(250,304),(254,310),(246,318),(228,324),(206,326),(192,322)])))
    o.append(og('spleen',cr([(250,270),(260,278),(262,298),(254,306),(248,292)])))
    o.append(og('stomach',cr([(214,262),(224,264),(238,266),(250,278),(252,296),(244,310),(228,316),(212,316),(202,310),(204,300),(218,300),(230,292),(228,280),(218,272)])))
    # liver: big wedge on the body's right side (viewer left), thinning across the midline
    o.append(og('liver',cr([(144,268),(158,258),(184,258),(206,264),(226,266),(236,272),(222,280),(204,288),(184,300),(164,310),(150,306),(142,290)])))
    o.append(og('gallbladder',cr([(176,298),(184,294),(190,302),(186,312),(178,312)])))
    # large intestine frame, then the small intestine coil inside it
    o.append('<g class="ogk" data-k="large-intestine">'+P(sp(LI),'colon')+P(sp(LI),'colon-in')+''.join(P(line([(x-4,y),(x+4,y)]),'gy') for x,y in ((156,350),(156,370),(248,350),(248,370)))+''.join(P(line([(x,y-4),(x,y+4)]),'gy') for x,y in ((182,331),(218,331)))+tube([(160,388),(162,402),(158,408)],' s')+'</g>')
    si=[]
    for r in range(5):
        y=346+r*10;xs=(174,226) if r%2==0 else (226,174)
        si+=[(xs[0],y),((xs[0]+xs[1])/2,y+2),(xs[1],y)]
    si=[(214,318),(222,330),(212,340)]+si+[(180,394),(166,392)]
    o.append('<g class="ogk" data-k="small-intestine">'+P(sp(si),'si')+P(sp(si),'si-in')+'</g>')
    for s_ in (-1,1):
        o.append('<g class="ogk back" data-k="kidneys">'+P(cr(M([(232,300),(244,304),(248,320),(244,336),(232,338),(228,326),(234,320),(228,312)],s_)),'og bk')+'</g>')
    o.append(og('bladder',cr([(190,414),(200,410),(210,414),(212,426),(206,432),(194,432),(188,426)])))
    o.append('</g></g>')
    return ''.join(o)

# ---- nerves ----
def nv(pts,k=None,w=''):
    return f'<g class="nvk"{f" data-k=\"{k}\"" if k else ""}>'+P(sp(pts),'nv'+w)+P(sp(pts),'nv-in'+w)+'</g>'
def nerves():
    o=[ghost(),'<g class="nerves">']
    o.append(brain().replace('ogk','nvk',1))
    o.append(nv([(200,88),(200,120),(200,200),(200,300),(200,330)],'spinal-cord',' cord'))
    o.append('<g class="nvk" data-k="spinal-cord">'+''.join(P(sp([(200,330),(200+d,370),(200+d*1.6,410)]),'nv') for d in (-6,-2,2,6))+'</g>')
    for s_ in (1,-1):
        # brachial plexus -> median nerve to the hand
        o.append(nv(M([(202,150),(230,158),(262,170),(290,196),(304,240),(318,292),(340,344),(360,396),(374,424)],s_),'arm-nerves'))
        o.append(nv(M([(306,250),(298,290),(330,340),(354,400)],s_),'arm-nerves',' t'))
        # intercostal nerves
        for i in range(6):
            y=178+i*17
            o.append(nv(M([(202,y),(226,y+2),(246,y+10),(256,y+22)],s_),'intercostal',' t'))
        # lumbar plexus -> femoral (front thigh)
        o.append(nv(M([(202,340),(220,380),(236,420),(246,470),(252,520)],s_),'femoral'))
        # sciatic (back of thigh) -> tibial down the leg (dashed: it runs behind)
        o.append('<g class="nvk" data-k="sciatic">'+P(sp(M([(204,380),(222,412),(232,450),(236,500),(236,556),(238,620),(240,700),(244,740)],s_)),'nv back')+'</g>')
    # vagus: brain stem to heart and gut
    o.append('<g class="nvk" data-k="vagus">'+P(sp([(194,90),(192,140),(194,200),(198,260),(206,300),(200,340)]),'nv vg')+'</g>')
    o.append('</g>')
    return ''.join(o)

# ---- circulation ----
ART={'aorta':[(214,196),(216,180),(206,176),(202,190),(203,230),(203,290),(202,352)],
 'carotid':[(198,178),(194,140),(192,110),(194,90)],
 'arm-artery':[(206,178),(236,160),(266,170),(290,200),(306,250),(318,292),(338,340),(360,392),(370,420)],
 'leg-artery':[(202,352),(216,380),(232,420),(238,470),(236,540),(236,560),(238,620),(240,700),(246,736)]}
VEIN={'vena-cava':[(194,196),(194,140),(196,120)],
 'vena-cava-low':[(194,236),(196,300),(198,354)],
 'jugular':[(190,180),(186,140),(184,108),(186,90)],
 'arm-vein':[(196,170),(234,154),(262,164),(282,196),(296,250),(310,292),(330,344),(352,396),(360,420)],
 'leg-vein':[(198,354),(210,382),(226,420),(230,470),(229,540),(230,560),(232,620),(234,700),(238,736)]}
PORTAL=[(204,360),(206,340),(200,322),(190,306),(182,292),(184,280)]
THORACIC=[(198,312),(197,280),(198,230),(200,190),(204,160),(214,148),(224,148)]
def vessel(pts,cls,k): return f'<g class="cvk" data-k="{k}">'+P(sp(pts),cls)+'</g>'
def circulation():
    o=[ghost(),'<g class="circ">']
    for s_ in (1,-1):
        for k,pts in VEIN.items():
            if k.startswith('vena'): 
                if s_<0: continue
                o.append(vessel(pts,'vn big',k.replace('-low','')))
            else: o.append(vessel(M(pts,s_) if s_>0 else M(pts,-1),'vn',k))
    for s_ in (1,-1):
        for k,pts in ART.items():
            if k=='aorta':
                if s_<0: continue
                o.append(vessel(pts,'ar big',k))
            elif k=='carotid': o.append(vessel(pts if s_<0 else [(206,178),(208,140),(208,110),(206,90)],'ar',k))
            else: o.append(vessel(M(pts,s_),'ar',k))
    o.append(vessel(PORTAL,'vn portal','portal-vein'))
    o.append(vessel(THORACIC,'lym','thoracic-duct'))
    o.append('<g class="cvk" data-k="heart">'+P(HEART,'og hrt')+P(sp([(206,200),(214,228),(224,250)]),'gy')+'</g>')
    o.append('</g>')
    return ''.join(o)

# ---- close-ups (drawn beside the body; the dive moves the viewBox onto them) ----
def frame_box(x,y,w,h,title_k):
    return f'<rect class="cu-bg" x="{x}" y="{y}" width="{w}" height="{h}" rx="10"/>'
def skin_close():
    X,Y=450,100;o=['<g class="cu" data-close="skin">',frame_box(X,Y,200,400,'skin')]
    # layers
    o.append('<g class="ogk" data-k="epidermis">'+P(f'M{X+10},{Y+60} '+' '.join(f'Q{X+10+i*30+15},{Y+52+(i%2)*6} {X+10+(i+1)*30},{Y+60}' for i in range(6))+f' L{X+190},{Y+92} L{X+10},{Y+92}Z','og ep')+'</g>')
    o.append('<g class="ogk" data-k="dermis">'+P(f'M{X+10},{Y+92} L{X+190},{Y+92} L{X+190},{Y+250} L{X+10},{Y+250}Z','og de')+'</g>')
    fat=''.join(f'<ellipse class="fc" cx="{X+22+c*26+(r%2)*13}" cy="{Y+268+r*22}" rx="12" ry="10"/>' for r in range(6) for c in range(7) if X+22+c*26+(r%2)*13<X+190)
    o.append(f'<g class="ogk" data-k="subcutaneous-fat"><rect class="og sf" x="{X+10}" y="{Y+250}" width="180" height="140"/>{fat}</g>')
    # hair follicle + hair
    o.append('<g class="ogk" data-k="hair-follicle">'+P(sp([(X+60,Y+10),(X+62,Y+60),(X+66,Y+150),(X+70,Y+210)]),'hair')+P(cr([(X+58,Y+92),(X+74,Y+92),(X+80,Y+200),(X+76,Y+222),(X+64,Y+222),(X+58,Y+200)]),'og fol')+'</g>')
    # sweat gland: coil in the deep dermis, duct up to a pore
    coil=' '.join(f'{X+142+12*__import__("math").cos(t/2)},{Y+222+7*__import__("math").sin(t/2)+t*0.5}' for t in range(0,30))
    o.append('<g class="ogk" data-k="sweat-gland">'+P(sp([(X+150,Y+56),(X+146,Y+120),(X+152,Y+180),(X+142,Y+220)]),'duct')+f'<polyline class="duct" points="{coil}"/></g>')
    # capillary loop
    o.append('<g class="ogk" data-k="skin-vessels">'+P(sp([(X+10,Y+236),(X+100,Y+226),(X+112,Y+110),(X+120,Y+104),(X+128,Y+110),(X+130,Y+226),(X+190,Y+238)]),'ar')+P(sp([(X+10,Y+244),(X+100,Y+236),(X+118,Y+120),(X+136,Y+236),(X+190,Y+246)]),'vn')+'</g>')
    o.append('</g>');return ''.join(o)
def bone_close():
    X,Y=700,100;o=['<g class="cu" data-close="bone">',frame_box(X,Y,200,400,'bone')]
    out=cr([(X+60,Y+40),(X+100,Y+26),(X+140,Y+40),(X+150,Y+80),(X+126,Y+110),(X+122,Y+300),(X+148,Y+330),(X+146,Y+372),(X+100,Y+384),(X+54,Y+372),(X+52,Y+330),(X+78,Y+300),(X+74,Y+110),(X+50,Y+80)])
    o.append(f'<g class="ogk" data-k="compact-bone">{P(out,"og cb")}</g>')
    o.append('<g class="ogk" data-k="marrow">'+P(cr([(X+88,Y+120),(X+112,Y+120),(X+110,Y+290),(X+90,Y+290)]),'mar')+'</g>')
    sp_=''
    for (cx,cy) in ((X+100,Y+72),(X+100,Y+338)):
        sp_+=P(cr([(cx-36,cy-20),(cx,cy-34),(cx+36,cy-20),(cx+28,cy+20),(cx,cy+28),(cx-28,cy+20)]),'spg')
        sp_+=''.join(f'<circle class="tr" cx="{cx+dx}" cy="{cy+dy}" r="3.2"/>' for dx in range(-24,30,10) for dy in range(-18,24,9) if abs(dx)+abs(dy)<38)
    o.append(f'<g class="ogk" data-k="spongy-bone">{sp_}</g>')
    o.append('<g class="ogk" data-k="cartilage">'+P(sp([(X+58,Y+46),(X+100,Y+30),(X+142,Y+46)]),'cart-c')+P(sp([(X+58,Y+368),(X+100,Y+380),(X+142,Y+368)]),'cart-c')+'</g>')
    o.append('<g class="ogk" data-k="periosteum">'+P(sp([(X+71,Y+120),(X+70,Y+290)]),'peri')+P(sp([(X+129,Y+120),(X+130,Y+290)]),'peri')+'</g>')
    o.append('</g>');return ''.join(o)
def villus_close():
    X,Y=950,100;o=['<g class="cu" data-close="villus">',frame_box(X,Y,200,400,'villus')]
    V=[(X+60,Y+330),(X+56,Y+200),(X+60,Y+90),(X+80,Y+46),(X+100,Y+38),(X+120,Y+46),(X+140,Y+90),(X+144,Y+200),(X+140,Y+330)]
    o.append('<g class="ogk" data-k="villus">'+P(sp(V),'vil')+P(f'M{X+10},{Y+330}L{X+190},{Y+330}L{X+190},{Y+390}L{X+10},{Y+390}Z','og wall')+P(sp([(X+10,Y+330),(X+30,Y+300),(X+40,Y+330)]),'vil s')+P(sp([(X+160,Y+330),(X+172,Y+300),(X+190,Y+330)]),'vil s')+'</g>')
    # absorbing cells with a brush border along the outside
    o.append('<g class="ogk" data-k="enterocytes">'+P(sp([(X+66,Y+320),(X+63,Y+200),(X+67,Y+96),(X+84,Y+56),(X+100,Y+49),(X+116,Y+56),(X+133,Y+96),(X+137,Y+200),(X+134,Y+320)]),'ent')+''.join(P(line([(X+57,y),(X+66,y)]),'cellw') for y in range(Y+110,Y+330,14))+''.join(P(line([(X+134,y),(X+143,y)]),'cellw') for y in range(Y+110,Y+330,14))+'</g>')
    o.append('<g class="ogk" data-k="microvilli">'+P(sp(V),'brush')+'</g>')
    o.append('<g class="ogk" data-k="villus-capillaries">'+P(sp([(X+76,Y+380),(X+76,Y+200),(X+80,Y+90),(X+100,Y+70),(X+120,Y+90)]),'ar')+P(sp([(X+120,Y+90),(X+124,Y+200),(X+124,Y+380)]),'vn')+''.join(P(sp([(X+77,y),(X+100,y-8),(X+123,y)]),'cap') for y in range(Y+120,Y+320,40))+'</g>')
    o.append('<g class="ogk" data-k="lacteal">'+P(sp([(X+100,Y+96),(X+100,Y+200),(X+100,Y+390)]),'lac')+'</g>')
    o.append('</g>');return ''.join(o)
