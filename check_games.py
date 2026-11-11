import pandas as pd

games = pd.read_csv("data/games.csv")

# Check 1: any duplicated games?
print("Duplicate rows:", games.duplicated().sum())

# Check 2: games per team (home + away) over the 4 seasons
home = games["team_name"].value_counts()
away = games["opponent_team_name"].value_counts()
total = home.add(away, fill_value=0).sort_values(ascending=False)
print(total.head(8))
print(total.tail(3))