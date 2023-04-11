"""Map Function
Description
Using the function Map, count the number of words that start with ‘S’ in input_list.

Sample Input:

['Santa Cruz','Santa fe','Mumbai','Delhi']

Sample Output:

2"""

import ast,sys
input_str = input()#sys.stdin.read()
input_list = ast.literal_eval(input_str)


count = sum(list(map((lambda x: x[0].lower()=='s'), input_list)))#Type your code here

print(count)