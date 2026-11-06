---
published: true
title: "A Quantitative Collision Principle"
category: "Research"
order: 2
summary: "A short proof: how far a point must sit from its symmetry-forced zero set."
lede: A three-page note on odd Lipschitz functions. It is the math under my Directional Collision Principle project.
cover: ./cover.png
coverAlt: "Theorem 4.3 from the note: dist(v, Z) is at least |A(v) − A(τ(v))| divided by L(1 + K), followed by its proof."
caption: Theorem 4.3 and its proof, cropped from page 3 of the note.
stats:
  - value: "3"
    label: pages, written as a standalone math note
  - value: "2"
    label: "theorems: a zero must exist, and how far away it must be"
  - value: "K = 1"
    label: for the logit swap used in the follow-up paper
when: January 2026
builtWith: LaTeX
links:
  - label: The note (PDF)
    href: https://github.com/greenporsche/Directional-Collision-Principle/blob/main/research/%CF%84-Collision%20Short%20Note.pdf
  - label: Project repo
    href: https://github.com/greenporsche/Directional-Collision-Principle
---

## Why I built it

I wanted to know why some inputs to a neural network break under a small change and others don't. A classifier choosing between two answers has a built-in symmetry: swap the two answers and the question is the same. I wanted to see how much that symmetry, plus a limit on how fast the model's output can change, tells you about where the model gets confused.

## How I built it

The setup is a space of points V with a distance d, and a symmetry τ that undoes itself: applying it twice gets you back where you started. Take any score A on the points. Compare the score at a point with the score at its mirror image:

g(v) = A(v) − A(τ(v))

This gap flips sign under the symmetry: g(τ(v)) = −g(v). The points where the gap is zero, where a point and its mirror score the same, I call the collision set Z.

The note proves two things.

**A collision has to exist.** If you can walk continuously from any point to its mirror image, the gap starts at g(v) and ends at −g(v). So it crosses zero somewhere on the way. That is the intermediate value theorem, and it needs no distance at all (Theorem 3.1).

**A point with a big gap is far from every collision.** Suppose A can change by at most L per unit of distance, and τ stretches distances by at most a factor K. Then the gap can change by at most L(1 + K) per unit of distance (Lemma 4.2). Precisely, for every point v (Theorem 4.3):

dist(v, Z) ≥ |A(v) − A(τ(v))| / (L(1 + K))

In words: the more lopsided a point is, the farther you have to move it before it can reach a tie. A local version follows. If g changes at most C per unit inside a ball of radius r around v, and r < |g(v)| / C, that ball contains no collision (Corollary 5.1).

The bound only goes one way. It says how close a collision can't be. It never says a collision is nearby. Getting that would take extra assumptions (Section 6).

## The hard part

The proofs are short. Theorem 4.3 is one line once Lemma 4.2 is in place. The hard part was being honest about what that buys you.

The first problem was the bridge to real networks. The note defines τ on an abstract space, and there is no natural symmetry on token sequences that swaps a model's answer. A review of the project flagged this as its most serious gap, before the final paper was written. The fix was to put the symmetry where it is exact. In the model's output space, τ swaps the two logits, (z₁, z₂) → (z₂, z₁). That swap preserves distance, so K = 1, and g becomes the model's margin between its two answers.

The second problem was that the bound is weak in practice. The Lipschitz bound I could certify from the weights of OpenAI's sparse bracket-counting model was about 2.29 × 10¹¹. The value I estimated from experiments was about 3.04. A guarantee built on the certified number is true but very loose. In the follow-up paper I kept the certified and estimated versions separate and labeled them that way.

## What I did

- Wrote the note and its proofs. I am the only author listed.
- Used it as the base of the Directional Collision Principle paper. There, the margin bound becomes a lower bound on how many tokens an attacker has to change to reach a tie. See [Directional Collision Principle](../directional-collision-principle/).

## Where it stands

The note is public in the project repo. The project archive outlines a stronger version that makes the bound local and direction-aware, so that it predicts which way an attack has to push.
