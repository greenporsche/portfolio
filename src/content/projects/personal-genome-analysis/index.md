---
title: "Personal genome analysis"
category: "Research"
order: 5
summary: "Raw reads to variant calls for my own genome on U-Michigan's HPC cluster. miRcore, 2025."
lede: "I ran my own DNA sequencing reads through a five-step pipeline on the University of Michigan's Great Lakes cluster, from raw reads to variant calls."
cover: ./cover.png
coverAlt: "Pipeline diagram. Cutadapt trims adapters, Bowtie2 aligns reads to GRCh38, Samtools sorts and indexes, bcftools mpileup and bcftools call produce variant calls, and a script pulls out per-gene alignments."
caption: "The five cluster jobs and the gene-extraction step, redrawn from the diagram in my project README. Read counts and alignment rate are from the job logs."
stats:
  - value: "25.4M"
    label: "read pairs, 150 bp, trimmed and aligned"
  - value: "95.99%"
    label: "overall alignment rate to GRCh38"
  - value: "5"
    label: "SLURM jobs, one per pipeline step"
when: "Summer 2025. miRcore summer camp, Sequencing Your Genome track"
builtWith: "Great Lakes HPC (SLURM), Linux shell, cutadapt 1.18, Bowtie2, SAMtools, bcftools"
links:
  - label: "My scripts and study notes"
    href: "https://github.com/greenporsche/miRcore"
  - label: "miRcore"
    href: "https://www.mircore.org/"
---

## How I built it

This was the last of three miRcore summer tracks. Earlier in the summer I learned the same tools on eight patient samples. I aligned their reads to the human genome, then aligned the leftover reads to SARS-CoV-2 to find the pathogen.

For my own genome I started from 25.4 million pairs of 150 bp reads. Each step ran as its own SLURM job on the Great Lakes cluster:

1. Cutadapt trimmed the Illumina TruSeq adapters and dropped reads shorter than 30 bp.
2. Bowtie2 aligned the trimmed reads to GRCh38. I saved the reads that did not align, for contamination screening.
3. Samtools converted the alignment to BAM, sorted it and indexed it.
4. bcftools mpileup computed genotype likelihoods from the sorted alignment.
5. bcftools call called the variants and wrote them to a VCF.

Then I pulled small per-gene alignments out of the full one, so I could look at single genes without loading the whole file. I did this for five genes linked to everyday traits: ABO, ABCC11, BHLHE41, MMP1 and TAS2R38. The extraction script takes a region and a gene name, so it works for any gene.

## The hard part

My first mpileup run wrote a 17 GB log. It held about 278 million copies of one error: `Failed to retrieve block: unexpected end of file`. The step had failed at every position it tried.

The most likely cause was the reference genome on the cluster. Its FASTA file was probably truncated, or still being unpacked, when the job started. I re-ran mpileup and it finished cleanly with a 216-byte log. Then I re-ran variant calling on the new output.

I had seen failures like this in the patient-sample week. Several of those jobs failed because a script pointed at the wrong index name or the wrong project folder, and each time the log said so.

## What I did

- Ran the full pipeline on my own reads, from raw reads to variant calls.
- Wrote the general gene-extraction script and used it on five genes.
- Found the failed mpileup run, worked out the likely cause and re-ran the last two steps.
- Wrote the project READMEs and my own study notes, now in a public repo. The camp material itself belongs to miRcore and Dr. Inhan Lee.

## Where it stands

The pipeline is done and the variant calls exist. I keep the results private. The public repo has my scripts and notes, not my sequence data.
