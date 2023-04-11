"""Extract the words that start with a vowel from a list input_list=[wood, old, apple, big, item, euphoria] 
using list comprehensions."""

import ast,sys
input_str = input() #sys.stdin.read()
input_list = ast.literal_eval(input_str)

list_vowel = [word for word in input_list if word[0].lower() in "aeiou"]# [Type your answer here]

print(list_vowel)