"""Sorting a dictionary
Description
Given is a list consisting of dictionary elements. Each dictionary contains the name of a student as a first item 
and his/her corresponding rank as the second item. 
Your task is to write a Python program to print the list (dictionary elements) in a sorted ascending order 
according to student ranks. In case the rank of two or more students are the same, 
then sort them in ascending order (alphabetically) according to their names.
Note: Use the sorted() function to solve the question.
Input: Dictionary
Output: Dictionary

----------------------------------------------------------------------

Sample input: [{ "name" : "Arpit", "rank" : 20}, { "name" : "Manjeet", "rank" : 20 },{ "name" : "Aravind" , "rank" : 19 }]
Sample output: [{ "name" : "Aravind" , "rank" : 19 }, { "name" : "Arpit", "rank" : 20}, { "name" : "Manjeet", "rank" : 20 }]

"""

#take input here using ast sys
import ast

# write the code here

list_in = ast.literal_eval(input())

list_out = sorted(list_in, key = lambda x: (x["rank"], x["name"])) #help https://docs.python.org/3/library/functions.html#sorted

print(list_out)

