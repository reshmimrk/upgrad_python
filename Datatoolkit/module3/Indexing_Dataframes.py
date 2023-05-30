"""
Indexing Dataframes
Description
Print only the even numbers of rows of the dataframe 'df'.

Note: Don't include the row indexed zero."""

import pandas as pd
df = pd.read_csv('https://cdn.upgrad.com/uploads/production/b3467ba4-4e13-44e9-8087-4d7e94cc7586/forestfires.csv')
df_2 = df.iloc[2::2,:]#Type your code here for indexing the dataframe
print(df_2.head(20))