"""Selecting Columns of a Dataframe
Description
Print out the columns 'month', 'day', 'temp', 'area' from the dataframe 'df'.

Execution Time Limit"""

import pandas as pd
###as we are getting error in upgrad terminal, need to add 2 extra lines for workng this code
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

df = pd.read_csv('https://query.data.world/s/vBDCsoHCytUSLKkLvq851k2b8JOCkF')
df_2 = df[["month", "day", "temp", "area"]]#Type your code for selecting columns 'month', 'day' , 'temp' , 'area'
print(df_2.head(20))