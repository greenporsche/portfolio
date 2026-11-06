---
published: true
title: "This site"
category: "Utils"
order: 8
summary: "The portfolio itself, and how it was made."
lede: "A static site that puts my projects in one place. AI coding agents designed and built it. A person chose the design."
cover: ./cover.png
coverAlt: "Four home-page mockups side by side: a cream notebook design with a serif headline, a dark design with a large sans-serif slogan, a beige brutalist design with heavy black type and a green italic word, and the final white design with the name in huge black capitals above black section bands and a grid of tiles."
caption: "The design directions, left to right: A (lab notebook), B (pit wall), C (brutalist, first pass), and the third pass of C that the site now uses."
stats:
  - value: "41"
    label: "projects in the source, released one at a time"
  - value: "3"
    label: "design directions tried"
  - value: "3"
    label: "passes on the one chosen"
when: "November 2026"
builtWith: "Astro 7, TypeScript, plain CSS, Bun"
---

## Why I built it

I'm applying to The Academy. I wanted one place that shows each project and says plainly what I did on it. The early deadline set the schedule.

## How I built it

I planned and built the site by directing AI coding agents. One agent wrote the code. A second agent reviewed it, and work only counted as done once that second agent had checked it.

The agents first built three different design directions as mockups: a lab notebook, a racing "pit wall," and a brutalist one. Direction C was picked. It went through two more passes before the structure was approved.

The final design is written down in one file. It uses one typeface (Archivo), five colors and square corners. Links are British racing green, a nod to my handle "greenporsche."

The site is built with Astro as a static site, with plain CSS. Each project is one Markdown file in a single content collection. That one collection drives both the tiles on the home page and each project's own page. The first list of projects came from a small script that also generated the home mockup.

## The hard part

The first passes looked AI-generated. The first version of direction C had a slogan with one italic word, counter boxes ("2×", "30+"), a scrolling ticker, status badges, "01 / 02" section numbers, small letter-spaced labels and a cream background. All of those were cut. The design file now lists them as things the site must not have. What's left is black rules, heavy type, plain sentences, and my own figures and papers as the only images.

The second problem showed up in review. When a reader turned up their browser's text size, the grid columns would not shrink and long words pushed past the edge of the page. The fix was to let the columns shrink, let long words wrap, and let the breadcrumb row wrap. The same review added a visible focus ring, a main landmark, clearer names for the tile links, a 65-character line length, and type sizes in rem so the reader's text setting applies.

## What I did

- Directed the agents and picked the design.
- Reviewed the pages and asked for changes.

## Where it stands

The site runs locally and is not published yet. All 41 projects are in the source. Each one goes live once its page is finished, and the rest stay hidden until then. The agent checks so far cover the build, navigation, keyboard use, reflow and focus. That is not a full accessibility review. Screen-reader output has not been checked. The next step is to finish the content, then choose where to host it.
