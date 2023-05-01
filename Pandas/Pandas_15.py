"""
Dataframe Append
Description
Append two datasets df_1 and df_2, and print the combined dataframe.
"""
# Suppressing warnings
import warnings
warnings.simplefilter("ignore")

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

import pandas as pd
df_1 = pd.read_csv('https://query.data.world/s/vv3snq28bp0TJq2ggCdxGOghEQKPZo')
df_2 = pd.read_csv('https://query.data.world/s/9wVKjNT0yiRc3YbVJaiI8a6HGl2d74')

print(df_1)
print("------------------------------------------------------------------------------")
print(df_2.head)
df_3 = pd.concat([df_1, df_2], axis=0)  #Type your code here.

print(df_3.head())