---
published: true
title: "Dobinski's Formula"
category: "Research"
order: 5
summary: "Expository paper on Dobinski's formula for the Bell numbers, proved two ways."
lede: "An expository paper on a formula that counts the ways to split up a set using an infinite series with e in it, proved two ways and read as a fact about probability."
cover: ./cover.png
coverAlt: "Dobinski's formula, typeset in LaTeX: B sub n equals one over e times the sum, from k equals 0 to infinity, of k to the n over k factorial."
caption: "Dobinski's formula as stated in Theorem 3.1, cropped from page 3 of the paper."
stats:
  - value: "8"
    label: "pages"
  - value: "2"
    label: "proofs of the same formula"
when: "Winter 2026. Expository paper for Euler Circle's Infinite Series course, January to March 2026"
builtWith: "LaTeX"
links:
  - label: "Read the paper (PDF)"
    href: "https://github.com/greenporsche/euler-circle/blob/main/5.%20infinite%20series/Dobinski%27s%20Formula/Dobinski%27s%20Formula.pdf"
  - label: "Euler Circle Infinite Series course"
    href: "https://eulercircle.com/classes/infinite-series/"
---

## Why I built it

I wrote this paper for the Infinite Series course at Euler Circle in winter 2026. <mark>[In Sisi's own words: why he picked Dobinski's formula, and whether it was the course's final project.]</mark>

## How I built it

The paper is expository. It explains a known result and proves nothing new. It goes from counting, to series, to probability.

**Bell numbers.** The Bell number Bₙ counts the ways to split a set of n things into nonempty groups. The set {1, 2, 3} can be split 5 ways, so B₃ = 5. The sequence starts 1, 1, 2, 5, 15, 52. The Stirling number S(n, j) counts the splits into exactly j groups, so Bₙ is the sum of S(n, j) over all j.

**The formula.** G. Dobinski found this identity in 1877:

Bₙ = (1/e) · Σ kⁿ / k!, summed over k = 0, 1, 2, …

The left side counts finite objects. The right side is an infinite series with e in it. They are equal for every n, so the series always comes out to a whole number. Before proving anything, I check that the series converges. The ratio of consecutive terms is (1 + 1/k)ⁿ / (k + 1), which goes to 0, so the ratio test applies.

**First proof: a generating function.** An exponential generating function packs a sequence a₀, a₁, a₂, … into one power series, Σ aₙ xⁿ / n!. For the Bell numbers it is e^(eˣ − 1). I cite this from Stanley and sketch why: a nonempty group has generating function eˣ − 1, and a split is a set of such groups. Then I expand. Write e^(eˣ − 1) as e⁻¹ · Σ e^(kx) / k!, expand each e^(kx) as a power series, and swap the two sums. That is allowed because the double sum converges absolutely. Matching the coefficients of xⁿ / n! on both sides gives the formula.

**Second proof: counting functions.** There are kⁿ functions from a set of n things to a set of k labels. Each function splits the n things into groups, by which label they get. Going the other way, a split into j groups can be labeled in k(k − 1)⋯(k − j + 1) ways. So

kⁿ = Σ S(n, j) · k(k − 1)⋯(k − j + 1), summed over j.

Divide by k! and add over all k. For each j, the sum over k collapses to 1 + 1 + 1/2! + 1/3! + ⋯ = e. The e cancels the 1/e, and what remains is the sum of S(n, j) over j, which is Bₙ.

**A probability reading.** A Poisson random variable X with mean 1 takes the value k with probability e⁻¹ / k!. Its n-th moment is E[Xⁿ] = Σ kⁿ · e⁻¹ / k!. That is exactly the right side of Dobinski's formula. So Bₙ = E[Xⁿ]: the Bell numbers are the moments of a Poisson(1) variable.

**Estimating by sampling.** The last section uses that reading to approximate Bₙ without summing the series. Draw m independent Poisson(1) samples X₁, …, Xₘ and average their n-th powers:

B̂ₙ = (1/m) · Σ Xᵢⁿ.

I show this estimator is unbiased: its expected value is exactly Bₙ. The paper connects this to a general idea in statistics and machine learning: write a hard sum as an expectation, then estimate it with random samples.

## What I did

- I wrote the paper and typeset it in LaTeX. The title page lists only me.
- I wrote out the convergence check, both proofs, the Poisson reading, and the proof that the sampling estimator is unbiased.
- The formula dates to 1877. I cite Stanley's *Enumerative Combinatorics* for the generating function of the Bell numbers.

## Where it stands

The paper is finished and public in my Euler Circle repo. It describes the sampling estimator and proves it is unbiased, but does not run it or measure how many samples it needs. <mark>[Anything Sisi wants to add about next steps, in his words.]</mark>
