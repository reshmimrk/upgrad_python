"""Dataframes Merge
Description
Perform an inner merge on two data frames df_1 and df_2 on  'unique_id' and print the combined dataframe.
Execution Time Limit"""

import pandas as pd
df_1 = pd.read_csv('https://cdn.upgrad.com/uploads/production/1ed2840b-f083-44fe-9eb4-acda009ac620/restaurant-1.csv')
df_2 = pd.read_csv('https://cdn.upgrad.com/uploads/production/c87b99b4-467c-4128-8729-85bff0b0acbe/restaurant-2.csv')
df_3 = df_1.merge(df_2, on="unique_id", how="inner")#Type your code here.
print(df_3.head(20))