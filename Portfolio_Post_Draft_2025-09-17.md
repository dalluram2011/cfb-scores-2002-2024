# Portfolio Post Draft (Public-Facing Story)

**Title:** Are College Football Games Really Getting Wilder? Two Decades of Scores, 2002–2024

**Deck (1 sentence):** Using 20+ seasons of game-level results from a Kaggle box-scores dataset, I test whether scoring has climbed and which programs dominated.

## The Question (Plain Language)
Are college football games becoming higher scoring over time? Which conferences and teams have shown the most dominance since 2002—and how do traditional powerhouses compare to mid-tier programs?

## What the Data Is (Brief, Non-Technical)
Game-level box scores from 2002–2024. Each row represents a game with date, teams, and final scores. This post uses total points per game and team win percentage. Full technical details are in the Technical Report.

## Visual 1 — Season Scoring Trend (2002–2024)
_(Insert image: `output.png`)_  
**What to notice:** Average total points per game show a long-run trend, with inflection points around the 2014 College Football Playoff launch and the 2020 COVID anomaly.

## Visual 2 — Dominance Since 2002 (Top-N by Win Percentage)
_(Insert image: `output (1).png`)_  
**What to notice:** A small set of teams maintain the highest long-run win rates. A minimum-games threshold (e.g., 150+) keeps rankings fair.

## (Optional) Visual 3 — Powerhouses vs. Mid-Tier
Group teams by long-run win percentage (powerhouse = top quartile with ≥150 games; mid-tier = middle quartiles). Compare scoring or point differential by decade.

## Why This Matters
If games are getting higher scoring, it affects strategy (offense vs. defense balance) and feeds into debates about rules. Identifying dominance patterns ties into playoff expansion and conference realignment discussions.

## Limitations (Transparency)
- Team name standardization (e.g., “Alabama Crimson Tide” vs “Alabama”).
- Postseason and neutral-site games flagged and optionally excluded.
- 2020 schedules were irregular.
- Conference membership changes over time; treat conference as seasonal, not fixed.

## Sources & Notes
- **Data:** Kaggle box scores (2002–2024).  
- **Tools:** Tableau for visualizations; Python/pandas for preprocessing.  
- **AI Assistance:** Planning/drafting with ChatGPT (paste course-required chat link).