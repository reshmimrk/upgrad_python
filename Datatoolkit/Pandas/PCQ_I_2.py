"""
Series in Series
Description
Given two Pandas series, s1 and s2, write a program to print the elements of s1 that are not present in s2.

Input: The first line has a 1D list containing elements of the first series, s1 and the second line has another 1D 
list containing elements of the second series, s2.

Output: Rows of the series whose value.

Sample Input 1: [1, 2, 3, 4, 5]

[2, 4, 6, 8, 10]

Sample Output 1: 

0  1

2  3

4  5

"""

import pandas as pd
import ast
# input has been taken for you
inp_list1=ast.literal_eval(input())
inp_list2=ast.literal_eval(input())
s1 = pd.Series(inp_list1)
s2 = pd.Series(inp_list2)

# Write your code here

out_s = s1[~s1.isin(s2)]

print(out_s)
