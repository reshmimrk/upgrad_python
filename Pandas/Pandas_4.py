"""Hierarchical Indexing
Description
You are provided with the dataset of a company which has offices across three cities 
- Mumbai, Bangalore and New Delhi. The dataset contains the rating (out of 5) 
of all the employees from different departments (Finance, HR, Marketing and Sales). 
Create a hierarchical index based on two columns: Office and Department
Print the first 5 rows as the output. Refer to the image below for your reference.
Note: You should not sort or modify values in other columns of the dataframe. Use sort_index(inplace=True) 
to club the same locations together."""

import numpy as np
import pandas as pd

# The file is stored at the following path:
# 'https://media-doselect.s3.amazonaws.com/generic/NMgEjwkAEGGQZBoNYGr9Ld7w0/rating.csv'
df = pd.read_csv('https://media-doselect.s3.amazonaws.com/generic/NMgEjwkAEGGQZBoNYGr9Ld7w0/rating.csv', index_col=['Office', 'Department'])

# Provide your answer below
df.sort_index( inplace=True )

print(df.head(5))

## Alternate method 


df = pd.read_csv('https://media-doselect.s3.amazonaws.com/generic/NMgEjwkAEGGQZBoNYGr9Ld7w0/rating.csv')

# Provide your answer below
df.set_index(['Office', 'Department'], inplace=True)
df.sort_index( inplace=True )

print(df.head(5))

###
