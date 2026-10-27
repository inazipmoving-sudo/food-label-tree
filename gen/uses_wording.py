# Wording for the cell + places design of the body-uses figures (no statue), approved Oct 27, 2026 (old -> new list: /workspace/nutrition/cellonly-wording-changes.md).
# Each entry: (old sentence or phrase, new text or '' to remove). Applied to USES[slug]['segs'] text, plus cue/part changes.
SUB_NEW='Tap a number on the cell to see what that part does; the list below it gives every other place in the body.'
INTRO={
 'macronutrients-fats':("Here's a marble statue of the body with every place fat is used or stored.","Here's where fat is used or stored: first inside a single cell, then everywhere else in the body."),
 'macronutrients-lipids':("Here's the statue with every place the other lipids are used.","Here's where the other lipids are used: first inside a single cell, then everywhere else in the body."),
 'macronutrients-carbohydrates':("Here's the statue with every place carbohydrates are used.","Here's where carbohydrates are used: first inside a single cell, then everywhere else in the body."),
 'macronutrients-water-ethanol':("Here's the statue with the places water and ethanol are used or end up.","Here's where water and ethanol are used or end up: first inside a single cell, then everywhere else in the body."),
 'micronutrients-fat-soluble-vitamins':("Here's the statue with every place the fat-soluble vitamins are used or stored.","Here's where the fat-soluble vitamins are used or stored: first inside a single cell, then everywhere else in the body."),
 'micronutrients-water-soluble-vitamins':("Here's the statue with the places the water-soluble vitamins are used.","Here's where the water-soluble vitamins are used: first inside a single cell, then everywhere else in the body."),
 'micronutrients-major-minerals':("Here's the statue with every place the major minerals are used.","Here's where the major minerals are used: first inside a single cell, then everywhere else in the body."),
 'micronutrients-trace-minerals':("Here's the statue with the places the trace minerals are used.","Here's where the trace minerals are used: first inside a single cell, then everywhere else in the body."),
 'additives':("Here's the statue with the places additives act or end up.","Here's where additives act or end up: first inside a single cell, then everywhere else in the body."),
 'antinutrients':("Here's the statue with the places antinutrients act.","Here's where antinutrients act: first inside a single cell, then everywhere else in the body."),
 'processing':("Here's the statue with the places that compounds from cooking and processing act.","Here's where compounds from cooking and processing act: first inside a single cell, then everywhere else in the body."),
 'bioactives':("Here's the statue with the places bioactives are used.","Here's where bioactives are used: first inside a single cell, then everywhere else in the body."),
 'flavorings':("Here's the statue with the places flavorings are used.","Here's where flavorings are used: first inside a single cell, then everywhere else in the body."),
 'macronutrients-protein':("Here's the statue with every place protein is used.","Here's where protein is used: first inside a single cell, then everywhere else in the body."),
}
TAP=[" Tap a number to see what that place does with it."," Tap a number to see what that place does."," Tap a number to see what happens there."," Tap a number to see what each place does with them."," Tap a number to see what each place does."]
NOTE={
 'macronutrients-fats':("so the numbers mark typical places, not every one.","so the list gives each place's main job, not every detail."),
 'macronutrients-lipids':("so the numbers mark typical places, not every one.","so the list gives each place's main job, not every detail."),
 'macronutrients-carbohydrates':("so the numbers mark the places that depend on it most or store it, not every one.","so the list gives the places that depend on it most or store it, and each one's main job."),
 'macronutrients-water-ethanol':("so the numbers mark typical places.","so the list gives each place's main job, not every detail."),
 'micronutrients-fat-soluble-vitamins':("so the numbers mark the main places, not every one.","so the list gives each place's main job, not every detail."),
 'micronutrients-water-soluble-vitamins':("so the numbers mark the places that need them most or store them, not every one.","so the list gives the places that need them most or store them, and each one's main job."),
 'micronutrients-major-minerals':("so the numbers mark the main places, not every one.","so the list gives each place's main job, not every detail."),
 'micronutrients-trace-minerals':("so the numbers mark the main places, not every one.","so the list gives each place's main job, not every detail."),
 'additives':("so the numbers mark typical places, not every one.","so the list gives each one's main path, not every detail."),
 'antinutrients':None,
 'processing':("so the numbers mark where these compounds act, not a measure of harm.","so the list shows where these compounds act, not a measure of harm."),
 'bioactives':("so the numbers mark where these compounds act, not proven health benefits.","so the list shows where these compounds act, not proven health benefits."),
 'flavorings':("so the numbers mark where they act, not a dose.","so the list shows where they act, not a dose."),
 'macronutrients-protein':("so the numbers mark typical places, not every one.","so the list gives each place's main job, not every detail."),
}
CUE_INTRO='The cell drawing and the list of places'
CUE_NOTE='The note under the list'
CELL_CUE='The cell drawing and its numbered parts'
import re as _re
def site_cue(old):
    """'Numbers 1 and 2: under the skin and around the organs' -> 'In the list: under the skin and around the organs'"""
    return _re.sub(r'^Numbers? [0-9, and to]+: ','In the list: ',old)
