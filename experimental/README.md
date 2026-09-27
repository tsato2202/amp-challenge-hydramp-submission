# Experimentally characterized HydrAMP peptides

> **These are not the candidates in
> [`generate_broad_spectrum/top.fasta`](../generate_broad_spectrum/top.fasta).** This
> directory is HydrAMP's *historical* wet-lab track record: peptides that were actually
> synthesized and assayed in prior HydrAMP work (the 2023 paper plus unpublished
> follow-up). The challenge asks each baseline to ship "the complete set of experimentally
> characterized peptides ... with their measured MIC values" (AMP Challenge, §1.6), and that
> is what this is. The generated top-100 in `generate_broad_spectrum/` is a separate,
> freshly generated set of *new, unsynthesized* candidates; the challenge's novelty rule
> (< 80% identity to any known AMP) keeps it disjoint from these already-tested peptides, so
> the two sets share no sequences.

Experimentally measured activity of HydrAMP peptides, stored in **µM**.

- **`mic.csv`**: minimum inhibitory concentration, one row per (peptide, strain):
  `peptide_id, sequence, is_prototype, strain, strain_type, mic_uM, mic_censored`.
- **`hemolysis.csv`**: half-maximal hemolytic concentration, one row per peptide:
  `peptide_id, sequence, hc50_uM, hc50_censored`.

`*_censored = True` marks a value at the assay ceiling (i.e. `> mic_uM`); an untested
(peptide, strain) pair simply has no row. `is_prototype = True` marks a known input peptide
(not a HydrAMP design).

## Peptides

47 peptides, 6 of them prototypes:

- **26 designed analogues** of four clinically relevant prototypes (GQ20, Syphaxin, OP-145,
  Omiganan) plus Pexiganan, tested against 5 strains, with HC50.
- **7 first-round analogues** of Temporin-A and Pexiganan, tested against 2 *E. coli*
  strains (no HC50).
- **8 unconstrained (de-novo) peptides**, tested against 2 strains. **Unpublished** (not in
  the 2023 paper); the set most directly comparable to this kit's unconstrained library.

## Measurement and units

MIC/HC50 were determined by CLSI broth microdilution in Mueller-Hinton broth (inoculum
0.5×10⁵ CFU/mL, 18 h, 37 °C), in triplicate, as 2-fold dilutions up to a 512 µg/mL ceiling.
Values are converted to µM using each peptide's TFA-salt molar mass computed from its
sequence (C-amidated peptide + one TFA per basic group), which reproduces the source
molar masses to <0.05 Da. See Szymczak et al. 2023, *Nature Communications* 14, 1453.
