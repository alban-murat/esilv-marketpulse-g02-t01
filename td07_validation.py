
from src.analytics import (
    align_series,
    calculate_period_return,
    calculate_base_100,
    calculate_relative_performance,
)

# Deux séries fictives avec des dates différentes
instrument = [
    {"date": "2026-11-20", "ticker": "AAPL", "close": 100},
    {"date": "2026-11-21", "ticker": "AAPL", "close": 110},
    {"date": "2026-11-22", "ticker": "AAPL", "close": 121},
]

benchmark = [
    {"date": "2026-11-20", "ticker": "SP500", "close": 200},
    {"date": "2026-11-22", "ticker": "SP500", "close": 210},
    {"date": "2026-11-23", "ticker": "SP500", "close": 220},
]

# 1. Vérification de l'alignement des dates
aligned_instrument, aligned_benchmark = align_series(instrument, benchmark)

assert [row["date"] for row in aligned_instrument] == [
    "2026-11-20", "2026-11-22"
]
assert [row["date"] for row in aligned_benchmark] == [
    "2026-11-20", "2026-11-22"
]

# 2. Vérification du rendement
instrument_return = calculate_period_return(aligned_instrument)
benchmark_return = calculate_period_return(aligned_benchmark)

assert round(instrument_return, 2) == 21.0
assert round(benchmark_return, 2) == 5.0

# 3. Vérification de la base 100
base_100 = calculate_base_100(aligned_instrument)

assert round(base_100[0]["value"], 2) == 100.0
assert round(base_100[-1]["value"], 2) == 121.0

# 4. Vérification de la performance relative
relative_performance = calculate_relative_performance(
    instrument_return, benchmark_return
)

assert round(relative_performance, 2) == 16.0

# 5. Vérification d'une série vide
try:
    calculate_period_return([])
except ValueError:
    pass
else:
    raise AssertionError("Une série vide doit déclencher ValueError")

print("Tous les tests du TD07 ont réussi.")
