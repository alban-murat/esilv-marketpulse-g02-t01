import json
from src.providers.bloomberg_provider import (
    fetch_bloomberg_prices,
    normalize_reference_series,
)


def main():
    # 1. Cas valide (APPROVED_SAMPLE) + comparaison exacte avec bloomberg_reference_expected.json
    aapl = fetch_bloomberg_prices("AAPL", mode="APPROVED_SAMPLE")
    sp500 = fetch_bloomberg_prices("SP500", mode="APPROVED_SAMPLE")

    with open("data/sample/bloomberg_reference_expected.json", encoding="utf-8") as file:
        expected = json.load(file)["rows"]

    assert aapl + sp500 == expected, "Mismatch with bloomberg_reference_expected.json"
    assert all(
        isinstance(row["close"], float) and isinstance(row["volume"], int)
        for row in aapl + sp500
    )
    print(f"1. Valid APPROVED_SAMPLE & exact match: OK (AAPL: {len(aapl)}, SP500: {len(sp500)})")

    # 2. Liste observations vide -> ValueError
    try:
        normalize_reference_series({"canonical_ticker": "AAPL", "observations": []})
        raise AssertionError("Expected ValueError for empty observations")
    except ValueError as exc:
        print(f"2. Empty observations -> ValueError: OK ({exc})")

    # 3. Champ close_value manquant -> ValueError
    try:
        normalize_reference_series(
            {
                "canonical_ticker": "AAPL",
                "observations": [{"observation_date": "2026-11-18"}],
            }
        )
        raise AssertionError("Expected ValueError for missing field")
    except ValueError as exc:
        print(f"3. Missing field -> ValueError: OK ({exc})")

    # 4. Dates dupliquees -> ValueError
    try:
        normalize_reference_series(
            {
                "canonical_ticker": "AAPL",
                "observations": [
                    {
                        "observation_date": "2026-11-18",
                        "open_value": 100.0,
                        "high_value": 112.0,
                        "low_value": 99.0,
                        "close_value": 110.0,
                        "volume_value": 1500,
                    },
                    {
                        "observation_date": "2026-11-18",
                        "open_value": 101.0,
                        "high_value": 113.0,
                        "low_value": 100.0,
                        "close_value": 111.0,
                        "volume_value": 1600,
                    },
                ],
            }
        )
        raise AssertionError("Expected ValueError for duplicate date")
    except ValueError as exc:
        print(f"4. Duplicate observation_date -> ValueError: OK ({exc})")

    # 5. Frontiere LIVE -> NotImplementedError
    try:
        fetch_bloomberg_prices("AAPL", mode="LIVE")
        raise AssertionError("Expected NotImplementedError for LIVE mode")
    except NotImplementedError as exc:
        print(f"5. LIVE mode boundary -> NotImplementedError: OK ({exc})")

    print("\nBloomberg stage APPROVED_SAMPLE — ALL TD10 VALIDATION CHECKS PASSED")


if __name__ == "__main__":
    main()
