import pandas as pd

def expected_win(rating_a, rating_b):
        rating = 1 / (1 + 10 ** ((rating_b - rating_a) / 400))
        return rating

def update_ratings(rating_home, rating_away, home_won, k=20):
    expected = expected_win(rating_home, rating_away)
    actual_home = int(home_won)
    actual_away = int(not home_won)

    new_home = rating_home + k * (actual_home - expected)
    new_away = rating_away + k * (actual_away - (1 - expected))

    return new_home, new_away

# STORING THE RATINGS
games = pd.read_csv("data/games.csv")

ratings = {}
correct = 0

for index, row in games.iterrows():
    home_rating = ratings.get(row["team_name"], 1500)  #default rating of 1500
    away_rating = ratings.get(row["opponent_team_name"], 1500)

    home_expected = expected_win(home_rating, away_rating)

    predicted_home_win = home_expected > 0.5  # Equal to True if home team is predicted to win

    if (predicted_home_win == row["team_winner"]): #checks if our predicted winner was the real winner
        correct += 1

    home_updated = update_ratings(home_rating, away_rating, row["team_winner"])

    ratings[row["team_name"]] = home_updated[0]
    ratings[row["opponent_team_name"]] = home_updated[1]

print(len(games))                              # number of games
print(correct / len(games))                    # accuracy
print(sum(ratings.values()) / len(ratings))    # average rating