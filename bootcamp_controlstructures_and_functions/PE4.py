"""Filter Function
Description
You are given a list of strings such as input_list = ['hdjk', 'salsap', 'sherpa'].
Extract a list of names that start with an ‘s’ and end with a ‘p’ (both 's' and 'p' are lowercase) in input_list.

Sample Input:

['soap','sharp','shy','silent','ship','summer','sheep']
Sample Output:

['soap', 'sharp', 'ship', 'sheep']
Note: Use the filter() function."""

import ast,sys
input_str = input() #sys.stdin.read()
input_list = ast.literal_eval(input_str)

sp = list(filter(lambda w: w[0]=='s' and w[-1]=='p', input_list))#Write your code here

print(sp)