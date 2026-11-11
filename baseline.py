import pandas as pd

# Model has to beat the baseline created by always predicting the home team to win.

box = pd.read_csv("data/nba_team_box.csv")

regular_season = box[box["season_type"] == 2]

home_team = regular_season[regular_season["team_home_away"] == "home"]

games = pd.read_csv("data/games.csv")    # load the cleaned file
print(len(games))                        # 4922
print(games["team_winner"].mean())       # home win rate 55%