# Checkpoint B — Collaboration and Data

## Student
- Name: Alexis Jacques
- GitHub: @Droopysss
- Evidence branch: `feature/checkpoint-b-droopysss`

## Contribution
- TD05 branch: `alexis_jacques_projet`
- TD05 commit: `4d2eaf2` — Quick start documentation
- TD05 Pull Request: #7 (merged)
- TD07 commit: `36e7347` — `calculate_period_return`
- TD08 branch: `feature/yahoo-provider`
- TD08 commits: `6ae6f64` (provider stub and dependency), `4fd3473` (Yahoo provider implementation)
- TD08 Pull Request: #9 (merged)
- Reviewed Pull Request: #6 (Paul Courty, `PAULCO6`)

## Work completed
Implemented the Yahoo Finance adapter for AAPL and SP500, mapping `^GSPC` back to the canonical `SP500` ticker and returning normalized daily market observations. Validated live Yahoo retrieval and the unchanged TD07 analytics on both series.

## Main difficulty
Converting Yahoo's DataFrame columns and values into the canonical MarketPulse row format while preserving ticker names and numeric data types.

## Evidence
- `01_pull_request.png`
- `02_code_review.png`
- `03_yahoo_market_data.png`
- `04_instrument_benchmark.png`

## Supplementary evidence
- `extras/TD07_personal_commit.png` — Personal analytics contribution
