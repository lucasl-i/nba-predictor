import pandas as pd

CUTOFF = "2024-10-01"

# Model has to beat the baseline created by always predicting the home team to win.
games = pd.read_csv("data/games.csv")       # load the cleaned file

games_after_cutoff = games[games["game_date"] >= CUTOFF]

print(len(games_after_cutoff))                        # 1231 games after cutoff
print(games_after_cutoff["team_winner"].mean())       # home win rate 54.3%