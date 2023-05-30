"""
Which of the following would extract all the first 3 rows of the last 5 columns in 
a given numpy 2D array ‘a’?"""

import numpy as np
list1 = list(range(1,65,1))
arr = np.array(list1).reshape([8,8])

print(arr)

print(arr[:3, -5:])