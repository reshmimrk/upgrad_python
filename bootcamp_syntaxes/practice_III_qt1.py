"""
Multiplication Table
Description
Write a program to display the multiplication table of a given number.
"""

#Take input
n=int(input())

#write your code here

for i in range(1,11):
    print(f"{n} * {i} = {n*i}")   # if we use f before a string, inside the {} we can put variable to get its value