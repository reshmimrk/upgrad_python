"""Rename Columns"""

# Importing the pandas package
import pandas as pd

# Reading the dataframe
df = pd.read_csv('https://media-doselect.s3.amazonaws.com/generic/XWvQjYY4LZWdxLvPWOj2pPwn/heart.csv')

# Write your code here

df.columns = [name.title() for name in df.columns]

# Printing the final columns. Do not edit this part.
print(df.columns)