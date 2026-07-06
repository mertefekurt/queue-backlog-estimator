# Queue Backlog Estimator

![Queue Backlog Estimator cover](assets/readme-cover.svg)

Review queue workload plans for backlog and worker-capacity risk.

## The rule file is the product

- `capacity-below-arrival` (high): worker capacity appears below arrival rate. Fix: Increase workers, reduce arrival rate, or add backpressure..
- `missing-backlog-limit` (medium): backlog limit is missing. Fix: Set queue depth alerts and discard policy..
- `missing-dlq` (low): dead-letter queue is missing. Fix: Add DLQ handling for poisoned messages..

Everything else in the repo exists to feed records into those checks and render the answer in a way a person can act on.

## Shell session

```bash
git clone https://github.com/mertefekurt/queue-backlog-estimator.git
cd queue-backlog-estimator
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
queue-backlog-estimator examples/sample.txt
queue-backlog-estimator examples/sample.txt --json
```

## Repository shape

```text
.github/        CI workflow
examples/       sample inputs
src/            package source
tests/          test coverage
.gitignore      project file
pyproject.toml  package metadata
```
