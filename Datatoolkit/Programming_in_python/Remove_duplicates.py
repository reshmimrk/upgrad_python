"""Remove Duplicates
Description
Sometimes the data has few duplicate values which will affect the analysis done. In this problem,
 you will be given a list. You have to find and delete the duplicates and print the updated list with no duplicates.

----------------------------------------------------------------------
Input:
A list of integers.

Output:
A list of integers, with duplicates removed if any.

----------------------------------------------------------------------
Sample input:
[8, 9, 2, 2, 3, 4, 5, 2]

Sample output:
[8, 9, 2, 3, 4, 5]

----------------------------------------------------------------------
Sample input:
[4, 4, 4, 4]

Sample output:
[4]

----------------------------------------------------------------------
Note the order of the data did not change in input and output."""

#take input here
import ast
list_in = ast.literal_eval(input())

#remove duplicates from the list

dict_out = {}
for element in list_in:
    if element not in dict_out:
        dict_out[element] = 1


#print the list without duplicates
print(list(dict_out.keys()))

