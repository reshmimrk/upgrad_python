"""
Sum of digits
Description
Write a program to calculate the sum of the digits of a given number 
"""

#Take input
n=int(input())

# write your code here

sum = 0

while n:
    temp = n % 10
    #print(temp)
    sum += temp  # sum = sum + (n%10) # %  is modulus operator
    #print(sum)
    n //= 10  # n = n//10 # // is floor divison
    #print(n)  




# print the results
print(sum)