"""Increment list elements
Description
Given a list of strings, increment the value of the numeric strings by 'k’. 

Hint: The function isdigit() may be useful here.
---------------------------------------------------------------------------------------------
Input - A list in the first line and an integer in the second line

Output - A list

---------------------------------------------------------------------------------------------

Sample Input :

['Python', '123', 'Data']

  4

Sample Output : ['Python', '127', 'Data']
---------------------------------------------------------------------------------------------

"""

#Input has been taken for you
import ast
input_list = ast.literal_eval(input())
K = int(input())

#write the code

for i in range(len(input_list)):
    if (input_list[i]).isdigit():
        new_str = str(int(input_list[i])+K)
        input_list[i] = new_str

print(input_list)
