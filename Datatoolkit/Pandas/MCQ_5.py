"""Replacing Null values
What is the count of movies made in the English language after replacing the NaN values with English?"""

import pandas as pd

movies = pd.read_csv("Pandas/Movies.csv")


movies = movies.drop( columns= ["color", "director_facebook_likes",  "actor_1_facebook_likes",  "actor_2_facebook_likes",  "actor_3_facebook_likes", 
"actor_2_name",   "cast_total_facebook_likes",   "actor_3_name",    "duration",    "facenumber_in_poster",
"content_rating",   "country",    "movie_imdb_link",     "aspect_ratio",    "plot_keywords"])

movies["language"] = movies.language.fillna("English")

print(movies.language.value_counts()["English"])

# alternate approach

# movies.loc[pd.isnull(movies["language"]), ["language"]] = 'English'

# print((movies.language == 'English').sum())  
# 
# #  approaximate ans 3674 