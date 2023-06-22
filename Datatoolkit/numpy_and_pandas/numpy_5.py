"""Create border array
Description
Given a single integer n, create an (n x n) 2D array with 1 on the border and 0 on the inside.

Note: Make sure the array is of type int.

Example:
Input 1:
4
Output 1:
[[1 1 1 1]
[1 0 0 1]
[1 0 0 1]
[1 1 1 1]]
Input 2:
2
Output 2:
[[1 1] 
 [1 1]] """

 # Read the variable from STDIN
n = int(input())

import numpy as np

# Create an 'n*n' array of all ones

np_array = np.ones([n,n], dtype=int)

# Fill the array with zeroes from second index (i.e. index 1) to second last index.
# Do this for both row indices and column indices

np_array[1:-1,1:-1] = 0

# Print the array created

print(np_array)
