import pandas as pd

df = pd.read_csv("spotify_history.csv")
print(df[['track_name','reason_start']].head())