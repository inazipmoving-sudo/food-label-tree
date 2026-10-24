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
`/curriculum/` holds teaching modules with numbered, linkable figures (`#fig-N`). Module 1 › Fats is built by `python3 gen/curriculum.py`. All figures are inline SVG, and the molecule drawings are computed from real skeletal geometry: 120° zigzag, and a cis double bond bends the chain. The script that goes with it is kept outside the repo.
