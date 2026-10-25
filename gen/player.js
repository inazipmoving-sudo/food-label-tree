/* Food Label Tree lesson player (shared by every curriculum page).
   Needs: <script type="application/json" id="lesson-script"> (schemaVersion 1),
   a .lp[data-player] stage with figure.fig[data-fig] cards and ol.lp-segs[data-fig] lists,
   and the .lp-ctl control bar. State is {fig, seg, playing}; position is saved in
   localStorage and in the URL hash (#fig-3/seg-2). Old #fig-N links still work. */
(function () {
  'use strict';
  var dataEl = document.getElementById('lesson-script');
  var root = document.querySelector('[data-player]');
  if (!dataEl || !root) return;
  var D = JSON.parse(dataEl.textContent);
  if (D.schemaVersion !== 1) { console.warn('lesson player: unknown schemaVersion', D.schemaVersion); }
  var MOD = D.module, KEY = 'flt-lesson:' + MOD, QKEY = 'flt-lesson-q:' + MOD, TKEY = 'flt-lesson-tts';
  var FIGS = D.figures, NF = FIGS.length;
  var flat = [];
  FIGS.forEach(function (f, fi) { f.segments.forEach(function (s, si) { flat.push({ fig: f.fig, seg: s.seg, s: s, fi: fi, si: si }); }); });
  var $ = function (sel, el) { return (el || document).querySelector(sel); };
  var $$ = function (sel, el) { return Array.prototype.slice.call((el || document).querySelectorAll(sel)); };
  var store = {
    get: function (k) { try { return JSON.parse(localStorage.getItem(k)); } catch (e) { return null; } },
    set: function (k, v) { try { if (v == null) localStorage.removeItem(k); else localStorage.setItem(k, JSON.stringify(v)); } catch (e) {} }
  };
  var S = { fig: 1, seg: 1, playing: false };
  var mark = store.get(QKEY);
  var canSpeak = 'speechSynthesis' in window && typeof SpeechSynthesisUtterance === 'function';
  var tts = canSpeak && store.get(TKEY) === true;
  var token = 0, timer = null;
  var ctl = $('.lp-ctl'), figCol = $('.lp-figcol', root), scrCol = $('.lp-scriptcol', root);
  var mq = window.matchMedia('(max-width: 900px)');

  function figData(n) { return FIGS.filter(function (f) { return f.fig === n; })[0]; }
  function idx(fig, seg) { for (var i = 0; i < flat.length; i++) if (flat[i].fig === fig && flat[i].seg === seg) return i; return -1; }
  function valid(fig, seg) { return idx(fig, seg) >= 0; }
  function cur() { return flat[idx(S.fig, S.seg)]; }
  function parseHash(h) {
    var m = /^#fig-(\d+)(?:\/seg-(\d+))?$/.exec(h || '');
    if (!m) return null;
    var f = +m[1], s = m[2] ? +m[2] : 1;
    if (!figData(f)) return null;
    if (!valid(f, s)) s = 1;
    return { fig: f, seg: s };
  }
  function hashOf(p) { return '#fig-' + p.fig + '/seg-' + p.seg; }
  function label(p) { return p.fig + '.' + p.seg; }

  /* ---------- rendering ---------- */
  function render(opts) {
    opts = opts || {};
    var figChanged = opts.figChanged;
    $$('.fig[data-fig]', root).forEach(function (el) { el.classList.toggle('cur', +el.dataset.fig === S.fig); });
    $$('.lp-segs[data-fig]', root).forEach(function (el) { el.hidden = +el.dataset.fig !== S.fig; });
    $$('.lp-seg', root).forEach(function (li) {
      var on = li.dataset.id === label(S);
      li.classList.toggle('on', on);
      li.classList.toggle('qmark', !!(mark && li.dataset.id === label(mark)));
      if (on) li.setAttribute('aria-current', 'step'); else li.removeAttribute('aria-current');
    });
    $$('.findex a[href^="#fig-"]').forEach(function (a) { a.classList.toggle('on', a.getAttribute('href') === '#fig-' + S.fig); });
    var f = figData(S.fig), i = idx(S.fig, S.seg);
    $('.lp-where', ctl).textContent = label(S);
    $('.lp-of', ctl).textContent = 'Segment ' + (i + 1) + ' of ' + flat.length;
    var h = $('.lp-scripthead', root);
    if (h) h.innerHTML = '<span class="lp-k">Figure ' + f.fig + ' script</span><span class="lp-t"></span><span class="lp-n">' + f.segments.length + ' segments</span>';
    if (h) $('.lp-t', h).textContent = f.title;
    var pb = $('[data-act=play]', ctl);
    pb.setAttribute('aria-pressed', S.playing ? 'true' : 'false');
    pb.setAttribute('aria-label', S.playing ? 'Pause' : 'Play');
    pb.title = (S.playing ? 'Pause' : 'Play') + ' (Space)';
    $('.lp-pl', pb).textContent = S.playing ? 'Pause' : 'Play';
    root.classList.toggle('playing', S.playing);
    $('[data-act=prevseg]', ctl).disabled = i <= 0;
    $('[data-act=nextseg]', ctl).disabled = i >= flat.length - 1;
    $('[data-act=prevfig]', ctl).disabled = i <= 0;
    $('[data-act=nextfig]', ctl).disabled = S.fig >= FIGS[NF - 1].fig;
    var q = $('[data-act=question]', ctl);
    q.textContent = mark ? 'Back to lesson' : 'Question';
    q.classList.toggle('on', !!mark);
    q.title = mark ? 'Return to ' + label(mark) : 'Pause and mark this spot';
    var qb = $('.lp-qbanner', root);
    if (qb) { qb.hidden = !mark; if (mark) qb.textContent = 'Question break at ' + label(mark) + '. Press Back to lesson to return.'; }
    var now = $('.lp-now', ctl); if (now) { var cs = cur().s; now.textContent = (cs.q ? cs.q + ' ' : '') + cs.text; }
    var live = $('.lp-live', root); if (live) live.textContent = 'Segment ' + label(S);
    if (!opts.noScroll) reveal(figChanged);
  }
  function scrollWithin(col, el, pad) {
    var top = el.getBoundingClientRect().top - col.getBoundingClientRect().top + col.scrollTop - (pad || 12);
    col.scrollTo({ top: Math.max(0, top), behavior: 'smooth' });
  }
  function stripH() { var s = $('.findex'); return s ? s.getBoundingClientRect().height : 0; }
  function reveal(figChanged) {
    var li = $('.lp-seg.on', root);
    var c = cur(), figEl = $('.fig.cur', root);
    if (mq.matches) {
      if (figChanged) window.scrollTo({ top: root.getBoundingClientRect().top + window.scrollY - stripH() - 8, behavior: 'smooth' });
      else if (li) li.scrollIntoView({ block: 'nearest', behavior: 'smooth' });
      return;
    }
    if (figChanged) {
      var r = root.getBoundingClientRect();
      if (r.top > stripH() + 40 || r.top < 0) window.scrollTo({ top: r.top + window.scrollY - stripH() - 12, behavior: 'smooth' });
    }
    if (figCol) {
      var part = c && c.s.part ? $('[data-part="' + c.s.part + '"]', figEl) : null;
      if (part) scrollWithin(figCol, part, 16); else if (figChanged) figCol.scrollTo({ top: 0 });
    }
    if (scrCol && li) {
      if (figChanged) scrCol.scrollTo({ top: 0 });
      var lr = li.getBoundingClientRect(), cr = scrCol.getBoundingClientRect();
      if (lr.top < cr.top + 70 || lr.bottom > cr.bottom - 10) scrollWithin(scrCol, li, 80);
    }
  }

  /* ---------- state changes ---------- */
  function save() {
    store.set(KEY, { fig: S.fig, seg: S.seg, t: Date.now() });
    if (location.hash !== hashOf(S)) history.replaceState(null, '', hashOf(S));
    var rb = $('[data-act=resume]', root); if (rb) rb.hidden = true;
  }
  function go(fig, seg, how) {
    how = how || {};
    if (!valid(fig, seg)) return;
    var figChanged = fig !== S.fig;
    S.fig = fig; S.seg = seg;
    if (how.save !== false) save();
    render({ figChanged: figChanged, noScroll: how.noScroll });
    if (S.playing) runSeg();
  }
  function step(d) { var i = idx(S.fig, S.seg) + d; if (i >= 0 && i < flat.length) go(flat[i].fig, flat[i].seg); }
  function stepFig(d) {
    var fi = FIGS.indexOf(figData(S.fig));
    if (d < 0 && S.seg > 1) return go(S.fig, 1);
    var t = FIGS[fi + d]; if (t) go(t.fig, 1);
  }
  function stopRun() {
    token++;
    if (timer) { clearTimeout(timer); timer = null; }
    if (canSpeak) { try { window.speechSynthesis.cancel(); } catch (e) {} }
    var li = $('.lp-seg.on', root); if (li) li.style.removeProperty('--dur');
    $$('.lp-seg.run', root).forEach(function (x) { x.classList.remove('run'); });
  }
  function words(s) { return ((s.q ? s.q + ' ' : '') + s.text).split(/\s+/).length; }
  function runSeg() {
    stopRun();
    var my = token, c = cur(), li = $('.lp-seg.on', root);
    var done = function () { if (my === token && S.playing) advance(); };
    if (tts) {
      var u = new SpeechSynthesisUtterance((c.s.q ? c.s.q + ' ' : '') + c.s.text);
      u.lang = D.lang || 'en';
      u.onend = done;
      u.onerror = function (e) { if (my === token && e.error !== 'interrupted' && e.error !== 'canceled') { S.playing = false; render({ noScroll: true }); } };
      window.speechSynthesis.speak(u);
    } else {
      var ms = Math.round(words(c.s) / 2.6 * 1000) + 900; /* about 155 words a minute, then a short pause */
      if (li) { li.style.setProperty('--dur', ms + 'ms'); void li.offsetWidth; li.classList.add('run'); }
      timer = setTimeout(done, ms);
    }
  }
  function advance() {
    var i = idx(S.fig, S.seg);
    if (i < flat.length - 1) go(flat[i + 1].fig, flat[i + 1].seg);
    else { pause(); }
  }
  function play() {
    if (mark) { var m = mark; mark = null; store.set(QKEY, null); S.playing = true; go(m.fig, m.seg); return; }
    S.playing = true; render({ noScroll: true }); runSeg();
  }
  function pause() { S.playing = false; stopRun(); render({ noScroll: true }); }
  function toggle() { if (S.playing) pause(); else play(); }
  function question() {
    if (mark) { var m = mark; mark = null; store.set(QKEY, null); pause(); go(m.fig, m.seg); return; }
    pause(); mark = { fig: S.fig, seg: S.seg }; store.set(QKEY, mark); render({ noScroll: true });
  }

  /* ---------- wiring ---------- */
  ctl.addEventListener('click', function (e) {
    var b = e.target.closest('button[data-act]'); if (!b) return;
    var a = b.dataset.act;
    if (a === 'now') { var l = $('.lp-seg.on', root); if (l) l.scrollIntoView({ block: 'center', behavior: 'smooth' }); }
    else if (a === 'play') toggle();
    else if (a === 'prevseg') step(-1);
    else if (a === 'nextseg') step(1);
    else if (a === 'prevfig') stepFig(-1);
    else if (a === 'nextfig') stepFig(1);
    else if (a === 'question') question();
    if (e.detail > 0) b.blur(); /* mouse/touch: keep Space for play/pause */
  });
  var tt = $('[data-act=tts]', ctl);
  if (tt) {
    if (!canSpeak) tt.closest('label').hidden = true;
    tt.checked = tts;
    tt.addEventListener('change', function () { tts = tt.checked; store.set(TKEY, tts); if (S.playing) runSeg(); tt.blur(); });
  }
  root.addEventListener('click', function (e) {
    var r = e.target.closest('[data-act=resume]');
    if (r) { var sv = store.get(KEY); if (sv && valid(sv.fig, sv.seg)) go(sv.fig, sv.seg); return; }
    var li = e.target.closest('.lp-seg'); if (!li) return;
    var p = li.dataset.id.split('.'); go(+p[0], +p[1]);
  });
  root.addEventListener('keydown', function (e) {
    var li = e.target.closest && e.target.closest('.lp-seg');
    if (li && (e.key === 'Enter')) { e.preventDefault(); li.click(); }
  });
  $$('.findex a[href^="#fig-"]').forEach(function (a) {
    a.addEventListener('click', function (e) { var p = parseHash(a.getAttribute('href')); if (!p) return; e.preventDefault(); go(p.fig, p.seg); });
  });
  $$('.lp a.badge').forEach(function (a) { a.addEventListener('click', function (e) { e.preventDefault(); }); });
  document.addEventListener('keydown', function (e) {
    if (e.ctrlKey || e.metaKey || e.altKey) return;
    var t = e.target, tag = (t.tagName || '').toLowerCase();
    if (tag === 'input' || tag === 'textarea' || tag === 'select' || t.isContentEditable) return;
    if (e.key === ' ' || e.code === 'Space') {
      if (tag === 'button' || tag === 'summary' || tag === 'a') return;
      e.preventDefault(); toggle();
    } else if (e.key === 'ArrowRight') { e.preventDefault(); e.shiftKey ? stepFig(1) : step(1); }
    else if (e.key === 'ArrowLeft') { e.preventDefault(); e.shiftKey ? stepFig(-1) : step(-1); }
  });
  window.addEventListener('hashchange', function () { var p = parseHash(location.hash); if (p) go(p.fig, p.seg); });
  window.addEventListener('pagehide', function () { stopRun(); });

  /* ---------- start ---------- */
  var fromHash = parseHash(location.hash);
  var saved = store.get(KEY);
  if (saved && !valid(saved.fig, saved.seg)) saved = null;
  if (fromHash) { S.fig = fromHash.fig; S.seg = fromHash.seg; }
  root.classList.add('ready');
  document.documentElement.classList.add('has-player');
  render({ figChanged: true, noScroll: true });
  if (fromHash) {
    save();
    requestAnimationFrame(function () {
      var li = $('.lp-seg.on', root);
      if (mq.matches && S.seg > 1 && li) li.scrollIntoView({ block: 'center' });
      else { window.scrollTo({ top: root.getBoundingClientRect().top + window.scrollY - stripH() - 8 }); reveal(true); }
    });
  }
  var rb = $('[data-act=resume]', root);
  if (rb && saved && !(saved.fig === S.fig && saved.seg === S.seg)) {
    rb.hidden = false;
    $('.lp-rs', rb).textContent = label(saved);
  }
  window.lessonPlayer = {
    get state() { return { fig: S.fig, seg: S.seg, playing: S.playing }; },
    get mark() { return mark ? { fig: mark.fig, seg: mark.seg } : null; },
    script: D, go: go, play: play, pause: pause, next: function () { step(1); }, prev: function () { step(-1); },
    nextFigure: function () { stepFig(1); }, prevFigure: function () { stepFig(-1); }, question: question
  };
})();
