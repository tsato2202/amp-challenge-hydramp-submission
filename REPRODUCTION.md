# HydrAMP Challenge contract adapter: reproduction

This repository is derived from the official HydrAMP starter kit at commit
`7804df862872ccc6d09fe01c41bafbca194cfa31`. The only generation change is
the destination directory of the new `generate` entry point. The original
`generate_broad_spectrum` entry point and generation logic remain available.

## Requirements and fixed inputs

- `git` and `uv` (verified locally with uv 0.12.18)
- Python 3.8, selected from `.python-version` by `uv`
- The committed epoch-37 model, PCA decomposer, reference FASTA, and `uv.lock`
- A clean clone of the candidate repository. No GPU is required.

Do not upgrade TensorFlow, Keras, Python, or other locked dependencies during
submission reproduction.

## Generate

```bash
git clone <candidate-repository-url> amp-hydramp-candidate
cd amp-hydramp-candidate
uv sync --frozen
uv run --no-sync generate
```

`generate` uses the official defaults: 50,000 unique sequences, ranked Top 100,
seed 42, and the checkpoint and reference data committed to this repository.
The output is exactly:

```text
generate/library.fasta
generate/top.fasta
```

The `--no-sync` flag above makes the environment used by generation explicit.
The organizer's command `uv run generate` is equivalent after `uv sync` and is
the canonical entry point. It can also create the environment itself in a fresh
clone.

## Official validator

Run the validator **from the current official Challenge template**. Its own
Python environment is separate from this candidate's frozen Python 3.8 model
environment. The validator clones this repository, runs `uv sync`, generates
the full library twice and compares bytes.

```bash
git clone https://github.com/szczurek-lab/amp-challenge-2027.git challenge-template
cd challenge-template
uv sync --frozen
uv run --no-sync python scripts/verify_submission.py <candidate-repository-url>
```

For an offline/local verification, replace `<candidate-repository-url>` with
the absolute path to a committed local clone. The Challenge template and
HydrAMP source commit used for the Phase 02 audit are recorded in the evidence
manifest. Do not invoke the original kit's legacy category-based validator as
the current submission-contract validator.

## Data and limits

The training datasets and their provenance are described in `data/README.md`
and the original `README.md`. Method, filtering and ranking are documented in
`SUBMISSION_METHOD.md`. Generated FASTA files have linear unmodified sequences
using the 20 standard amino acids. The computational classifier scores are not
experimental MIC or HC50 measurements.
