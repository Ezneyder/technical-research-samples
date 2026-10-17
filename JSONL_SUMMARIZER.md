# JSONL Summarizer

`jsonl_summarizer.py` validates a UTF-8 JSON Lines file and produces a deterministic JSON report. It counts valid and invalid rows, records how often each key appears, and reports missing values for fields selected by the caller.

## Requirements

- Python 3.10 or newer
- No third-party packages

## Quickstart

Create `records.jsonl`:

```jsonl
{"id": 1, "name": "Ada", "country": "GB"}
{"id": 2, "name": "", "country": "BO"}
not-json
```

Run:

```bash
python examples/jsonl_summarizer.py records.jsonl --required id name country
```

The report includes:

```json
{
  "rows": {"total": 3, "valid": 2, "invalid": 1},
  "required_missing": {"name": 1},
  "invalid_rows": [{"line": 3, "error": "Expecting value: line 1 column 1 (char 0)"}]
}
```

The exact parser error may differ slightly between Python versions. Line numbers and counts remain stable.

## Options

| Argument | Required | Meaning |
|---|---:|---|
| `input` | Yes | Path to the UTF-8 JSONL file. |
| `--required KEY ...` | No | Fields that must exist and cannot be `null` or an empty string. |
| `--output PATH` | No | Write the report to a file instead of standard output. |

## Failure behavior

- A missing input path exits with code 2 and an argparse error.
- A malformed JSON row is recorded in `invalid_rows`; it does not stop the remaining rows from being checked.
- A valid JSON value that is not an object is treated as invalid.
- File permission and decoding errors are surfaced to the caller rather than hidden.

## Scope

The utility reads one line at a time, so raw input is not loaded into memory. The final report retains one small error object per invalid row; unusually large invalid files can therefore produce a large report.
