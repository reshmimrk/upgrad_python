"""**Subtask 3.4: Find the critic-favorite and audience-favorite actors**

   1. Create three new dataframes namely, `Meryl_Streep`, `Leo_Caprio`, and `Brad_Pitt` which contain the movies in which the actors: 'Meryl Streep', 'Leonardo DiCaprio', and 'Brad Pitt' are the lead actors. Use only the `actor_1_name` column for extraction. Also, make sure that you use the names 'Meryl Streep', 'Leonardo DiCaprio', and 'Brad Pitt' for the said extraction.
   2. Append the rows of all these dataframes and store them in a new dataframe named `Combined`.
   3. Group the combined dataframe using the `actor_1_name` column.
   4. Find the mean of the `num_critic_for_reviews` and `num_user_for_review` and identify the actors which have the highest mean."""


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

Meryl_Streep = movies[movies["actor_1_name"] == "Meryl Streep"]
 
Leo_Caprio = movies[movies["actor_1_name"] == "Leonardo DiCaprio"]

Brad_Pitt = movies[movies["actor_1_name"] == "Brad Pitt"]


combined = pd.concat([Meryl_Streep, Leo_Caprio, Brad_Pitt], axis = 0).reset_index(drop=True)

combined = combined.pivot_table(index = ["actor_1_name"], values=[ "num_user_for_reviews","num_critic_for_reviews"], aggfunc="mean" )

print(combined)


# alternate method

# Meryl_Streep = movies.loc[movies.actor_1_name == 'Meryl Streep']
# Leo_Caprio = movies.loc[movies.actor_1_name == 'Leonardo DiCaprio']
# Brad_Pitt = movies.loc[movies.actor_1_name == 'Brad Pitt']
# Combined = pd.concat([Meryl_Streep, Brad_Pitt, Leo_Caprio])
# Combined_by_segment = Combined.groupby('actor_1_name')

# Combined_by_segment['num_user_for_reviews'].mean()