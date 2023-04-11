"""Filter Function
Description
Extract a list of numbers that are multiples of 5 from a list of integers named input_list.

Sample Input:

[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]

Sample Output:

[5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

Note: Use the filter() function."""

import ast,sys
input_str = input()#sys.stdin.read()
input_list = ast.literal_eval(input_str)

list_answer = list(filter(lambda n: n%5==0, input_list))#Write your answer here

print(list_answer)