"""Smallest Element
Description
You have to find and print the smallest element of the list given as input. 

----------------------------------------------------------------------
Input:
A non-empty list of integers.

Output:
The smallest integer of the input list.

----------------------------------------------------------------------
Sample input:
[2, -3, 0, 7, 21]

Sample output:
-3"""

#input have been taken for you here
import ast
input_str = input()
input_list = ast.literal_eval(input_str)

#start writing your code here

min_value = input_list[0]

len_list = len(input_list)

# starting from index 1, as we took element in 0th place as min.
for index in range(1,len_list):     
    if input_list[index] < min_value:
        min_value = input_list[index]


print(min_value)

# ##Alternate approach
# print(min(input_list))



