"""DataFrames
Description
Given a dataframe 'df' use the following commands and analyse the result.
describe() 
columns
shape"""

#Need to add 2 extra lines for workng this code

import numpy as np
import pandas as pd
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
df = pd.read_csv('https://query.data.world/s/vBDCsoHCytUSLKkLvq851k2b8JOCkF')

print(df.describe())#Type your code for describing the dataset)
print(df.columns)#Type your code for printing the columns of the dataset)
print(df.shape)