/* 2D zoom for molecule drawings (.lm), the same controls as the 3D viewer: wheel / trackpad pinch / two-finger pinch zooms,
   drag pans while zoomed, double-click / double-tap resets, + / - / 0 when the drawing has focus. Nothing on the page changes
   until the first zoom, and zooming back to 1x removes every inline style, so the default view is the drawing as built.
   The image is scaled in place (clipped to its own box); the numbered markers move with it and keep their size. */
(()=>{const S=new WeakMap(),MAX=6;
const st=lm=>{let s=S.get(lm);if(!s){s={z:1,x:0,y:0,p:new Map(),mv:0,t:0};S.set(lm,s)}return s};
function apply(lm,s){const mz=lm.querySelector(":scope>.mz"),W=lm.clientWidth,H=mz.offsetHeight;
 if(s.z<=1.001){s.z=1;s.x=s.y=0;lm.classList.remove("z2");mz.style.transform=mz.style.clipPath=mz.style.transformOrigin="";
  lm.querySelectorAll(":scope>.mk").forEach(m=>{if(m.dataset.zl!=null){m.style.left=m.dataset.zl;m.style.top=m.dataset.zt;m.style.visibility=""}});return}
 s.x=Math.min(0,Math.max(W*(1-s.z),s.x));s.y=Math.min(0,Math.max(H*(1-s.z),s.y));lm.classList.add("z2");
 mz.style.transformOrigin="0 0";mz.style.transform=`translate(${s.x}px,${s.y}px) scale(${s.z})`;
 const L=-s.x/s.z,T=-s.y/s.z;mz.style.clipPath=`inset(${T}px ${W-L-W/s.z}px ${H-T-H/s.z}px ${L}px)`;
 lm.querySelectorAll(":scope>.mk").forEach(m=>{if(m.dataset.zl==null){m.dataset.zl=m.style.left;m.dataset.zt=m.style.top}
  const px=s.x+s.z*parseFloat(m.dataset.zl)/100*W,py=s.y+s.z*parseFloat(m.dataset.zt)/100*H;
  m.style.left=px+"px";m.style.top=py+"px";m.style.visibility=(px<0||py<0||px>W||py>H)?"hidden":""})}
function zoom(lm,f,cx,cy){const s=st(lm),z=Math.min(MAX,Math.max(1,s.z*f));s.x=cx-(cx-s.x)*z/s.z;s.y=cy-(cy-s.y)*z/s.z;s.z=z;apply(lm,s)}
const reset=lm=>{const s=st(lm);s.z=1;apply(lm,s)};
const lmOf=e=>{const lm=e.target.closest&&e.target.closest(".lm");return lm&&!lm.closest("dialog")&&!lm.classList.contains("m3on")&&lm.querySelector(":scope>.mz")?lm:null};
const rel=(lm,e)=>{const r=lm.getBoundingClientRect();return[e.clientX-r.left,e.clientY-r.top]};
document.addEventListener("wheel",e=>{const lm=lmOf(e);if(!lm||!e.target.closest(".mz"))return;const s=st(lm);
 if(e.deltaY>0&&s.z<=1)return;e.preventDefault();zoom(lm,Math.exp(-e.deltaY*(e.ctrlKey?0.01:0.0015)),...rel(lm,e))},{passive:false});
document.addEventListener("pointerdown",e=>{const lm=lmOf(e);if(!lm||!e.target.closest(".mz"))return;const s=st(lm);
 s.p.set(e.pointerId,[e.clientX,e.clientY]);if(s.p.size===1){s.mv=0;s.d0=[e.clientX,e.clientY]}
 if(s.p.size===2){const[a,b]=[...s.p.values()];s.pd=Math.hypot(a[0]-b[0],a[1]-b[1]);s.mv=1}
 if(s.z>1||s.p.size===2)try{e.target.setPointerCapture(e.pointerId)}catch(_){}});
document.addEventListener("pointermove",e=>{const lm=lmOf(e)||[...document.querySelectorAll(".lm.z2")].find(l=>st(l).p.has(e.pointerId));if(!lm)return;const s=S.get(lm);
 if(!s||!s.p.has(e.pointerId))return;const o=s.p.get(e.pointerId);s.p.set(e.pointerId,[e.clientX,e.clientY]);
 if(s.p.size===2){const[a,b]=[...s.p.values()],d=Math.hypot(a[0]-b[0],a[1]-b[1]),r=lm.getBoundingClientRect();
  if(s.pd)zoom(lm,d/s.pd,(a[0]+b[0])/2-r.left,(a[1]+b[1])/2-r.top);s.pd=d;return}
 if(s.z>1){if(Math.hypot(e.clientX-s.d0[0],e.clientY-s.d0[1])>4)s.mv=1;s.x+=e.clientX-o[0];s.y+=e.clientY-o[1];apply(lm,s)}});
const up=e=>{document.querySelectorAll(".lm").forEach(lm=>{const s=S.get(lm);if(s&&s.p.delete(e.pointerId)&&s.p.size<2)s.pd=0})};
document.addEventListener("pointerup",up);document.addEventListener("pointercancel",up);
/* a click that ended a drag/pinch does not enlarge; while zoomed a single click still enlarges (after the double-click window) */
document.addEventListener("click",e=>{if(e.m2z)return;const lm=lmOf(e);if(!lm||!e.target.closest(".lmz"))return;const s=st(lm);
 if(s.mv){s.mv=0;e.preventDefault();e.stopImmediatePropagation();return}
 if(s.z<=1)return;e.preventDefault();e.stopImmediatePropagation();
 if(s.t){clearTimeout(s.t);s.t=0;reset(lm);return}
 const b=e.target.closest(".lmz");s.t=setTimeout(()=>{s.t=0;const c=new MouseEvent("click",{bubbles:true,cancelable:true});c.m2z=1;b.dispatchEvent(c)},300)},true);
document.addEventListener("dblclick",e=>{const lm=lmOf(e);if(lm&&e.target.closest(".mz")&&st(lm).z>1){e.preventDefault();reset(lm)}});
document.addEventListener("keydown",e=>{const lm=lmOf(e);if(!lm||e.ctrlKey||e.metaKey||e.altKey)return;const k=e.key,W=lm.clientWidth,H=lm.querySelector(":scope>.mz").offsetHeight;
 if(k==="+"||k==="=")zoom(lm,1.25,W/2,H/2);else if(k==="-"||k==="_")zoom(lm,0.8,W/2,H/2);else if(k==="0")reset(lm);else return;e.preventDefault();e.stopPropagation()},true);
/* the enlarge dialog copies the drawing: show the copy unzoomed */
document.addEventListener("click",()=>document.querySelectorAll("dialog.lbm .lm").forEach(c=>{c.classList.remove("z2");
 c.querySelectorAll("[style]").forEach(x=>{if(x.dataset.zl!=null){x.style.left=x.dataset.zl;x.style.top=x.dataset.zt;x.style.visibility=""}else if(x.style.transform){x.style.transform=x.style.clipPath=x.style.transformOrigin=""}});
 c.querySelectorAll("img").forEach(x=>{x.style.transform=x.style.clipPath=""})}));
document.addEventListener("click",e=>{const b=e.target.closest&&e.target.closest(".m3b");const lm=b&&b.closest(".lm");if(lm&&S.has(lm))reset(lm)},true);
addEventListener("resize",()=>document.querySelectorAll(".lm.z2").forEach(reset));})();
