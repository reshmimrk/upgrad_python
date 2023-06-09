"""
Encrypt elements in a list
Description
A company stores the names of their employees in a list. They want to encrypt the names so that no one can read them and the data stays safe. One of the steps in encrypting is to reverse each name in the list and convert them to uppercase and your task is to write a Python code to execute the same.
Note: Use lambda and map functions.
Input: A list of names
Output: A list of encrypted names
----------------------------------------------------------------------
Sample input: ['Ronaldo', 'Cristiano', 'Rakesh', 'Ronak']

Sample output: ['ODLANOR', 'ONAITSIRC', 'HSEKAR', 'KANOR']"""

#take input here using ast sys
import ast

# write the code here
list_in = ast.literal_eval(input())

list_out = list(map(lambda n: n[::-1].upper(), list_in))

print(list_out)
