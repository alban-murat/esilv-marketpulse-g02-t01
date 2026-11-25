
from src.providers.yahoo_provider import fetch_prices_for_ticker

# 1. Tester Apple
apple = fetch_prices_for_ticker("AAPL")
assert len(apple) > 0
assert apple[0]["ticker"] == "AAPL"
print("Test AAPL réussi")

# 2. Tester le S&P 500
sp500 = fetch_prices_for_ticker("SP500")
assert len(sp500) > 0
assert sp500[0]["ticker"] == "SP500"
print("Test SP500 réussi")

# 3. Tester une période différente
apple_3_months = fetch_prices_for_ticker(
    "AAPL", period="3mo", interval="1d"
)
assert len(apple_3_months) > 0
print("Test période 3 mois réussi")

# 4. Tester un ticker inconnu
try:
    fetch_prices_for_ticker("UNKNOWN")
except ValueError:
    print("Test UNKNOWN réussi")
else:
    raise AssertionError("Une exception ValueError était attendue")

print("Tous les tests du TD08 ont réussi.")
