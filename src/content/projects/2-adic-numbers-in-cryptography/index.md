---
published: true
title: "2-adic Numbers in Cryptography"
category: "Research"
order: 6
summary: "Expository paper on how 2-adic numbers describe a keystream generator for stream ciphers."
lede: "An expository paper on a keystream generator that keeps track of its carries, and why reading its output as a 2-adic number shows it is always a fraction p/q."
cover: ./cover.png
coverAlt: "A presentation slide titled 'The connection integer'. It defines q = −1 + q₁2 + q₂2² + ⋯ + q_r2^r, notes that q is usually taken positive and so is odd, and states the main theorem in a shaded box: the 2-adic number α = a₀ + a₁2 + a₂2² + ⋯ made from the output of an FCSR with connection integer q equals p/q in ℤ₂ for some integer p."
caption: "The main theorem as I presented it. Slide 8 of my presentation, with the slide number cropped off. In the paper it is Theorem 6.1, on page 4."
stats:
  - value: "9"
    label: "pages"
  - value: "15"
    label: "presentation slides"
  - value: "1"
    label: "theorem, proved in full"
when: "Spring 2026. Final project for Euler Circle's p-adic Analysis course, dated May 2026"
builtWith: "LaTeX"
links:
  - label: "Read the paper (PDF)"
    href: "https://github.com/greenporsche/euler-circle/blob/main/6.%20p-adic-analysis/p-adic%20Cryptography/p-adic%20Cryptography.pdf"
  - label: "Presentation slides (PDF)"
    href: "https://github.com/greenporsche/euler-circle/blob/main/6.%20p-adic-analysis/p-adic%20Cryptography%20Presentation/p-adic%20Cryptography%20Presentation.pdf"
  - label: "Euler Circle p-adic Analysis course"
    href: "https://eulercircle.com/classes/p-adic-analysis/"
---

## Why I built it

This paper was my final project for the p-adic Analysis course at Euler Circle in spring 2026. <mark>[In Sisi's own words: why he picked cryptography as the application of p-adic numbers.]</mark>

## How I built it

The paper is expository. It explains a known connection and proves nothing new. It starts with a secret message and ends with an attack.

**Stream ciphers.** Alice writes her message as bits P₀, P₁, P₂, …. She and Bob share a keystream of bits K₀, K₁, K₂, …. She sends Cᵢ = Pᵢ + Kᵢ (mod 2), and Bob adds Kᵢ again to get Pᵢ back. So the whole problem is the keystream: Alice and Bob must make the same one, and Eve must not be able to predict it.

**2-adic integers.** A 2-adic integer is an infinite sum a₀ + a₁·2 + a₂·2² + a₃·2³ + ⋯, where each aᵢ is 0 or 1. In the 2-adic way of measuring size, a number divisible by a high power of 2 is small. So the terms shrink and the sum converges. That means any infinite bit string is one 2-adic number. Two examples:

- 1111… = 1 + 2 + 4 + 8 + ⋯ = −1. This matches how computers store −1.
- 1010… = 1 + 4 + 16 + ⋯ = 1/(1 − 4) = −1/3.

**Linear shift registers.** A shift register stores a few bits and makes each new bit from the old ones. The usual kind, the linear feedback shift register (LFSR), uses a rule like aₙ₊₃ = aₙ₊₁ + aₙ (mod 2). LFSRs are fast and simple and give long periods. But the rule is linear, so if Eve sees enough output she can recover it and predict every future bit.

**Shift registers with carry.** A feedback with carry shift register (FCSR) adds the chosen bits as ordinary integers, plus a stored carry m:

σₙ = q₁aₙ₋₁ + q₂aₙ₋₂ + ⋯ + q_r aₙ₋ᵣ + mₙ₋₁.

The new bit is aₙ = σₙ mod 2, and the new carry is mₙ = (σₙ − aₙ)/2. In an LFSR, 1 + 1 = 0 and the extra 1 is lost. In an FCSR, 1 + 1 gives output 0 and carry 1. The taps define the connection integer q = −1 + q₁·2 + q₂·2² + ⋯ + q_r·2ʳ.

**The main theorem.** Read the output as a 2-adic number α = a₀ + a₁·2 + a₂·2² + ⋯. Then α = p/q for some integer p, where q is the connection integer. I prove it in full. Substitute the FCSR rule into the tail of α. The bit terms re-index into (q + 1)·α minus a few finite pieces. The carry terms telescope: every one cancels except mᵣ₋₁·2ʳ, because mₙ·2ⁿ⁺¹ goes to 0 in the 2-adic sense. What is left is q·α = p, with p an ordinary integer built from the starting bits and the starting carry.

**An example.** Take q = 5. Then q + 1 = 6 = 2 + 4, so the register taps the last two bits. Start with bits 1, 1 and carry 0. The output is 11001100…, and as a 2-adic number that is (1 + 2)(1 + 16 + 16² + ⋯) = 3 · (−1/15) = −1/5. The denominator is 5, as the theorem says.

**What it means for security.** The carry makes the rule nonlinear, which is why someone might pick an FCSR over an LFSR. But the theorem shows the output is still a simple fraction. If Eve sees the first N bits, she knows α mod 2ᴺ, and she can look for a small fraction p/q that matches. The paper describes the 2-adic span, which measures the smallest FCSR that makes a given sequence. I cite Klapper and Goresky, who showed that a 2-adic rational approximation method can rebuild that smallest FCSR from a limited number of bits, depending on the 2-adic span.

## What I did

- I wrote the paper and typeset it in LaTeX. The title page lists only me.
- I wrote out the full proof of the main theorem and worked the example with connection integer 5.
- I made a 15-slide presentation on the paper, "From carries to stream ciphers", and gave it. It walks through the proof idea and the q = 5 example step by step, with a table of each sum, output bit and carry. <mark>[When and to whom he presented it.]</mark>
- I cite Klapper and Goresky's "2-adic Shift Registers" for the 2-adic span and the attack.

## Where it stands

The paper and the slides are finished and public in my Euler Circle repo. The paper explains the rational approximation attack in words. It does not carry one out. <mark>[Anything Sisi wants to add about next steps, in his words.]</mark>
