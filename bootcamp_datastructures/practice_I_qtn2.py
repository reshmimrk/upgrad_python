"""Length of list elements
Description
Given a list of strings, write a program to find the number of strings whose length is greater than or equal to K, 
where K is a positive integer.

Input - List of strings and an integer

Output - Integer
--------------------------------------------------------------------------------
Sample Input :

[Mumbai, Hyderabad, Calicut, Chennai]
  9
Sample Output: 1"""

import ast

#Take input here using ast sys

list_str = ast.literal_eval(input()) #input list of string
K = ast.literal_eval(input()) # input an integer K

#start writing your code here

count = 0
for element in list_str:
    if len(element) >= K:
        count +=1

print(count)