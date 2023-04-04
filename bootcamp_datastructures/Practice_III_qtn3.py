"""
Write a python code to merge two dictionaries into a single dictionary.
--------------------------------------------------------------------------------------------------
Input: Two dictionaries, one in each line

Output: A Dictionary
--------------------------------------------------------------------------------------------------
Sample Input :

{'a': 10, 'b': 8}

{'d': 6, 'c': 4}
Sample Output : {'c': 4, 'a': 10, 'b': 8, 'd': 6}"""

import ast

#take input of two dictionaries

dict1 = ast.literal_eval(input())
dict2 = ast.literal_eval(input())

#Write the code here

output_dict = dict1
output_dict.update(dict2)
print(output_dict)