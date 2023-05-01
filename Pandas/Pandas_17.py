"""Dataframe Pivot Table
Description
Group the data 'df' by 'month' and 'day' and find the mean value for column 'rain' and 'wind' using the pivot table command."""

import numpy as np
import pandas as pd

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

df = pd.read_csv('https://query.data.world/s/vBDCsoHCytUSLKkLvq851k2b8JOCkF')

# print(df.head())
df_1 = df.pivot_table( index = ["month", "day"], values= ["rain", "wind"], aggfunc= "mean")#Type your code here. 
print(df_1.head(20))