# Technical Report — NCAA Football Game Scores (2002–2024)

**Author:** [Your Name]  
**Date:** 2025-09-17

---

## 1) Dataset Origin & Description
- **Source:** Kaggle box scores, 2002–2024 (team names, scores, context like neutral site and game type).
- **Unit of analysis:** One row per **game** (after preprocessing).
- **Core fields:** `date`, `season`, `home_team`, `away_team`, `home_points`, `away_points`, `neutral_site`, `postseason`.
- **Derived fields:** `total_points`, `point_diff`, `winner`.

## 2) Preprocessing & Cleaning (with rationale)
1. **Column mapping:** From raw columns (`home`, `away`, `score_home`, `score_away`, `game_type`, `neutral`) to standardized fields.  
2. **Derived metrics:**  
   - `total_points = home_points + away_points`  
   - `point_diff = home_points - away_points`  
   - `winner = home_team if home_points > away_points else away_team`
3. **Flags:** `postseason = game_type != 'regular'` (where provided); `neutral_site` from raw `neutral`.
4. **Quality checks:** All seasons present; numeric parsing succeeded; dates converted to ISO strings.
5. **Export for Tableau:** `games_for_tableau_clean.csv` (no NaNs, True/False booleans).

**Repro command (example):**
```bash
# starting from the uploaded box-scores CSV
# (already executed during this session)
# outputs: /mnt/data/games_for_tableau_clean.csv
```

## 3) Visualization & Design Choices
- **Line (Avg Total Points by Season):** Direct lens on "scoring over time"; annotate 2014 (CFP) & 2020 (COVID).  
- **Bar (Top-N Win% since 2002):** Parameterize Top-N and Min Games (≥150). Filter `postseason = False` by default for fairness.  
- **Optional grouping:** Powerhouse vs mid-tier by long-run win% percentiles.

## 4) Results (draft state)
- **Figure A:** `output.png` — Avg total points by season.  
- **Figure B:** `output (1).png` — Top teams by win% (regular season, min 150 games).  
- **Tableau data source:** `games_for_tableau_clean.csv`.

## 5) Reflection
- **Worked well:** Simple pipeline from raw box scores to game-level CSV; fairness controls (min games).  
- **Challenges:** Team-name standardization can require a mapping file; 2020 irregularities.  
- **Next time:** Add opponent-strength adjustments and a decade-level “powerhouse vs mid-tier” panel.

## 6) Code & Reproducibility
- **Files:** `games_for_tableau_clean.csv` (for Tableau).  
- **Environment:** Python 3.x, pandas; Tableau for visuals.  
- **How to run:** Use the cleaned CSV directly in Tableau; recreate visuals as described.

## 7) Transparency (AI & Tools)
- Tableau for visuals; Python/pandas for preprocessing.  
- AI assistance: planning/drafting with ChatGPT (paste course-required chat link).