"""
String manipulation
Description
Write a program that takes a string as the input and does the following:

    -Removes the numbers, special characters

    -Converts uppercase letters to lowercase letters, and vice versa 
"""

#Take input
input_string=input()

#write your code here


list_out = []
for element in input_string:
    if element.isalpha():  # check for aphabet or not, this will eliminate numeric and special characters
        if element.isupper():
            list_out.append(element.lower())
        elif element.islower():
            list_out.append(element.upper())

output = "".join(list_out)

print(output)


