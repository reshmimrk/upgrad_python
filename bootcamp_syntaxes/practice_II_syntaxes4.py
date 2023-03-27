"""
Valid triangle
Description
Write a program to accept three sides of a triangle as the input and print whether the triangle is valid or not.

(A triangle is valid if the sum of any two sides is greater than the third side.)
"""

# Take input
a,b,c= input().split()

# Write your code here
# Convert a,b,c into numeric type and check for the validity of triangle

a = float(a)
b = float(b)
c = float(c)

if ((a+b) > c) and ((b+c) > a) and ((a+c) > b):  # all the condition should be true for a valid triangle
    flag = "Valid"
else:
    flag = "Invalid"

#print result

print(flag)
