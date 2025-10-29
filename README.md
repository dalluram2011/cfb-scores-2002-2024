# College Football Scores (2002–2024)

Two visuals + a clean dataset to examine (1) scoring trends and (2) dominance since 2002.

## Files
- `data/processed/games_for_tableau_clean.csv` — one row per game, Tableau-ready
- `figures/output.png` — Avg total points per season
- `figures/output (1).png` — Top teams by Win% (min 150 games, regular season)
- `scripts/prep_tableau_extract.py` — data prep script (optional)
- `report/Technical_Report_2025-09-17.md` (or `.docx`)
- `portfolio/Portfolio_Post_Draft_2025-09-17.md`

  
## NCAA Football Dashboard (2002–2024)
**Live Dashboard:** [View on Tableau Public](https://public.tableau.com/app/profile/matthewdallura/viz/NCAAFootballDashboard)
**Report:** [Project2_Technical_Report.md](./Project2_Technical_Report.md)
**Data:** [games_for_tableau_clean.csv](./data/processed/games_for_tableau_clean.csv)


## Reproduce
Open `data/processed/games_for_tableau_clean.csv` in Tableau.
Create:
- Line: `AVG(total_points)` by `season`
- Bar: Team Win% (use `winner`; filter `postseason=False`; Min Games ≥150)

## Links
- Portfolio post (GitHub Pages): https://<your-username>.github.io/cfb-scores-2002-2024/
- Dataset source: Kaggle box scores (2002–2024)
