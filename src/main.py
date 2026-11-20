from pathlib import Path
import csv
import json


DATA_DIR = Path("data/sample")

# These starter values mirror config/settings.yml.
# settings.yml is a human-readable configuration contract in the CORE.
# Parsing YAML is optional and is not required by the 18-hour lab sequence.
LOOKBACK_LABEL = "1 month"
INTERVAL_LABEL = "Daily"


def load_instruments():
    with open(DATA_DIR / "instruments.json", encoding="utf-8") as file:
        return json.load(file)


def load_prices():
    with open(DATA_DIR / "prices.csv", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def filter_prices(prices, ticker):
    return [row for row in prices if row["ticker"] == ticker]


def main():
    instruments = load_instruments()
    prices = load_prices()

    instrument = instruments["instrument"]
    benchmark = instruments["benchmark"]

    instrument_prices = filter_prices(prices, instrument["ticker"])
    benchmark_prices = filter_prices(prices, benchmark["ticker"])

    instrument_latest = instrument_prices[-1]
    benchmark_latest = benchmark_prices[-1]

    print("=== MarketPulse ===")
    print()
    print("Tracked Instrument")
    print(f"{instrument['ticker']} - {instrument['name']}")
    print(f"Latest close price: {instrument_latest['close']} {instrument['currency']}")
    print()
    print("Reference Benchmark")
    print(f"{benchmark['ticker']} - {benchmark['name']}")
    print(f"Latest close level: {benchmark_latest['close']}")
    print()
    print("Sample Configuration")
    print(f"Lookback period: {LOOKBACK_LABEL}")
    print(f"Sampling interval: {INTERVAL_LABEL}")
    print()
    print("Observation Count")
    print(f"{instrument['ticker']}: {len(instrument_prices)} observations")
    print(f"{benchmark['ticker']}: {len(benchmark_prices)} observations")


if __name__ == "__main__":
    main()
