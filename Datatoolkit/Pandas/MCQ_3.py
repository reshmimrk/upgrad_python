"""Drop columns 

"color", "director_facebook_likes",  "actor_1_facebook_likes",  "actor_2_facebook_likes",  "actor_3_facebook_likes", 
"actor_2_name",   "cast_total_facebook_likes",   "actor_3_name",    "duration",    "facenumber_in_poster",
"content_rating",   "country",    "movie_imdb_link",     "aspect_ratio",    "plot_keywords"""

import pandas as pd

movies = pd.read_csv("Pandas/Movies.csv")


movies = movies.drop( columns= ["color", "director_facebook_likes",  "actor_1_facebook_likes",  "actor_2_facebook_likes",  "actor_3_facebook_likes", 
"actor_2_name",   "cast_total_facebook_likes",   "actor_3_name",    "duration",    "facenumber_in_poster",
"content_rating",   "country",    "movie_imdb_link",     "aspect_ratio",    "plot_keywords"])

print(movies.shape[1])