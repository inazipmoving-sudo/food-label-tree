# Food Label Tree
A searchable, collapsible tree of 1,103 compounds and items found on food labels. Each item lists What it is, what it does In the body, and where it is Found in.
Live site: https://inazipmoving-sudo.github.io/food-label-tree/

Categories: Macronutrients (incl. Water, Ethanol), Micronutrients, Bioactives, Additives, Flavorings, Processing.
Category nodes can carry a short note: write `Name :: note` on the branch line in tree.txt. The Fats restructure is in gen/fats.py.

## Build
`python3 gen/gen.py && python3 build.py` builds `tree.txt`, then `data.json` and `data.js`. In `tree.txt`, each leaf has the format `Name|what|in the body|found in`.

## Sources
- **Additives:** UK Food Standards Agency, "Approved additives and E numbers" (https://www.food.gov.uk/business-guidance/approved-additives-and-e-numbers). This is the retained EU list under Regulation (EC) 1333/2008 Annex II. Items are grouped by function.
- **US-only additives:** 21 CFR Parts 73/74 (color additives), 172 (direct additives), and 182/184 (GRAS). Also the FDA "Substances Added to Food" inventory.
- **Vitamin and mineral forms:** Regulation (EC) 1925/2006 Annex II and Directive 2002/46/EC Annex II (permitted forms), plus 21 CFR forms where relevant.
- **Nutrition and bioactive descriptions:** general reference knowledge (e.g. NIH ODS fact sheets, standard biochemistry texts). They are not cited per item.

## Caveats
- The UK list follows the retained EU list, but the two have diverged. For example, E171 (titanium dioxide) has been banned in the EU since 2022 but is still authorized in the UK.
- The permitted vitamin and mineral forms were compiled from the regulations' content, not machine-fetched. Uncertain forms were left out.
- Descriptions are short summaries and are not medical advice. Some names appear in more than one branch on purpose.
- **Processing:** processing aids, cooking by-products and processing methods are summarized from general food-science references, e.g. IARC classifications and EFSA opinions on acrylamide, 3-MCPD/glycidyl esters and furan.

## Curriculum
`/curriculum/` holds teaching modules with numbered, linkable figures (`#fig-N`). Module 1 · Fats is one lesson of 9 figures built by `python3 gen/curriculum.py`: 1 the fat family tree (map of the lesson), then the molecule step by step (2 the fat molecule: meet the atoms + bond Q&A, triglyceride, fat vs oil, 3 saturated vs cis vs trans, 4 why solid vs liquid in space-filling style, 5 mono vs poly, 6 omega-3 vs omega-6), then 7 hydrogenation, 8 melting points with body fat, and last 9 breaking a fat down for energy (many kinds of triglyceride, then lipases releasing glycerol and fatty acids). Each figure's script is one flowing paragraph split into named sections. The molecule figures are PNGs in `curriculum/img/fats/` (RDKit + matplotlib, generated outside the repo); the family tree, melting-point chart and body-fat diagram are inline SVG. `macronutrients-fats-basics.html` is a redirect that maps old `#step-N` links to the new figures. The lesson script lives in `gen/scripts/macronutrients-fats.json` (40 named sections; `revision` 4, `idRevision` 3: `revision` goes up on any script change, `idRevision` only when figure or section IDs change) and is shown beside the figures by the lesson player below.

## Lesson player (template for curriculum pages)
Curriculum pages use a two-column player: the current figure on the left (sticky), the lesson script on the right with the current segment highlighted and the rest dimmed. On phones the figure stacks above the script and the controls sit fixed at the bottom. To build a new module the same way, you need only figures and a script JSON:
1. **Script:** write `gen/scripts/<module>.json` (schema v1): `{"schemaVersion":1,"module":"<module>","title":"...","figures":[{"fig":1,"title":"...","segments":[{"id":"1.1","seg":1,"text":"..."}]}]}`. Each segment is a named section of the figure's spoken paragraph. Optional fields: `name` (a short title shown as a serif subhead above the line and in the "Now" badge; its slug also works as a link, `#fig-1/three-categories`), `q` (a question heading, read before the text), `verbatim` (must be read word for word), `cue` (what to point at), `box` (`"body"` = pink "In your body" box, `"note"` = grey note), `part` (the `data-part` of an element in that figure; on desktop the figure column scrolls to it). IDs are `F.S` and must be in order; `load_script()` checks this and that every `part` exists.
2. **Figures:** build each one with `figure_card(n, title, art_html, caption, pre, after)` in `gen/curriculum.py`, which gives `id="fig-N"` and `data-fig`. Add `data-part="..."` to any image or box a segment should point at (`img(..., part=...)`).
3. **Page:** call `lesson_page(module, title, hero, figs_html, after_html)`. It writes `curriculum/<module>.html` with the number strip, the player and `after_html` (e.g. the quiz) below, embeds the script as `<script type="application/json" id="lesson-script">`, publishes `curriculum/scripts/<module>.json` (adds `pageUrl`, `scriptUrl`, `hashFormat`, `figureCount`, `segmentCount`), and copies `gen/player.js` and `gen/player.css` to `curriculum/assets/` (cache-busted by content hash). Run `python3 gen/curriculum.py`.

Behaviour (shared `player.js`, nothing module-specific):
- State is `{fig, seg, playing}`. Links: `#fig-3/seg-2` opens Figure 3 at segment 2; named lines also open by name (`#fig-1/three-categories`, case-insensitive; the hash is then shown as `#fig-1/seg-3`); `#fig-N` opens segment 1, and the `#step-N` redirects map to the current numbering. (Numbering changed twice in October 2026. Current order, revision 3: the breakdown figure is Figure 9 and the molecule figures are 2–8, so old 9-figure (revision 2) links map 2→9 and N→N−1 for 3–9; the original 8-figure links to 2–8 now land on the same figure number.) The hash updates as you move.
- Mode is "Live with Nutrition": the script is read aloud on the call, so the page never advances by itself (no timer, no browser speech). It moves only when you tap Next, tap a line, or use the keys. The bar shows a large "Now 3.2" and the next line's ID.
- Controls: previous/next figure, previous line, Next (labelled with the next ID), Pause / Continue, Question / Back to lesson; click any line to jump. Keys: Right/Left line, Shift+Right/Left figure, Space pause or continue (Up/Down still scroll the page).
- Pause marks the spot and Continue returns to it; Question does the same with a "Question break" note and "Back to lesson". The mark is saved in `flt-lesson-q:<module>` as `{fig, seg, kind, rev}`.
- Position is saved in localStorage (`flt-lesson:<module>`); opening the page again shows "Resume where you left off". Saved spots and marks carry the script's `idRevision` (or `revision` if there is none); ones from an older ID revision are ignored, so a renumbering never resumes on the wrong figure.
- `window.lessonPlayer` exposes `state` (`playing` = live, not paused), `mark`, `go(fig, seg)`, `pause()`, `play()` / `cont()` (Continue), `next()`, `prev()`, `nextFigure()`, `prevFigure()`, `question()` and `script` for a voice assistant or tests.
- Without JavaScript, all figures and script lines are shown in order.

