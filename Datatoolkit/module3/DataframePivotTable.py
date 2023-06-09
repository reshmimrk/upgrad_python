"""Dataframe Pivot Table
Description
Group the data 'df' by 'month' and 'day' and find the mean value for column 
'rain' and 'wind' using the pivot table command."""

import numpy as np
import pandas as pd
df = pd.read_csv('https://cdn.upgrad.com/uploads/production/b3467ba4-4e13-44e9-8087-4d7e94cc7586/forestfires.csv')
df_1 = df.pivot_table( index = ["month", "day"], values= ["rain", "wind"], aggfunc= "mean")#Type your code here. 
print(df_1.head(20))