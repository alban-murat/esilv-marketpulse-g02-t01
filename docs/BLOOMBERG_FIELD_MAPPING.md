# Bloomberg Field Mapping

## 1. Objectif et modes autorisés

### Objectif

Ce document décrit comment convertir les données du fournisseur Bloomberg au format commun utilisé dans MarketPulse.

L'objectif est de pouvoir utiliser différentes sources de données, comme Yahoo Finance et Bloomberg, sans modifier les fonctions d'analyse financière développées lors du TD07.

Les observations doivent respecter un format canonique commun contenant sept champs : `date`, `ticker`, `open`, `high`, `low`, `close` et `volume`.

### Mode utilisé : APPROVED_SAMPLE

Deux modes sont prévus dans le projet :

- **APPROVED_SAMPLE** : utilise les données JSON de référence approuvées pour l'enseignement. Ce mode permet de tester le mapping et la normalisation sans disposer d'un Terminal Bloomberg.
- **LIVE** : correspond à une connexion réelle à Bloomberg dans un environnement autorisé. Ce mode nécessite une méthode d'accès fournie par l'enseignant.

Pour ce TD09, le mode utilisé est **APPROVED_SAMPLE**.

Les fichiers de référence disponibles dans le projet sont :

- `data/sample/bloomberg_reference_sample.json` : observations utilisées pour la normalisation.
- `data/sample/bloomberg_reference_expected.json` : résultats canoniques attendus.
- `labs/10_BLOOMBERG_INSTRUCTOR_REFERENCE.md` : documentation de référence du professeur.

Les valeurs du JSON sont des données pédagogiques issues du jeu de données d'exemple MarketPulse. Elles ne constituent pas une extraction historique Bloomberg certifiée.

Aucune connexion Bloomberg LIVE n'a été démontrée dans ce travail.

## 2. Identifiants AAPL / SP500

MarketPulse utilise des identifiants internes pour reconnaître les instruments financiers. Bloomberg possède ses propres identifiants.

Le tableau suivant présente les correspondances :

| Rôle | Ticker MarketPulse | Identifiant Bloomberg | Instrument |
|---|---|---|---|
| Instrument | AAPL | AAPL US Equity | Apple Inc. (action) |
| Benchmark | SP500 | SPX Index | S&P 500 (indice) |

L'identifiant Bloomberg permet de retrouver la série correspondante dans la source de données.

Lors de la normalisation, nous devons cependant conserver le ticker interne de MarketPulse dans le champ `ticker`.

Par exemple, une observation provenant de `AAPL US Equity` doit contenir `"ticker": "AAPL"` après normalisation.

De même, les observations provenant de `SPX Index` doivent contenir `"ticker": "SP500"`.

Cela permet aux fonctions Analytics de fonctionner de la même manière, quelle que soit la source utilisée.

### Structure des séries de référence

Dans le fichier JSON approuvé, les données sont regroupées dans une liste `series`.

Chaque série possède notamment :

- `provider_identifier` : identifiant utilisé par le fournisseur.
- `canonical_ticker` : identifiant interne MarketPulse.
- `observations` : liste des observations financières.

Le fichier de référence contient deux séries :

| Identifiant fournisseur | Ticker canonique | Nombre d'observations |
|---|---|---|
| AAPL US Equity | AAPL | 21 |
| SPX Index | SP500 | 21 |

Ces observations correspondent à des données pédagogiques quotidiennes de septembre 2026.

## 3. Correspondance des champs et types

Les observations du JSON approuvé utilisent des noms de champs différents de ceux de MarketPulse.

Lors de la normalisation, les champs doivent être renommés et les valeurs numériques converties dans les types attendus.

| Champ source APPROVED_SAMPLE | Champ MarketPulse | Type cible |
|---|---|---|
| observation_date | date | str (AAAA-MM-JJ) |
| canonical_ticker | ticker | str |
| open_value | open | float |
| high_value | high | float |
| low_value | low | float |
| close_value | close | float |
| volume_value | volume | int |

Le champ `canonical_ticker` appartient à la série JSON et non à chaque observation individuelle.

Les champs `open`, `high`, `low` et `close` sont convertis en `float`, tandis que `volume` est converti en `int`.

Le champ `date` reste une chaîne de caractères au format AAAA-MM-JJ.

Après normalisation, chaque observation doit contenir exactement ces sept champs :

`date`, `ticker`, `open`, `high`, `low`, `close`, `volume`.

### Distinction importante entre SAMPLE et LIVE

Les noms `observation_date`, `open_value`, `close_value`, etc. sont des **clés pédagogiques utilisées dans le fichier JSON approuvé**.

Ils ne doivent pas être présentés comme des noms de champs natifs de Bloomberg LIVE.

Dans un environnement LIVE, il faudrait relever les véritables noms de champs renvoyés par la connexion autorisée et documenter leur correspondance avec MarketPulse.

Aucun champ Bloomberg LIVE non vérifié n'est supposé dans ce document.

## 4. Exemple fictif : brut → canonique

Cet exemple utilise des données fictives pour illustrer la normalisation. Il ne s'agit pas de données réellement extraites d'un Terminal Bloomberg.

### Observation brute

L'observation suivante correspond à l'instrument `AAPL US Equity` :

```python
raw = {
    "observation_date": "2026-11-18",
    "open_value": "100.0",
    "high_value": "112.0",
    "low_value": "99.0",
    "close_value": "110.0",
    "volume_value": "1500"
}
```

### Observation normalisée

Après conversion, l'observation doit respecter le format canonique de MarketPulse :

```python
canonical = {
    "date": raw["observation_date"],
    "ticker": "AAPL",
    "open": float(raw["open_value"]),
    "high": float(raw["high_value"]),
    "low": float(raw["low_value"]),
    "close": float(raw["close_value"]),
    "volume": int(raw["volume_value"])
}
```

Le résultat attendu est :

```python
{
    "date": "2026-11-18",
    "ticker": "AAPL",
    "open": 100.0,
    "high": 112.0,
    "low": 99.0,
    "close": 110.0,
    "volume": 1500
}
```

### Vérification

On peut vérifier les valeurs et les types à l'aide d'assertions :

```python
assert canonical["ticker"] == "AAPL"
assert canonical["date"] == "2026-11-18"
assert isinstance(canonical["close"], float)
assert isinstance(canonical["volume"], int)

assert set(canonical) == {
    "date", "ticker", "open", "high",
    "low", "close", "volume"
}
```

Ces assertions permettent de vérifier que la normalisation respecte le contrat commun de MarketPulse.

Le ticker `AAPL` provient de l'identifiant interne `canonical_ticker` associé à la série Bloomberg.

Les valeurs numériques sont converties explicitement afin de pouvoir être utilisées par les fonctions financières du TD07.

## 5. Vérifications et limites du mode LIVE

### Vérifications des données

Avant d'utiliser les données Bloomberg dans MarketPulse, il faut vérifier que les observations respectent le format canonique.

Chaque observation doit contenir exactement sept champs : `date`, `ticker`, `open`, `high`, `low`, `close` et `volume`.

Les contrôles à effectuer sont les suivants :

- Vérifier que le ticker correspond à un identifiant interne valide (AAPL ou SP500).
- Vérifier que la date est une chaîne au format AAAA-MM-JJ.
- Vérifier que les prix sont de type `float`.
- Vérifier que le volume est de type `int`.
- Vérifier qu'aucun champ obligatoire n'est manquant.
- Vérifier que les séries sont correctement associées à leur identifiant fournisseur.

Ces contrôles permettront de détecter des observations incompatibles avec le format MarketPulse.

### Mode APPROVED_SAMPLE

Le mode APPROVED_SAMPLE utilise le JSON de référence fourni avec le projet.

Il permet de tester le mapping et la normalisation sans disposer d'un Terminal Bloomberg.

Les données sont des exemples pédagogiques et ne représentent pas une extraction Bloomberg LIVE.

Le fichier `bloomberg_reference_expected.json` contient les résultats attendus après normalisation.

Lors du TD10, les observations produites par le fournisseur devront être comparées aux résultats de ce fichier pour vérifier leur conformité.

La simple présence du fichier expected ne suffit pas à démontrer que les résultats correspondent : il faudra comparer effectivement les valeurs.

### Limites du mode LIVE

Le mode LIVE nécessiterait un accès autorisé à Bloomberg et une connexion réellement implémentée.

Cette fonctionnalité n'est pas encore disponible dans le travail présenté ici.

Il ne faut donc pas présenter les résultats du mode APPROVED_SAMPLE comme des données récupérées en temps réel depuis Bloomberg.

Si le mode LIVE est utilisé ultérieurement, les champs et la structure des données devront être vérifiés dans l'environnement réellement accessible.

### Transmission au TD10

Le TD10 aura pour objectif de développer `src/providers/bloomberg_provider.py` à partir du mapping documenté dans ce fichier.

Les éléments à conserver sont :

| Élément | Information |
|---|---|
| Mode utilisé pour les tests | APPROVED_SAMPLE |
| Instrument | AAPL |
| Identifiant Bloomberg instrument | AAPL US Equity |
| Benchmark | SP500 |
| Identifiant Bloomberg benchmark | SPX Index |
| Structure d'entrée | JSON contenant une liste `series`, chacune avec une liste `observations` |
| Représentation des dates | Chaîne AAAA-MM-JJ |
| Champs source | observation_date, open_value, high_value, low_value, close_value, volume_value |
| Identifiant interne | canonical_ticker, au niveau de la série |
| Champs canoniques | date, ticker, open, high, low, close, volume |
| Champs manquants | À contrôler explicitement lors de la validation des observations |
| Référence attendue | data/sample/bloomberg_reference_expected.json |
| Connexion Bloomberg LIVE | Non démontrée |

Le futur fournisseur devra lire le JSON approuvé, sélectionner la série correspondante, convertir les champs et produire les observations canoniques.

Il devra notamment conserver `AAPL` et `SP500` comme tickers internes.

Les fonctions Analytics déjà développées lors du TD07 pourront ensuite être réutilisées sans modification.

Aucune connexion LIVE ne devra être simulée et aucune donnée manquante ne devra être inventée.

Ce document constitue ainsi la référence de mapping pour l'implémentation du fournisseur Bloomberg lors du TD10.
