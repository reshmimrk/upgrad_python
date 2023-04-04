"""
List sum
Description
Suppose you want to know the total score of the Indian cricket team in a given match.
 To do so, your task is to find the sum of all the scores of the Indian team players. 
 The scores are provided as a list, with each element as an individual score of the players.
 Also, there is a condition that if the number of elements in the list is more than 11, 
 then it is an invalid input and the output should be -1.
"""

import ast

#Take input 

score_list = ast.literal_eval(input())
# print(score_list)
#Write your code here

if len(score_list) >11:
    output = -1
else:
    output = sum(score_list)
print(output)