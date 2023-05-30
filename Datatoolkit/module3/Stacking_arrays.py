"""Stacking arrays
Description
Merge the three arrays provided to you to form a one 4x4 array.

[Hint: Check the function np.transpose() in the 'Manipulating Arrays' notebook provided.]



Input: [[[7, 13, 14], [18, 10, 17], [11, 12, 19]], [16, 6, 1], [[5, 8, 4, 3]]]

Array 1: 3*3

[[7, 13, 14], [18, 10, 17], [11, 12, 19]]



Array 2: 1-D array

[16, 6, 1]



Array 3: 1*4 array

[[5, 8, 4, 3]]



Output:

[[7 13 14 5]

[18 10 17 8]

[11 12 19 4]

[16 6 1 3]]"""


# Read the input


import ast,sys
input_str = input() #sys.stdin.read()
input_list = ast.literal_eval(input_str)
list_1 = input_list[0]
list_2 = input_list[1]
list_3 = input_list[2]

# Import NumPy
import numpy as np

# Write your code here
arr_temp = np.vstack((np.array(list_1),np.array(list_2)))
arr_3 = np.array(list_3).transpose()
final_array = np.hstack( (arr_temp, arr_3) )
print(final_array)
