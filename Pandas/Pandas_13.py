"""Dataframe grouping
Description
Group the dataframe 'df' by 'month' and 'day' and find the mean value for column 'rain' and 'wind'."""

import pandas as pd
df = pd.read_csv('https://query.data.world/s/vBDCsoHCytUSLKkLvq851k2b8JOCkF')
#Type your groupby command here
df_1 = (df.groupby( by=['month', 'day']).mean())[["rain","wind"]]#Type your code to find the mean of columns 'rain' and 'wind'
print(df_1.head(20))