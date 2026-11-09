---
published: true
title: "USAAIO Training"
category: "Learning"
order: 20
summary: "My study repo for the USA AI Olympiad: the 2025 contest problems worked through, and a 12-unit plan for 2026."
lede: "The repo I kept while training for the USA AI Olympiad. It holds my worked answers to the 2025 contest problems, study notebooks, and a 12-unit study plan with practice sets for 2026."
cover: ./cover.png
coverAlt: "Two heat maps side by side, time t from 0 to 1 across and position x from 0 to 1 up, coloured by temperature from dark purple (0) to yellow (1). Both show the same pattern: hottest at x = 0.5 when t = 0, fading over time and pinned to zero at both edges. Left is the exact solution, right is the neural network's output."
caption: "2025 Round 2, Problem 1: the 1D heat equation solved with a physics-informed neural network. Left, the exact solution. Right, the trained network. Both plots are the outputs saved in my notebook, with their titles cropped off because the notebook has them swapped."
stats:
  - value: "6"
    label: "2025 contest problems with every part answered (83 parts)"
  - value: "12"
    label: "study units in the 2026 plan, Markdown to graph neural networks"
  - value: "14"
    label: "practice sets built on the 2026 Round 1 sample problems"
when: "2025 to 2026. Repo uploaded February 2026"
builtWith: "Python, PyTorch, NumPy, pandas, scikit-learn, Matplotlib, Hugging Face Transformers, Jupyter"
links:
  - label: "The repo"
    href: "https://github.com/greenporsche/usaaio-training"
  - label: "USA AI Olympiad"
    href: "https://www.usaaio.org/"
---

## How I built it

The USA AI Olympiad has two rounds. Round 1 is taken at school. Round 2 is held at MIT. Contestants derive results by hand and also code them in Python and PyTorch, often without high-level libraries. In 2025 Round 1 was on 24 March and Round 2 on 27 April. In 2026 they were on 30 January and 4–5 April.

The repo has three parts.

**The 2025 contest problems, answered.** Round 1 and Round 2 each had three problems worth 100 points, every one split into parts. The repo has all six with every part filled in, 83 parts in all. The answers differ from the official Round 1 solutions, which are also in the repo. The topics:

- Round 1: Fibonacci numbers through eigendecomposition, a small neural network trained in PyTorch, and a Titanic data pipeline with logistic regression by gradient descent and by Newton's method.
- Round 2: a physics-informed neural network for the heat equation, multi-head attention and two of its variants (grouped-query and multi-head latent attention), and CLIP.

For the heat-equation problem, the network takes a time and a position and outputs a temperature. The loss punishes it for breaking the equation, the starting condition and the edge conditions. Derivatives come from `torch.autograd.grad`. After 1,000 epochs its mean squared error against the exact solution was 3.9 × 10⁻⁵ on a 101 × 101 grid.

**Study notebooks from 2025.** Ten Jupyter notebooks, from mathematical foundations to generative AI.

**A plan for 2026.** Twelve units follow the USAAIO syllabus and the BeaverEdge course sequence. Each unit has a cheat sheet, study guides, pencil-and-paper exercises with solutions, and practice notebooks in the Round 2 format with blank answer cells. There are also 14 practice sets built as variations on the official 2026 Round 1 sample problems, and a Round 2 plan that works backward from the three 2025 Round 2 problems. I did not write the 2026 material by hand. The twelve units were generated in one day, 24 February 2026, and the practice sets were generated too. A small Python script converts the practice sets from Markdown to notebooks.

## What I did

- Trained the heat-equation network and checked it against the exact solution.
- Set up the 2026 study plan and practice sets, and the Round 2 gap analysis.

## Where it stands

The repo was last updated on 24 February 2026, between the two 2026 rounds. Its README still says I had requalified for Round 2. I won national gold in 2025 and again in 2026. The repo does not record how I prepared after February, so this page does not claim that the 2026 plan led to the result.
