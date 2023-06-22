"""Which movie is ranked 5th from the top in the list based on the net profit obtained?

Note: net profit = gross - budget
"""

import pandas as pd

movies = pd.read_csv("Pandas/Movies.csv")


movies = movies.drop( columns= ["color", "director_facebook_likes",  "actor_1_facebook_likes",  "actor_2_facebook_likes",  "actor_3_facebook_likes", 
"actor_2_name",   "cast_total_facebook_likes",   "actor_3_name",    "duration",    "facenumber_in_poster",
"content_rating",   "country",    "movie_imdb_link",     "aspect_ratio",    "plot_keywords"])

movies["language"] = movies.language.fillna("English")

movies["profit"] = movies["gross"] - movies["budget"]

movies = movies.sort_values(by="profit", ascending=False)

top_10 = movies.head(10).reset_index()

print(top_10["movie_title"][4])