from src.providers.yahoo_provider import fetch_prices_for_ticker


def check_canonical_rows(rows, ticker):
    assert len(rows) > 0, f"{ticker}: no data returned"
    for row in rows:
        assert row["ticker"] == ticker
        assert isinstance(row["date"], str) and len(row["date"]) == 10
        assert isinstance(row["open"], float)
        assert isinstance(row["high"], float)
        assert isinstance(row["low"], float)
        assert isinstance(row["close"], float)
        assert isinstance(row["volume"], int)
    assert [row["date"] for row in rows] == sorted(row["date"] for row in rows)


# 1. AAPL avec les paramètres par défaut (1 mois, quotidien)
apple = fetch_prices_for_ticker("AAPL")
check_canonical_rows(apple, "AAPL")
print("AAPL :", len(apple), "observations,", apple[0]["date"], "->", apple[-1]["date"])

# 2. SP500 : le ticker reste SP500, jamais ^GSPC
sp500 = fetch_prices_for_ticker("SP500")
check_canonical_rows(sp500, "SP500")
print("SP500 :", len(sp500), "observations,", sp500[0]["date"], "->", sp500[-1]["date"])

# 3. Transmission de period et interval
apple_3_months = fetch_prices_for_ticker("AAPL", period="3mo", interval="1d")
check_canonical_rows(apple_3_months, "AAPL")
assert len(apple_3_months) > len(apple)
print("AAPL 3 mois :", len(apple_3_months), "observations")

# 4. Ticker inconnu : ValueError avec un message explicite
try:
    fetch_prices_for_ticker("UNKNOWN")
except ValueError as error:
    print("UNKNOWN :", error)
else:
    raise AssertionError("Un ticker inconnu doit déclencher ValueError")

print("Tous les tests du TD08 ont réussi.")
