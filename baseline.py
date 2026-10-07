import pandas as pd

# Model has to beat the baseline created by always predicting the home team to win.

box = pd.read_csv("data/nba_team_box.csv")

regular_season = box[box["season_type"] == 2]
# playoffs_game = box[box["season_type"] == 3]
# playin_game = box[box["season_type"] == 5]


home_team = regular_season[regular_season["team_home_away"] == "home"]

print(len(home_team))
print(home_team["team_winner"].mean()) #Output: 0.55


