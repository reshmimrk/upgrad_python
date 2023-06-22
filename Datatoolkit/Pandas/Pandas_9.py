"""Applying Conditions on Dataframes
Description
Print all the columns and the rows where 'area' is greater than 0, 'wind' is greater than 1 and the 'temp' is greater than 15.
Execution Time Limit"""

import pandas as pd

import ssl
ssl._create_default_https_context = ssl._create_unverified_context
df = pd.read_csv('https://query.data.world/s/vBDCsoHCytUSLKkLvq851k2b8JOCkF')

# print(df)
df_2 = df[ (df['area'] > 0) & (df['wind'] > 1) & (df['temp'] > 15) ]#Type your code here.
print(df_2.head(20))