#Creating numpy array from Scratch

import numpy as np

# n1 = np.ones((5,4), dtype=int)

# print(n1)

# # help(np.ones)

# n2 = np.zeros((5,3))

# print(n2)

# n3 = np.random.randint(3,4,size=(5,2)) 

# print(n3)

# n4= np.random.random([4,4])

# print(n4)

# # help(np.random.random)

# n5 = np.arange(0,55,5) # 0 to 55 with a step of 5, excluding 55

# print(n5)

# n6 = np.linspace(2,5,10) # 2 to 5 with a length of 10

# print(n6)

# n7 = np.full([4,5],55)

# print(n7)
# help(np.full)


a = np.array([0, 1, 2])
n8 = np.tile(a, 2)

print(n8)

# array([0, 1, 2, 0, 1, 2])


np.tile(a, (2, 2))
# array([[0, 1, 2, 0, 1, 2],
#         [0, 1, 2, 0, 1, 2]])

np.tile(a, (2, 1, 2))
# array([[[0, 1, 2, 0, 1, 2]],
#         [[0, 1, 2, 0, 1, 2]]])

b = np.array([[1, 2], [3, 4]])
np.tile(b, 2)
# array([[1, 2, 1, 2],
#         [3, 4, 3, 4]])
np.tile(b, (2, 1))
# array([[1, 2],
#         [3, 4],
#         [1, 2],
#         [3, 4]])

c = np.array([1,2,3,4])
np.tile(c,(4,1))
# array([[1, 2, 3, 4],
#         [1, 2, 3, 4],
#         [1, 2, 3, 4],
#         [1, 2, 3, 4]])

# help(np.tile)


n10 = np.eye(4,5)
print(n10)