---
title: "Hyperplane Arrangements"
category: "Research"
order: 3
summary: "Expository paper connecting hyperplane arrangements to ReLU networks."
lede: "An expository paper on how a few hyperplanes cut space into regions, how to count those regions, and why the linear pieces of a ReLU layer are exactly those regions."
cover: ./cover.png
coverAlt: "Three straight lines that cross pairwise at three points, dividing the plane into seven regions."
caption: "Three lines in general position cut the plane into seven regions. Figure 1 of the paper."
stats:
  - value: "9"
    label: "pages"
  - value: "6"
    label: "worked examples"
when: "Fall 2025. Final project for Euler Circle's Combinatorics course, finished December 2025"
builtWith: "LaTeX"
links:
  - label: "Read the paper (PDF)"
    href: "https://github.com/greenporsche/euler-circle/blob/main/4.%20combinatorics/Hyperplane%20Arrangements.pdf"
  - label: "Euler Circle Combinatorics course"
    href: "https://eulercircle.com/classes/combinatorics/"
---

## Why I built it

This paper was my final project for the Combinatorics course at Euler Circle in fall 2025.

## How I built it

The paper is expository. It explains known results and proves nothing new. It moves from the geometry to the counting, then to neural networks.

**Regions.** A hyperplane in ℝᵈ is the set of points where w · x + b = 0. A finite collection of them is an arrangement. Remove the hyperplanes and the space falls apart into pieces called regions. Two crossing lines make 4 regions. Three lines in general position make 7.

**Sign patterns.** For each hyperplane, a point is on the + side, the − side, or on it (0). Two points are in the same region exactly when their signs agree for every hyperplane. Choosing >, = or < for each hyperplane gives the faces of the arrangement. Regions are the faces with no equalities.

**Counting.** Intersect hyperplanes in every possible way and you get the flats. Ordered by reverse inclusion, they form the intersection poset. Its Möbius function μ gives the characteristic polynomial:

χ(t) = Σ μ(ℝᵈ, X) · t^dim(X), summed over all flats X.

Zaslavsky's theorem then counts regions from χ alone. If k is the rank of the arrangement, the number of regions is (−1)^k · χ(−1), and the number of bounded regions is (−1)^k · χ(1). For three lines in general position, χ(t) = t² − 3t + 3, and χ(−1) = 7. I sketch the proof idea: delete one hyperplane H, and the count splits as r(A) = r(A without H) + r(A restricted to H). The polynomial satisfies the same recurrence.

**Structure.** The faces form a poset ordered by inclusion, with the regions on top. The sign vectors satisfy the axioms of an oriented matroid. Moving to a neighboring region flips exactly one sign.

**The bridge to ReLU networks.** A ReLU neuron computes max{0, w · x + b}. It switches on or off along the hyperplane w · x + b = 0. A layer of n neurons gives an arrangement of n hyperplanes. Inside each region every neuron's state is fixed, so the layer is linear there. Its linear pieces match the regions one to one, so Zaslavsky's theorem counts them. The sign vectors are the layer's activation patterns, and crossing into a neighboring region flips one neuron.

The paper ends on fragility. A point close to several activation boundaries can cross more than one with a small push. I suggest that adversarial examples may be more likely in such places. That is a heuristic, not a theorem.

## What I did

- I wrote the paper and typeset it in LaTeX. I am its only author.
- I worked the six examples, including the characteristic polynomials for two and three lines in the plane.
- I wrote the final section, which reads a ReLU layer as a hyperplane arrangement.
- The core results are standard. I cite Chen and Wang (MIT PRIMES, 2017) for the characteristic polynomial, and Montúfar et al. (2014) and Hanin and Rolnick (2019) for region counts in deep networks.

## Where it stands

The paper is finished and public in my Euler Circle repo. It covers a single ReLU layer only. It names two next steps: how region counts grow through many layers, and how arrangements relate to robustness.
