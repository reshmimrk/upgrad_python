
## loc and iloc
import pandas as pd


df = pd.read_csv('https://query.data.world/s/vBDCsoHCytUSLKkLvq851k2b8JOCkF')

print(df)

df1 = df.loc[3]

print(df1)

df_2 = df.loc[3,"temp"]
print(df_2)

df3 = df.iloc[3]

print(df3)

df4 = df.iloc[3, 8]

print(df4)