"""Border Rows and Columns

Description
Extract all the border rows and columns from a 2-D array.

Format:
Input: A 2-D Python list
Output: Four NumPy arrays - First column of the input array, first row of the input array, last column of the input
array, last row of the input array respectively.

Example:
Input 1:
[[11, 12, 13, 14],
 [21, 22, 23, 24],
 [31, 32, 33, 34]]
Output 1:
[11 21 31]
[11 12 13 14]
[14 24 34]
[31 32 33 34]"""


# Read the input list
import ast,sys
input_str = input() #sys.stdin.read()
input_list = ast.literal_eval(input_str)

import numpy as np

# Convert the input list to a NumPy array
array_2d =np.array(input_list)

# Extract the first column, first row, last column and last row respectively using
# appropriate indexing
col_first = array_2d[:,0]
row_first = array_2d[0,:]
col_last = array_2d[:,-1]
row_last = array_2d[-1,:]

print(col_first)
print(row_first)
print(col_last)
print(row_last)
