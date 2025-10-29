# Project 2 – Interactive Dashboard: NCAA Football Performance Trends (2002 – 2024)
**Author:** Matthew D'Allura  
**Date:** October 1, 2025  
**Repository:** https://github.com/dalluram2011/cfb-scores-2002-2024  
**Dashboard Link:** [Tableau Public URL here]  

---

## 1. Audience & Context
**Primary audience:** Athletic department analysts and sports information staff.  
They need a quick view of performance trends and context to support decisions about strategy and media narratives.  

**Secondary audience:** Fans and student media who want interactive exploration of scoring trends and team dominance.  

**Goal:** Provide a tool that summarizes seasonal performance and lets users filter by team, conference, and season range to spot trends and compare teams.

---

## 2. KPIs Chosen
| KPI | Formula | Rationale |
| ---- | --------- | ----------- |
| **Win %** | SUM([Win Flag])/COUNTD([Game ID]) | Quick success metric across teams or seasons. |
| **Avg Point Differential per Game** | AVG([points_for]-[points_against]) | Shows dominance and consistency. |
| **Avg Total Points per Game** | AVG([total_points]) | Measures pace and scoring environment. |
| **Close-Game Win %** | Wins in ≤ 7 pt games / Total ≤ 7 pt games | Highlights clutch performance. |

These KPIs were selected for clarity, comparability, and stakeholder relevance.

---

## 3. Dashboard Structure
**Layout:**
1. Header – global filters: Season range, Team multiselect, Home/Away/Neutral, Postseason toggle.  
2. Top row – KPI cards (Win %, Avg PD/G, Avg Total Pts/G, Close-Game Win %).  
3. Middle row – Left: Line chart of Avg Total Points by Season (annotated 2014 CFP & 2020 COVID). Right: Dominance table (Team | Win % | PD/G | Games).  
4. Bottom – Game detail table (Date | Opponent | Site | Score | Point Diff).  

**Interactions:**  
- Click a team → filters trend and detail table.  
- Hover tooltips define each KPI.  
- Parameters: Top N (5–25), Min Games (≥150), Close-Game Margin (≤7).  

---

## 4. Data Cleaning & Pre-processing
- Source: cfb_box-scores_2002-2024.csv from Kaggle.  
- Converted to games_for_tableau_clean.csv.  
- Derived columns: total_points, point_diff, winner, Win Flag, points_for, points_against.  
- Unioned home and away rows for team-level KPIs.  
- Removed null scores and standardized booleans (True/False).  

All steps documented in scripts/prep_tableau_extract.py.

---

## 5. Design Choices
| Element | Decision | Rationale |
| ---------- | ----------- | ------------- |
| Color | Neutral grays + 1 accent (blue/orange) | Accessibility & contrast |
| Typography | Sans-serif (Arial/Open Sans) | Legibility |
| Layout | Grid (12-col) | Predictable scan pattern |
| Annotations | 2014 & 2020 lines | Historical context |
| Tooltips | Plain language definitions | Transparency |

---

## 6. Reflection
**Worked well:** Tableau cross-filters made KPI cards dynamic and intuitive.  
**Challenges:** Union/pivot setup for team-game rows and balancing chart density.  
**Next steps:** Add conference filter and rolling averages; improve mobile layout.  

---

## 7. Code & Data Access
- **GitHub Repo:** https://github.com/dalluram2011/cfb-scores-2002-2024  
- **Dashboard (Tableau Public):** [Insert link]  
- **Dataset:** data/processed/games_for_tableau_clean.csv  

---

## 8. Transparency Note
Assignment developed with guidance from ChatGPT (GPT-5 Thinking) for formatting and clarity.
