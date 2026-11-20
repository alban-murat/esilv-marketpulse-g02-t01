# Checkpoint B – josephineSov

- Étudiante : Joséphine Sauvé (@josephineSov)
- Groupe / équipe : G02 – T01
- Dépôt : `esilv-marketpulse-g02-t01`

Checkpoint B est clôturé après le TD08. Ce dossier est complété au fil des TD05 à TD08.

## Preuves

| Fichier | TD | Contenu |
|---|---|---|
| `01_pull_request.png` | TD05 | PR #5 `feat: display market metadata` : `main` ← `feature/display-market-metadata`, autrice josephineSov, description What changed / Why / Validation |
| `02_code_review.png` | TD07 | ma revue (relectrice officielle, Student 2) de la PR #8 `feat: add core quantitative analytics module` d'alban-murat : vérifications détaillées et **Approve**, PR fusionnée après la revue |
| `02_code_review_pr4.png` | TD06 | ma revue de la PR #4 d'alban-murat (`feat: display data provider label in summary`) : commentaire technique et **Approve** |
| `pr5_review_merged.png` | TD06 | ma PR #5 relue et approuvée par PAULCO6, puis fusionnée dans `main` après la revue |
| `td07_comparison_run.png` | TD07 | `python src/main.py` sur `main` après le merge : bloc de comparaison et base 100 |

## TD05 – Remote branch + Pull Request

- Team Baseline Gate : `archive/td04-local` créée (locale), `main` aligné sur `origin/main`.
- Branche `feature/display-market-metadata` créée depuis le `main` commun.
- Commit `feat: display market metadata` : helper `display_market_metadata(asset)` qui affiche `market` et `currency`, réutilisé pour l'instrument (NASDAQ, USD) et le benchmark (US, USD).
- `git push -u origin feature/display-market-metadata`, puis PR #5 vers le `main` de l'équipe.

## TD06 – Code review

- Revue de la PR #4 : Files changed vérifié (1 ligne dans `src/main.py`), exécution de `python src/main.py` sur la branche, description cohérente avec le diff. Suggestion non bloquante : utiliser une constante `PROVIDER_LABEL` plutôt que `"CSV"` en dur. Résultat : **Approve**.
- Ma PR #5 a été approuvée par PAULCO6 sans correction demandée, donc aucun commit de correction. Fusionnée après la revue.
- `main` local synchronisé avec `git switch main` puis `git pull`, et `python src/main.py` fonctionne.

## TD07 – Data normalization + comparison

- Rôle : Student 2. J'ai codé `index_by_date` et `calculate_relative_performance` dans `src/analytics.py`, sur la branche commune `feature/analytics` :
  - `7ed7509 feat(analytics): implement index_by_date`
  - `09ee508 feat(analytics): implement calculate_relative_performance`
- Relectrice officielle de la PR #8 : vérification des 5 fonctions, de la pureté du module (pas de `print`, pas de chargement de données), des formules, des cas limites (série vide, premier close à 0), de l'alignement et des valeurs attendues. **Approve**, puis merge par le Lead.
- `main` local synchronisé (`git switch main`, `git pull origin main`), branche locale `feature/analytics` supprimée avec `git branch -d`.
- Résultat de `python src/main.py` : 21 séances alignées, AAPL +6.48 %, SP500 +2.15 %, performance relative +4.33 points, base 100 : 106.48 contre 102.15.
