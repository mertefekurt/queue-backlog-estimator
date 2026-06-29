# queue-backlog-estimator

`queue-backlog-estimator` is a small local CLI that review queue workload plans for backlog and worker-capacity risk.

## Why it is useful

Async systems fail quietly when arrival rate exceeds worker capacity. This CLI flags queue plans with weak capacity assumptions.

## Key features

- reads text, JSON, JSONL, or CSV inputs
- returns Markdown or JSON reports
- supports severity-based CI exit codes
- keeps all checks deterministic and offline
- includes focused rules for this project:
- `capacity-below-arrival`: worker capacity appears below arrival rate
- `missing-backlog-limit`: backlog limit is missing
- `missing-dlq`: dead-letter queue is missing

## Installation

```bash
python -m pip install -e ".[dev]"
```

## Usage

```bash
queue-backlog-estimator examples/sample.txt
queue-backlog-estimator examples/sample.txt --json
queue-backlog-estimator path/to/input.txt --fail-on medium --out report.md
python -m queue_backlog_estimator --help
```

Example input:

```text
arrival_rate: 500/min worker_capacity: 100/min max_backlog: unknown dlq: none
```

## CLI options

```text
queue-backlog-estimator INPUT [--format auto|text|jsonl|csv|json] [--json]
             [--fail-on low|medium|high] [--out PATH]
```

`INPUT` is any queue workload plan or incident notes. The tool exits with code `2` when findings meet the selected
threshold, which makes it easy to use in GitHub Actions or release checks.

## Workflow

```mermaid
flowchart LR
    A[input file] --> B[format reader]
    B --> C[project-specific rules]
    C --> D[risk score]
    D --> E[Markdown or JSON report]
```

## Tests

```bash
ruff check .
pytest
python -m queue_backlog_estimator --help
```

## License

MIT
