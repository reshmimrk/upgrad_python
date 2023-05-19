L=[2, 3, 4, 2, 1, 2, 3]

# print(L[2:6:2])
print(L.index(2))

#
L=[10,20,30,40,50,60,70,80,90,100]
# print(L[[1,3,5,7]])
print([L[i] for i in range(1,9,2)])
print(L[1:-1:2])
# print(L[1::2])
# print(L[1, 3, 5, 7])

A = [10,20,30]
B = [45,35,25]
B.extend(A)
print(B)
# B.append(A)
# print(B)
