/* 2D zoom for molecule drawings, the same controls as the 3D viewer: pinch zooms (trackpad pinch = ctrl+wheel, or two
   fingers); a plain mouse wheel scrolls the page and never zooms. Drag pans while zoomed, double-click / double-tap resets,
   + / - / 0 when the drawing has focus. Nothing on the page changes until the first zoom, and zooming back to 1x removes
   every inline style, so the default view is the drawing as built. The image is scaled in place (clipped to its own box);
   the numbered markers move with it and keep their size.
   Containers: .lm (image box .mz, markers .mk); .z2c (its img, markers .cn/.cw/.cend); .z2i (a lone img). */
(()=>{const S=new WeakMap(),MAX=6,SEL=".lm,.z2c,.z2i",MK=":scope>.mk,:scope>.cn,:scope>.cw,:scope>.cend";
const st=c=>{let s=S.get(c);if(!s){s={z:1,x:0,y:0,p:new Map(),mv:0,t:0};S.set(c,s)}return s};
const tg=c=>c.classList.contains("lm")?c.querySelector(":scope>.mz"):c.classList.contains("z2i")?c:c.querySelector("img");
const dims=c=>{const t=tg(c);return[c.classList.contains("lm")?c.clientWidth:t.offsetWidth,t.offsetHeight]};
function apply(c,s){const t=tg(c),[W,H]=dims(c);
 if(s.z<=1.001){s.z=1;s.x=s.y=0;c.classList.remove("z2");t.style.transform=t.style.clipPath=t.style.transformOrigin="";
  c.querySelectorAll(MK).forEach(m=>{if(m.dataset.zl!=null){m.style.left=m.dataset.zl;m.style.top=m.dataset.zt;m.style.visibility=""}});return}
 s.x=Math.min(0,Math.max(W*(1-s.z),s.x));s.y=Math.min(0,Math.max(H*(1-s.z),s.y));c.classList.add("z2");
 t.style.transformOrigin="0 0";t.style.transform=`translate(${s.x}px,${s.y}px) scale(${s.z})`;
 const L=-s.x/s.z,T=-s.y/s.z;t.style.clipPath=`inset(${T}px ${W-L-W/s.z}px ${H-T-H/s.z}px ${L}px)`;
 c.querySelectorAll(MK).forEach(m=>{if(m.dataset.zl==null){m.dataset.zl=m.style.left;m.dataset.zt=m.style.top}
  const px=s.x+s.z*parseFloat(m.dataset.zl)/100*W,py=s.y+s.z*parseFloat(m.dataset.zt)/100*H;
  m.style.left=px+"px";m.style.top=py+"px";m.style.visibility=(px<0||py<0||px>W||py>H)?"hidden":""})}
function zoom(c,f,cx,cy){const s=st(c),z=Math.min(MAX,Math.max(1,s.z*f));s.x=cx-(cx-s.x)*z/s.z;s.y=cy-(cy-s.y)*z/s.z;s.z=z;apply(c,s)}
const reset=c=>{const s=st(c);s.z=1;apply(c,s)};
const cOf=e=>{const c=e.target.closest&&e.target.closest(SEL);if(!c||c.closest("dialog")||c.classList.contains("m3on"))return null;
 const t=tg(c);return t&&(t===e.target||t.contains(e.target)||!c.classList.contains("lm")&&e.type==="keydown")?c:null};
const cK=e=>{const c=e.target.closest&&(e.target.closest(SEL)||e.target.querySelector(":scope>.z2c"));return c&&!c.closest("dialog")&&!c.classList.contains("m3on")&&tg(c)?c:null};
/* untransformed top-left of the image: its drawn box minus the current pan */
const org=c=>{const r=tg(c).getBoundingClientRect(),s=st(c);return[r.left-s.x,r.top-s.y]};
const rel=(c,x,y)=>{const o=org(c);return[x-o[0],y-o[1]]};
document.addEventListener("wheel",e=>{if(!e.ctrlKey)return;const c=cOf(e);if(!c)return;const s=st(c);
 if(e.deltaY>0&&s.z<=1)return;e.preventDefault();zoom(c,Math.exp(-e.deltaY*0.01),...rel(c,e.clientX,e.clientY))},{passive:false});
document.addEventListener("pointerdown",e=>{const c=cOf(e);if(!c)return;const s=st(c);
 s.p.set(e.pointerId,[e.clientX,e.clientY]);if(s.p.size===1){s.mv=0;s.d0=[e.clientX,e.clientY]}
 if(s.p.size===2){const[a,b]=[...s.p.values()];s.pd=Math.hypot(a[0]-b[0],a[1]-b[1]);s.mv=1}
 if(s.z>1||s.p.size===2)try{e.target.setPointerCapture(e.pointerId)}catch(_){}});
document.addEventListener("pointermove",e=>{const c=[...document.querySelectorAll(".z2,"+SEL)].find(l=>{const s=S.get(l);return s&&s.p.has(e.pointerId)});if(!c)return;const s=S.get(c);
 const o=s.p.get(e.pointerId);s.p.set(e.pointerId,[e.clientX,e.clientY]);
 if(s.p.size===2){const[a,b]=[...s.p.values()],d=Math.hypot(a[0]-b[0],a[1]-b[1]);
  if(s.pd)zoom(c,d/s.pd,...rel(c,(a[0]+b[0])/2,(a[1]+b[1])/2));s.pd=d;return}
 if(s.z>1){if(Math.hypot(e.clientX-s.d0[0],e.clientY-s.d0[1])>4)s.mv=1;s.x+=e.clientX-o[0];s.y+=e.clientY-o[1];apply(c,s)}});
const up=e=>{document.querySelectorAll(SEL).forEach(c=>{const s=S.get(c);if(s&&s.p.delete(e.pointerId)&&s.p.size<2)s.pd=0})};
document.addEventListener("pointerup",up);document.addEventListener("pointercancel",up);
/* a click that ended a drag/pinch does not enlarge; while zoomed a single click still enlarges (after the double-click window) */
document.addEventListener("click",e=>{if(e.m2z)return;const c=cOf(e);if(!c)return;const s=st(c);
 if(s.mv){s.mv=0;e.preventDefault();e.stopImmediatePropagation();return}
 if(s.z<=1)return;e.preventDefault();e.stopImmediatePropagation();
 if(s.t){clearTimeout(s.t);s.t=0;reset(c);return}
 const b=e.target.closest(".lmz,button,a")||e.target;s.t=setTimeout(()=>{s.t=0;const k=new MouseEvent("click",{bubbles:true,cancelable:true});k.m2z=1;b.dispatchEvent(k)},300)},true);
document.addEventListener("dblclick",e=>{const c=cOf(e);if(c&&st(c).z>1){e.preventDefault();reset(c)}});
document.addEventListener("keydown",e=>{const c=cK(e);if(!c||e.ctrlKey||e.metaKey||e.altKey)return;const k=e.key,[W,H]=dims(c);
 if(k==="+"||k==="=")zoom(c,1.25,W/2,H/2);else if(k==="-"||k==="_")zoom(c,0.8,W/2,H/2);else if(k==="0")reset(c);else return;e.preventDefault();e.stopPropagation()},true);
/* the enlarge dialogs copy the drawing: show the copy unzoomed */
const clean=()=>document.querySelectorAll("dialog .lm,dialog .z2c,dialog .z2i,dialog img").forEach(c=>{c.classList.remove("z2");
 [c,...c.querySelectorAll("[style]")].forEach(x=>{if(x.dataset&&x.dataset.zl!=null){x.style.left=x.dataset.zl;x.style.top=x.dataset.zt;x.style.visibility=""}else if(x.style&&x.style.transform&&x.style.transform.includes("scale(")){x.style.transform=x.style.clipPath=x.style.transformOrigin=""}})});
document.addEventListener("click",()=>{clean();setTimeout(clean,0)});
document.addEventListener("dragstart",e=>{const c=e.target.closest&&e.target.closest(SEL);if(c&&!c.closest("dialog"))e.preventDefault()});
document.addEventListener("click",e=>{const b=e.target.closest&&e.target.closest(".m3b");const h=b&&b.closest(".lm,.m3c");if(h)[h,...h.querySelectorAll(SEL)].forEach(c=>{if(S.has(c))reset(c)})},true);
addEventListener("resize",()=>document.querySelectorAll(".z2").forEach(c=>{if(c.matches(SEL))reset(c)}));})();
