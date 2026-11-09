---
published: true
title: "Generating Functions Paper Summary"
category: "Research"
order: 7
summary: "Proposal for an expository paper on how many children the root of a large random tree has."
lede: "A two-page proposal, not a finished paper. It sets out what I plan to show about the root of a large random tree, for two kinds of tree, and how one framework covers both."
cover: ./cover.png
coverAlt: "Text and formulas from page 1 of the summary. It says 'I'll show that' for a uniformly random plane tree with n vertices, the probability that the root has k children tends to k over 2 to the k plus 1. It then gives T(z) = z e^T(z) for Cayley trees and says 'I will show' that their limit is e to the minus 1 over (k − 1) factorial."
caption: "The two limits the summary plans to prove, cropped from page 1. They are stated as goals, not yet proved."
stats:
  - value: "2"
    label: "pages"
  - value: "2"
    label: "kinds of tree compared"
when: "Fall 2026. Summary for Euler Circle's Generating Functions course, dated October 2026. The course is still in progress"
builtWith: "LaTeX"
links:
  - label: "Read the summary (PDF)"
    href: "https://github.com/greenporsche/euler-circle/blob/main/7.%20generating-functions/Paper%20Summary/Paper%20Summary.pdf"
  - label: "Euler Circle Generating Functions course"
    href: "https://eulercircle.com/classes/generating-functions/"
---

## Why I built it

I wrote this summary for the Generating Functions course at Euler Circle in October 2026. It previews the expository paper I will write for the course.

## How I built it

The summary is a plan. It says what the paper will show and how. Nothing in it is proved yet, and the results it aims at are known ones.

**The question.** Pick a tree with n vertices uniformly at random. How many children does its root have? As n grows, the answer settles into a fixed probability distribution. The summary compares that distribution for two kinds of tree.

**Plane trees.** In a plane tree, the children of each vertex come in a set order. A generating function packs all the counts into one power series T(z). For plane trees it satisfies

T(z) = z / (1 − T(z)).

Adding a second variable u to count the root's children gives T(z, u) = z / (1 − u·T(z)). From that, I plan to show that if Xₙ is the root degree of a random plane tree with n vertices, then for each fixed k ≥ 1,

lim P(Xₙ = k) = k / 2^(k+1), as n → ∞.

**Cayley trees.** In a Cayley tree the vertices are labelled and the children are not ordered. Its exponential generating function satisfies T(z) = z·e^(T(z)), and marking the root degree gives T(z, u) = z·e^(u·T(z)). Here I plan to show

lim P(Xₙ = k) = e⁻¹ / (k − 1)!, as n → ∞.

**One framework for both.** The paper will end with Flajolet and Sedgewick's simply generated trees. These are tree classes with T(z) = z·Φ(T(z)) for some function Φ. They show that, under certain conditions, the root degree in the limit has probability generating function

P(u) = u·Φ′(τu) / Φ′(τ), where τ solves Φ(τ) = τ·Φ′(τ).

I plan to show how this one formula gives back both limits above. Flajolet and Sedgewick's book is the main reference.

## What I did

- I wrote the two-page summary and typeset it in LaTeX.

## Where it stands

This is a proposal. The summary states the goals, and none of the proofs are written yet. The full paper is not in my repo. The course itself is still running this fall.
