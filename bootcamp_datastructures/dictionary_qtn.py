"""Write code to fetch the profession of the employee with Employee id - 104 from an employee input given in the form of a dictionary 
where key represent employ id and values represent the name, age, and profession (in the same order).

Sample input:

Employee_data = { 101:['Shiva', 24, 'Content Strategist'] ,102:['Udit',25,'Content Strategist'], 103:['Sonam', 28,'Sr Manager'], 104:['Ansari',29,'Product Lead' ],105:['Huzefa',32,'Project Manager' ]}

Sample output:

'Product Lead'"""

input_dict = { 101:['Shiva', 24, 'Content Strategist'] ,102:['Udit',25,'Content Strategist'], 103:['Sonam', 28,'Sr Manager'], 104:['Ansari',29,'Product Lead' ],105:['Huzefa',32,'Project Manager' ]}


#Type you answer here
profession = input_dict[104][2]

print(profession)


"""From a Dictionary input_dict={'Name': 'Monty', 'Profession': 'Singer' }, 
get the value of a key ‘Label’ which is not a part of the dictionary, in such a way that Python doesn't hit an error.
If the key does not exist in the dictionary, Python should return 'NA'.

Sample Input:

{'Name': 'Monty', 'Profession': 'Singer' }

Sample Output:

NA"""

input_dict={'Name': 'Monty', 'Profession': 'Singer' }

# Type your answer here

answer = input_dict.get('Label','NA')

print(answer)


"""
Create a SORTED list of all values from the dictionary 
input_dict = {'Jack Dorsey' : 'Twitter' , 'Tim Cook' : 'Apple','Jeff Bezos' : 'Amazon' ,'Mukesh Ambani' : 'RJIO'}

Sample Input:

{'Jack Dorsey' : 'Twitter' , 'Tim Cook' : 'Apple','Jeff Bezos' : 'Amazon' ,'Mukesh Ambani' : 'RJIO'}

Sample Output:

['Amazon', 'Apple', 'RJIO', 'Twitter']"""

input_dict = {'Jack Dorsey' : 'Twitter' , 'Tim Cook' : 'Apple','Jeff Bezos' : 'Amazon' ,'Mukesh Ambani' : 'RJIO'}

#type your answer here

answer = sorted(input_dict.values())

print(answer)
