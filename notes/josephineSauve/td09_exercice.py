"""TD09 - Exercice : corriger une mauvaise normalisation (données fictives)."""

CANONICAL_KEYS = {"date", "ticker", "open", "high", "low", "close", "volume"}

wrong = {
    "date": "2026-11-18",
    "ticker": "AAPL US Equity",
    "open": "100.0",
    "high": 112.0,
    "low": 99.0,
    "close": 110.0,
    "volume": "1500",
}

# 1. Champs au mauvais type : open est une chaîne (float attendu),
#    volume est une chaîne (int attendu).
# 2. Ticker interne correct : "AAPL" ("AAPL US Equity" est l'identifiant Bloomberg).

# 3. Trois assertions qui échouent sur le dictionnaire incorrect
failing_checks = [
    ("ticker interne", lambda row: row["ticker"] == "AAPL"),
    ("open en float", lambda row: isinstance(row["open"], float)),
    ("volume en int", lambda row: isinstance(row["volume"], int)),
]

for name, check in failing_checks:
    try:
        assert check(wrong)
    except AssertionError:
        print(f"Assertion échouée comme prévu : {name}")
    else:
        raise AssertionError(f"Cette assertion aurait dû échouer : {name}")

# 4. Dictionnaire corrigé
fixed = {
    "date": "2026-11-18",
    "ticker": "AAPL",
    "open": 100.0,
    "high": 112.0,
    "low": 99.0,
    "close": 110.0,
    "volume": 1500,
}

assert set(fixed) == CANONICAL_KEYS
assert fixed["ticker"] == "AAPL"
assert fixed["date"] == "2026-11-18"
for field in ("open", "high", "low", "close"):
    assert isinstance(fixed[field], float), field
assert isinstance(fixed["volume"], int)
for name, check in failing_checks:
    assert check(fixed), name

print("Dictionnaire corrigé : 7 clés, ticker AAPL, types numériques corrects.")
