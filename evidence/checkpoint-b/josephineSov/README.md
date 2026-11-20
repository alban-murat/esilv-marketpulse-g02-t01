# Checkpoint B – josephineSov

- Étudiante : Joséphine Sauvé (@josephineSov)
- Groupe / équipe : G02 – T01
- Dépôt : `esilv-marketpulse-g02-t01`

Checkpoint B est clôturé après le TD08. Ce dossier est complété au fil des TD05 à TD08.

## Preuves

| Fichier | TD | Contenu |
|---|---|---|
| `01_pull_request.png` | TD05 | PR #5 `feat: display market metadata` : `main` ← `feature/display-market-metadata`, autrice josephineSov, description What changed / Why / Validation |
| `02_code_review.png` | TD06 | ma revue de la PR #4 d'alban-murat (`feat: display data provider label in summary`) : commentaire technique et **Approve** |
| `pr5_review_merged.png` | TD06 | ma PR #5 relue et approuvée par PAULCO6, puis fusionnée dans `main` après la revue |

## TD05 – Remote branch + Pull Request

- Team Baseline Gate : `archive/td04-local` créée (locale), `main` aligné sur `origin/main`.
- Branche `feature/display-market-metadata` créée depuis le `main` commun.
- Commit `feat: display market metadata` : helper `display_market_metadata(asset)` qui affiche `market` et `currency`, réutilisé pour l'instrument (NASDAQ, USD) et le benchmark (US, USD).
- `git push -u origin feature/display-market-metadata`, puis PR #5 vers le `main` de l'équipe.

## TD06 – Code review

- Revue de la PR #4 : Files changed vérifié (1 ligne dans `src/main.py`), exécution de `python src/main.py` sur la branche, description cohérente avec le diff. Suggestion non bloquante : utiliser une constante `PROVIDER_LABEL` plutôt que `"CSV"` en dur. Résultat : **Approve**.
- Ma PR #5 a été approuvée par PAULCO6 sans correction demandée, donc aucun commit de correction. Fusionnée après la revue.
- `main` local synchronisé avec `git switch main` puis `git pull`, et `python src/main.py` fonctionne.
