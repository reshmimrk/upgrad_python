"""Index of 50th element
Consider an (8, 8) shape NumPy array. What is the index (x,y) of the 50th element?

Note: For counting the elements go row-wise. For example, in the array,

[[1, 5, 9],

 [3, 0, 2]]

the 5th element would be '0'."""

import numpy as np
list1 = list(range(1,65,1))
arr = np.array(list1).reshape([8,8])

print(arr[6,1])

print(np.where(arr == 50))

