import yfinance as yf


CANONICAL_TO_YAHOO = {
    "AAPL": "AAPL",
    "SP500": "^GSPC",
}

YAHOO_SYMBOL_MAPPING = CANONICAL_TO_YAHOO


def fetch_yahoo_prices(canonical_ticker, lookback="1mo", interval="1d"):
    yahoo_symbol = CANONICAL_TO_YAHOO[canonical_ticker]

    data = yf.download(
        yahoo_symbol,
        period=lookback,
        interval=interval,
        auto_adjust=False,
        multi_level_index=False,
        progress=False,
    )

    prices = []

    for date, row in data.iterrows():
        observation = {
            "date": date.strftime("%Y-%m-%d"),
            "ticker": canonical_ticker,
            "open": float(row["Open"]),
            "high": float(row["High"]),
            "low": float(row["Low"]),
            "close": float(row["Close"]),
            "volume": int(row["Volume"]),
        }

        prices.append(observation)

    prices.sort(key=lambda row: row["date"])

    return prices


def fetch_prices_for_ticker(ticker, period="1mo", interval="1d"):
    if ticker not in YAHOO_SYMBOL_MAPPING:
        supported = ", ".join(sorted(YAHOO_SYMBOL_MAPPING))
        raise ValueError(
            f"Unknown MarketPulse ticker '{ticker}'. Supported tickers: {supported}."
        )

    return fetch_yahoo_prices(ticker, lookback=period, interval=interval)
