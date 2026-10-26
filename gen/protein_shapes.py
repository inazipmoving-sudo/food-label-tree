# Protein Figure 5 close-up diagrams (secondary + tertiary structure). Geometry is computed here; every label is page HTML
# positioned over the drawing (never SVG text). Atom colours match the course's ball-and-stick molecules (lipids_mol / molkit).
import math, html as _h
FC={'C':'#333333','O':'#e02020','H':'#f2f2f2','N':'#3050F8','S':'#E8D21E'}; EC={'C':'#111','O':'#7a0000','H':'#6f6f6f','N':'#0b1f8a','S':'#7a6a00'}
RAD={'C':0.27,'O':0.25,'H':0.15,'N':0.26,'S':0.30}   # bond-length units, same ratios as the molecule drawings
HB='#1F4E79'
def _sub(a,b): return [a[i]-b[i] for i in range(3)]
def _add(a,b): return [a[i]+b[i] for i in range(3)]
def _mul(a,k): return [x*k for x in a]
def _dot(a,b): return sum(a[i]*b[i] for i in range(3))
def _cross(a,b): return [a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]]
def _nrm(a): l=math.sqrt(_dot(a,a)); return _mul(a,1/l)
def _place(A,B,C,bond,ang,tor):
    ang,tor=math.radians(ang),math.radians(tor); bc=_nrm(_sub(C,B)); n=_nrm(_cross(_sub(B,A),bc)); m=_cross(n,bc)
    return _add(C,_add(_mul(bc,-bond*math.cos(ang)),_add(_mul(m,bond*math.sin(ang)*math.cos(tor)),_mul(n,bond*math.sin(ang)*math.sin(tor)))))
def _backbone(n,phi,psi):
    """real backbone geometry (NeRF): standard bond lengths/angles, given phi/psi, trans peptide bonds; adds carbonyl O and amide H"""
    N=[0,0,0];CA=[1.458,0,0];C=_place([0,1,0],N,CA,1.525,111.2,-60);R=[dict(N=N,CA=CA,C=C)]
    for i in range(1,n):
        p=R[-1];Nn=_place(p['N'],p['CA'],p['C'],1.329,116.2,psi);CAn=_place(p['CA'],p['C'],Nn,1.458,121.7,180);Cn=_place(p['C'],Nn,CAn,1.525,111.2,phi)
        R.append(dict(N=Nn,CA=CAn,C=Cn))
    for i,r in enumerate(R):
        if i+1<n: r['O']=_place(R[i+1]['N'],r['CA'],r['C'],1.231,120.5,180)
        if i>0: r['H']=_place(R[i-1]['O'],R[i-1]['C'],r['N'],1.01,119.5,180)
    return R
def _axis(P):
    c=_mul([sum(p[i] for p in P) for i in range(3)],1/len(P)); Q=[_sub(p,c) for p in P]
    v=_nrm(_sub(P[-1],P[0]))
    for _ in range(60):
        w=[sum(q[i]*_dot(q,v) for q in Q) for i in range(3)]; v=_nrm(w)
    return c,v
def _lab(x,y,vb,txt,cls=''):
    return f'<span class="ssl{(" "+cls) if cls else ""}" style="left:{100*(x-vb[0])/vb[2]:.2f}%;top:{100*(y-vb[1])/vb[3]:.2f}%">{txt}</span>'
def _atoms_svg(atoms,bonds,hbonds,s,hi=()):
    """atoms: list of (el,x,y,z) already in drawing units; painter's order by depth (z toward the viewer = larger)."""
    z=[a[3] for a in atoms]; z0,z1=min(z),max(z); f=lambda zz:(zz-z0)/(z1-z0) if z1>z0 else 1.0
    items=[]
    for i,j in bonds:
        a,b=atoms[i],atoms[j]; isH='H' in (a[0],b[0]); d=f((a[3]+b[3])/2)
        items.append(((a[3]+b[3])/2-0.01,f'<line x1="{a[1]:.1f}" y1="{a[2]:.1f}" x2="{b[1]:.1f}" y2="{b[2]:.1f}" stroke="{"#9a9a9a" if isH else "#7a7a7a"}" stroke-width="{(0.075 if isH else 0.12)*s:.1f}" stroke-linecap="round" opacity="{0.55+0.45*d:.2f}"/>'))
    for k,(i,j) in enumerate(hbonds):
        a,b=atoms[i],atoms[j]; on=k in hi
        items.append((max(a[3],b[3])+0.02,f'<line x1="{a[1]:.1f}" y1="{a[2]:.1f}" x2="{b[1]:.1f}" y2="{b[2]:.1f}" stroke="{"#C2410C" if on else HB}" stroke-width="{3.2 if on else 2.2}" stroke-dasharray="{"6 4" if on else "4 4"}" stroke-linecap="round"/>'))
    for el,x,y,zz in atoms:
        d=f(zz); r=RAD[el]*s*(0.85+0.15*d)
        items.append((zz,f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.1f}" fill="{FC[el]}" stroke="{EC[el]}" stroke-width="{1.3 if el=="H" else 1}" opacity="{0.6+0.4*d:.2f}"/>'))
    items.sort(key=lambda t:t[0]); return ''.join(t[1] for t in items)
def _panel(title,vb,inner,labels,aria,legend,cap=None,maxw=None):
    return (f'<div class="ssp" role="button" tabindex="0" aria-label="{_h.escape(title)}: tap to enlarge"{f" style=\"max-width:{maxw}px\"" if maxw else ""}><p class="ssh">{title}</p>'
            f'<div class="ssa"><svg class="sgd" viewBox="{" ".join(str(v) for v in vb)}" role="img" aria-label="{_h.escape(aria)}">{inner}</svg>{"".join(labels)}</div>'
            +(f'<div class="sslg">{legend}</div>' if legend else '')+(f'<p class="ssc">{cap}</p>' if cap else '')
            +'<svg class="zi" viewBox="0 0 16 16" aria-hidden="true"><circle cx="6.5" cy="6.5" r="4.5"/><path d="M10 10l4 4M4.5 6.5h4M6.5 4.5v4"/></svg></div>')
def _dot_(c,ec,t): return f'<span><i style="background:{c};border-color:{ec}"></i>{t}</span>'
ATOM_LEGEND=_dot_(FC['C'],EC['C'],'carbon')+_dot_(FC['N'],EC['N'],'nitrogen')+_dot_(FC['O'],EC['O'],'oxygen')+_dot_(FC['H'],EC['H'],'hydrogen')+'<span><b class="hbk"></b>hydrogen bond</span>'

def helix_panel():
    n=9; R=_backbone(n,-57.8,-47.0)
    P=[r['CA'] for r in R]; c,ax=_axis(P)
    up=_nrm(_cross(ax,[0.3,0.2,0.93])); dep=_cross(ax,up)
    s=34.0  # drawing units per angstrom
    atoms=[];idx={}
    def add(key,el,p):
        q=_sub(p,c); idx[key]=len(atoms); atoms.append((el,_dot(q,ax)*s,-_dot(q,up)*s,_dot(q,dep)))
    for i,r in enumerate(R):
        for k,el in (('N','N'),('CA','C'),('C','C'),('O','O'),('H','H')):
            if k in r: add((i,k),el,r[k])
    bonds=[]
    for i,r in enumerate(R):
        bonds+= [(idx[(i,'N')],idx[(i,'CA')]),(idx[(i,'CA')],idx[(i,'C')])]
        if 'O' in r: bonds.append((idx[(i,'C')],idx[(i,'O')]))
        if 'H' in r: bonds.append((idx[(i,'N')],idx[(i,'H')]))
        if i+1<n: bonds.append((idx[(i,'C')],idx[(i+1,'N')]))
    hb=[(idx[(i,'O')],idx[(i+4,'H')]) for i in range(n-4)]
    # highlight the hydrogen bond nearest the viewer
    k=max(range(len(hb)),key=lambda k:atoms[hb[k][0]][3]+atoms[hb[k][1]][3]); i0=k
    xs=[a[1] for a in atoms]; ys=[a[2] for a in atoms]; pad=0.4*s
    x0,x1,y0,y1=min(xs)-pad,max(xs)+pad,min(ys)-pad-58,max(ys)+pad+58
    vb=(round(x0),round(y0),round(x1-x0),round(y1-y0))
    # translucent spiral ribbon through the alpha carbons, behind the atoms
    ca=[atoms[idx[(i,'CA')]] for i in range(n)]
    d='M'+' '.join(f'{p[1]:.1f},{p[2]:.1f}' for p in ca[:1])
    for a,b,cc,dd in zip([ca[0]]+ca[:-2],ca[:-1],ca[1:],ca[2:]+[ca[-1]]):
        d+=f' C{b[1]+(cc[1]-a[1])/6:.1f},{b[2]+(cc[2]-a[2])/6:.1f} {cc[1]-(dd[1]-b[1])/6:.1f},{cc[2]-(dd[2]-b[2])/6:.1f} {cc[1]:.1f},{cc[2]:.1f}'
    rib=f'<path d="{d}" fill="none" stroke="#3E5C76" stroke-opacity=".16" stroke-width="{0.9*s:.0f}" stroke-linecap="round" stroke-linejoin="round"/>'
    inner=rib+_atoms_svg(atoms,bonds,hb,s,hi=(k,))
    O=atoms[hb[k][0]];H=atoms[hb[k][1]]; mid=(y0+y1)/2
    # C=O label in the top margin, N–H label in the bottom margin, so they never collide even on a phone
    def lead(a,top):
        ty=y0+40 if top else y1-40
        return f'<line x1="{a[1]:.1f}" y1="{a[2]:.1f}" x2="{a[1]:.1f}" y2="{ty:.1f}" stroke="#C2410C" stroke-width="1.6"/>'
    inner+=lead(O,True)+lead(H,False)
    labs=[_lab(O[1],y0+22,vb,'C=O<small>amino acid 1</small>','hot two'),_lab(H[1],y1-22,vb,'N–H<small>amino acid 5</small>','hot two'),
          _lab(x0+4,y0+16,vb,'N-terminus','end l'),_lab(x1-4,y0+16,vb,'C-terminus','end r')]
    return _panel('Alpha helix: each C=O bonds to the N–H four amino acids along',vb,inner,labs,
        'Alpha helix drawn ball-and-stick, backbone only: the chain winds into a spiral, and every C=O (red oxygen) is joined by a dashed hydrogen bond to the N–H (blue nitrogen, white hydrogen) four amino acids further along. One bond is highlighted.',
        ATOM_LEGEND,'Backbone only (side chains left off), real helix geometry: 3.6 amino acids per turn. The bonds all run along the spiral\'s length, which holds it like a spring.')
def sheet_panel():
    s=30.0; dx=3.4; dy=4.8; nres=5; atoms=[]; bonds=[]; hb=[]; Hpos={}; Opos={}
    strands=[(0,1),(1,-1),(2,1)]  # (row, direction): +1 runs left to right (N to C), -1 right to left: antiparallel
    for row,dr in strands:
        y=-row*dy; prevC=None
        order=range(nres) if dr==1 else range(nres-1,-1,-1)
        for t,k in enumerate(order):
            x=k*dx; side=(1 if (k+row)%2==0 else -1)   # +1 = points up the page (toward the next strand up)
            ca=len(atoms); atoms.append(('C',x,y+0.25*side,0))
            nx=x-dr*1.15; ni=len(atoms); atoms.append(('N',nx,y+0.32*side,0))
            cx=x+dr*1.15; ci=len(atoms); atoms.append(('C',cx,y+0.32*side,0))
            bonds+=[(ni,ca),(ca,ci)]
            if prevC is not None: bonds.append((prevC,ni))
            if t>0 or True:
                hi=len(atoms); atoms.append(('H',nx,y+0.32*side+1.0*side,0)); bonds.append((ni,hi)); Hpos[(row,round(nx,2),side)]=hi
            if t<nres-1:
                oi=len(atoms); atoms.append(('O',cx,y+0.32*side+1.23*side,0)); bonds.append((ci,oi)); Opos[(row,round(cx,2),side)]=oi
            prevC=ci
    for (row,x,side),o in Opos.items():
        tr=row-side
        for key in ((tr,x,-side),):
            if key in Hpos: hb.append((o,Hpos[key]))
    # to drawing coords (y down)
    atoms=[(e,x*s,-y*s,z) for e,x,y,z in atoms]
    xs=[a[1] for a in atoms]; ys=[a[2] for a in atoms]; padx=1.9*s; pady=0.6*s
    x0,x1,y0,y1=min(xs)-padx,max(xs)+padx,min(ys)-pady,max(ys)+pady
    vb=(round(x0),round(y0),round(x1-x0),round(y1-y0))
    arrows=''
    for row,dr in strands:
        yy=row*dy*s; a,b=(min(xs)-0.6*s,max(xs)+0.6*s)
        if dr==-1: a,b=b,a
        hw=0.55*s; L=b-a; hl=0.9*s*(1 if L>0 else -1)
        arrows+=(f'<path d="M{a:.1f},{yy-hw:.1f} L{b-hl:.1f},{yy-hw:.1f} L{b-hl:.1f},{yy-hw*1.7:.1f} L{b:.1f},{yy:.1f} L{b-hl:.1f},{yy+hw*1.7:.1f} L{b-hl:.1f},{yy+hw:.1f} L{a:.1f},{yy+hw:.1f}Z" fill="#7A8256" fill-opacity=".16" stroke="#7A8256" stroke-opacity=".5" stroke-width="1.5"/>')
    k=0; best=None
    for k2,(o,h) in enumerate(hb):
        if best is None or abs(atoms[o][1]-sum(xs)/len(xs))+abs(atoms[o][2]-((0.5*dy*s)))<best[0]: best=(abs(atoms[o][1]-sum(xs)/len(xs))+abs(atoms[o][2]-0.5*dy*s),k2)
    k=best[1]
    inner=arrows+_atoms_svg(atoms,bonds,hb,s,hi=(k,))
    O=atoms[hb[k][0]];H=atoms[hb[k][1]]
    labs=[_lab(O[1]+(0.95*s),O[2],vb,'C=O','hot'),_lab(H[1]+(0.95*s),H[2],vb,'N–H','hot')]
    for row,dr in strands:
        yy=row*dy*s
        labs.append(_lab(x0+0.8*s if dr==1 else x1-0.8*s,yy,vb,'N','end'))
        labs.append(_lab(x1-0.8*s if dr==1 else x0+0.8*s,yy,vb,'C','end'))
    return _panel('Beta sheet: strands side by side, C=O on one bonded to N–H on the next',vb,inner,labs,
        'Beta sheet drawn ball-and-stick, backbone only, seen from above: three straight strands lie side by side, the middle one running the opposite way (antiparallel, shown by the arrows). Dashed hydrogen bonds join each C=O on one strand to an N–H on the next strand. One bond is highlighted.',
        ATOM_LEGEND,'Antiparallel: neighbouring strands run in opposite directions, N to C (the arrows). In a parallel sheet they all run the same way. Here the bonds run across, between strands, not along them. Backbone only, seen from above.')

# ---------- tertiary: one chain folded, oily inside, water-loving outside, S–S links; enzyme-pocket inset ----------
OILY='#D9A441'; OILY_E='#8a6414'; POLAR='#2A9D8F'; POLAR_E='#145a52'; CHAIN='#3E5C76'
def _smooth(pts,closed=False):
    d=f'M{pts[0][0]:.1f},{pts[0][1]:.1f}'
    P=pts
    for i in range(len(P)-1):
        a=P[i-1] if i>0 else P[i]; b=P[i]; c=P[i+1]; e=P[i+2] if i+2<len(P) else P[i+1]
        d+=f' C{b[0]+(c[0]-a[0])/6:.1f},{b[1]+(c[1]-a[1])/6:.1f} {c[0]-(e[0]-b[0])/6:.1f},{c[1]-(e[1]-b[1])/6:.1f} {c[0]:.1f},{c[1]:.1f}'
    return d
def _water(x,y,ang,k=1.0):
    a=math.radians(ang); h=[(x+15*k*math.cos(a+s_),y+15*k*math.sin(a+s_)) for s_ in (-0.91,0.91)]
    return (''.join(f'<line x1="{x:.1f}" y1="{y:.1f}" x2="{hx:.1f}" y2="{hy:.1f}" stroke="#9a9a9a" stroke-width="{3*k:.1f}"/>' for hx,hy in h)
            +f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{8*k:.1f}" fill="{FC["O"]}" stroke="{EC["O"]}"/>'+''.join(f'<circle cx="{hx:.1f}" cy="{hy:.1f}" r="{4.6*k:.1f}" fill="{FC["H"]}" stroke="{EC["H"]}" stroke-width="1.2"/>' for hx,hy in h))
def _sc(x,y,col,ec,charge=None,r=11):
    o=f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{col}" stroke="{ec}" stroke-width="1.5"/>'
    if charge: o+=f'<path d="M{x-5:.1f},{y:.1f}h10'+(f'M{x:.1f},{y-5:.1f}v10' if charge=='+' else '')+'" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>'
    return o
def tertiary_panel():
    cx,cy=280,250; L=5; ph=math.pi/2
    r=lambda t:112+40*math.sin(L*t+ph)
    pt=lambda t,rr=None:(cx+(rr if rr is not None else r(t))*math.cos(t),cy+(rr if rr is not None else r(t))*math.sin(t))
    t0,t1=-math.pi/2+0.22,1.5*math.pi-0.30
    ts=[t0+(t1-t0)*i/220 for i in range(221)]
    chain=_smooth([pt(t) for t in ts])
    bg=f'<rect x="0" y="0" width="560" height="500" fill="#DCEAF5"/><circle cx="{cx}" cy="{cy}" r="178" fill="#F4F8FB"/>'
    o=bg
    # water molecules all round the outside
    import random; rnd=random.Random(7); W=''
    for k in range(26):
        a=2*math.pi*k/26+rnd.uniform(-.08,.08); rr=rnd.uniform(196,232)
        x,y=cx+rr*math.cos(a),cy+rr*math.sin(a)
        if 8<x<552 and 8<y<492: W+=_water(x,y,rnd.uniform(0,360))
    o+=W
    sc_in=''; sc_out=''; ss=''
    peaks=[(-ph+2*math.pi*k)/L for k in range(-2,8)]; peaks=[t+(math.pi/2)/L*0 for t in peaks]
    # peaks: L*t+ph = pi/2 + 2pi k -> t=(pi/2-ph+2pi k)/L ; troughs: 3pi/2
    pk=[(math.pi/2-ph+2*math.pi*k)/L for k in range(-3,9)]; tr=[(1.5*math.pi-ph+2*math.pi*k)/L for k in range(-3,9)]
    pk=[t for t in pk if t0+0.05<t<t1-0.05]; tr=[t for t in tr if t0+0.05<t<t1-0.05]
    charges=['+','-',None,'-','+',None]
    for i,t in enumerate(pk):
        for dt in (-0.07,0.07):
            a=pt(t+dt); b=pt(t+dt,r(t+dt)+34)
            sc_out+=f'<line x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{b[0]:.1f}" y2="{b[1]:.1f}" stroke="#7a7a7a" stroke-width="3"/>'+_sc(*b,POLAR,POLAR_E,charges[(2*i+(dt>0))%6])
    cys=[]
    for i,t in enumerate(tr):
        a=pt(t); b=(cx+(a[0]-cx)*0.42,cy+(a[1]-cy)*0.42)
        sc_in+=f'<line x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{b[0]:.1f}" y2="{b[1]:.1f}" stroke="#7a7a7a" stroke-width="3"/>'+_sc(*b,OILY,OILY_E,r=12)
    # extra oily side chains filling the core
    for a_ in (0.3,2.4,4.4):
        x,y=cx+30*math.cos(a_),cy+30*math.sin(a_); sc_in+=_sc(x,y,OILY,OILY_E,r=12)
    # disulfide bridges across two of the hairpins (between the two sides of a trough)
    SS=[]
    for t in (tr[0],tr[2]):
        p1=pt(t-0.20);p2=pt(t+0.20); m=((p1[0]+p2[0])/2,(p1[1]+p2[1])/2)
        s1=(p1[0]+(m[0]-p1[0])*0.55,p1[1]+(m[1]-p1[1])*0.55); s2=(p2[0]+(m[0]-p2[0])*0.55,p2[1]+(m[1]-p2[1])*0.55)
        ss+=(f'<line x1="{p1[0]:.1f}" y1="{p1[1]:.1f}" x2="{s1[0]:.1f}" y2="{s1[1]:.1f}" stroke="#7a7a7a" stroke-width="3"/><line x1="{p2[0]:.1f}" y1="{p2[1]:.1f}" x2="{s2[0]:.1f}" y2="{s2[1]:.1f}" stroke="#7a7a7a" stroke-width="3"/>'
             f'<line x1="{s1[0]:.1f}" y1="{s1[1]:.1f}" x2="{s2[0]:.1f}" y2="{s2[1]:.1f}" stroke="{EC["S"]}" stroke-width="5"/>'
             +''.join(f'<circle cx="{q[0]:.1f}" cy="{q[1]:.1f}" r="9" fill="{FC["S"]}" stroke="{EC["S"]}" stroke-width="1.5"/>' for q in (s1,s2)))
        u=(m[0]-cx,m[1]-cy); ul=math.hypot(*u); SS.append((m[0]+u[0]/ul*30,m[1]+u[1]/ul*30))
    o+=sc_in+sc_out+f'<path d="{chain}" fill="none" stroke="{CHAIN}" stroke-width="11" stroke-linecap="round" stroke-linejoin="round"/>'+ss
    vb=(0,0,560,500); n0=pt(t0); c1=pt(t1)
    labs=[_lab(cx,cy,vb,'oily core','dk'),_lab(70,30,vb,'water','wt'),_lab(490,470,vb,'water','wt'),
          _lab(*SS[0],vb,'S–S','ss'),_lab(*SS[1],vb,'S–S','ss'),
          _lab(n0[0]-22,n0[1]-4,vb,'N','end'),_lab(c1[0]-22,c1[1]+4,vb,'C','end')]
    leg=(_dot_(OILY,OILY_E,'oily (hydrophobic) side chain, inside')+_dot_(POLAR,POLAR_E,'water-loving (polar or charged) side chain, outside')
         +_dot_(FC['S'],EC['S'],'sulfur: S–S cross-link between two cysteines')+_dot_(FC['O'],EC['O'],'water (H₂O) all around'))
    return _panel('Tertiary: one chain folds into its final shape',vb,o,labs,
        'Cartoon of one protein chain, drawn as a thick blue line, folded into a compact rounded shape surrounded by water molecules. Amber oily side chains point inward and pack together in the core, away from the water. Teal water-loving side chains, some charged plus or minus, point outward into the water. Two yellow sulfur pairs mark S–S cross-links between cysteines that hold two loops together.',
        leg,'Cartoon, not to scale: the blue line is the chain, each ball a side chain. Water pushes the oily ones together in the middle; the charged and polar ones stay out in the water.')
def pocket_panel():
    E='M20,250 C10,170 40,80 120,70 L150,70 C150,70 152,128 200,128 C248,128 250,70 250,70 L300,70 C380,80 410,170 400,250 Z'
    fit='M156,74 L244,74 C244,74 242,124 200,124 C158,124 156,74 156,74 Z'
    o=(f'<rect x="0" y="0" width="420" height="270" fill="#F4F8FB"/><path d="{E}" fill="#3E5C76" fill-opacity=".22" stroke="#3E5C76" stroke-width="3"/>'
       f'<path d="{fit}" transform="translate(0,-4)" fill="#A86B53" stroke="#5e3527" stroke-width="2"/>'
       '<path d="M178,30 l14,14 l28,-30" fill="none" stroke="#2E7D32" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/>'
       '<path d="M330,10 L370,40 L330,58 Z" fill="#7A8256" stroke="#3f4428" stroke-width="2"/>'
       '<path d="M372,8 l26,26 M398,8 l-26,26" stroke="#C62828" stroke-width="5" stroke-linecap="round"/>')
    vb=(0,0,420,270)
    labs=[_lab(210,200,vb,'enzyme','dk'),_lab(200,150,vb,'pocket','dk'),_lab(14,34,vb,'right shape:<br>fits','hot l'),_lab(412,92,vb,'wrong shape:<br>doesn’t fit','bad r')]
    return _panel('Shape decides the job: an enzyme’s pocket',vb,o,labs,
        'Cartoon of an enzyme as a large blue shape with a rounded pocket in its top edge. A brown molecule shaped exactly like the pocket sits in it, marked with a green tick. A green triangular molecule beside it does not match the pocket and is marked with a red cross.',
        '','Only the molecule that matches the pocket’s shape fits and gets worked on. If the chain unfolds, the pocket is lost.',maxw=460)

# ---------- quaternary: hemoglobin (2 alpha + 2 beta, each with a heme, Fe and O2) and collagen's triple helix ----------
FE='#E06633'; FE_E='#7a2a0a'; HEME='#8E3B46'
def _blob(cx,cy,rx,ry,seed,col):
    rnd=__import__('random').Random(seed); pts=[]
    for k in range(18):
        a=2*math.pi*k/18; w=1+rnd.uniform(-.09,.09)
        pts.append((cx+rx*w*math.cos(a),cy+ry*w*math.sin(a)))
    pts=pts+pts[:3]; d=_smooth(pts)
    rows=[-.5,-.17,.17,.5]; pts=[]
    for k,yy in enumerate(rows):
        xs_=(-.62,.62) if k%2==0 else (.62,-.62)
        pts+=[(cx+rx*xs_[0],cy+ry*yy),(cx+rx*xs_[1],cy+ry*yy)]
    sq=_smooth(pts)
    return f'<path d="{d}" fill="{col}" stroke="#2B2B2B" stroke-opacity=".45" stroke-width="2"/><path d="{sq}" fill="none" stroke="#fff" stroke-opacity=".28" stroke-width="9" stroke-linecap="round" stroke-linejoin="round"/>'
def _heme(x,y,s=1.0):
    h=26*s
    o=f'<circle cx="{x}" cy="{y}" r="{h+10*s:.1f}" fill="#fff" fill-opacity=".92"/>'
    o+=f'<rect x="{x-h:.1f}" y="{y-h:.1f}" width="{2*h:.1f}" height="{2*h:.1f}" rx="{10*s:.1f}" fill="none" stroke="{HEME}" stroke-width="{7*s:.1f}"/>'
    for dx,dy in ((-1,-1),(1,-1),(1,1),(-1,1)):
        nx,ny=x+dx*h*.5,y+dy*h*.5; o+=f'<line x1="{x}" y1="{y}" x2="{nx:.1f}" y2="{ny:.1f}" stroke="#7a7a7a" stroke-width="{2.4*s:.1f}"/><circle cx="{nx:.1f}" cy="{ny:.1f}" r="{5*s:.1f}" fill="{FC["N"]}" stroke="{EC["N"]}"/>'
    o+=f'<line x1="{x}" y1="{y}" x2="{x+14*s:.1f}" y2="{y-30*s:.1f}" stroke="#7a7a7a" stroke-width="{3*s:.1f}"/><line x1="{x+14*s:.1f}" y1="{y-30*s:.1f}" x2="{x+32*s:.1f}" y2="{y-42*s:.1f}" stroke="#7a7a7a" stroke-width="{3*s:.1f}"/>'
    o+=''.join(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="{8*s:.1f}" fill="{FC["O"]}" stroke="{EC["O"]}" stroke-width="1.2"/>' for px,py in ((x+14*s,y-30*s),(x+32*s,y-42*s)))
    o+=f'<circle cx="{x}" cy="{y}" r="{9*s:.1f}" fill="{FE}" stroke="{FE_E}" stroke-width="1.5"/>'
    return o
HB_COL={'α1':'#3E5C76','α2':'#86A9C7','β1':'#7A8256','β2':'#BDB07A'}
def hemoglobin_panel():
    C=[('α1',150,128,1),('β1',370,128,2),('β2',150,320,3),('α2',370,320,4)]
    o='<rect x="0" y="0" width="520" height="450" fill="#F4F8FB"/>'
    o+=''.join(_blob(x,y,118,92,sd,HB_COL[n]) for n,x,y,sd in C)
    H=[(x+(-30 if x<260 else 30),y+(-6 if y<230 else 10)) for n,x,y,sd in C]
    o+=''.join(_heme(hx,hy) for hx,hy in H)
    vb=(0,0,520,450); hx,hy=H[0]
    labs=[_lab(x+(-58 if x<260 else 58),y+(-76 if y<230 else 76),vb,f'{n[0]} chain','chn') for n,x,y,sd in C]
    labs+=[_lab(hx,hy+52,vb,'heme (see close-up)','hm'),_lab(hx-50,hy,vb,'Fe','fe'),_lab(hx+52,hy-48,vb,'O₂','ox')]
    leg=(_dot_(HB_COL['α1'],'#2B2B2B','α chain')+_dot_(HB_COL['α2'],'#2B2B2B','α chain')+_dot_(HB_COL['β1'],'#2B2B2B','β chain')+_dot_(HB_COL['β2'],'#2B2B2B','β chain')
         +f'<span><b class="hmk"></b>heme ring</span>'+_dot_(FE,FE_E,'iron (Fe)')+_dot_(FC['O'],EC['O'],'oxygen (O₂)')+_dot_(FC['N'],EC['N'],'nitrogen'))
    return _panel('Hemoglobin: four chains, each with a heme',vb,o,labs,
        'Cartoon of hemoglobin: four folded chains packed together in a square, two alpha chains in blues and two beta chains in olive and sand. Each chain holds one heme, a flat square ring held by four nitrogens around an orange iron atom; a red two-atom oxygen molecule is bound to each iron.',
        leg,'Cartoon, not to scale. Each heme’s iron holds one O₂, so one hemoglobin carries four. The close-up below shows one heme atom by atom.',maxw=560)
def collagen_panel():
    W,Hh=420,150; cy=75; A=36; cols=['#3E5C76','#A86B53','#7A8256']; segs=[]; beads=[]
    N=240; per=170.0
    for s_ in range(3):
        ph=2*math.pi*s_/3; prev=None
        for i in range(N+1):
            x=20+(W-40)*i/N; th=2*math.pi*x/per+ph; y=cy+A*math.sin(th); z=math.cos(th)
            if prev: segs.append(((z+prev[2])/2,f'<line x1="{prev[0]:.1f}" y1="{prev[1]:.1f}" x2="{x:.1f}" y2="{y:.1f}" stroke="{cols[s_]}" stroke-width="18" stroke-linecap="round"/>'))
            prev=(x,y,z)
        for j in range(32):
            x=28+j*11.6+s_*3.9; th=2*math.pi*x/per+ph; y=cy+A*math.sin(th); z=math.cos(th)
            g=(j%3==0); segs.append((z+0.001,f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{5.6 if g else 2.6}" fill="{"#fff" if g else "#fff"}" fill-opacity="{1 if g else .45}" stroke="{"#2B2B2B" if g else "none"}" stroke-width="1.3"/>'))
    segs.sort(key=lambda t:t[0])
    o='<rect x="0" y="0" width="420" height="150" fill="#F4F8FB"/>'+''.join(t[1] for t in segs)
    vb=(0,0,W,Hh)
    labs=[]
    leg=''.join(_dot_(c,'#2B2B2B',f'chain {k}') for k,c in enumerate(cols,1))+'<span><i style="background:#fff;border-color:#2B2B2B"></i>glycine</span>'
    return _panel('Collagen: three chains wound into a rope',vb,o,labs,
        'Cartoon of collagen: three chains, in blue, terracotta and olive, twist around each other into a rope-like triple helix. White dots along each chain mark glycine, every third amino acid.',
        leg,'<b>A triple helix.</b> The white dots mark glycine: <b>every third amino acid is glycine</b>, the smallest one, the only one small enough to fit in the middle of the tight rope.',maxw=560)

# tap / Enter on any close-up panel opens it large in a dialog (scrolls sideways on a narrow phone); tap or Escape closes
SS_LBX_=('<dialog class="lbx lbs" aria-label="Diagram, enlarged"><button type="button" class="lbx-x" aria-label="Close">×</button><div class="lbx-b"></div></dialog>'
 '<script>(()=>{const d=document.querySelector("dialog.lbs");if(!d)return;const open=p=>{const c=p.cloneNode(true);c.removeAttribute("role");c.removeAttribute("tabindex");c.querySelector(".zi")?.remove();'
 'd.querySelector(".lbx-b").replaceChildren(c);d.showModal();d.scrollLeft=0;};'
 'document.addEventListener("click",e=>{const p=e.target.closest(".ssp");if(p&&!p.closest("dialog"))open(p);});'
 'document.addEventListener("keydown",e=>{const p=e.target.closest&&e.target.closest(".ssp");if(p&&!p.closest("dialog")&&(e.key==="Enter"||e.key===" ")){e.preventDefault();open(p);}});'
 'd.addEventListener("click",()=>d.close());})();</script>')

# page-only CSS (kept out of curr.css so no other page changes)
SS_CSS="""<style>/* Protein Figure 5 close-ups (secondary, tertiary, quaternary): white drawing panels like the molecule panels, labels are page HTML over the drawing */
.ssg{display:flex;flex-wrap:wrap;gap:12px;align-items:flex-start;margin:10px 0 4px}.ssg>.ssp{flex:1 1 320px;margin:0}
.ssp{position:relative;background:#fff;color:#2B2B2B;border:1px solid var(--line);border-radius:6px;padding:10px 12px 8px;margin:10px auto 4px;cursor:zoom-in;width:100%;box-sizing:border-box}
.ssp:focus-visible{outline:2px solid var(--acc);outline-offset:2px}
.ssh{font-family:var(--serif);font-weight:600;font-size:1.05rem;margin:0 26px 6px 0;color:#2B2B2B;line-height:1.3}
.ssa{position:relative}.ssa svg.sgd{display:block;width:100%;height:auto;max-height:none;min-width:0}
.ssl{position:absolute;transform:translate(-50%,-50%);font-size:.88rem;line-height:1.15;font-weight:600;color:#2B2B2B;background:#ffffffd9;padding:1px 5px;border-radius:3px;white-space:nowrap;pointer-events:none}
.ssl.l{transform:translate(0,-50%)}.ssl.r{transform:translate(-100%,-50%)}
.ssl.hot{color:#B23A0C}.ssl.bad{color:#B71C1C}.ssl.end{background:none;color:#3E5C76}.ssl.wt{background:none;color:#1F4E79;font-style:italic}
.ssl.ss{background:#FFF6C2;border:1px solid #b9a600;padding:0 4px}.ssl.fe{color:#8a2f0c}.ssl.ox{color:#B71C1C}.ssl.hm{color:#6e2632}.ssl.chn{background:#ffffffe6}
.sslg{display:flex;flex-wrap:wrap;gap:4px 14px;font-size:.88rem;color:#2B2B2B;margin:6px 0 0}.sslg span{display:inline-flex;align-items:center;gap:5px}
.sslg i{display:inline-block;width:12px;height:12px;border-radius:50%;border:1px solid}
.sslg b.hbk{display:inline-block;width:22px;border-top:2.5px dashed #1F4E79}.sslg b.hmk{display:inline-block;width:12px;height:12px;border:3px solid #8E3B46;border-radius:3px;box-sizing:border-box}
.ssc{margin:6px 0 0;font-size:.88rem;line-height:1.45;color:#55534E}
.ssp .zi{position:absolute;right:8px;top:8px;width:20px;height:20px;padding:3px;border-radius:50%;background:var(--acc);fill:none;stroke:#fff;stroke-width:1.6;stroke-linecap:round;opacity:.85}
[data-theme=dark] .ssp .zi{stroke:#1F1F1E}
dialog.lbs{overflow:auto;background:#fff;padding:14px}dialog.lbs .ssp{width:min(1240px,max(880px,92vw));max-width:none!important;cursor:zoom-out;border:0;margin:0}
dialog.lbs .ssl{font-size:1rem}
.ssl.two{text-align:center}.ssl small{display:block;font-size:.8em;font-weight:500}
@media(max-width:600px){.ssl{font-size:.76rem;padding:0 3px}.ssp{padding:8px 8px 6px}.ssh{font-size:.98rem}.sslg,.ssc{font-size:.84rem}dialog.lbs .ssl{font-size:.95rem}}
.art .ssp svg.zi,dialog .ssp svg.zi{width:20px;height:20px;min-width:0;max-height:none;display:block}</style>"""
SS_LBX=SS_CSS+SS_LBX_
