import pandas as pd

HOME_BONUS = 50         # taking into account home team advantage, add 50 to rating
CUTOFF = "2024-10-01"

def expected_win(rating_a, rating_b):
        rating = 1 / (1 + 10 ** ((rating_b - rating_a) / 400))
        return rating

def update_ratings(rating_home, rating_away, home_won, k=20, home_bonus=0):
    expected = expected_win(rating_home + home_bonus, rating_away)
    actual_home = int(home_won)
    actual_away = int(not home_won)

    new_home = rating_home + k * (actual_home - expected)
    new_away = rating_away + k * (actual_away - (1 - expected))

    return new_home, new_away


# STORING THE RATINGS
games = pd.read_csv("data/games.csv")

ratings = {}
correct_before_cutoff = 0
total_before_cutoff = 0
correct_after_cutoff = 0
total_after_cutoff = 0

for index, row in games.iterrows():
    home_rating = ratings.get(row["team_name"], 1500)  #default rating of 1500
    away_rating = ratings.get(row["opponent_team_name"], 1500)

    home_expected = expected_win(home_rating + HOME_BONUS, away_rating)
    predicted_home_win = home_expected > 0.5  # Equal to True if home team is predicted to win
    was_correct = (predicted_home_win == row["team_winner"])

    if row["game_date"] < CUTOFF:
         total_before_cutoff += 1
         if was_correct:
              correct_before_cutoff += 1
    else:
         total_after_cutoff += 1
         if was_correct:
              correct_after_cutoff += 1

    home_updated = update_ratings(home_rating, away_rating, row["team_winner"], HOME_BONUS)

    ratings[row["team_name"]] = home_updated[0]
    ratings[row["opponent_team_name"]] = home_updated[1]

print("Avant", CUTOFF, ":", total_before_cutoff, "matchs,", correct_before_cutoff / total_before_cutoff)
print("Après", CUTOFF, ":", total_after_cutoff, "matchs,", correct_after_cutoff / total_after_cutoff)