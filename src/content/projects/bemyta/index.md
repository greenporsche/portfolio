---
published: true
title: "BeMyTA"
category: "Software I built"
order: 11.5
summary: "A free, interactive map of Stanford's math, computer science and AI courses, for anyone studying them on their own."
lede: "Pick a subject and Stanford's courses are laid out as learning routes, from first courses to advanced ones. Click a course to see what it needs, what it leads to, when it runs, who teaches it and where to find its free lectures."
cover: ./cover.png
coverAlt: "The BeMyTA AI map in dark mode. CS229 Machine Learning is selected in its learning route between CS221 and CS230, with lines to the courses before and after it. The side panel shows CS229 / STATS229, its Winter and Spring 2027 terms and teachers, its place in the route, links to lecture recordings and cs229.stanford.edu, and its catalogue facts."
caption: "The live site at bemyta.com with CS229 Machine Learning selected on the AI map. Screenshot in headless Chromium, 1280 × 860 at 2×."
when: "November 2026"
builtWith: "JavaScript, React, React Flow, Vite, Python, Vercel"
links:
  - label: "Open the map (bemyta.com)"
    href: "https://bemyta.com/stanford/"
  - label: "Code"
    href: "https://github.com/greenporsche/BeMyTA"
---

## What you can do with it

- **Find where to start.** Each subject (mathematics, computer science or artificial intelligence) is a set of learning routes, read left to right. A course's preparation is shown before you take it.
- **Check what a course needs.** Every prerequisite says where it comes from: the Stanford catalogue, a course website or a department page.
- **Learn for free.** 📺 marks courses with free recorded lectures, and 🌐 marks a public course site or materials.
- **See when it runs and who teaches it.** Recorded terms and teachers are shown, this year and in past years, where available. They come from Explore Courses, Stanford's catalogue.
- **Search** for a course by name, number or teacher.

It's free, needs no account and works on a phone.

## How I built it

The course data is a hand-compiled atlas: one Markdown note per subject plus a course graph, built from Stanford's public course pages. The wording says how strong each placement is. "Requires" means a stated prerequisite, "placed by recommended preparation" means only recommended courses are named, and "suggested after" is a judgement with its reasoning given.

Python scripts read Explore Courses to add each course's terms, teachers and offering history. Only trimmed facts reach the public site. A check after every build fails it if any development-only data slips into the output.

The map itself is a static site built with Vite, React and React Flow. Vercel rebuilds it on every push.

## Where it stands

The Stanford course map is live. The larger goal, stated in the README, is a personal teaching assistant that helps you understand course content, work through misconceptions and apply what you learn. That part is still being built.

BeMyTA is an independent project, not affiliated with or endorsed by the schools whose courses it covers.
