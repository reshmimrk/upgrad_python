"""Create a list ‘name’ consisting of the combination of the first name and the second name from list 1 and 2 respectively. 

For e.g. if the input list is:
[ ['Ankur', 'Avik', 'Kiran', 'Nitin'], ['Narang', 'Sarkar', 'R', 'Sareen']]

the output list should be the list:
['Ankur Narang', 'Avik Sarkar', 'Kiran R', 'Nitin Sareen']

Note: Add a space between first name and last name."""

import ast,sys
input_str = input() #sys.stdin.read()
input_list = ast.literal_eval(input_str)
first_name = input_list[0]
last_name = input_list[1]

name = list(map( lambda w1,w2: f"{w1} {w2}", first_name, last_name))#Write your code here

print(name)