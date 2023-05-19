"""Anagrams
Description
Two strings are anagrams of each other if you can rearrange the characters of one string to make the other string.
Given two strings, can you find if they are anagrams or no?

----------------------------------------------------------------------
Input:
Two lines of input, each line will contain a string without space.

Output:
True or False based on whether the strings are anagrams or not.

----------------------------------------------------------------------
Sample input:
thing
night

Sample output:
True

----------------------------------------------------------------------
Sample input:
upgrad
found

Sample output:
False

----------------------------------------------------------------------
Note: the code will be case-Sensitive
Hint: if the length of the strings doesn't match, the strings are obviously not anagrams."""

#take input here
str1 = input()
str2 = input()

#code here to check if they are anagrams or no
def check_anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    else:
        for c in s1:
            if s1.count(c) != s2.count(c):
                return False
        return True
    
print(check_anagram(str1, str2))
