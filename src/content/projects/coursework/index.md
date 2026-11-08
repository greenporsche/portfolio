---
published: true
title: "Coursework"
category: "Learning"
order: 22
summary: "My solutions from three college CS courses and six Euler Circle proof courses, 2023 to now."
lede: "This is my coursework, not original research. It covers three college computer science courses in Python and Java, and six proof-based math courses at Euler Circle with a written problem set every week."
cover: ./cover.png
coverAlt: "A typeset solution titled Problem 2. Starting from the recurrence a sub n plus 1 equals 2 a sub n plus 3 to the n, it multiplies by x to the n plus 1, sums over n, solves for the generating function A(x) = (2 − 5x) / ((1 − 2x)(1 − 3x)), splits it into partial fractions, and concludes a sub n = 2 to the n plus 3 to the n."
caption: "My solution to Problem 2 of Combinatorics 7 (Euler Circle, October 2025), cropped from the compiled PDF in my euler-circle repo."
stats:
  - value: "9"
    label: "courses: 3 in computer science, 6 in proof-based math"
  - value: "93"
    label: "weekly math problem sets, each written up as a PDF"
when: "Fall 2023 to now. Euler Circle since fall 2023; college CS in fall 2024 and spring 2025"
builtWith: "Python, Java, Jupyter notebooks, LaTeX"
links:
  - label: "CIS 61: Structure and Interpretation of Computer Programs"
    href: "https://github.com/greenporsche/CIS-61-program-structures"
  - label: "COMSC 76: Data Structures"
    href: "https://github.com/greenporsche/COMSC-076-data-structures"
  - label: "COMSC 28: Foundations of Data Science"
    href: "https://github.com/greenporsche/COMSC-028-data-science"
  - label: "Euler Circle problem sets and papers"
    href: "https://github.com/greenporsche/euler-circle"
---

## Computer science

**CIS 61, Structure and Interpretation of Computer Programs.** Fall 2024, in the Peralta Community College District <mark>(which college?)</mark>. The course is about procedural and data abstraction, modularity and state. The repo has my code for 10 labs and 4 projects, in Python. The labs move from functions and recursion to trees, objects and linked lists. The projects come with starter code and autograders from UC Berkeley's 61A course.

In the Maps project I charted the mood of tweets across the US. I grouped tweets by state, scored each tweet's words for sentiment, and averaged the scores per state. To place each state on the map, I found the center of its polygons, weighted by area. Two projects are not complete. Ants vs. SomeBees still has one unwritten method. The Scheme interpreter is in the repo as starter code only.

**COMSC 76, Computer Science II: Introduction to Data Structures.** Fall 2024, at Evergreen Valley College, fully online. The course covers lists, stacks, queues, trees, hash tables, and searching and sorting, in Java. The repo has 13 folders: 12 assignments and one test. Most assignments start from the instructor's handout. For seven of them the repo keeps his starter file next to my version.

I wrote a hash map, a binary search tree, and insertion sort, Shell sort, merge sort and quicksort. The last assignment was a small library system. It started as a class of empty methods. I stored the books in a linked list and indexed them with two binary search trees, one by title and author and one by ISBN. It can check books out, return them, and save and load the library from a file.

**COMSC 28, Foundations of Data Science.** Spring 2025 <mark>(which school?)</mark>. The course uses the public materials of Berkeley's Data 8, in Jupyter notebooks. I completed the first three homeworks and the first three labs, and submitted them in February 2025. The rest of the notebooks in the repo are still blank. In Homework 3 I used Census population estimates for 2015 to 2016 to compute the US birth rate for that year, about 1.24%. Then I plotted birth rate against death rate for all 50 states, DC and Puerto Rico.

## Euler Circle mathematics

Euler Circle teaches proof-based math to high school students. Each course has weekly lectures, and a written problem set is due every week. I typeset most of my solutions in LaTeX. Problem sets 1 to 6 of my first course were not written in LaTeX, so only their PDFs exist.

- **Transition to Proofs**, fall 2023 to spring 2024. 30 problem sets: number theory in the fall, combinatorics in the winter, analysis in the spring. Sets 11 and 22 are missing from the repo.
- **Fundamentals of Higher Mathematics**, fall 2024 to spring 2025. 30 problem sets: linear and abstract algebra, then real analysis, then point-set topology.
- **Combinatorics**, fall 2025. 9 problem sets on permutations, Stirling numbers, posets, Möbius functions and generating functions.
- **Infinite Series**, winter 2026. 9 problem sets on evaluating series and products in closed form, from Fourier series to continued fractions and nested radicals.
- **p-adic Analysis**, spring 2026. 9 problem sets on p-adic numbers, Hensel's lemma, Newton polygons and the profinite integers.
- **Generating Functions**, fall 2026, in progress. 6 problem sets so far, on the symbolic method, labeled objects, trees and probability.

One example is the cover. The recurrence a(n+1) = 2a(n) + 3ⁿ becomes a statement about the generating function A(x). Solving for A(x) and splitting it into partial fractions gives the closed form a(n) = 2ⁿ + 3ⁿ.

In several of these courses I also wrote an expository paper. Those have their own pages here <mark>(link which ones?)</mark>.

## Where it stands

The CS courses are over. The repos hold my code, plus the unfinished starter code I noted above. The Euler Circle repo holds 93 problem sets so far. I am taking Generating Functions now, so it is still growing.
