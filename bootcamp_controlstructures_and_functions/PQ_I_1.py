"""Description
Given a list of integers, write a python code to find all the even numbers present in the list.
Note: Try using lambda and filter functions to solve the problem.
Input: A list of integers
Output: A list of integers
----------------------------------------------------------------------
Sample input: [5, 7, 22, 97, 54, 62, 77, 23, 73, 61] 

Sample output: [22, 54, 62]"""

#take input here using ast sys
import ast

# write the code here
list_in = ast.literal_eval(input())

list_out = list(filter(lambda n: n%2==0, list_in))

print(list_out)
