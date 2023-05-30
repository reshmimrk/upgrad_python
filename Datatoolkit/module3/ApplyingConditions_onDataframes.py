"""Applying Conditions on Dataframes
Description
Print all the columns and the rows where 'area' is greater than 0, 'wind' is greater than 1 and the 'temp' is greater than 15."""

import pandas as pd
df = pd.read_csv('https://cdn.upgrad.com/uploads/production/b3467ba4-4e13-44e9-8087-4d7e94cc7586/forestfires.csv')
df_2 =  df[ (df['area'] > 0) & (df['wind'] > 1) & (df['temp'] > 15) ]#Type your code here.
print(df_2.head(20))