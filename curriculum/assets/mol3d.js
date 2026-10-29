/* mol3d.js: tiny self-hosted 3D ball-and-stick viewer for the curriculum's 2D/3D molecule toggle (no dependencies).
   Loaded lazily by the page's toggle bootstrap on the first 3D click. Models: curriculum/mol3d/<slug>/<name>.json
   (built by gen/mol3d.py). Drawn on a 2D canvas in the same style as the PNGs (flat CPK discs with dark rims, grey sticks,
   painter's order back to front, slight depth fade), so 2D and 3D look like the same molecule.
   Controls: drag (mouse/finger) rotates, wheel or pinch zooms, double-click/double-tap resets; when the canvas has focus:
   arrow keys rotate, + / - zoom, 0 resets. API: Mol3D.mount(lmElement, model, labels) -> {destroy()}. */
(function () {
  'use strict';
  var cache = {};
  function load(url) {
    if (!cache[url]) cache[url] = fetch(url).then(function (r) { if (!r.ok) throw new Error('mol3d: ' + url + ' ' + r.status); return r.json(); });
    return cache[url];
  }
  function mul(a, b) { var r = new Array(9); for (var i = 0; i < 3; i++) for (var j = 0; j < 3; j++) r[i * 3 + j] = a[i * 3] * b[j] + a[i * 3 + 1] * b[3 + j] + a[i * 3 + 2] * b[6 + j]; return r; }
  function rotX(t) { var c = Math.cos(t), s = Math.sin(t); return [1, 0, 0, 0, c, -s, 0, s, c]; }
  function rotY(t) { var c = Math.cos(t), s = Math.sin(t); return [c, 0, s, 0, 1, 0, -s, 0, c]; }
  function mix(hex, t) { /* fade a colour toward white by t (0..1) */
    var h = hex.replace('#', ''); if (h.length === 3) h = h.replace(/./g, '$&$&');
    var n = parseInt(h, 16), r = n >> 16 & 255, g = n >> 8 & 255, b = n & 255;
    return 'rgb(' + Math.round(r + (255 - r) * t) + ',' + Math.round(g + (255 - g) * t) + ',' + Math.round(b + (255 - b) * t) + ')';
  }
  function mount(lm, model, labels) {
    var units = +lm.style.getPropertyValue('--u') || 8, img = lm.querySelector('img');
    var cv = document.createElement('canvas'); cv.className = 'm3v'; cv.tabIndex = 0;
    cv.setAttribute('role', 'img');
    var nm = lm.getAttribute('data-m3n') || model.name;
    cv.setAttribute('aria-label', '3D model of ' + nm + ', ' + model.formula + '. Drag to rotate, scroll or pinch to zoom, double-click to reset. With focus: arrow keys rotate, plus and minus zoom, 0 resets.');
    var A = model.atoms, B = model.bonds, S = model.style, nA = A.length;
    var P = A.map(function (a) { return [a[1], a[2], a[3]]; });
    var ext = 0; P.forEach(function (p, i) { ext = Math.max(ext, Math.hypot(p[0], p[1], p[2]) + S[A[i][0]][0]); });
    function mkCol() { var mk = lm.querySelector('.mk'); return mk ? getComputedStyle(mk).backgroundColor : '#3E5C76'; } /* same colour as the 2D markers (light/dark) */
    var lab = (labels || []).map(function (l) { var ix = model.anchors[l[1]]; return ix && ix.length ? { t: l[0], ix: ix } : null; }).filter(Boolean);
    var hint = null, R0 = [1, 0, 0, 0, 1, 0, 0, 0, 1], R = R0.slice(), zoom = 1, W = 0, H = 0, ppu = 0, dpr = 1, raf = 0;
    function size() {
      var w = lm.getBoundingClientRect().width || (img && img.getBoundingClientRect().width) || 300;
      var xh = Math.max.apply(null, P.map(function (p, i) { return Math.abs(p[0]) + S[A[i][0]][0]; }));
      ppu = Math.min(w / units, (w - 8) / (2 * xh * 1.06));     /* same px-per-bond as the drawing, unless that would clip the sides */
      var ih = img && img.getBoundingClientRect().height || 0;
      var ys = P.map(function (p, i) { return Math.abs(p[1]) + S[A[i][0]][0]; }), yh = Math.max.apply(null, ys);
      var h = Math.max(ih, (2 * yh + 0.8) * ppu, Math.min(w, 2 * ext * ppu * 0.8));
      W = w; H = Math.round(h); if (hint) hint.hidden = w < 180; dpr = Math.min(window.devicePixelRatio || 1, 3);
      cv.style.width = W + 'px'; cv.style.height = H + 'px'; cv.width = Math.round(W * dpr); cv.height = Math.round(H * dpr);
      draw();
    }
    function draw() {
      raf = 0; var g = cv.getContext('2d'); g.setTransform(dpr, 0, 0, dpr, 0, 0); g.clearRect(0, 0, W, H);
      var s = ppu * zoom, cx = W / 2, cy = H / 2, D = Math.max(12, ext * 4);
      var Q = new Array(nA), zmin = 1e9, zmax = -1e9;
      for (var i = 0; i < nA; i++) {
        var p = P[i], x = R[0] * p[0] + R[1] * p[1] + R[2] * p[2], y = R[3] * p[0] + R[4] * p[1] + R[5] * p[2], z = R[6] * p[0] + R[7] * p[1] + R[8] * p[2];
        var f = D / (D - z);                                   /* gentle perspective */
        Q[i] = [cx + x * s * f, cy - y * s * f, z, f]; if (z < zmin) zmin = z; if (z > zmax) zmax = z;
      }
      var zr = Math.max(zmax - zmin, 1e-6), items = [];
      for (i = 0; i < nA; i++) items.push([Q[i][2], 0, i]);
      for (var k = 0; k < B.length; k++) items.push([Math.min(Q[B[k][0]][2], Q[B[k][1]][2]) - 1e-4, 1, k]);
      items.sort(function (a, b) { return a[0] - b[0]; });
      g.lineCap = 'round';
      items.forEach(function (it) {
        var fade = 0.28 * (zmax - it[0]) / zr;                   /* far things a little paler, like aerial perspective */
        if (it[1] === 1) {
          var b = B[it[2]], a1 = Q[b[0]], a2 = Q[b[1]], isH = A[b[0]][0] === 'H' || A[b[1]][0] === 'H', ff = (a1[3] + a2[3]) / 2;
          g.strokeStyle = mix(isH ? '#9a9a9a' : '#7a7a7a', fade);
          if (b[2] === 2) {
            var dx = a2[0] - a1[0], dy = a2[1] - a1[1], L = Math.hypot(dx, dy) || 1, nx = -dy / L * 0.085 * s * ff, ny = dx / L * 0.085 * s * ff;
            g.lineWidth = 0.07 * s * ff; g.lineCap = 'butt';
            for (var sgn = -1; sgn <= 1; sgn += 2) { g.beginPath(); g.moveTo(a1[0] + sgn * nx, a1[1] + sgn * ny); g.lineTo(a2[0] + sgn * nx, a2[1] + sgn * ny); g.stroke(); }
            g.lineCap = 'round';
          } else { g.lineWidth = (isH ? 0.075 : 0.12) * s * ff; g.beginPath(); g.moveTo(a1[0], a1[1]); g.lineTo(a2[0], a2[1]); g.stroke(); }
        } else {
          var q = Q[it[2]], st = S[A[it[2]][0]] || [0.27, '#ff1493', '#800a4a'], H_ = A[it[2]][0] === 'H';
          g.beginPath(); g.arc(q[0], q[1], st[0] * s * q[3], 0, 2 * Math.PI);
          g.fillStyle = mix(st[1], fade); g.fill(); g.lineWidth = Math.max(0.6, (H_ ? 0.025 : 0.0193) * s); g.strokeStyle = mix(st[2], fade); g.stroke();
        }
      });
      if (lab.length) {                                          /* numbered markers on the same atoms as the 2D drawing */
        var fs = W < 260 || innerWidth <= 600 ? 11 : 12.5, bh = fs < 12 ? 18 : 21;
        g.font = '600 ' + fs + 'px ' + (getComputedStyle(lm).getPropertyValue('--sans') || 'system-ui, sans-serif');
        g.textAlign = 'center'; g.textBaseline = 'middle'; var col = mkCol();
        var placed = [];
        lab.forEach(function (l) {
          var x = 0, y = 0, r = 0, zl = -1e9; l.ix.forEach(function (j) { x += Q[j][0]; y += Q[j][1]; zl = Math.max(zl, Q[j][2]); r = Math.max(r, S[A[j][0]][0] * s * Q[j][3]); }); x /= l.ix.length; y /= l.ix.length;
          if (l.ix.length > 1) { r = 0; l.ix.forEach(function (j) { r = Math.max(r, Math.hypot(Q[j][0] - x, Q[j][1] - y) + S[A[j][0]][0] * s * Q[j][3]); }); r *= 0.8; } /* a group: stand clear of the whole group */
          var w = Math.max(bh, g.measureText(l.t).width + 10), best = null;
          for (var k = 0; k < 16; k++) {                         /* try 16 spots round the atom; keep the one that hides the fewest atoms */
            var th = k / 16 * 2 * Math.PI, d = r + bh * 0.62, px = x + Math.cos(th) * d, py = y + Math.sin(th) * d, sc = 0;
            for (var j = 0; j < nA; j++) {
              if (l.ix.indexOf(j) >= 0) continue;
              var rr = S[A[j][0]][0] * s * Q[j][3] + bh / 2, dd = Math.hypot(Q[j][0] - px, Q[j][1] - py);
              if (dd < rr) sc += (rr - dd) / rr * (A[j][0] === 'H' ? 0.6 : 1.4) * (Q[j][2] > zl ? 1.5 : 1);
            }
            placed.forEach(function (o) { var dd = Math.hypot(o[0] - px, o[1] - py); if (dd < bh * 1.3) sc += 4 * (bh * 1.3 - dd) / bh; });
            if (px < w / 2 + 2 || px > W - w / 2 - 2 || py < bh / 2 + 2 || py > H - bh / 2 - 2) sc += 3;
            sc += 0.02 * Math.abs(Math.sin(th / 2 - Math.PI / 8));   /* tie-break: prefer up-right, like the drawings */
            if (!best || sc < best[0]) best = [sc, px, py];
          }
          x = Math.min(Math.max(best[1], w / 2 + 2), W - w / 2 - 2); y = Math.min(Math.max(best[2], bh / 2 + 2), H - bh / 2 - 2); placed.push([x, y]);
          g.beginPath(); g.roundRect ? g.roundRect(x - w / 2 - 2, y - bh / 2 - 2, w + 4, bh + 4, bh / 2 + 2) : g.arc(x, y, bh / 2 + 2, 0, 7);
          g.fillStyle = '#fff'; g.fill();
          g.beginPath(); g.roundRect ? g.roundRect(x - w / 2, y - bh / 2, w, bh, bh / 2) : g.arc(x, y, bh / 2, 0, 7);
          g.fillStyle = col; g.fill(); g.fillStyle = '#fff'; g.fillText(l.t, x, y + 0.5);
        });
      }
    }
    function req() { if (!raf) raf = requestAnimationFrame(draw); }
    function rotate(dx, dy) { R = mul(rotX(dy), mul(rotY(dx), R)); req(); }
    function setZoom(z) { zoom = Math.min(6, Math.max(0.3, z)); req(); }
    function reset() { R = R0.slice(); zoom = 1; req(); }
    var pts = {}, last = null, pinch0 = 0, zoom0 = 1, lastTap = 0;
    function onDown(e) { cv.setPointerCapture && cv.setPointerCapture(e.pointerId); pts[e.pointerId] = [e.clientX, e.clientY]; var ks = Object.keys(pts); if (ks.length === 2) { var a = pts[ks[0]], b = pts[ks[1]]; pinch0 = Math.hypot(a[0] - b[0], a[1] - b[1]); zoom0 = zoom; } last = [e.clientX, e.clientY];
      if (e.pointerType === 'touch') { var now = Date.now(); if (now - lastTap < 300 && ks.length === 1) reset(); lastTap = now; } e.preventDefault(); }
    function onMove(e) { if (!pts[e.pointerId]) return; pts[e.pointerId] = [e.clientX, e.clientY]; var ks = Object.keys(pts);
      if (ks.length >= 2) { var a = pts[ks[0]], b = pts[ks[1]], d = Math.hypot(a[0] - b[0], a[1] - b[1]); if (pinch0) setZoom(zoom0 * d / pinch0); }
      else if (last) { rotate((e.clientX - last[0]) * 0.01, (e.clientY - last[1]) * 0.01); last = [e.clientX, e.clientY]; } e.preventDefault(); }
    function onUp(e) { delete pts[e.pointerId]; var ks = Object.keys(pts); last = ks.length ? pts[ks[0]].slice() : null; if (ks.length < 2) pinch0 = 0; }
    function onWheel(e) { e.preventDefault(); setZoom(zoom * Math.exp(-e.deltaY * (e.deltaMode ? 0.05 : 0.0015))); }
    function onKey(e) {
      var k = e.key, st = 0.12, h = true;
      if (k === 'ArrowLeft') rotate(-st, 0); else if (k === 'ArrowRight') rotate(st, 0); else if (k === 'ArrowUp') rotate(0, -st); else if (k === 'ArrowDown') rotate(0, st);
      else if (k === '+' || k === '=') setZoom(zoom * 1.15); else if (k === '-' || k === '_') setZoom(zoom / 1.15); else if (k === '0') reset(); else h = false;
      if (h) { e.preventDefault(); e.stopPropagation(); }       /* keep the lesson player's arrow keys off while rotating */
    }
    cv.addEventListener('pointerdown', onDown); cv.addEventListener('pointermove', onMove); cv.addEventListener('pointerup', onUp); cv.addEventListener('pointercancel', onUp);
    cv.addEventListener('wheel', onWheel, { passive: false }); cv.addEventListener('dblclick', reset); cv.addEventListener('keydown', onKey);
    var ro = window.ResizeObserver ? new ResizeObserver(function () { var w = lm.getBoundingClientRect().width; if (w && Math.abs(w - W) > 0.5) size(); }) : null;
    hint = document.createElement('p'); hint.className = 'm3h'; hint.setAttribute('aria-hidden', 'true');
    hint.textContent = (matchMedia('(pointer: coarse)').matches ? 'Drag to turn · pinch to zoom · double-tap to reset' : 'Drag to turn · scroll to zoom · double-click to reset');
    lm.insertBefore(cv, lm.firstChild); cv.after(hint); size(); if (ro) ro.observe(lm);
    var mo = new MutationObserver(function () { draw(); }); mo.observe(document.documentElement, { attributes: true, attributeFilter: ['data-theme'] });
    return { canvas: cv, reset: reset, draw: draw, destroy: function () { if (ro) ro.disconnect(); mo.disconnect(); cv.remove(); hint.remove(); } };
  }
  window.Mol3D = { load: load, mount: mount };
})();
