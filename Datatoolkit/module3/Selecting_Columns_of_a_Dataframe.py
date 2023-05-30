"""Selecting Columns of a Dataframe
Description
Print out the columns 'month', 'day', 'temp', 'area' from the dataframe 'df'."""

import pandas as pd
df = pd.read_csv('https://cdn.upgrad.com/uploads/production/b3467ba4-4e13-44e9-8087-4d7e94cc7586/forestfires.csv')
df_2 = df[["month", "day", "temp", "area"]]#Type your code for selecting columns 'month', 'day' , 'temp' , 'area'
print(df_2.head(20))