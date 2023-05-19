"""Shift Vowels
Description
Write a program that receives a string and shifts all the vowels present in it to the beginning. Output the resultant string. The order of all the vowels with respect to each other as well as the order of all the other characters with respect to each other should stay the same.

----------------------------------------------------------------------
Input:
A string

Output:
Vowels shifted to the beginning in the input string.

----------------------------------------------------------------------
Sample input:
programming

Sample output:
oaiprgrmmng

----------------------------------------------------------------------
Sample input:
You love Python!

Sample output:
ouoeoY lv Pythn!"""

# Read the input string

s = input()

vowels = "aeiouAEIOU"

temp_v = ""
temp_c = ""

for char in s:
    if char in vowels:
        temp_v = temp_v + char
    else:
        temp_c = temp_c + char

output = temp_v+temp_c

print(output)
