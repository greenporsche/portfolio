---
title: Directional Collision Principle
category: Research
order: 1
wide: true
summary: Predicting which neural-network inputs are vulnerable to attack. 87.5% accuracy, 100% recall.
lede: A geometric theory that predicts which neural-network inputs are vulnerable to adversarial attack, validated on OpenAI's sparse circuits.
cover: ./cover.png
coverAlt: Before-and-after points for each successful attack. Every one crosses the decision boundary at g(v) = 0.
caption: Every successful attack crosses the boundary g(v) = 0. Attacks pushing the other way never succeed. From symmetry_visualization.py.
stats:
  - value: 87.5%
    label: accuracy predicting vulnerable inputs before attacking
  - value: 100%
    label: recall, no vulnerable input missed
  - value: 15.5×
    label: more efficient than random perturbations
when: 2025–2026. Science fair entry, January 2026
builtWith: Python 3.11, uv, OpenAI sparse circuits
links:
  - label: Code and data
    href: https://github.com/greenporsche/Directional-Collision-Principle
---

## Why I built it

<mark>[In Sisi's own words: what made him ask why some inputs break a network and others don't, and what he wanted to find out.]</mark>

## How I built it

I combined Lipschitz continuity bounds with the symmetry structure of sparse circuits. That gives a lower bound on how far an input sits from the decision boundary, and a per-family "directional budget" that says which way an attack has to push.

Then I tested the predictions on OpenAI's interpretable sparse circuits, on two independent tasks: bracket matching (estimated L ≈ 3.04) and quote matching (L ≈ 1.35). I predicted which inputs were vulnerable first and attacked second.

<figure>

![Bar chart of attack success rate by strategy: random baseline 1.6%, combined circuit-informed attack 24.2%.](./attack-strategies.png)

<figcaption>Circuit-informed attacks against a random baseline. The combined strategy succeeds 24.2% of the time against 1.6% for random.</figcaption>
</figure>

## The hard part

<mark>[What didn't work at first, and what he changed.]</mark>

## What I did

- The theory: the distance bound and the directional budget. The underlying collision result is its own short note.
- All of the experiment code, data and figures in the repo.
- The paper and the presentation. <mark>[confirm, and name any mentor]</mark>

## Where it stands

The code and data are public. <mark>[Next step, in his words.]</mark>
