"""Impute Missing Values
Description
You're given a movies dataframe which contains quite a few aspects of some movies from 1916-2016. 
Here are the first few rows of the dataframe.

There are a lot of columns that aren't visible. But you might have noticed straight away that there are quite a 
few missing values in the data frame. Two columns for instance, 'aspect_ratio' and 'facenumber_in_poster' 
also have a few missing values(NaN). Now, replace the missing values with the 'median' value of the respective columns 
and print the null value count for both.

Expected Output: First print the number of missing values in both of these columns, then output the median in both the
 columns and then impute the missing values with the respective medians and print the count of missing values again. 
 Store all of these in a dictionary format like the following:

{'aspect_ratio_mv': 431, 'facenumber_in_poster_mv': 97}

{'aspect_ratio_median: 1.44, 'facenumber_in_poster': 2.0}

{'aspect_ratio_final': 0, 'facenumber_in_poster_final': 0}"""

# Importing the pandas package
import pandas as pd 

# Reading the movies dataframe
movies = pd.read_csv('https://media-doselect.s3.amazonaws.com/generic/1M2ZzY2M9PEBPJovgoaBgZdbM/movie_data.csv')

# Your aim is to complete the following three print statements after all the colons

aspect_nan_count = movies["aspect_ratio"].isna().sum()
facenum_nan_count = movies["facenumber_in_poster"].isna().sum()

med_val = movies[['aspect_ratio', 'facenumber_in_poster']].median()

movies[["aspect_ratio", "facenumber_in_poster"]] = movies[["aspect_ratio", "facenumber_in_poster"]].fillna(value=med_val)

final_aspect_nan_count = movies["aspect_ratio"].isna().sum()
final_facenum_nan_count = movies["facenumber_in_poster"].isna().sum()

mv = {'aspect_ratio_mv': aspect_nan_count, 'facenumber_in_poster_mv': facenum_nan_count}
median = {'aspect_ratio_median': med_val["aspect_ratio"], 'facenumber_in_poster_median': med_val["facenumber_in_poster"]}
final = {'aspect_ratio_final': final_aspect_nan_count, 'facenumber_in_poster_final': final_facenum_nan_count}

# # Printing the values in the three dictionaries. Please do not edit this part
print(sorted(mv.values()))
print(sorted(median.values()))
print(sorted(final.values()))

print()