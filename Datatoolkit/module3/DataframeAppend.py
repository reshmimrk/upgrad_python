"""Dataframe Append
Description
Append two datasets df_1 and df_2, and print the combined dataframe."""

# Suppressing warnings
import warnings
warnings.simplefilter("ignore")

import pandas as pd
df_1 = pd.read_csv('https://cdn.upgrad.com/uploads/production/1ed2840b-f083-44fe-9eb4-acda009ac620/restaurant-1.csv')
df_2 = pd.read_csv('https://cdn.upgrad.com/uploads/production/c87b99b4-467c-4128-8729-85bff0b0acbe/restaurant-2.csv')
df_3 = pd.concat([df_1, df_2], axis=0)   #Type your code here.

print(df_3.head())