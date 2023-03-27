"""
No Vowels
Description
Write a program to accept a string from the user, delete all vowels from the string and display the result. 
"""

# Take input
s=input()

# Write your code here

vowels = ('a', 'e', 'i', 'o', 'u')


#
list_letter = []
for letter in s:
    if letter.lower() not in vowels: #comparing the letter after converting to lower case
        list_letter.append(letter)

# print(list_letter)
#join with empty space
output = "".join(list_letter)

print(output)


