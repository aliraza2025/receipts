#!/usr/bin/env python3
"""Per-arm sample size for a two-proportion test (normal approximation).

Example:
    python3 sample_size.py --baseline 0.40 --mde 0.15
"""

import argparse
import math
from statistics import NormalDist


def per_arm(baseline: float, mde: float, alpha: float = 0.05, power: float = 0.80) -> int:
    p1 = baseline
    p2 = baseline + mde
    if not (0 < p1 < 1 and 0 < p2 < 1):
        raise ValueError("baseline and baseline + mde must both be between 0 and 1")
    z_alpha = NormalDist().inv_cdf(1 - alpha / 2)
    z_beta = NormalDist().inv_cdf(power)
    p_bar = (p1 + p2) / 2
    numerator = (
        z_alpha * math.sqrt(2 * p_bar * (1 - p_bar))
        + z_beta * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))
    ) ** 2
    return math.ceil(numerator / (mde ** 2))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--baseline", type=float, required=True, help="control conversion rate, e.g. 0.40")
    parser.add_argument("--mde", type=float, required=True, help="absolute minimum detectable effect, e.g. 0.15")
    parser.add_argument("--alpha", type=float, default=0.05, help="two-sided significance level")
    parser.add_argument("--power", type=float, default=0.80, help="statistical power")
    args = parser.parse_args()

    n = per_arm(args.baseline, args.mde, args.alpha, args.power)
    print(f"per arm: {n} (two-sided alpha {args.alpha}, power {args.power:.2f})")
    print("label this a planning assumption until a pilot gives a real baseline")


if __name__ == "__main__":
    main()
