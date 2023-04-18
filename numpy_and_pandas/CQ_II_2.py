"""Sort by Column
Description
Given a 2D NumPy array, sort it by the 1st column. Print the final sorted array as a NumPy array only.

Note: If two values in the 1st column are equal then the column in which the 2nd column value is lesser should come first. If the value in the second column is also the same then go to the third value and so on.

Example:
Input 1:
[[9 3 2]
 [4 0 1]
 [5 8 6]]
Output 2:
[[4 0 1]
 [5 8 6]
 [9 3 2]]
 
 input2:
 [[9 3 2]
 [4 0 1]
 [9 8 6]]
 output2:
 [[4 0 1]
 [9 3 2]
 [9 8 6]]
 """

 # Reading the input list
import ast,sys
input_str = input() #sys.stdin.read()
input_list = ast.literal_eval(input_str)

# Import the NumPy package
import numpy as np

# Converting the list to a NumPy array
n_array = np.array(input_list)

# Write your code here

print(n_array[np.lexsort((n_array[:,2], n_array[:,1], n_array[:, 0])), :])

   # help https://numpy.org/doc/stable/reference/generated/numpy.lexsort.html#numpy.lexsort


