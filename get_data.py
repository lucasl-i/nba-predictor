from sportsdataverse.nba import load_nba_schedule, load_nba_team_boxscore
import os

seasons = [2022, 2023, 2024, 2025]

os.makedirs("data", exist_ok=True)

schedule = load_nba_schedule(seasons=seasons, return_as_pandas=True)
print("Schedule shape (rows, columns):", schedule.shape)
print(schedule.columns.tolist())

team_box = load_nba_team_boxscore(seasons=seasons, return_as_pandas=True)
print("Team box score shape:", team_box.shape)
print(team_box.columns.tolist())

schedule.to_csv("data/nba_schedule.csv", index=False)
team_box.to_csv("data/nba_team_box.csv", index=False)
print("Saved!")