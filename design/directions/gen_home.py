"""Generate the C3 home mock from one project list (the seed of the site's project data)."""
import html, pathlib

# (category, subgroup or None, title, one line, cover class or None, href)
P = [
  ("Research", None, "Directional Collision Principle", "Predicting which neural-network inputs are vulnerable to attack. 87.5% accuracy, 100% recall.", "fig-dcp", "c3-project.html"),
  ("Research", None, "A Quantitative Collision Principle", "Short note on odd Lipschitz functions, January 2026.", "fig-tau", "#"),
  ("Research", None, "Hyperplane Arrangements", "Expository paper connecting hyperplane arrangements to ReLU networks.", None, "#"),
  ("Research", None, "Stability Analysis in Dynamical Systems", "Lyapunov, phase-plane and bifurcation methods. Euler Circle, 2024.", None, "#"),
  ("Research", None, "Personal genome analysis", "Bioinformatics pipelines on the U-Michigan HPC cluster. miRcore, 2025.", None, "#"),

  ("Racing", None, "Assetto Corsa: Jev", "[one line]", None, "#"),
  ("Racing", None, "F1 Tracks Explorer", "Formula 1 circuits in the browser.", None, "#"),

  ("Utils", None, "This site", "The portfolio itself, and how it was made.", None, "#"),
  ("Utils", "Personal productivity", "sortmails", "Smart mail.", None, "#"),
  ("Utils", "Personal productivity", "Calendar + planner", "Sunsama-style daily planning.", None, "#"),
  ("Utils", "Personal productivity", "Tasks + projects", "Linear-style task and project management.", None, "#"),
  ("Utils", "Personal productivity", "CRM", "People authority.", None, "#"),
  ("Utils", "Personal productivity", "Agents", "[one line]", None, "#"),
  ("Utils", "More tools", "samgram", "TweetDeck-style crowd intelligence.", None, "#"),
  ("Utils", "More tools", "talk-unroller", "[one line]", None, "#"),
  ("Utils", "More tools", "veggie-menus", "Only the menu items you can eat.", None, "#"),
  ("Utils", "More tools", "carumathy", "[one line]", None, "#"),

  ("Catalog + Consume", "Music", "TBOSM + Trichur Brothers", "Practice app and recordings.", None, "#"),
  ("Catalog + Consume", "Music", "arrahman.in", "[one line]", None, "#"),
  ("Catalog + Consume", "Music", "CarnaticTube", "Carnatic music, grouped by raga.", None, "#"),
  ("Catalog + Consume", "Movies", "Friday Night", "[one line]", None, "#"),
  ("Catalog + Consume", "Movies", "1% Club", "A family game-show night.", None, "#"),
  ("Catalog + Consume", "Movies", "VidAngel", "[one line]", None, "#"),
  ("Catalog + Consume", "Movies", "Saturday Afternoon", "[one line]", None, "#"),
  ("Catalog + Consume", "CourseTube", "AI + CS course viewer", "[one line]", None, "#"),
  ("Catalog + Consume", "CourseTube", "Course KG viewer", "A course as a map of its concepts.", None, "#"),
  ("Catalog + Consume", "CourseTube", "Lecture summaries", "[one line]", None, "#"),
  ("Catalog + Consume", "CourseTube", "Textbooks viewer", "[one line]", None, "#"),
  ("Catalog + Consume", "CourseTube", "Book KG viewer", "A book as a graph of its concepts.", None, "#"),

  ("MetaMatx Learning", "Codecrafters style", "Code in Place", "[one line]", None, "#"),
  ("MetaMatx Learning", "Codecrafters style", "AI", "[one line]", None, "#"),
  ("MetaMatx Learning", "AoPS / Math Academy style", "Math", "[one line]", None, "#"),
  ("MetaMatx Learning", "AoPS / Math Academy style", "AI", "[one line]", None, "#"),
  ("MetaMatx Learning", "AoPS / Math Academy style", "Lean: thusproved.com", "[one line]", None, "#"),
  ("MetaMatx Learning", "AoPS / Math Academy style", "Physics", "[one line]", None, "#"),
  ("MetaMatx Learning", "AoPS / Math Academy style", "Chemistry", "[one line]", None, "#"),
  ("MetaMatx Learning", "Articulate & Sana style", "YC", "[one line]", None, "#"),
  ("MetaMatx Learning", "Articulate & Sana style", "The Academy", "[one line]", None, "#"),
  ("MetaMatx Learning", "More", "LexiGraf", "Spelling and vocabulary, by word family.", None, "#"),
  ("MetaMatx Learning", "More", "Timelines: AI", "[one line]", None, "#"),
  ("MetaMatx Learning", "More", "Manim-style videos: LexiGraf", "[one line]", None, "#"),
]

e = html.escape
out, cat, sub = [], None, object()
def close():
    if out and out[-1] != "OPEN": out.append("  </section>")
for c, s, t, line, cover, href in P:
    if c != cat:
        if cat is not None: out.append("  </section>")
        out.append(f'  <h2 class="row head" id="{e(c.lower().replace(" ", "-").replace("+", "and"))}">{e(c)}</h2>')
        cat, sub = c, object()
        if s is None: out.append('  <section class="row tiles">')
    if s != sub:
        if s is not None:
            if out[-1].startswith("    <a"): out.append("  </section>")
            out.append(f'  <h3 class="row subhead">{e(s)}</h3>')
            out.append('  <section class="row tiles">')
        sub = s
    media = (f'<span class="media {cover}" role="img" aria-label="{e(t)}"></span>' if cover
             else '<span class="media todo">[cover image or clip]</span>')
    wide = " wide" if cover == "fig-dcp" else ""
    out.append(f'    <a class="tile{wide}" href="{href}">{media}<span class="label"><b>{e(t)}</b><span>{e(line)}</span></span></a>')
out.append("  </section>")

page = pathlib.Path(__file__).with_name("c3-home.html")
src = page.read_text()
start, end = src.index("  <h2 class=\"row head\""), src.index("  <footer")
page.write_text(src[:start] + "\n".join(out) + "\n\n" + src[end:])
print(len(P), "projects")
