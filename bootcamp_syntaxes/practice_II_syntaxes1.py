"""
Digit or Alphabet
Description
Write a program to display whether the input is a digit or a letter of the alphabet.

"""
# Take input
inp=input("Enter the input here:")

#write your code here
#Checking input alphabet or integer

if inp.isalpha():
    print("Alphabet")
elif inp.isdigit():
    print('Integer')
