"""Columns with Null values
How many columns have null values present in them? Try writing code for this instead of counting them manually."""

import pandas as pd

movies = pd.read_csv("Pandas/Movies.csv")

print(movies.isnull().any().sum())

#alternate method

print( ( movies.isnull().sum() > 0).sum())

print( movies.isnull().sum())
