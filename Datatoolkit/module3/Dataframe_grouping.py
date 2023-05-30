"""Dataframe grouping
Description
Group the dataframe 'df' by 'month' and 'day' and find the mean value for column 'rain' and 'wind'."""


import pandas as pd
df = pd.read_csv('https://cdn.upgrad.com/uploads/production/b3467ba4-4e13-44e9-8087-4d7e94cc7586/forestfires.csv')
#Type your groupby command here
df_1 = (df.groupby( by=['month', 'day']).mean())[["rain","wind"]] #Type your code to find the mean of columns 'rain' and 'wind'
print(df_1.head(20))