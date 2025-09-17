import argparse
import pandas as pd
from pathlib import Path

def load_team_map(path: Path) -> dict:
    if path is None or not path.exists():
        return {}
    df = pd.read_csv(path)
    df.columns = [c.strip().lower() for c in df.columns]
    # Expect columns: original, canonical
    if not set(['original', 'canonical']).issubset(df.columns):
        raise ValueError("teams_dim.csv must have columns: original, canonical")
    return dict(zip(df['original'].astype(str).str.strip(), df['canonical'].astype(str).str.strip()))

def canon_name(name: str, mapping: dict) -> str:
    if pd.isna(name):
        return name
    key = str(name).strip()
    return mapping.get(key, key)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--in', dest='inp', required=True, help='Path to raw Kaggle CSV')
    ap.add_argument('--out', dest='outp', required=True, help='Path to output cleaned CSV for Tableau')
    ap.add_argument('--teams', dest='teams', default=None, help='Path to teams_dim.csv (original,canonical)')
    args = ap.parse_args()

    in_path = Path(args.inp)
    out_path = Path(args.outp)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    team_map = load_team_map(Path(args.teams)) if args.teams else {}

    # Read raw CSV
    df = pd.read_csv(in_path)

    # Standardize column names
    df.columns = [c.strip().lower() for c in df.columns]

    # Expected columns (best effort): date, season, home_team, away_team, home_points, away_points
    # Optional columns: home_conference, away_conference, neutral_site, postseason
    # Rename common variants if found
    rename_map = {
        'home_score': 'home_points',
        'away_score': 'away_points',
        'home_pts': 'home_points',
        'away_pts': 'away_points',
    }
    df = df.rename(columns=rename_map)

    required = ['date', 'season', 'home_team', 'away_team', 'home_points', 'away_points']
    missing = [c for c in required if c not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}. "
                         f"Make sure your Kaggle CSV uses common names or update rename_map.")

    # Canonicalize names
    df['home_team'] = df['home_team'].apply(lambda x: canon_name(x, team_map))
    df['away_team'] = df['away_team'].apply(lambda x: canon_name(x, team_map))

    # Derived fields
    df['total_points'] = df['home_points'].astype(float) + df['away_points'].astype(float)
    df['point_diff'] = df['home_points'].astype(float) - df['away_points'].astype(float)
    df['winner'] = df.apply(lambda r: r['home_team'] if r['home_points'] > r['away_points'] else r['away_team'], axis=1)

    # Optional flags with safe defaults
    for col, default in [('neutral_site', False), ('postseason', False)]:
        if col not in df.columns:
            df[col] = default

    # Optional conferences (left if missing)
    if 'home_conference' not in df.columns:
        df['home_conference'] = None
    if 'away_conference' not in df.columns:
        df['away_conference'] = None

    # Tidy export columns
    keep = ['date', 'season', 'home_team', 'away_team', 'home_points', 'away_points',
            'total_points', 'point_diff', 'winner', 'neutral_site', 'postseason',
            'home_conference', 'away_conference']
    tidy = df[keep].copy()

    # Ensure date is ISO formatted string (Tableau-friendly)
    try:
        tidy['date'] = pd.to_datetime(tidy['date']).dt.date.astype(str)
    except Exception:
        pass

    tidy.to_csv(out_path, index=False)
    print(f"Wrote {len(tidy):,} rows to {out_path}")

if __name__ == '__main__':
    main()
