# Restart handoff: 2026-11-01

Room 78 ("portfolio"), board plan 47. PM: claude. EM and verifier: codex. PO: kiku.

## Where things stand

- **Goal:** Siddharth Krishna's (Sisi) portfolio for The Academy's early deadline, **Thu 2026-11-05**. The site must be live and link-checked by **Tue 11-03**.
- **Design:** direction C, third pass, approved by kiku (#46622). `DESIGN.md` lints with 0 errors. Tokens are in `src/styles/tokens.css`, and the lookbook is at `/lookbook/`.
- **Stack (EM ruling #46624):** Astro 7.3.8, TypeScript and plain CSS, built as a static site. There is one content collection, `src/content/projects/<slug>/index.md`, with its media beside it. It drives both the home tiles (`src/pages/index.astro`) and `/projects/<slug>/` (`src/pages/projects/[id].astro`). Category order is in `src/data/categories.ts`.
- **S1.1 working slice:** built at `3bc955c`. It has the home page with the Directional Collision tile and the full project page for that tile. Evidence is in `design/evidence/s1.1/`. **Codex verified it independently (#46635):** codex rebuilt the site, checked home, project and lookbook with their local links and media, and reviewed the phone screenshot. `ui:check` is clean, with the CSS-only limit noted. There was no automated click test, because the MCP browser daemon was unavailable. Codex signed off for a local merge, and it is merged to `main`.
- **Permissions:** a local git repo only. **Do not push to GitHub or deploy** until kiku says so (#46630).

## Commands

    bun install
    ASTRO_TELEMETRY_DISABLED=1 bun --bun astro build    # Node is not installed; Bun runs Astro
    python3 -m http.server 4329 --directory dist        # local preview
    bun run ui:check                                    # design-token check (scans CSS; .astro is not scanned)

Telemetry must be off, because Astro otherwise writes to ~/Library/Preferences, which the sandbox blocks. Headless Chrome screenshots need `--no-sandbox --user-data-dir=<scratch>`, and it renders no narrower than 500px, so phone views are rendered inside 390px iframes.

## Next

1. Done: S1.1 verified (codex #46635) and merged to `main`. **The board still shows S1.1 `in_progress`**, because the server refused the move to proven: this MCP session was not tied to the repo (#46636). After the restart with `--cwd <repo>`, attach commit proof (`3bc955c`, merge tip `affddaf`) and let codex mark it proven. No rebuild is needed.
2. **S1.2:** add the other 40 projects from kiku's write-up. Their names, groups and one-liners are already in `design/directions/gen_home.py`, so turn each into a `src/content/projects/<slug>/index.md`.
3. **S1.3:** publish once kiku picks hosting (board S2.1). The first slice proves the Pages workflow when that is authorized (#46628).

## Waiting on kiku and Sisi (board F2)

- Where the site lives: replace greenporsche.github.io, or use siddharthkrishna.com.
- Live URLs or repos for each project, used to capture covers automatically.
- Clips and photos: F1 explorer, Assetto Corsa, the apps, the sim rig.
- Sisi's own words: the intro lines, and "Why I built it" for his top 3 projects. The Academy FAQ says no AI writing, so **leave the `<mark>[...]</mark>` placeholders for him**.
