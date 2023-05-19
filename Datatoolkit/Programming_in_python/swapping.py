"""
Swapping
Description
You are given two integer variables,  x and y. You have to swap the values stored in x and y.

----------------------------------------------------------------------
Input:
Two numbers x and y separated by a comma.

Output:
Print 5 lines. The first two lines will have values of variables shown before swapping, and the last two lines
will have values of variables shown after swapping. The third line will be blank.

----------------------------------------------------------------------
Sample input:
20, 50
"""

#Take input using input()

#input() takes input in form of the string
in_string=input()

#here extract the two numbers from the string
x = int(in_string.split(",")[0])

y = int(in_string.split(",")[1])

#print x and y before swapping

print(f"x before swapping: {x}")
print(f"y before swapping: {y}\n")

# #Writing your swapping code here

x, y = y, x

#print x and y after swapping

print(f"x after swapping: {x}")
print(f"y after swapping: {y}")


####alternate method

# #Writing your swapping code here

# x = x+y
# y = x-y
# x = x-y

# #print x and y after swapping

# print(f"x after swapping: {x}")
# print(f"y after swapping: {y}")