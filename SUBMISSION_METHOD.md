# Submission method summary: frozen HydrAMP baseline adapter

## Abstract

This candidate uses the published HydrAMP conditional variational autoencoder
and its epoch-37 checkpoint to produce 50,000 unique antimicrobial peptide
sequences under the official default unconstrained AMP-generation setting.
The model's AMP and low-MIC classifier heads filter generated candidates. A
ranked Top 100 is selected by HydrAMP's low-MIC score, subject to the starter
kit's biological synthesizability and known-antibacterial similarity filters.
The only Phase 02 adaptation changes the output directory and executable name
to the current AMP Challenge contract; there is no new model or optimization.

## Training data and model

The official kit includes the full disclosed HydrAMP training data in
`data/training/`, with per-file provenance in `data/README.md`. Its sources
include DBAASP, DRAMP, APD, GRAMPA, AMP Scanner v2 and UniProt. The inference
dependency is fixed to HydrAMP commit
`6590d2f4c2963f25d30669052a4c4a857e0e7279`; the epoch-37 weights and
latent PCA decomposer are committed under `checkpoint/`. This Phase 02 work
does not retrain the model or add data.

## Computational selection and ranking

1. HydrAMP generates candidates with `mode="amp"`, softmax decoding,
   `filter_out=True`, seed 42, and the official checkpoint. Built-in predicted
   AMP and low-MIC probabilities must each be in `[0.8, 1.0]`.
2. The library retains only 8–50 residue sequences from the 20 standard amino
   acids, globally unique and without exact overlap with
   `data/antibacterial.fasta`.
3. Candidates are ranked by the HydrAMP `mic` head (higher predicted
   probability of low E. coli MIC first).
4. The Top 100 additionally excludes cysteine-containing candidates and
   candidates that fail the starter kit's positive-residue cluster, repeated
   residue, or hydrophobic cluster checks. It excludes candidates whose
   Levenshtein ratio with any known antibacterial reference exceeds 0.8.

There is no manual selection, prompt engineering, external scoring model,
new generator family or test-set optimization in this adapter. The generator
only produces the broad-spectrum entry; its E. coli-oriented MIC head is not
a direct predictor of activity across all 20 Challenge strains. Hemolysis and
HC50 are not directly optimized, and predicted potency is not measured MIC.

## Deliverables

`uv run generate` produces `generate/library.fasta` (50,000 sequences) and
`generate/top.fasta` (100 ordered sequences). Both files use FASTA headers
`>seq1`, `>seq2`, etc. Their hashes and independent-run comparison are in the
Phase 02 evidence manifest.

The official HydrAMP starter kit is a benchmark baseline that the organizers
exclude from rankings and prizes. This contract adaptation alone is not an
algorithmic improvement or a claim of prize eligibility.
