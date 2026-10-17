"""Summarize structure and validity of a JSON Lines file."""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path
from typing import Any


def summarize(path: Path, required: list[str]) -> dict[str, Any]:
    total = 0
    valid = 0
    invalid: list[dict[str, Any]] = []
    key_counts: Counter[str] = Counter()
    missing_counts: Counter[str] = Counter()

    with path.open("r", encoding="utf-8") as source:
        for line_number, raw_line in enumerate(source, start=1):
            total += 1
            try:
                record = json.loads(raw_line)
                if not isinstance(record, dict):
                    raise ValueError("top-level value is not an object")
            except (json.JSONDecodeError, ValueError) as exc:
                invalid.append({"line": line_number, "error": str(exc)})
                continue

            valid += 1
            key_counts.update(record.keys())
            for key in required:
                if key not in record or record[key] in (None, ""):
                    missing_counts[key] += 1

    return {
        "file": str(path),
        "rows": {"total": total, "valid": valid, "invalid": len(invalid)},
        "keys": dict(sorted(key_counts.items())),
        "required_missing": dict(sorted(missing_counts.items())),
        "invalid_rows": invalid,
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Summarize keys, invalid rows, and missing required values in JSONL."
    )
    parser.add_argument("input", type=Path, help="UTF-8 JSONL input file")
    parser.add_argument(
        "--required",
        nargs="*",
        default=[],
        metavar="KEY",
        help="Keys that must be present and non-empty",
    )
    parser.add_argument("--output", type=Path, help="Write report to this JSON file")
    args = parser.parse_args()

    if not args.input.is_file():
        parser.error(f"input file does not exist: {args.input}")

    report = summarize(args.input, args.required)
    rendered = json.dumps(report, indent=2, ensure_ascii=False)
    if args.output:
        args.output.write_text(rendered + "\n", encoding="utf-8")
    else:
        print(rendered)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
