function fixN(g){g.computeVertexNormals();const n=g.attributes.normal.array;for(let i=0;i<n.length;i+=3){const l=n[i]*n[i]+n[i+1]*n[i+1]+n[i+2]*n[i+2];if(!(l>1e-8)){n[i]=0;n[i+1]=1;n[i+2]=0}}g.attributes.normal.needsUpdate=true}
// Shared 3D anatomy viewer (LeClaire Institute). three.js r160. Meshes: BodyParts3D (CC BY-SA 2.1 JP), modified.
import * as THREE from 'three';
import {OrbitControls} from 'three/addons/controls/OrbitControls.js';
import {RoomEnvironment} from 'three/addons/environments/RoomEnvironment.js';
import {EffectComposer} from 'three/addons/postprocessing/EffectComposer.js';
import {RenderPass} from 'three/addons/postprocessing/RenderPass.js';
import {SSAOPass} from 'three/addons/postprocessing/SSAOPass.js';
import {UnrealBloomPass} from 'three/addons/postprocessing/UnrealBloomPass.js';
import {BokehPass} from 'three/addons/postprocessing/BokehPass.js';
import {ShaderPass} from 'three/addons/postprocessing/ShaderPass.js';
import {OutputPass} from 'three/addons/postprocessing/OutputPass.js';
const V=(x,y,z)=>new THREE.Vector3(x,y,z);
export async function start(CFG){
const Q=new URLSearchParams(location.search);
const scene=new THREE.Scene();window.__scene=scene;
const renderer=new THREE.WebGLRenderer({antialias:true});renderer.setSize(innerWidth,innerHeight);renderer.setPixelRatio(Math.min(devicePixelRatio,2));
renderer.shadowMap.enabled=true;renderer.shadowMap.type=THREE.PCFSoftShadowMap;renderer.toneMapping=THREE.ACESFilmicToneMapping;renderer.toneMappingExposure=.8;
document.body.appendChild(renderer.domElement);
{const c=document.createElement('canvas');c.width=2;c.height=256;const g=c.getContext('2d');const gr=g.createLinearGradient(0,0,0,256);gr.addColorStop(0,'#262b31');gr.addColorStop(.6,'#121519');gr.addColorStop(1,'#060708');g.fillStyle=gr;g.fillRect(0,0,2,256);
const t=new THREE.CanvasTexture(c);t.colorSpace=THREE.SRGBColorSpace;scene.background=t}
const pmrem=new THREE.PMREMGenerator(renderer);scene.environment=pmrem.fromScene(new RoomEnvironment(),.04).texture;scene.environmentIntensity=.6;
const S=CFG.size||6;
const camera=new THREE.PerspectiveCamera(35,innerWidth/innerHeight,S*.01,S*40);camera.position.set(...(CFG.cam||[S*.4,S*.15,S*1.5]));
const controls=new OrbitControls(camera,renderer.domElement);controls.target.set(...(CFG.target||[0,0,0]));controls.enableDamping=true;controls.minDistance=S*.3;controls.maxDistance=S*3.5;
renderer.domElement.addEventListener('webglcontextlost',e=>{e.preventDefault();document.body.insertAdjacentHTML('beforeend','<div style="position:absolute;top:45%;left:50%;color:#ccc">Reloading graphics…</div>')});
renderer.domElement.addEventListener('webglcontextrestored',()=>location.reload());
scene.add(new THREE.HemisphereLight(0xfff1e0,0x2a2e35,.7));
const key=new THREE.DirectionalLight(0xfff6ec,2.6);key.position.set(S*.8,S*1.3,S*1.3);key.castShadow=true;key.shadow.mapSize.set(2048,2048);key.shadow.radius=6;key.shadow.bias=-.0005;
Object.assign(key.shadow.camera,{left:-S,right:S,top:S,bottom:-S,near:S*.1,far:S*6});key.target.position.set(...(CFG.target||[0,0,0]));scene.add(key,key.target);
const rim=new THREE.DirectionalLight(0xcfe2ff,3.2);rim.position.set(-7,4,-8);scene.add(rim);const rim2=new THREE.DirectionalLight(0xfff0e8,2.2);rim2.position.set(8,2,-6);scene.add(rim2);
const fill=new THREE.DirectionalLight(0xffe0d0,.5);fill.position.set(-5,-2,6);scene.add(fill);
import('three/addons/lights/RectAreaLightUniformsLib.js').then(m=>{m.RectAreaLightUniformsLib.init();const sb=new THREE.RectAreaLight(0xffffff,3,6,6);sb.position.set(3,5,9);sb.lookAt(0,0,0);scene.add(sb)});
// ---------- procedural textures ----------
function canvasTex(w,h,draw){const c=document.createElement('canvas');c.width=w;c.height=h;draw(c.getContext('2d'),w,h);return c}
function heightToNormal(src,strength){const w=src.width,h=src.height,s=src.getContext('2d').getImageData(0,0,w,h).data;
 const c=document.createElement('canvas');c.width=w;c.height=h;const g=c.getContext('2d');const o=g.createImageData(w,h);const H=(x,y)=>s[(((y+h)%h)*w+((x+w)%w))*4]/255;
 for(let y=0;y<h;y++)for(let x=0;x<w;x++){const dx=(H(x-1,y)-H(x+1,y))*strength,dy=(H(x,y-1)-H(x,y+1))*strength;const l=Math.hypot(dx,dy,1);const i=(y*w+x)*4;
 o.data[i]=(dx/l*.5+.5)*255;o.data[i+1]=(dy/l*.5+.5)*255;o.data[i+2]=(1/l*.5+.5)*255;o.data[i+3]=255}g.putImageData(o,0,0);return c}
function tex(c,rx,ry,srgb){const t=new THREE.CanvasTexture(c);t.wrapS=t.wrapT=THREE.RepeatWrapping;t.repeat.set(rx,ry);if(srgb)t.colorSpace=THREE.SRGBColorSpace;t.anisotropy=8;return t}
const R=Math.random;
// bone porosity: speckles + soft noise
const boneH=canvasTex(512,512,(g,w,h)=>{g.fillStyle='#888';g.fillRect(0,0,w,h);for(let i=0;i<5000;i++){const r=R()*2+.5;g.fillStyle=`rgba(0,0,0,${.25+R()*.4})`;g.beginPath();g.arc(R()*w,R()*h,r,0,7);g.fill()}
 for(let i=0;i<400;i++){g.fillStyle=`rgba(255,255,255,${R()*.08})`;g.beginPath();g.arc(R()*w,R()*h,R()*25+5,0,7);g.fill()}});
const boneC=canvasTex(512,512,(g,w,h)=>{g.fillStyle='#e6d9bb';g.fillRect(0,0,w,h);for(let i=0;i<600;i++){g.fillStyle=R()<.5?`rgba(190,165,120,${R()*.12})`:`rgba(255,250,235,${R()*.12})`;g.beginPath();g.arc(R()*w,R()*h,R()*30+4,0,7);g.fill()}});
// fibres: vertical striations
function fibres(base,lines,alpha){return canvasTex(512,512,(g,w,h)=>{g.fillStyle=base;g.fillRect(0,0,w,h);for(let i=0;i<lines;i++){const x=R()*w,lw=R()*3+.5;g.strokeStyle=R()<.5?`rgba(0,0,0,${R()*alpha})`:`rgba(255,255,255,${R()*alpha})`;g.lineWidth=lw;g.beginPath();g.moveTo(x,0);
 let xx=x;for(let y=0;y<=h;y+=16){xx+=(R()-.5)*1.5;g.lineTo(xx,y)}g.stroke()}})}
const ligH=fibres('#808080',1400,.6),ligC=fibres('#f1ddd6',700,.14),musH=fibres('#808080',700,.7),musC=fibres('#8c2c22',600,.25),tenC=fibres('#f6e8e4',900,.1);
// cartilage subtle
const cartH=canvasTex(256,256,(g,w,h)=>{g.fillStyle='#808080';g.fillRect(0,0,w,h);for(let i=0;i<300;i++){g.fillStyle=`rgba(${R()<.5?0:255},${R()<.5?0:255},${R()<.5?0:255},.05)`;g.beginPath();g.arc(R()*w,R()*h,R()*20+3,0,7);g.fill()}});
const M={
bone:new THREE.MeshPhysicalMaterial({color:0xf2e6cc,map:tex(boneC,3,6,1),normalMap:tex(heightToNormal(boneH,2.5),3,6),normalScale:new THREE.Vector2(.6,.6),roughness:.62,roughnessMap:tex(boneH,3,6),sheen:.25,sheenColor:new THREE.Color(0xfff0d8),sheenRoughness:.6}),
cart:new THREE.MeshPhysicalMaterial({color:0xd4e4f2,roughness:.08,clearcoat:1,clearcoatRoughness:.02,sheen:.8,sheenColor:new THREE.Color(0xa8ccff),normalMap:tex(heightToNormal(cartH,1),2,2),normalScale:new THREE.Vector2(.3,.3),transparent:true,opacity:.92,ior:1.4,specularIntensity:1}),
men:new THREE.MeshPhysicalMaterial({color:0xe2e8ea,roughness:.25,clearcoat:.8,clearcoatRoughness:.15,sheen:.5,sheenColor:new THREE.Color(0xd0e0ff),normalMap:tex(heightToNormal(ligH,1.5),1,4),normalScale:new THREE.Vector2(.4,.4)}),
lig:new THREE.MeshPhysicalMaterial({color:0xffffff,map:tex(ligC,1,1,1),normalMap:tex(heightToNormal(ligH,3),1,1),normalScale:new THREE.Vector2(.9,.9),roughness:.38,clearcoat:.7,clearcoatRoughness:.18,sheen:.9,sheenColor:new THREE.Color(0xffd8d0)}),
ten:new THREE.MeshPhysicalMaterial({color:0xfff4f2,map:tex(tenC,1,1,1),normalMap:tex(heightToNormal(ligH,3),1,1),normalScale:new THREE.Vector2(.7,.7),roughness:.3,clearcoat:.6,clearcoatRoughness:.2,sheen:1,sheenColor:new THREE.Color(0xdde8ff)}),
mus:new THREE.MeshPhysicalMaterial({color:0xffffff,map:tex(musC,6,3,1),normalMap:tex(heightToNormal(musH,3),6,3),normalScale:new THREE.Vector2(.8,.8),roughness:.45,clearcoat:.35,clearcoatRoughness:.35,sheen:.7,sheenColor:new THREE.Color(0xff8a7a),sheenRoughness:.5}),
cap:new THREE.MeshPhysicalMaterial({color:0xdfe6ff,transparent:true,opacity:.09,roughness:.2,clearcoat:1,side:THREE.DoubleSide,depthWrite:false}),
bur:new THREE.MeshPhysicalMaterial({color:0x9cc8f0,transparent:true,opacity:.5,roughness:.1,clearcoat:1,transmission:.3,thickness:.2}),
fat:new THREE.MeshPhysicalMaterial({color:0xf0c75a,roughness:.45,clearcoat:.5,sheen:.6,sheenColor:new THREE.Color(0xfff0a0),normalMap:tex(heightToNormal(boneH,4),2,2)}),
nerve:new THREE.MeshPhysicalMaterial({color:0xf3dc7a,roughness:.4,clearcoat:.5,sheen:.6,sheenColor:new THREE.Color(0xfff2b0)}),
artery:new THREE.MeshPhysicalMaterial({color:0xb3221c,roughness:.35,clearcoat:.7,clearcoatRoughness:.2}),
vein:new THREE.MeshPhysicalMaterial({color:0x3c4f9a,roughness:.35,clearcoat:.7,clearcoatRoughness:.2}),
organ:new THREE.MeshPhysicalMaterial({color:0xb5655a,roughness:.4,clearcoat:.8,clearcoatRoughness:.2,sheen:.6,sheenColor:new THREE.Color(0xffb0a0)}),
skin:new THREE.MeshPhysicalMaterial({color:0xe2b59a,transparent:true,opacity:.16,roughness:.45,depthWrite:false,side:THREE.DoubleSide}),
disc:new THREE.MeshPhysicalMaterial({color:0xdfe8ec,roughness:.3,clearcoat:.6,sheen:.5,sheenColor:new THREE.Color(0xd0e0ff)})};
for(const k in CFG.colors||{}){M[k]=M[CFG.colors[k][0]].clone();M[k].color=new THREE.Color(CFG.colors[k][1])}
// ---------- frames: chains of rotations driven by sliders ----------
const sl={};(CFG.sliders||[]).forEach(s=>sl[s.id]=(s.val||0)*Math.PI/180);
const FR={};(CFG.frames||[]).forEach(f=>FR[f.name]=f);
function chain(f){const out=[];while(f&&FR[f]){out.unshift(...(FR[f].rots||[]).map(r=>({...r,frame:f})));f=FR[f].parent}return out}
const q=new THREE.Quaternion(),tmp=V(),AX=V();
function rotP(p,r,w){const a=(sl[r.slider]||0)*(r.k??1)*w;if(!a)return;AX.set(...r.axis).normalize();q.setFromAxisAngle(AX,a);p.sub(tmp.set(...r.pivot)).applyQuaternion(q).add(tmp.set(...r.pivot))}
function xform(p,f){const c=chain(f);for(let i=c.length-1;i>=0;i--)rotP(p,c[i],1);return p}
const P1=V();function xformSkin(p,s,w){const cf=chain(s.from),ct=chain(s.to).slice(cf.length);P1.copy(p);for(let i=ct.length-1;i>=0;i--)rotP(P1,ct[i],1);p.lerp(P1,w);for(let i=cf.length-1;i>=0;i--)rotP(p,cf[i],1);return p}
function frameMatrix(f){const m=new THREE.Matrix4();for(const r of chain(f)){const a=(sl[r.slider]||0)*(r.k??1);const P=V(...r.pivot);
 m.multiply(new THREE.Matrix4().makeTranslation(P.x,P.y,P.z)).multiply(new THREE.Matrix4().makeRotationAxis(V(...r.axis).normalize(),a)).multiply(new THREE.Matrix4().makeTranslation(-P.x,-P.y,-P.z))}return m}
// ---------- components ----------
const comps=[],byName={},pickables=[],rigid=[],skins=[],dyns=[];
function comp(p){let c=byName[p.name];if(!c){c=byName[p.name]={name:p.name,group:p.group,desc:p.desc||'',meshes:[],scan:p.scan,mat:p.mat,sex:p.sex};comps.push(c)}return c}
function addMesh(c,geo,mat,frame){const m=new THREE.Mesh(geo,mat);m.castShadow=!mat.transparent;m.receiveShadow=true;m.userData.comp=c;scene.add(m);c.meshes.push(m);if(!mat.transparent||mat===M.bur)pickables.push(m);
 if(c.hidden)m.visible=false;return m}
function uvs(g){const pos=g.attributes.position.array;g.computeBoundingBox();const c=g.boundingBox.getCenter(V()),sz=g.boundingBox.getSize(V());
 const ax=sz.x>sz.y&&sz.x>sz.z?0:sz.z>sz.y?2:1;const a1=(ax+1)%3,a2=(ax+2)%3;const cc=[c.x,c.y,c.z];const uv=new Float32Array(pos.length/3*2);
 for(let i=0;i<pos.length/3;i++){uv[2*i]=(Math.atan2(pos[3*i+a1]-cc[a1],pos[3*i+a2]-cc[a2])/Math.PI+1)*.5;uv[2*i+1]=pos[3*i+ax]*.25*(6/S)}g.setAttribute('uv',new THREE.BufferAttribute(uv,2))}
function decode(buf,e){const q=new Uint16Array(buf,e.o,e.nv*3);const pos=new Float32Array(q.length);for(let i=0;i<q.length;i++){const k=i%3;pos[i]=e.min[k]+q[i]/65535*(e.max[k]-e.min[k])}
 const idx=e.i32?new Uint32Array(buf,e.oi,e.ni):new Uint16Array(buf,e.oi,e.ni);const g=new THREE.BufferGeometry();g.setAttribute('position',new THREE.BufferAttribute(pos,3));g.setIndex(new THREE.BufferAttribute(idx.slice(),1));fixN(g);uvs(g);if(e.ow!=null)g.userData.w=new Uint8Array(buf,e.ow,e.nv).slice();if(e.of!=null)g.userData.mf=new Uint8Array(buf,e.of,e.nv*3).slice();return g}
const smooth=(e0,e1,x)=>{const t=Math.min(1,Math.max(0,(x-e0)/(e1-e0)));return t*t*(3-2*t)};
function placeRigid(r){r.m.matrixAutoUpdate=false;r.m.matrix.copy(frameMatrix(r.frame));r.m.matrixWorldNeedsUpdate=true}
function applySkin(s){const p=s.m.geometry.attributes.position,a=p.array,o=s.orig,d=V(...s.dir);const P=V();
 if(s.multi&&s.mf){const Ms=s.multi.map(frameMatrix),A=V(),B=V(),f=s.mf;for(let i=0,j=0;i<a.length;i+=3,j+=3){A.set(o[i],o[i+1],o[i+2]);B.copy(A);A.applyMatrix4(Ms[f[j]]);B.applyMatrix4(Ms[f[j+1]]);A.lerp(B,f[j+2]/255);a[i]=A.x;a[i+1]=A.y;a[i+2]=A.z}
  p.needsUpdate=true;fixN(s.m.geometry);s.m.geometry.computeBoundingSphere();return}
 for(let i=0;i<a.length;i+=3){P.set(o[i],o[i+1],o[i+2]);const w=s.wts?s.wts[i/3]/255:smooth(s.a,s.b,P.dot(d));xformSkin(P,s,w);a[i]=P.x;a[i+1]=P.y;a[i+2]=P.z}
 p.needsUpdate=true;fixN(s.m.geometry);s.m.geometry.computeBoundingSphere()}
function rebuild(d){const P=d.pts.map(p=>xform(V(p[0],p[1],p[2]),p[3]||'F'));const cur=new THREE.CatmullRomCurve3(P,false,'centripetal');
 const SG=48,RS=20;const g=new THREE.TubeGeometry(cur,SG,1,RS,false);const pos=g.attributes.position;const fr=cur.computeFrenetFrames(SG,false);
 for(let i=0;i<=SG;i++){const t=i/SG;const pt=cur.getPointAt(t);const r=Array.isArray(d.r)?d.r[0]+(d.r[1]-d.r[0])*t:d.r;const Rr=r*(.75+.25*Math.min(1,Math.min(t,1-t)/.12));const T=cur.getTangentAt(t);
  let n=d.ref?V(...d.ref).sub(T.clone().multiplyScalar(V(...d.ref).dot(T))).normalize():fr.normals[i];if(!isFinite(n.x)||n.lengthSq()<.5)n=fr.normals[i];const b=T.clone().cross(n);
  for(let j=0;j<=RS;j++){const k=i*(RS+1)+j;const a=j/RS*Math.PI*2;const fib=1+.04*Math.sin(a*9+i*.3);
   const v=pt.clone().addScaledVector(n,Math.cos(a)*Rr*(d.flat||1)*fib).addScaledVector(b,Math.sin(a)*Rr*fib);pos.setXYZ(k,v.x,v.y,v.z)}}
 fixN(g);uvs(g);d.m.geometry.dispose();d.m.geometry=g}
function update(){rigid.forEach(placeRigid);skins.forEach(applySkin);dyns.forEach(rebuild)}
// ---------- UI ----------
const panel=document.getElementById('list');const groups={};const boxes=[];
function mkDet(label,parent,isSys){const det=document.createElement('details');det.open=!CFG.collapsed&&!isSys?true:!CFG.collapsed;if(CFG.collapsed&&isSys)det.open=false;const sum=document.createElement('summary');
 const mcb=document.createElement('input');mcb.type='checkbox';mcb.checked=true;mcb.className='master';mcb.onclick=e=>e.stopPropagation();
 sum.append(mcb,' '+label);if(isSys)sum.style.cssText='font-size:13px;color:#cde';det.append(sum);parent.append(det);const g={det,mcb,items:[],up:null};
 mcb.onchange=()=>{const v=mcb.checked;mcb.indeterminate=false;g.items.forEach(b=>{if(!b.off&&b.checked!==v){b.checked=v;b.onchange()}});syncMaster(g)};return g}
const systems={};
function groupEl(name){if(groups[name])return groups[name];const i=name.indexOf(' / ');let g;
 if(i>0){const sn=name.slice(0,i);const sy=systems[sn]||(systems[sn]=mkDet(sn,panel,true));sy.det.style.marginLeft='0';g=mkDet(name.slice(i+3),sy.det,false);g.det.style.marginLeft='12px';g.up=sy}
 else g=mkDet(name,panel,false);groups[name]=g;return g}
function syncMaster(g){if(!g)return;const it=g.items.filter(b=>!b.off);const n=it.filter(b=>b.checked).length;g.mcb.checked=n==it.length;g.mcb.indeterminate=n>0&&n<it.length;if(g.up)syncMaster(g.up)}
const QK=[];function syncQ(){QK.forEach(q=>{const bs=comps.filter(c=>q.mats.includes(c.mat)&&c.cb&&!c.cb.off).map(c=>c.cb);const n=bs.filter(b=>b.checked).length;q.cb.checked=n==bs.length&&n>0;q.cb.indeterminate=n>0&&n<bs.length})}
if(CFG.quick){const d=document.createElement('div');d.innerHTML='<div style="font-size:11px;color:#9ab;margin-top:6px">By tissue type:</div>';panel.before(d);
 CFG.quick.forEach(q=>{const l=document.createElement('label');l.style.display='inline-block';l.style.marginRight='8px';const cb=document.createElement('input');cb.type='checkbox';cb.checked=true;cb.className='master';l.append(cb,' '+q.label);d.append(l);
  const o={...q,cb};QK.push(o);cb.onchange=()=>{const v=cb.checked;cb.indeterminate=false;comps.filter(c=>q.mats.includes(c.mat)&&c.cb&&!c.cb.off).forEach(c=>{if(c.cb.checked!==v){c.cb.checked=v;c.cb.onchange()}});syncQ()}})}
const SW={bone:'#e6d9bb',cart:'#cfe2ee',men:'#e2e8ea',lig:'#efe5cf',ten:'#f8f0ee',mus:'#a8443a',cap:'#aab4ff',bur:'#9cc8f0',fat:'#f0c75a',nerve:'#f3dc7a',artery:'#b3221c',vein:'#3c4f9a',organ:'#b5655a',skin:'#e2b59a',disc:'#dfe8ec'};
function uiFor(c){const g=groupEl(c.group);const l=document.createElement('label');const cb=document.createElement('input');cb.type='checkbox';cb.checked=!c.hidden;
 cb.onchange=()=>{c.hidden=!cb.checked;c.meshes.forEach(m=>m.visible=cb.checked&&!cb.off);syncMaster(g);syncQ()};const col=CFG.colors?.[c.mat]?.[1]||SW[c.mat]||'#ccc';
 l.append(cb);l.insertAdjacentHTML('beforeend',` <span class="sw" style="background:${col}"></span>${c.name}${c.scan?'<span class="tag">◆</span>':''}`);g.det.append(l);g.items.push(cb);if(g.up)g.up.items.push(cb);boxes.push(cb);c.cb=cb;cb.lab=l;syncMaster(g)}
document.getElementById('all').onclick=()=>boxes.forEach(b=>{if(!b.off){b.checked=true;b.onchange()}});
document.getElementById('none').onclick=()=>boxes.forEach(b=>{if(!b.off){b.checked=false;b.onchange()}});
document.getElementById('abt').onclick=()=>{const a=document.getElementById('about');a.style.display=a.style.display=='block'?'none':'block'};
let SEX=null;function setSex(x){SEX=x;comps.forEach(c=>{if(!c.sex||!c.cb)return;const off=c.sex!==x;c.cb.off=off;c.cb.lab.style.display=off?'none':'';c.meshes.forEach(m=>m.visible=!off&&c.cb.checked)});
 [...Object.values(groups),...Object.values(systems)].forEach(g=>{g.det.style.display=g.items.length&&g.items.every(b=>b.off)?'none':'';syncMaster(g)});syncQ();
 document.querySelectorAll('.sexbtn').forEach(b=>b.classList.toggle('on',b.dataset.s===x))}
window.__setSex=setSex;
if(CFG.sexes){const d=document.createElement('div');d.style.cssText='margin:4px 0 6px;display:flex;gap:0;border:1px solid #456;border-radius:6px;overflow:hidden;width:max-content';
 const st=document.createElement('style');st.textContent='.sexbtn{background:#1c2733;color:#cde;border:0;padding:5px 14px;font-size:13px;cursor:pointer}.sexbtn.on{background:#3d7cc9;color:#fff;font-weight:600}';document.head.append(st);
 CFG.sexes.forEach(([k,lab])=>{const b=document.createElement('button');b.className='sexbtn';b.dataset.s=k;b.textContent=lab;b.onclick=()=>setSex(k);d.append(b)});
 (panel.previousElementSibling&&QK.length?panel.previousElementSibling:panel).before(d)}
const sd=document.getElementById('sliders');
(CFG.sliders||[]).forEach(s=>{const d=document.createElement('div');d.innerHTML=`${s.label}: <span>${s.val||0}</span>°<br><input type="range" min="${s.min}" max="${s.max}" value="${s.val||0}" style="width:100%">`;sd.append(d);
 const inp=d.querySelector('input'),sp=d.querySelector('span');inp.oninput=()=>{sp.textContent=inp.value;sl[s.id]=inp.value*Math.PI/180;update()};s.inp=inp});
window.__setSlider=(id,v)=>{const s=CFG.sliders.find(s=>s.id==id);s.inp.value=v;s.inp.oninput()};
const vb=document.getElementById('views');for(const k in CFG.views){const b=document.createElement('button');b.textContent=k;b.onclick=()=>{camera.position.set(...CFG.views[k]);controls.target.set(...(CFG.target||[0,0,0]))};vb.append(b)}
const tip=document.getElementById('tip'),info=document.getElementById('info'),lblCb=document.getElementById('lbl');
const ray=new THREE.Raycaster(),mouse=new THREE.Vector2();let hl=null;
function pick(e){mouse.set(e.clientX/innerWidth*2-1,-e.clientY/innerHeight*2+1);ray.setFromCamera(mouse,camera);const h=ray.intersectObjects(pickables.filter(m=>m.visible),false);return h.length?h[0].object.userData.comp:null}
function setHl(c){if(hl===c)return;if(hl)hl.meshes.forEach(m=>{if(m.userData.orig)m.material=m.userData.orig});hl=c;
 if(c)c.meshes.forEach(m=>{if(m.material.transparent&&m.material!==M.bur)return;m.userData.orig=m.material;const k=m.material.clone();k.emissive=new THREE.Color(0x2a4466);m.material=k})}
renderer.domElement.addEventListener('pointermove',e=>{if(!lblCb.checked){tip.style.display='none';setHl(null);return}const c=pick(e);setHl(c);
 if(c){tip.style.display='block';tip.style.left=e.clientX+14+'px';tip.style.top=e.clientY+10+'px';tip.innerHTML=`<b>${c.name}</b><br>${c.desc}`}else tip.style.display='none'});
let down=[0,0];renderer.domElement.addEventListener('pointerdown',e=>down=[e.clientX,e.clientY]);
renderer.domElement.addEventListener('pointerup',e=>{if(!lblCb.checked||Math.hypot(e.clientX-down[0],e.clientY-down[1])>4)return;const c=pick(e);if(c)info.innerHTML=`<b>${c.name}</b> <i>(${c.group})</i><br>${c.desc}`});
// ---------- post ----------
const composer=new EffectComposer(renderer);window.__composer=composer;composer.addPass(new RenderPass(scene,camera));
const gtao=new SSAOPass(scene,camera,innerWidth,innerHeight);window.__gtao=gtao;gtao.kernelRadius=.25*S/6;gtao.minDistance=.0005;gtao.maxDistance=.02;composer.addPass(gtao);
composer.addPass(new ShaderPass({uniforms:{tDiffuse:{value:null}},vertexShader:'varying vec2 vUv;void main(){vUv=uv;gl_Position=projectionMatrix*modelViewMatrix*vec4(position,1.);}',fragmentShader:'uniform sampler2D tDiffuse;varying vec2 vUv;void main(){vec4 c=texture2D(tDiffuse,vUv);bool bad=!(abs(c.r)<=1e4)||!(abs(c.g)<=1e4)||!(abs(c.b)<=1e4)||!(abs(c.a)<=1e4);gl_FragColor=bad?vec4(0.):clamp(c,0.,64.);}'}));
const bloom=new UnrealBloomPass(new THREE.Vector2(innerWidth,innerHeight),.12,.5,.92);composer.addPass(bloom);
const bokeh=new BokehPass(scene,camera,{focus:S*2,aperture:.0006*6/S,maxblur:.006});bokeh.enabled=false;composer.addPass(bokeh);composer.addPass(new OutputPass());
if(Q.has('lite')){gtao.enabled=false;document.getElementById('ao').checked=false}
document.getElementById('ao').onchange=e=>gtao.enabled=e.target.checked;document.getElementById('bl').onchange=e=>bloom.enabled=e.target.checked;document.getElementById('dof').onchange=e=>bokeh.enabled=e.target.checked;
addEventListener('resize',()=>{camera.aspect=innerWidth/innerHeight;camera.updateProjectionMatrix();renderer.setSize(innerWidth,innerHeight);composer.setSize(innerWidth,innerHeight)});
// ---------- build: procedural first, then mesh files progressively ----------
function addPart(p,geo){const c=comp(p);if(p.hidden)c.hidden=true;const mat=M[p.mat];const m=addMesh(c,geo,mat,p.frame||'F');
 if(p.skin){skins.push({m,orig:geo.attributes.position.array.slice(),dir:[0,1,0],a:0,b:1,wts:geo.userData.w,mf:geo.userData.mf,...p.skin});applySkin(skins[skins.length-1])}else{const r={m,frame:p.frame||'F'};rigid.push(r);placeRigid(r)}
 if(p.renderOrder)m.renderOrder=p.renderOrder;if(!c.cb)uiFor(c);if(c.sex&&SEX&&c.sex!==SEX)m.visible=false;return m}
// declare UI order up-front
(CFG.parts||[]).forEach(p=>{const c=comp(p);if(p.hidden)c.hidden=true});(CFG.tubes||[]).forEach(p=>comp(p));(CFG.shapes||[]).forEach(p=>comp(p));
const order=[...new Set(comps.map(c=>c.group))];order.forEach(groupEl);comps.forEach(uiFor);if(CFG.sexes)setSex(CFG.sexes[0][0]);
(CFG.tubes||[]).forEach(t=>{const c=comp(t);const m=addMesh(c,new THREE.BufferGeometry(),M[t.mat]);const d={m,...t};dyns.push(d);rebuild(d)});
(CFG.shapes||[]).forEach(s=>{const c=comp(s);let g;if(s.type=='lathe')g=new THREE.LatheGeometry(s.prof.map(p=>new THREE.Vector2(...p)),64);else g=new THREE.SphereGeometry(1,48,32);uvs(g);
 const m=new THREE.Mesh(g,M[s.mat]);m.position.set(...(s.pos||[0,0,0]));m.scale.set(...(s.scale||[1,1,1]));if(s.rot)m.rotation.set(...s.rot);
 const holder=addMesh(c,new THREE.BufferGeometry(),M[s.mat]);scene.remove(holder);c.meshes.pop();pickables.splice(pickables.indexOf(holder),1);
 const grp=new THREE.Group();grp.add(m);scene.add(grp);m.castShadow=!M[s.mat].transparent;m.receiveShadow=true;m.userData.comp=c;c.meshes.push(m);if(!M[s.mat].transparent||M[s.mat]===M.bur)pickables.push(m);if(c.hidden)m.visible=false;
 if(s.renderOrder)m.renderOrder=s.renderOrder;rigid.push({m:grp,frame:s.frame||'F'});placeRigid(rigid[rigid.length-1])});
window.__ok=false;window.__cam=camera;window.__ctl=controls;window.__render=()=>{controls.update();composer.render();return 1};
if(!Q.has('still'))(function loop(){requestAnimationFrame(loop);controls.update();if(bokeh.enabled)bokeh.uniforms.focus.value=camera.position.distanceTo(controls.target);composer.render()})();
const ld=document.getElementById('load');
for(const file of CFG.files){ld.textContent='Loading '+(file.label||'model')+'…';
 const buf=await (await fetch(file.url)).arrayBuffer();
 for(const p of CFG.parts.filter(p=>(p.file||0)===CFG.files.indexOf(file))){const e=file.meshes[p.mesh];if(!e){console.warn('missing',p.mesh);continue}addPart(p,decode(buf,e))}}
ld.remove();window.__ok=true;
}
