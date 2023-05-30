"""Extracting Elements from Array
Extracting Elements from Array
Description
From a given array, extract all the elements which are greater than 'm' and less than 'n'. Note: 'm' and 'n' are integer
values provided as input.

Input format:

A list of integers on line one

Integer 'm' on line two

Integer 'n' on line three



Output format:

1-D array containing integers greater than 'm' and smaller than 'n'.


Sample input:

[ 1, 5, 9, 12, 15, 7, 12, 9 ] (array)

6 (m)

12 (n)



Sample output:

[ 9 7 9 ]





Sample input:

[ 1, 5, 9, 12, 15, 7, 12, 9 ]

12

6



Sample output:

[ ]"""

#take input here
import ast 
input_list=ast.literal_eval(input())
m=int(input())
n=int(input())

import numpy as np
array_1 = np.array(input_list)#start writing your code from here
final_array = array_1[(array_1 > m) & (array_1 <n) ]#start writing your code from here


print(final_array)

