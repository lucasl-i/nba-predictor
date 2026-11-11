import pandas as pd

# Model has to beat the baseline created by always predicting the home team to win.

box = pd.read_csv("data/nba_team_box.csv")

regular_season = box[box["season_type"] == 2]
# playoffs_game = box[box["season_type"] == 3]
# playin_game = box[box["season_type"] == 5]


home_team = regular_season[regular_season["team_home_away"] == "home"]

print(len(home_team))
print(home_team["team_winner"].mean()) #Output: 0.55

sorted_dates = home_team.sort_values(by = "game_date") # sort dates in ascending order to use last 10 game feature
columns = ["game_date", "team_name", "opponent_team_name", "team_score", "opponent_team_score", "team_winner"]
print(home_team[columns].head(10))
