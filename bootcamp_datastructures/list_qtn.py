"""
Remove SPSS from input_list=['SAS', 'R', 'PYTHON', 'SPSS'] and add 'SPARK' in its place.

"""

input_list=['SAS', 'R', 'PYTHON', 'SPSS'] 
# Write code to remove 'SPSS'

input_list.pop()
# Write code to append 'SPARK'
input_list.append('SPARK')

print(input_list)


"""
Convert a list ['Pythons syntax is easy to learn', 'Pythons syntax is very clear'] to a string using ‘&’. 
The sample output of this string will be:

Pythons syntax is easy to learn & Pythons syntax is very clear
"""
input_str = ['Pythons syntax is easy to learn', 'Pythons syntax is very clear']
string_1 = input_str[0] + " & " +input_str[1]#Type your answer here
print(string_1)

"""
Split the string input_str = 'Kumar_Ravi_003' to the person's second name, first name and unique customer code.
 In this example, second_name= 'Kumar', first_name= 'Ravi', customer_code = '003'.
"""
input_str = 'Kumar_Ravi_003'
first_name = input_str.split('_')[1]#write your answer here
second_name = input_str.split('_')[0]#write your answer here
customer_code = input_str.split('_')[2]#write your answer here
print(first_name)
print(second_name)
print(customer_code)