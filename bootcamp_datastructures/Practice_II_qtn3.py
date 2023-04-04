"""Given an integer ‘n’, your task is to write a Python code to find whether ‘n’ is divisible by all its digits or not. 
If they divide the number, then the number ‘n’ is a happy number. Otherwise, it is a sad number.
The number ‘n’ may be provided with commas. At first, you have to clean the number (by removing the commas involved) and then check whether the number is happy or sad.
---------------------------------------------------------------------------------------------------
Input - String
Output - String
---------------------------------------------------------------------------------------------------
Sample Input - 2,128
Sample Output - Happy Number"""

# Take input as a string
input_str = input()
n = int(input_str.replace(',',''))  # remove commas
# write your code here
number = n
while n:
    temp = n % 10  # get each digit
    if (number % temp) !=0:
        flag = "Sad Number"
        break
    else:
        flag = "Happy Number"

    n //= 10  # n = n//10 # // is floor divison ie. 234//10 = 23
    #print(n)

print(flag)