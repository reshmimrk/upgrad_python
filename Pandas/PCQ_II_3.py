"""
Data Analysis
Description
This time you've a fully cleaned movie dataset. The first few rows of the dataset are shown below:

You're a producer looking to make a blockbuster movie. There will primarily be three lead roles in your movie 
and you wish to cast the most popular actors for it. Now, since you don't want to take a risk, you will cast a 
trio which has already acted in together in a movie before. The metric that you've chosen to check the popularity 
is the Facebook likes of each of these actors.

The dataframe has three columns to help you out for the same, viz. 'actor_1_facebook_likes', 'actor_2_facebook_likes',
 and 'actor_3_facebook_likes'. Your objective is to find the trio which has the most number of Facebook likes combined. 
 But there is a small condition which is that none of the three actors' Facebook likes should be less than half of the other two. 
 For example, the following is a valid combo:
actor_1_facebook_likes: 70000
actor_2_facebook_likes: 40000
actor_3_facebook_likes: 50000

But the below one is not:
actor_1_facebook_likes: 70000
actor_2_facebook_likes: 40000
actor_3_facebook_likes: 30000

since in this case, actor_3_facebook_likes is 30000, which is less than half of actor_1_facebook_likes.

Expected Output: Find out the most popular trio and print them as a list sorted in alphabetical order. For example:
['Brad Pitt', 'Jake Gyllenhaal' 'Meryl Streep']"""


### columns available in data extracted from csv data
"""
'color', 'director_name', 'num_critic_for_reviews',
       'duration', 'director_facebook_likes', 'actor_3_facebook_likes',
       'actor_2_name', 'actor_1_facebook_likes', 'gross', 'genres',
       'actor_1_name', 'movie_title', 'num_voted_users',
       'cast_total_facebook_likes', 'actor_3_name', 'facenumber_in_poster',
       'plot_keywords', 'movie_imdb_link', 'num_user_for_reviews', 'language',
       'country', 'content_rating', 'budget', 'title_year',
       'actor_2_facebook_likes', 'imdb_score', 'aspect_ratio',
       'movie_facebook_likes'
"""

###


# Importing the pandas package
import pandas as pd

# Reading the movies file
# movies = pd.read_csv('https://media-doselect.s3.amazonaws.com/generic/pLLQowB8OYx0oBWdMbY4gp4wb/movies_final (2).csv', sep='\t')
movies = pd.read_csv('https://media-doselect.s3.amazonaws.com/generic/pLLQowB8OYx0oBWdMbY4gp4wb/movies_final%20(2).csv', sep='\t')

# Write your code here
movies_filtered = movies.pivot_table(values = ['actor_1_facebook_likes', 'actor_2_facebook_likes', 'actor_3_facebook_likes'],
                           index = ['actor_1_name', 'actor_2_name', 'actor_3_name'], aggfunc='sum')

movies_filtered["combined_likes"] = movies_filtered["actor_1_facebook_likes"] + movies_filtered["actor_2_facebook_likes"] + \
                                    movies_filtered["actor_3_facebook_likes"]



def check_status(movies_row):
    valid_status = 0
    temp_list = sorted([movies_row["actor_1_facebook_likes"], movies_row["actor_2_facebook_likes"], movies_row["actor_3_facebook_likes"]])
    # print(temp_list)
    if (temp_list[0] >= (temp_list[1]/2)) and (temp_list[0] >= (temp_list[2]/2)) and (temp_list[1] >= (temp_list[2]/2)) :
        valid_status = 1
    return valid_status

    
movies_filtered["valid_combo"] = movies_filtered.apply( check_status , axis = 1)

movies_filtered = movies_filtered[movies_filtered["valid_combo"] == 1].sort_values(by="combined_likes", ascending=False)

# print(movies_filtered)

output_actor_names = sorted(movies_filtered.index[0])

print(output_actor_names)





