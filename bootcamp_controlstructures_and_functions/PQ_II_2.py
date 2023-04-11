"""
Intersection of lists
Description
In ‘ABC’ university, company ‘XYZ’ conducted three rounds of interviews to recruit students. Those students who passed all the rounds were selected. The company released the results for each round in a separate list. Your task is to write a Python code to display the list of the students who passed all the three rounds.

Note: 
 a. Name of the person can be given in uppercase or lowercase.
 b. Print the names in lowercase in the output.

Input: 
List
List
List

Output: List
Sample input: ['Arkam', 'Bairstow', 'Cairy', 'Darpan'] 

 ['ARKAM', 'Bairstow', 'Cairy', 'Darpan', 'Dhoni', 'Sachin']

 ['arkam', 'bairstow', 'Cheteshwar', 'Dinesh']

Sample output: ['arkam', 'bairstow']"""

#take input here using ast sys
import ast

# write the code here
list1 = ast.literal_eval(input())
list2 = ast.literal_eval(input())
list3 = ast.literal_eval(input())

lower_list1 = list(map(lambda x: x.lower(), list1))
lower_list2 = list(map(lambda x: x.lower(), list2))
lower_list3 = list(map(lambda x: x.lower(), list3))

list1_2_intersect = [word for word in lower_list1 if word in lower_list2]

list_out = [word for word in lower_list3 if word in list1_2_intersect]
print(list_out)

# #another method

# lower_list1 = list(map(lambda x: x.lower(), list1))
# lower_list2 = list(map(lambda x: x.lower(), list2))
# lower_list3 = list(map(lambda x: x.lower(), list3))
# list_out = list( (set(lower_list1) & set(lower_list2)) & set(lower_list3) )

# print(list_out)





