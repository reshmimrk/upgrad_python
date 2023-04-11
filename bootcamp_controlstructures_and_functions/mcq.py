# from functools import reduce
# print(list(reduce(lambda x,y:x+y,range(5,15))))


import functools
lis=[1, 2, 3, 4, 5]
m=functools.reduce(lambda x, y:x if x<y else y, lis)
print(m)
lis=[1, 2, 3, 4, 5]
c=lis[0]
for i in range(len(lis)-1):
    if lis[i]<c:
       c=lis[i]
print(c)