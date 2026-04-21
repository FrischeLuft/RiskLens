"""Command-line entrypoint for local project checks."""

from __future__ import annotations

import argparse

from risklens.config import Settings


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="RiskLens local CLI")
    parser.add_argument(
        "--show-config",
        action="store_true",
        help="Print the resolved runtime configuration from the environment.",
    )
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    if args.show_config:
        settings = Settings.from_env()
        print(settings)
        return 0

    print("RiskLens scaffold is ready. Use --show-config to inspect environment settings.")
    return 0
