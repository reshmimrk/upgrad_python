"""
ASCII values
Description
Write a program to accept a character and display its next and previous character. 

Hint: Make use of Ascii values here.
"""

inp = input("")

# The ord() function returns the number representing the unicode code of a specified character.
# chr() function returns the character back from unicode number

prev = ord(inp) - 1
prev_char = chr(prev)

next = ord(inp) + 1
next_char = chr(next)


print(prev_char)
print(next_char)

