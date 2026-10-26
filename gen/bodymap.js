/* Module 6 body map: layers, dive-in zoom, nutrient routes; synced with the lesson player */
(function () {
  'use strict';
  function $(s, r) { return (r || document).querySelector(s); }
  function $$(s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); }
  function esc(t) { return String(t).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }
  var FULL = [0, 0, 400, 800];
  function vbOf(s) { return s.split(/\s+/).map(Number); }
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  function BodyMap(root) {
    var D = JSON.parse($('.bm-data', root).textContent);
    var svg = $('.bm-svg', root), pins = $('.bm-pins', root), panel = $('.bm-panel', root), back = $('.bm-back', root);
    var st = { layer: null, dive: null, sel: null, route: null }, vb = FULL.slice(), anim = 0;
    function setVB(v) { vb = v; svg.setAttribute('viewBox', v.join(' ')); }
    function zoom(to, done) {
      cancelAnimationFrame(anim);
      var from = vb.slice(), t0 = performance.now(), dur = reduce ? 0 : 520;
      pins.classList.add('moving');
      function step(t) {
        var k = dur ? Math.min(1, (t - t0) / dur) : 1, e = k < .5 ? 2 * k * k : 1 - Math.pow(-2 * k + 2, 2) / 2;
        setVB(from.map(function (a, i) { return a + (to[i] - a) * e; }));
        if (k < 1) anim = requestAnimationFrame(step); else { pins.classList.remove('moving'); if (done) done(); }
      }
      anim = requestAnimationFrame(step);
    }
    function pinHTML(list) {
      // list: [[x, y, label, key]]
      pins.innerHTML = list.map(function (p, i) {
        var l = (p[0] - vb[0]) / vb[2] * 100, t = (p[1] - vb[1]) / vb[3] * 100;
        return '<span class="bm-pin" data-k="' + esc(p[3] || '') + '" style="left:' + l.toFixed(2) + '%;top:' + t.toFixed(2) + '%">' + (i + 1) + '</span>';
      }).join('');
    }
    function setTabs() {
      root.setAttribute('data-layer', st.route ? 'route' : st.layer);
      root.setAttribute('data-mode', st.route ? 'route' : (st.dive ? 'dive' : 'layer'));
      root.setAttribute('data-dive', st.dive || '');
      $$('.bm-tab', root).forEach(function (b) { b.setAttribute('aria-pressed', String(!st.route && b.dataset.layer === st.layer)); });
      $$('.bm-chip', root).forEach(function (b) { b.setAttribute('aria-pressed', String(b.dataset.n === st.route)); });
      $$('.bm-dv', root).forEach(function (b) { b.classList.toggle('on', b.dataset.dive === st.dive); b.hidden = !!st.route || b.dataset.for !== st.layer; });
      $$('.bm-route', root).forEach(function (g) { g.classList.toggle('on', g.dataset.n === st.route); });
      back.hidden = !(st.dive || st.route);
      back.textContent = st.route ? '← Back to the layers' : '← Whole body';
    }
    function hilite() {
      $$('.hi', svg).forEach(function (e) { e.classList.remove('hi'); });
      $$('.bm-pin', pins).forEach(function (p) { p.classList.toggle('on', !!st.sel && p.dataset.k === st.sel); });
      $$('.bm-part', panel).forEach(function (p) { p.classList.toggle('on', p.dataset.k === st.sel); });
      if (!st.sel) return;
      var lay = $('.bm-l[data-layer="' + st.layer + '"]', svg);
      var cu = st.dive && $('[data-close="' + st.dive + '"]', svg);
      [lay, cu].forEach(function (g) { if (g) $$('[data-k="' + st.sel + '"]', g).forEach(function (e) { e.classList.add('hi'); }); });
    }
    function partLi(k, n) {
      var p = D.parts[k]; if (!p) return '';
      var closer = D.closer[k] && D.closer[k] !== st.dive && D.dives[D.closer[k]] && D.dives[D.closer[k]].layer === st.layer ? D.closer[k] : null;
      return '<li class="bm-part" data-k="' + k + '"><button type="button" class="bm-pb" data-k="' + k + '">' + (n ? '<span class="bm-n">' + n + '</span>' : '') + '<b>' + esc(p[0]) + '</b></button><span class="bm-job">' + esc(p[1]) +
        (closer ? ' <button type="button" class="bm-closer" data-dive="' + closer + '">Zoom closer: ' + esc(D.dives[closer].t) + ' →</button>' : '') + '</span></li>';
    }
    function layerPanel() {
      var keys = [], seen = {};
      (D.order[st.layer] || []).forEach(function (d) { D.dives[d].parts.forEach(function (k) { if (!seen[k] && D.dives[d].layer === st.layer && d !== 'villus' && d !== 'bone' && d !== 'skin') { seen[k] = 1; keys.push(k); } }); });
      if (st.layer === 'skin') keys = ['skin'];
      panel.innerHTML = '<p class="bm-h">' + esc(D.names[st.layer]) + '</p><p class="bm-lead">' + esc(D.intro[st.layer]) + '</p><ul class="bm-list">' + keys.map(function (k) { return partLi(k); }).join('') + '</ul>';
      pins.innerHTML = '';
    }
    function divePanel() {
      var d = D.dives[st.dive];
      panel.innerHTML = '<p class="bm-h">' + esc(d.t) + '</p><p class="bm-lead">' + esc(d.lead) + '</p><ol class="bm-list">' + d.parts.map(function (k, i) { return partLi(k, i + 1); }).join('') + '</ol>';
    }
    function dioPins() { var d = D.dives[st.dive]; pinHTML(d.parts.map(function (k) { var a = d.pins[k]; return [a[0], a[1], '', k]; })); }
    function routePanel() {
      var r = D.routes[st.route];
      panel.innerHTML = '<p class="bm-h">' + esc(r.name) + '</p><ol class="bm-list bm-steps">' + r.stops.map(function (s, i) { return '<li><span class="bm-n">' + (i + 1) + '</span><b>' + esc(s[2]) + '</b> <span class="bm-job">' + esc(s[3]) + '</span></li>'; }).join('') + '</ol>' +
        '<p class="bm-end"><b>Ends up:</b> ' + esc(r.end) + '</p><p class="bm-simp"><b>Simplified:</b> ' + esc(r.simp) + '</p><p class="bm-les">Lesson: <a href="' + r.lesson[0] + '">' + esc(r.lesson[1]) + ' →</a></p>';
      pinHTML(r.stops.map(function (s) { return [s[0], s[1], s[2], '']; }));
    }
    function layer(l) {
      st.layer = l; st.dive = null; st.sel = null; st.route = null; setTabs(); layerPanel(); zoom(FULL); hilite();
    }
    function dive(k, sel) {
      var d = D.dives[k]; if (!d) return;
      st.route = null; st.layer = d.layer; st.dive = k; st.sel = sel || null; setTabs(); divePanel(); pins.innerHTML = '';
      zoom(vbOf(d.vb), function () { dioPins(); hilite(); }); hilite();
    }
    function route(n) {
      if (!D.routes[n]) return;
      st.route = n; st.dive = null; st.sel = null; setTabs(); pins.innerHTML = '';
      $$('.bm-route.on .rt', svg).forEach(function (p) { p.style.animation = 'none'; p.getBoundingClientRect(); p.style.animation = ''; });
      zoom(FULL, routePanel); hilite();
    }
    function select(k) {
      if (st.route) return;
      if (!st.dive) {
        if (st.layer === 'skin') return dive('skin');
        var dk = (D.order[st.layer] || []).filter(function (d) { return D.dives[d].parts.indexOf(k) >= 0; })[0];
        if (dk) return dive(dk, k);
      }
      st.sel = st.sel === k ? null : k; hilite();
    }
    function near(e) {
      // a tap that misses every part (gaps, hollows, thin lines): take the part whose box holds the point, smallest first, else the nearest within 24 units
      if (st.route) return null;
      var m = svg.getScreenCTM(); if (!m) return null;
      var pt = svg.createSVGPoint(); pt.x = e.clientX; pt.y = e.clientY; pt = pt.matrixTransform(m.inverse());
      var g = st.dive && $('[data-close="' + st.dive + '"]', svg);
      if (!g || !$('[data-k]', g)) g = $('.bm-l[data-layer="' + st.layer + '"]', svg);
      var best = null, bd = 1e9;
      $$('[data-k]', g).forEach(function (el) {
        var b; try { b = el.getBBox(); } catch (x) { return; }
        if (!b.width && !b.height) return;
        var dx = Math.max(b.x - pt.x, 0, pt.x - b.x - b.width), dy = Math.max(b.y - pt.y, 0, pt.y - b.y - b.height), d = Math.hypot(dx, dy) * 1e6 + b.width * b.height;
        if (d < bd) { bd = d; best = el.getAttribute('data-k'); }
      });
      return bd < 24e6 ? best : null;
    }
    root.addEventListener('click', function (e) {
      var b = e.target.closest('button'); 
      if (b && root.contains(b)) {
        if (b.classList.contains('bm-tab')) return layer(b.dataset.layer);
        if (b.classList.contains('bm-chip')) return st.route === b.dataset.n ? layer(st.layer) : route(b.dataset.n);
        if (b.classList.contains('bm-dv') || b.classList.contains('bm-closer')) return dive(b.dataset.dive);
        if (b.classList.contains('bm-back')) { if (st.route) return layer(st.layer); var up = st.dive && ['villus', 'bone'].indexOf(st.dive) >= 0 ? (st.dive === 'villus' ? 'torso' : 'bones-limb') : null; return up ? dive(up) : layer(st.layer); }
        if (b.classList.contains('bm-pb')) { if (!st.dive) return select(b.dataset.k); st.sel = st.sel === b.dataset.k ? null : b.dataset.k; return hilite(); }
        return;
      }
      var g = e.target.closest('[data-k]');
      if (g && svg.contains(g)) select(g.getAttribute('data-k'));
      else if (svg.contains(e.target)) { var k = near(e); if (k) select(k); }
      else if (g && pins.contains(g) && g.dataset.k) { st.sel = g.dataset.k; hilite(); }
    });
    this.apply = function (part) {
      var m;
      if ((m = /^layer-(.+)$/.exec(part))) layer(m[1]);
      else if ((m = /^dive-(.+)$/.exec(part))) dive(m[1]);
      else if ((m = /^n-(.+)$/.exec(part))) route(m[1]);
    };
    var s0 = D.start; if (s0.dive) { st.layer = D.dives[s0.dive].layer; dive(s0.dive); } else layer(s0.layer);
    if (s0.route) route(s0.route);
  }
  function init() {
    var maps = $$('.bm').map(function (r) { var m = new BodyMap(r); r._bm = m; return m; });
    if (!maps.length) return;
    var sc = $('#lesson-script'), segs = {};
    if (sc) { try { JSON.parse(sc.textContent).figures.forEach(function (f) { f.segments.forEach(function (s) { segs[s.id] = { fig: f.fig, part: s.part }; }); }); } catch (e) {} }
    var last = null;
    function sync() {
      var li = $('.lp-seg.on'); if (!li) return;
      var id = li.getAttribute('data-id'); if (id === last) return; last = id;
      var s = segs[id]; if (!s || !s.part) return;
      var fig = document.getElementById('fig-' + s.fig), r = fig && $('.bm', fig);
      if (r && r._bm) r._bm.apply(s.part);
    }
    var lp = $('[data-player]');
    if (lp && window.MutationObserver) new MutationObserver(sync).observe(lp, { subtree: true, attributes: true, attributeFilter: ['class'] });
    setTimeout(sync, 300);
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init); else init();
})();
