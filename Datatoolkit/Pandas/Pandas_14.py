"""Dataframes Merge
Description
Perform an inner merge on two data frames df_1 and df_2 on  'unique_id' and print the combined dataframe."""

import pandas as pd
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
df_1 = pd.read_csv('https://query.data.world/s/vv3snq28bp0TJq2ggCdxGOghEQKPZo')
df_2 = pd.read_csv('https://query.data.world/s/9wVKjNT0yiRc3YbVJaiI8a6HGl2d74')

# print(df_1.head())
# print("------------------------------------------------------------------------------")
# print(df_2.head())
df_3 = df_1.merge(df_2, on="unique_id", how="inner")#Type your code here.
# print("\n\n")
print(df_3.head(20))