# Site-wide settings and the course catalog shown on the home page (index.html at the site root).
# Rename the university/site here; every page title and the home page heading use this one constant.
UNIVERSITY_NAME = "LeClaire Institute"
BRAND_EMPHASIS = "ai"  # letters of the name shown in the accent colour (same case as in the name)
# Tagline under the site title on the home page; "" hides it.
TAGLINE = "The Orcutt Shortcut"
def brand_html(name=None):
    """The name as page HTML with BRAND_EMPHASIS emphasized (accent colour, slightly heavier); plain text is used in <title>."""
    name = name or UNIVERSITY_NAME
    e = BRAND_EMPHASIS; i = name.find(e) if e else -1
    return name if i < 0 else name[:i] + f'<span class="ai">{e}</span>' + name[i+len(e):]
BRAND_CSS = (".ai{color:var(--acc);font-weight:600;letter-spacing:.01em}"
             ".brand{display:inline-block;margin-bottom:10px;font-family:var(--serif);font-size:1.25rem;font-weight:500;letter-spacing:.02em;text-decoration:none;color:var(--text)}"
             ".brand:hover{color:var(--text)}.brand:hover .ai{text-decoration:underline;text-underline-offset:3px}")
# Courses on the home page, in order. To add a course: append a dict here (slug, title, href relative to the site root,
# desc, and either 'reg' = the lesson registry used to count modules/lessons, or explicit 'modules'/'lessons' numbers).
COURSES = [
    dict(slug='nutrition-101', title='Nutrition 101', href='curriculum/', code='NUTR 101',
         desc='What food is made of, down to molecules and elements: macronutrients, micronutrients and the non-nutrients in whole foods, '
              'a final review that reads real labels line by line, and the searchable Food Label Tree of over 1,000 label compounds.',
         reg='REG'),
]
