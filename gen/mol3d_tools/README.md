# 3D model specs for the 2D/3D toggle

How `gen/mol3d/<slug>.json` (input of `gen/mol3d.py`) was made for every lesson after Carbohydrates
(Carbohydrates' spec is hand-written and stays the reference).

1. `capture.py <builder.py> <tag>` re-runs a molecule builder (`/workspace/nutrition/lessons/<slug>_mols.py`,
   `/workspace/nutrition/build_lipid_mols.py`) in a sandbox copy of the repo with `lipids_mol.render` hooked, and records the
   molecule behind every PNG (atoms, 2D/3D drawing coordinates, bonds, atom-mapped SMILES). Every re-rendered PNG is
   checked byte-identical to the committed one.
2. `merge.py` maps every committed image (including copies reused across lessons, matched by pixels) to its record.
3. `auto.py <slugs...>` writes `spec-<slug>.json`: the drawing's own molecule (same tautomer, charges and H count as drawn)
   with stereo from PubChem (natural form; names/CIDs in `manual.json` when the drawing leaves stereo open), an identity
   check (same canonical SMILES, or same InChI skeleton with every PubChem stereo element agreeing by CIP label), marker
   anchors mapped to atoms, and the drawing's coordinates for a Kabsch alignment (`align`). Lone atoms/ions, ionic lattices
   and hydrated-ion pictures are skipped (`manual.json` gives the reason). PubChem answers are cached in `pc/`.
4. Copy the spec to `gen/mol3d/<slug>.json`, run `python3 gen/mol3d.py <slug>`, then `python3 gen/curriculum.py`.
5. `test_all.py [slugs]` (playwright): committed site on :8766 (`git archive HEAD`), working tree on :8765; checks 2D
   pixel-identical at default zoom, every toggle, 2D zoom (wheel / pinch, pan, +/-/0, double-click reset, enlarge), console
   errors and horizontal overflow, in light/desktop and dark/iPhone 13.
