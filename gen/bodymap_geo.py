# Geometry helpers for the Module 6 statue (original SVG; front-facing figure in a 400 x 800 box, centre line x=200).
import math
def F(v): return f'{v:.1f}'.rstrip('0').rstrip('.')
def cr(pts,closed=True,t=1.0):
    """Catmull-Rom spline through pts -> cubic Bezier path data."""
    n=len(pts)
    if n<2: return ''
    P=pts+[pts[0],pts[1]] if closed else [pts[0]]+pts+[pts[-1]]
    o=[f'M{F(pts[0][0])},{F(pts[0][1])}']
    rng=range(n) if closed else range(n-1)
    for i in rng:
        if closed: p0,p1,p2,p3=P[i-1] if i>0 else pts[-1],P[i],P[i+1],P[i+2]
        else: p0,p1,p2,p3=P[i],P[i+1],P[i+2],P[i+3]
        c1=(p1[0]+(p2[0]-p0[0])/6*t,p1[1]+(p2[1]-p0[1])/6*t);c2=(p2[0]-(p3[0]-p1[0])/6*t,p2[1]-(p3[1]-p1[1])/6*t)
        o.append(f'C{F(c1[0])},{F(c1[1])} {F(c2[0])},{F(c2[1])} {F(p2[0])},{F(p2[1])}')
    return ''.join(o)+('Z' if closed else '')
def mx(pts): return [(400-x,y) for x,y in pts]
def sym(right):
    """right half from top centre to bottom centre (x>=200) -> closed symmetric outline points"""
    left=[(400-x,y) for x,y in reversed(right)]
    if right[0][0]==200: left=left[:-1]
    if right[-1][0]==200: left=left[1:]
    return right+left
def _arcflag(C,A,B,P):
    a=math.atan2(A[1]-C[1],A[0]-C[0]);b=math.atan2(B[1]-C[1],B[0]-C[0]);p=math.atan2(P[1]-C[1],P[0]-C[0])
    norm=lambda x:x%(2*math.pi)
    db=norm(b-a);dp=norm(p-a)
    if dp<db: return (1 if db>math.pi else 0),1   # going +angle (clockwise on screen) reaches P first
    return (1 if 2*math.pi-db>math.pi else 0),0
def capsule(x1,y1,r1,x2,y2,r2):
    """tapered capsule (two circles + outer tangents)"""
    dx,dy=x2-x1,y2-y1;d=math.hypot(dx,dy);ux,uy=dx/d,dy/d;nx,ny=-uy,ux;k=max(-.95,min(.95,(r1-r2)/d));s=math.sqrt(1-k*k)
    m1=(k*ux+s*nx,k*uy+s*ny);m2=(k*ux-s*nx,k*uy-s*ny)
    A1=(x1+r1*m1[0],y1+r1*m1[1]);B1=(x2+r2*m1[0],y2+r2*m1[1]);B2=(x2+r2*m2[0],y2+r2*m2[1]);A2=(x1+r1*m2[0],y1+r1*m2[1])
    la2,sw2=_arcflag((x2,y2),B1,B2,(x2+r2*ux,y2+r2*uy));la1,sw1=_arcflag((x1,y1),A2,A1,(x1-r1*ux,y1-r1*uy))
    return (f'M{F(A1[0])},{F(A1[1])}L{F(B1[0])},{F(B1[1])}A{F(r2)},{F(r2)} 0 {la2} {sw2} {F(B2[0])},{F(B2[1])}'
            f'L{F(A2[0])},{F(A2[1])}A{F(r1)},{F(r1)} 0 {la1} {sw1} {F(A1[0])},{F(A1[1])}Z')
def frame(o,u_end,pts):
    """local (u along the limb, v across; v>0 = outward for a right-side limb heading down-right) -> world"""
    dx,dy=u_end[0]-o[0],u_end[1]-o[1];d=math.hypot(dx,dy);ux,uy=dx/d,dy/d;vx,vy=uy,-ux
    return [(o[0]+u*ux+v*vx,o[1]+u*uy+v*vy) for u,v in pts]
def ell(cx,cy,rx,ry,rot=0):
    return f'M{F(cx-rx)},{F(cy)}a{F(rx)},{F(ry)} 0 1 0 {F(2*rx)},0a{F(rx)},{F(ry)} 0 1 0 {F(-2*rx)},0Z' if not rot else None
def line(pts): return 'M'+'L'.join(f'{F(x)},{F(y)}' for x,y in pts)
def sp(pts): return cr(pts,closed=False)
