import numpy as np

array_1 = np.array([[1, 2, 3, 4, 5],
                [6, 7, 8, 9, 10],
                [11, 12, 13, 14, 15],
                [16, 17, 18, 19, 20]])

print(array_1)
# print(array_1.reshape(5, 4)[array_1%2 != 0])
# print(array_1[array_1%2 != 0])
# print(array_1[array_1%2 == 0].reshape(5, 2))
print(array_1[array_1%2 != 0].reshape(5, 2))
