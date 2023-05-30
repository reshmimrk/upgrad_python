"""DataFrames
Description
Given a dataframe 'df' use the following commands and analyse the result.
describe() 
columns
shape"""

import pandas as pd

df= pd.read_csv('https://cdn.upgrad.com/uploads/production/b3467ba4-4e13-44e9-8087-4d7e94cc7586/forestfires.csv')
print(df.describe())
print(df.columns)
print(df.shape)