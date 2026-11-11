import pandas as pd

box = pd.read_csv("data/nba_team_box.csv")

regular_season = box[box["season_type"] == 2]

home_team = regular_season[regular_season["team_home_away"] == "home"]

count = home_team["team_name"].value_counts()
real_teams = count[count > 100].index
print("Number of real teams:", len(real_teams))   # must print 30

both_real = home_team["team_name"].isin(real_teams) & home_team["opponent_team_name"].isin(real_teams)
games = home_team[both_real]
print("Games before:", len(home_team), "| after:", len(games)) #checks all games vs games without unwanted ones (all-star teams)

games = games.sort_values(by="game_date") #sort games in chronological order

columns = ["game_date", "team_name", "opponent_team_name", "team_score", "opponent_team_score", "team_winner"]
games = games[columns]

games.to_csv("data/games.csv", index=False)