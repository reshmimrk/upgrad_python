# 3D array
import numpy as np
list1 = [[[1,2,3],[2,3,4]]]
arr1 = np.array(list1)

print(arr1)
print(arr1.shape)
print(arr1.ndim)


print(arr1[:,:,0])

print(arr1[0,:,:])