# Restart handoff: 2026-11-01

Room 78 ("portfolio"), board plan 47. PM: claude. EM and verifier: codex. PO: kiku.

## Where things stand

- **Goal:** Siddharth Krishna's (Sisi) portfolio for The Academy's early deadline, **Thu 2026-11-05**. The site must be live and link-checked by **Tue 11-03**.
- **Design:** direction C, third pass, approved by kiku (#46622). `DESIGN.md` lints with 0 errors. Tokens are in `src/styles/tokens.css`, and the lookbook is at `/lookbook/`.
- **Stack (EM ruling #46624):** Astro 7.3.8, TypeScript and plain CSS, built as a static site. There is one content collection, `src/content/projects/<slug>/index.md`, with its media beside it. It drives both the home tiles (`src/pages/index.astro`) and `/projects/<slug>/` (`src/pages/projects/[id].astro`). Category order is in `src/data/categories.ts`.
- **Repo move:** kiku moved the repo to this folder to fix git identity (#46778). The new repo has none of the old history (`3bc955c`, `cecf208`, `affddaf` no longer exist). The fresh starting commit is `2542f19` on `main`, authored as greenporsche.
- **S1.1 working slice:** the home page with the Directional Collision tile, plus that tile's full project page. Evidence is in `design/evidence/s1.1/`. Codex verified `2542f19` (#46783): the build passes, all local links resolve, and `ui:check` is clean (CSS only). Still missing for proven: codex's desktop/phone navigation check, which only a non-author can log. The preview deploy moved to S1.3.
- **S1.2 full inventory:** branch `slice/s1.2-full-inventory`. All 41 projects are entries in the content collection, generated from `design/directions/gen_home.py`. Every tile reaches its own page (43 pages built). Covers and copy are placeholders until kiku and Sisi supply them. Evidence is in `design/evidence/s1.2/`.
- **Permissions:** a local git repo only. **Do not push to GitHub or deploy** until kiku says so (#46630).

## Commands

    bun install
    ASTRO_TELEMETRY_DISABLED=1 bun --bun astro build    # Node is not installed; Bun runs Astro
    python3 -m http.server 4329 --directory dist        # local preview
    bun run ui:check                                    # design-token check (scans CSS; .astro is not scanned)

Telemetry must be off, because Astro otherwise writes to ~/Library/Preferences, which the sandbox blocks. Headless Chrome screenshots need `--no-sandbox --user-data-dir=<scratch>`, and it renders no narrower than 500px, so phone views are rendered inside 390px iframes.

## Next

1. **S1.1 and S1.2 are proven and merged.** `main` is at `ebe7679`, with all 41 projects, review fixes and reflow fix (codex-verified).
2. **Content (current work):** as Sisi's words and media arrive, put them into each `src/content/projects/<slug>/` (the cover goes beside `index.md`). Never write his sections for him.
3. **S1.3 is deferred by kiku (#46799):** the site stays local until kiku says it's content complete and polished, and picks hosting (S2.1). Then: Pages workflow, deploy, public URL and link checks, and the review re-run over the final content. Codex's checks so far cover build, navigation, keyboard, reflow and focus. They are not a publication-readiness or full accessibility sign-off; screen-reader output is unverified.

## Waiting on kiku and Sisi (board F2)

- Where the site lives: replace greenporsche.github.io, or use siddharthkrishna.com.
- Live URLs or repos for each project, used to capture covers automatically.
- Clips and photos: F1 explorer, Assetto Corsa, the apps, the sim rig.
- Sisi's own words: the intro lines, and "Why I built it" for his top 3 projects. The Academy FAQ says no AI writing, so **leave the `<mark>[...]</mark>` placeholders for him**.
