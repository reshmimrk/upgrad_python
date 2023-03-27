"""
Count the digits
Description
Write a program to accept a number from the user and count the zeros, odd digits and non-zero even digits from the entered number.

"""

# Take input
n=int(input())

#write your code here

count_zero = 0
count_odd_num = 0
count_even_non_zero = 0

while n:
    each_digit = n % 10  

    if each_digit == 0: # check digit is zero
        count_zero = count_zero +1
    elif each_digit % 2 == 0: # check digit is even
        count_even_non_zero = count_even_non_zero + 1
    else:  # else number will be odd
        count_odd_num = count_odd_num + 1

    n //= 10  

print(f"Number of odd digits: {count_odd_num}")

print(f"Number of non-zero even digits: {count_even_non_zero}")

print(f"Number of zeros: {count_zero}")

