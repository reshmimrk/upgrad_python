"""Indexing Dataframes
Description
Print only the even numbers of rows of the dataframe 'df'.

Note: Don't include the row indexed zero."""

import pandas as pd

###as we are getting error in upgrad terminal, need to add 2 extra lines for workng this code
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

df = pd.read_csv('https://query.data.world/s/vBDCsoHCytUSLKkLvq851k2b8JOCkF')
df_2 = df.iloc[2::2,:]#Type your code here for indexing the dataframe  # 2 to end with a step of 2
print(df_2.head(20))