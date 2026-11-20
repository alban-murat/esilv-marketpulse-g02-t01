"""MarketPulse analytics: pure functions for comparison (TD07)."""


def index_by_date(prices):
    return {row["date"]: row for row in prices}


def align_series(instrument_prices, benchmark_prices):
    raise NotImplementedError  # Owner: Lead (Student 1)


def calculate_period_return(prices):
    if not prices:
        raise ValueError("Price series cannot be empty")

    first_close = float(prices[0]["close"])
    last_close = float(prices[-1]["close"])

    if first_close == 0:
        raise ValueError("First close cannot be zero")

    return ((last_close / first_close) - 1.0) * 100.0


def calculate_base_100(prices):
    raise NotImplementedError  # Owner: Student 4


def calculate_relative_performance(instrument_return, benchmark_return):
    return instrument_return - benchmark_return