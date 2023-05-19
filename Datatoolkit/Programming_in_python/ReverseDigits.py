"""Reverse The Digits
Description
You will be given a number. You have to reverse the digits of the number and print it.

hint: you will find % and // operators useful here
----------------------------------------------------------------------
Input:
A positive integer greater than zero

Output:
The number in reverse order. Check sample outputs for more details.

----------------------------------------------------------------------
Sample input:
345200

Sample output:
2543

----------------------------------------------------------------------
Sample input:
6752343

Sample output:
3432576"""

#take input of the number here

number = int(input())
#write code to reverse the number here

reversed_num = 0

while number >0:
    reversed_num = (reversed_num * 10) + (number % 10)
    number = number//10


print(reversed_num)