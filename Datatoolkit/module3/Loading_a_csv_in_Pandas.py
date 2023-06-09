"""
Loading a csv in Pandas

Description
Create a dataframe from the file ‘marks.csv’ and print the contents of the dataframe. 
Open the file from the link above and inspect the required elements in the file (header, separator, etc.).
If the top row is a regular entry, do not load it as the column header."""

import numpy as np
import pandas as pd

# The file is stored at the following path:
# 'https://media-doselect.s3.amazonaws.com/generic/A08MajL8qN4rq72EpVJbAP1Rw/marks_1.csv'
# Provide your answer below

df = pd.read_csv('https://media-doselect.s3.amazonaws.com/generic/A08MajL8qN4rq72EpVJbAP1Rw/marks_1.csv', header=None, sep = '|')

print(df)