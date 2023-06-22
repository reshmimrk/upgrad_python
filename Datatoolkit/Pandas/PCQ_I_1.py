"""Series Sub-setting
Description
Given a Pandas series and a value 'n', write a program to create a subset of the series whose value is greater than 'n'.

Input: The first line contains a 1D list that will be converted to a Pandas series, and the second line contains an integer 'n'.

Output: Rows of the series whose value is less than n"""

import pandas as pd
import ast
#input has been taken for you
inp_list=ast.literal_eval(input())
n=int(input())
s = pd.Series(inp_list)
# print(s)

#write your code here

s_out = s[s<n]

print(s_out)