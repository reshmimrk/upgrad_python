"""
Character frequency
Description
Write a program to accept a string value from the user and accept a char value from the user 
and find out the total occurrence of the char value in the string value. Note that the count is not case-sensitive
"""

# Take input
input_string=input()
input_char=input()

#write your code here

ch_count = input_string.count(input_char)

print(ch_count)
