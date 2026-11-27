import json
from pathlib import Path

BLOOMBERG_IDENTIFIERS = {
    "AAPL": "AAPL US Equity",
    "SP500": "SPX Index",
}

REQUIRED_OBSERVATION_FIELDS = {
    "observation_date",
    "open_value",
    "high_value",
    "low_value",
    "close_value",
    "volume_value",
}

REPO_ROOT = Path(__file__).resolve().parents[2]
REFERENCE_SAMPLE = REPO_ROOT / "data" / "sample" / "bloomberg_reference_sample.json"


def get_reference_sample_path():
    """Return the resolved path to the approved Bloomberg fallback JSON fixture."""
    return REFERENCE_SAMPLE


def load_bloomberg_reference_sample(path=None):
    """Load the approved Bloomberg reference JSON payload."""
    sample_path = Path(path) if path is not None else get_reference_sample_path()
    with open(sample_path, encoding="utf-8") as file:
        return json.load(file)


def find_reference_series(payload, provider_identifier):
    """Select one series from the approved payload by provider_identifier."""
    for series in payload.get("series", []):
        if series.get("provider_identifier") == provider_identifier:
            return series

    raise ValueError(
        f"Approved Bloomberg-stage series not found: {provider_identifier}"
    )


def validate_reference_series(series):
    """Validate structure, required fields, and unique dates before normalization."""
    if not isinstance(series, dict):
        raise ValueError("Reference series must be a dictionary.")

    canonical_ticker = series.get("canonical_ticker")
    if not isinstance(canonical_ticker, str) or not canonical_ticker.strip():
        raise ValueError("Reference series must define a non-empty canonical_ticker.")

    observations = series.get("observations")
    if not isinstance(observations, list) or len(observations) == 0:
        raise ValueError(
            f"Reference series for {canonical_ticker} must contain at least one observation."
        )

    seen_dates = set()
    for index, observation in enumerate(observations):
        if not isinstance(observation, dict):
            raise ValueError(
                f"Observation at index {index} for {canonical_ticker} must be a dictionary."
            )

        missing_fields = REQUIRED_OBSERVATION_FIELDS - set(observation.keys())
        if missing_fields:
            missing_list = ", ".join(sorted(missing_fields))
            raise ValueError(
                f"Observation at index {index} for {canonical_ticker} is missing required fields: {missing_list}"
            )

        obs_date = observation["observation_date"]
        if obs_date in seen_dates:
            raise ValueError(
                f"Duplicate observation_date '{obs_date}' found for {canonical_ticker}."
            )
        seen_dates.add(obs_date)


def normalize_reference_series(series):
    """Validate and normalize a Bloomberg reference series into canonical MarketPulse rows."""
    validate_reference_series(series)
    canonical_ticker = series["canonical_ticker"]
    rows = []

    for observation in series["observations"]:
        rows.append(
            {
                "date": str(observation["observation_date"]),
                "ticker": canonical_ticker,
                "open": float(observation["open_value"]),
                "high": float(observation["high_value"]),
                "low": float(observation["low_value"]),
                "close": float(observation["close_value"]),
                "volume": int(observation["volume_value"]),
            }
        )

    return rows


def fetch_approved_sample_prices(provider_identifier, path=None):
    """Load, select, and normalize prices from the approved Bloomberg fallback fixture."""
    payload = load_bloomberg_reference_sample(path=path)
    series = find_reference_series(payload, provider_identifier)
    return normalize_reference_series(series)


def fetch_raw_bloomberg_history(identifier, start_date=None, end_date=None):
    """Boundary for instructor-supplied LIVE Bloomberg retrieval."""
    raise NotImplementedError("Live mode not currently active.")


def normalize_bloomberg_history(raw_data, canonical_ticker):
    """Boundary for normalizing LIVE Bloomberg payloads into canonical rows."""
    raise NotImplementedError("Live Bloomberg normalization is not currently active.")


def fetch_bloomberg_prices(ticker, mode="APPROVED_SAMPLE", start_date=None, end_date=None):
    """Fetch canonical MarketPulse rows for a ticker using APPROVED_SAMPLE or LIVE mode."""
    if ticker not in BLOOMBERG_IDENTIFIERS:
        raise ValueError(f"Unsupported canonical ticker for Bloomberg provider: {ticker}")

    provider_id = BLOOMBERG_IDENTIFIERS[ticker]

    if mode == "APPROVED_SAMPLE":
        return fetch_approved_sample_prices(provider_id)
    if mode == "LIVE":
        raw_data = fetch_raw_bloomberg_history(provider_id, start_date, end_date)
        return normalize_bloomberg_history(raw_data, ticker)

    raise ValueError(f"Unrecognized Bloomberg mode: {mode}")
