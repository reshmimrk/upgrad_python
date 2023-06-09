"""Employee Training
Description
You are provided with the dataset of a company which has offices across three cities - 
Mumbai, Bangalore and New Delhi. The dataset contains the rating (out of 5) of all the employees 
from different departments (Finance, HR, Marketing and Sales). 

The company has come up with a new policy that any individual with a rating equal 
to or below 3.5 needs to attend a training. Using dataframes, load the dataset and 
then derive the column ‘Training’ which shows ‘Yes’ for people who require training and ‘No’ for those who do not.

Print the first 5 rows as the output. Refer to the image below for your reference.
Note: You should not sort or modify values in other columns of the dataframe."""

import numpy as np
import pandas as pd

# The file is stored at the following path:
# 'https://media-doselect.s3.amazonaws.com/generic/NMgEjwkAEGGQZBoNYGr9Ld7w0/rating.csv'
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
df = pd.read_csv('https://media-doselect.s3.amazonaws.com/generic/NMgEjwkAEGGQZBoNYGr9Ld7w0/rating.csv')

# Provide your answer below
df["Training"] = df["Rating"].apply( lambda x: 'Yes' if x <=3.5 else 'No')
print(df.head())