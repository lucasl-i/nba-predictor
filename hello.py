import pandas as pd

data = {
    "team": ["Liberty", "Aces", "Fever"],
    "wins": [30, 28, 22],
}
df = pd.DataFrame(data)
print(df)
print(df["wins"].mean())