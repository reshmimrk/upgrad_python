"""
Triple the list elements
Description
Given a list of integers, write a python code to triple all the values in the list.
Note: Try using lambda and map functions to solve the problem.
Input: A list of integers
Output: A list of integers
----------------------------------------------------------------------
Sample input: [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]

Output: [15, 21, 66, 291, 162, 186, 231, 69, 219, 183]"""

#take input here using ast sys
import ast

# write the code here
list_in = ast.literal_eval(input())

list_out = list(map(lambda n: n*3, list_in))

print(list_out)
