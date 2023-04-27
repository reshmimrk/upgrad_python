import pandas as pd

df = pd.read_csv('Pandas\weatherdata.csv')

print(df.head())

df["year"] = pd.DatetimeIndex( df["Date"]).year
df["month"] = pd.DatetimeIndex( df["Date"]).month
df["day"] = pd.DatetimeIndex( df["Date"]).day
df["dayofweek"] = pd.DatetimeIndex( df["Date"]).day_of_week


print(df.head())