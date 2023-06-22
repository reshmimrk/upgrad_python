"""
Analysing dataframes
Suppose movies are divided into 5 buckets based on the IMDb ratings:

[7.5, 8)
[8, 8.5)
[8.5, 9)
[9, 9.5)
[9.5, 10)
Which bucket holds the maximum number of movies from IMDb_Top_250?
"""

import pandas as pd

movies = pd.read_csv("Pandas/Movies.csv")


movies = movies.drop( columns= ["color", "director_facebook_likes",  "actor_1_facebook_likes",  "actor_2_facebook_likes",  "actor_3_facebook_likes", 
"actor_2_name",   "cast_total_facebook_likes",   "actor_3_name",    "duration",    "facenumber_in_poster",
"content_rating",   "country",    "movie_imdb_link",     "aspect_ratio",    "plot_keywords"])

movies["language"] = movies.language.fillna("English")

movies["profit"] = movies["gross"] - movies["budget"]

column_names = movies.columns

"""    'director_name', 'num_critic_for_reviews', 'gross', 'genres',
       'actor_1_name', 'movie_title', 'num_voted_users',
       'num_user_for_reviews', 'language', 'budget', 'title_year',
       'imdb_score', 'movie_facebook_likes', 'profit'
"""


imdb_top_250 = movies[movies["num_voted_users"] > 25000].sort_values(by="imdb_score", ascending=False).reset_index(drop=True).head(250)
rank_val_list = list(range(1,251))
imdb_top_250["Rank"] = rank_val_list

def bucket_group(val):
    if (val >=7.5) and (val < 8):
        return "bucket_1"
    elif (val >=8) and (val < 8.5):
        return "bucket_2"
    elif (val >=8.5) and (val < 9):
        return "bucket_3"
    elif (val >=9) and (val < 9.5):
        return "bucket_4"
    elif (val >=9.5) and (val <= 10):
        return "bucket_5"


imdb_top_250["Bucket"] = imdb_top_250["imdb_score"].apply(bucket_group)
imdb_top_250 = imdb_top_250.groupby(by= "Bucket").size()

print(imdb_top_250)

##  Alternate solution from upgrad


# IMDb_Top_250 = movies.sort_values(by = 'imdb_score', ascending = False)
# IMDb_Top_250 = IMDb_Top_250.loc[IMDb_Top_250.num_voted_users > 25000]
# IMDb_Top_250 = IMDb_Top_250.iloc[:250, ]
# IMDb_Top_250['Rank'] = range(1,251)

# import matplotlib.pyplot as plt
# plt.hist(IMDb_Top_250['imdb_score'], bins = 5, range = (7.5,10), edgecolor = 'cyan')
# plt.show()