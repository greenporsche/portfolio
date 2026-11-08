---
published: true
title: "QR Studio"
category: "Software I built"
order: 13
summary: "A web page that makes gradient QR codes and saves them as PNG or SVG. Nothing leaves the browser."
lede: "Paste a link, pick a style, and download a QR code with rounded shapes and a colour gradient. It runs in the browser, so the link is never sent anywhere."
cover: ./cover.png
coverAlt: "QR Studio in light mode. A white card holds the link field with https://example.com, four style buttons (Ink, Sunset, Orchid, Grove) with Sunset selected, a closed Customize section, and a QR code of round dots shading from orange to pink with dark red rounded corner squares on a pale peach tile. Below are a gradient Download PNG button and an SVG button."
caption: "The live site at qr.siddharthkrishna.com with its default Sunset style and sample link. Screenshot in headless Chromium, 1280 × 860 at 2×."
stats:
  - value: "4"
    label: "ready-made styles, each one line of code"
  - value: "6 × 3"
    label: "dot shapes by corner shapes to mix"
  - value: "1120 px"
    label: "square PNG export, or SVG at any size"
when: "October 2026"
builtWith: "TypeScript, Vite, qr-code-styling, GitHub Actions, GitHub Pages"
links:
  - label: "Make a code (qr.siddharthkrishna.com)"
    href: "https://qr.siddharthkrishna.com/"
  - label: "Code"
    href: "https://github.com/greenporsche/qr-studio"
---

## Why I built it

<mark>In my own words: what I needed a nicer QR code for.</mark>

## How I built it

It is one page built with Vite and TypeScript. The library qr-code-styling draws the code as SVG. Every code uses error-correction level H, the highest of the four.

There are four ready-made styles: Ink, Sunset, Orchid and Grove. Each is one line in `src/styles.ts`: a name, a dot shape, a corner shape and two colours. Everything else comes from those two colours. The pale tile behind the code is the first colour mixed almost all the way to white. The corner squares are the midpoint of the two colours, darkened. In dark mode the dots are lightened and the tile turns near-black. The page's own accent colours follow the chosen style too.

Under Customize you can change the dot shape (six choices), the corner shape (three), both ends of the gradient and the corner colour. Downloads come from a copy drawn four times larger than the preview: a 1120 × 1120 px PNG, or an SVG.

No link is sent to a server. The code is drawn in the page. A GitHub Actions workflow builds the site on every push and publishes it to GitHub Pages, which serves it at qr.siddharthkrishna.com.

<mark>How the code was written: by me, or by directing an AI coding agent?</mark>

## What I did

- <mark>What I decided: for example the four styles and their colours, deriving the whole look from two colours, and the light and dark modes.</mark>
- Put it online with an automatic deploy to GitHub Pages under my own domain.

## Where it stands

It is live and free to use, with no sign-up. The README warns that decorative codes are a little less robust than plain ones. Very pale gradients can fail to scan, and some scanners can't read the light-on-dark codes from dark mode, so it says to test-scan before printing. <mark>Anything planned next?</mark>
