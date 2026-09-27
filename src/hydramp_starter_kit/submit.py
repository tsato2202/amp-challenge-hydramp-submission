"""Adapt the official HydrAMP baseline's output location to the Challenge contract.

The generator, model, selection, filters, seed and CLI defaults stay in
``hydramp_starter_kit.generate``. Only its output-directory constant changes
for this entry point, from ``generate_broad_spectrum`` to ``generate``.
"""

from hydramp_starter_kit import generate as baseline


def main() -> None:
    original_category = baseline.CATEGORY
    if original_category != "generate_broad_spectrum":
        raise RuntimeError("Unexpected upstream HydrAMP output category")
    try:
        baseline.CATEGORY = "generate"
        baseline.main()
    finally:
        baseline.CATEGORY = original_category
