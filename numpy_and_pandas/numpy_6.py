import numpy as np
array1 = np.array(range(1, 11*12+1))

print(array1)

array1 = array1.reshape(11,12)

print(array1)

print( np.unravel_index(99, (11,12)) )