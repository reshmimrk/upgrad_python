import numpy as np
a1 = np.array([[1, 5],
 [3, 7],
 [4, 9]])
out = np.reshape(a1,(1,-1))
print(out)

print(out.ndim)