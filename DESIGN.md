---
version: alpha
name: Siddharth Krishna Portfolio
description: Artful brutalist portfolio. Ruled black grid, heavy condensed type, his own work as the imagery.
colors:
  primary: "#000000"
  secondary: "#555555"
  tertiary: "#1E5B3A"
  neutral: "#FFFFFF"
  wash: "#F0F0EC"
typography:
  display:
    fontFamily: Archivo
    fontSize: 168px
    fontWeight: 900
    lineHeight: 0.84
    letterSpacing: -0.02em
  display-project:
    fontFamily: Archivo
    fontSize: 120px
    fontWeight: 900
    lineHeight: 0.86
    letterSpacing: -0.02em
  section:
    fontFamily: Archivo
    fontSize: 28px
    fontWeight: 800
    lineHeight: 1.2
  title-lg:
    fontFamily: Archivo
    fontSize: 30px
    fontWeight: 800
    lineHeight: 1
  title-md:
    fontFamily: Archivo
    fontSize: 26px
    fontWeight: 800
    lineHeight: 1
  subsection:
    fontFamily: Archivo
    fontSize: 16px
    fontWeight: 800
    lineHeight: 1.4
  stat:
    fontFamily: Archivo
    fontSize: 30px
    fontWeight: 800
    lineHeight: 1
  lede:
    fontFamily: Archivo
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.45
  body:
    fontFamily: Archivo
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.5
  body-sm:
    fontFamily: Archivo
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
  caption:
    fontFamily: Archivo
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.45
rounded:
  none: 0px
spacing:
  xs: 4px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 24px
  2xl: 32px
  3xl: 48px
  4xl: 80px
  rule: 2px
  hairline: 1px
  measure: 680px
  page-max: 1360px
  side-column: 260px
components:
  section-head:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.neutral}"
    typography: "{typography.section}"
    padding: "{spacing.md} {spacing.xl}"
  subsection-head:
    backgroundColor: "{colors.wash}"
    textColor: "{colors.primary}"
    typography: "{typography.subsection}"
    padding: "{spacing.sm} {spacing.xl}"
  tile:
    backgroundColor: "{colors.neutral}"
    textColor: "{colors.primary}"
    rounded: "{rounded.none}"
  tile-media-empty:
    backgroundColor: "{colors.wash}"
    textColor: "{colors.secondary}"
    typography: "{typography.caption}"
  link:
    textColor: "{colors.tertiary}"
---

# Siddharth Krishna Portfolio

Approved by kiku (PO) on 2026-11-01: "this structure seems nice" (room 78, #46622), after picking direction C (#46603) and asking that it not read as AI-generated. Source mocks: `design/directions/c3-home.html` and `c3-project.html`.

## Overview

A portfolio for a high-school senior who builds things and proves why they work. It should feel bold and youthful, built with a professional's discipline. The structure is visible: black rules, a heavy condensed display face, plain facts. His own figures, papers and screen recordings are the only imagery, and they get the largest area on every page.

What it must not look like (kiku: "reads AI generated"): no slogans with one italic word, no counter strips ("2×", "30+"), no dot-and-pill status badges, no tiny letter-spaced monospace labels, no "01 / 02" section numbers, no tickers, no cream "paper" backgrounds, no identical boxed cards. Words are plain and factual, and Sisi writes the personal ones.

## Colors

- **Primary (#000000):** ink for all text, every rule and the section bands.
- **Secondary (#555555):** one-line descriptions, captions and supporting text. 7.5:1 on white.
- **Tertiary (#1E5B3A):** British racing green, a nod to his handle "greenporsche". Used only for links. 8.6:1 on white.
- **Neutral (#FFFFFF):** the page.
- **Wash (#F0F0EC):** empty media slots, subsection bands, and placeholder text waiting for Sisi's words.

Dark mode: not in v1. The page is black on white by design. Revisit only if the PO asks.

## Typography

One family, **Archivo** (variable, with a width axis), from Google Fonts.

- **Display** (his name, project titles): weight 900, width 68%, uppercase. Fluid: the home name runs from 56px to 168px and project titles from 48px to 120px, scaling with the viewport.
- **Section** bands and **titles** (tile and project-section headings): weight 800, width 75–80%, uppercase.
- **Body**: weight 400 at normal width, 18px, set in sentence case. Long text is capped at the 680px measure.
- **Captions**: 14px, secondary color.

Uppercase is for display and headings only. Never use letter-spaced small caps labels.

## Layout

- The page is a single 1360px-wide column framed by 2px black rules on the left and right, and every block ends with a 2px rule.
- **Home:** the name block, then for each category a black **section band**, optional wash **subsection bands**, and a three-column grid of **tiles** (one column on phones). A lead project can span two columns.
- **Project page:** breadcrumb row, title block, full-width media with a caption, then a 260px **side column** (headline numbers, when, built with, links) beside the prose (Why I built it, How I built it, The hard part, What I did, Where it stands). Previous and next links come last. On phones the side column becomes a 2×2 grid above the prose.
- Spacing comes from the scale: 4, 8, 12, 16, 24, 32, 48, 80.

## Elevation & Depth

Flat. Hierarchy comes from 2px rules, black section bands and type weight. No shadows.

## Shapes

Square corners everywhere. The only shape is the rule.

## Components

- **Tile:** the whole tile is one link. Media on top: a cover image, or a poster for a video. Below it, the title (title-md) and one line (body-sm, secondary). On hover or focus the title underlines with a 3px line, and focus also gets a 3px green outline.
- **Empty media slot:** wash background with a short bracketed note saying what goes there. Used until real media arrives, never as decoration.
- **Section band / subsection band:** see the tokens.
- **Project prose:** headings in the title-lg style, body text at the measure, figures framed by a 2px rule with a caption under a rule.

## Do's and Don'ts

- Do make the work the biggest thing on the page.
- Do say plainly what Sisi did on each project.
- Do leave Sisi's own words as visible placeholders until he writes them. The Academy asks for them in his words.
- Don't add slogans, counters, badges, numbered sections or tickers.
- Don't use rounded corners, shadows or gradients.
- Don't use a color other than the five tokens.
