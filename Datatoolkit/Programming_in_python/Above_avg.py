"""Above Average
Description
Finding the average of the data and comparing it with other values is often encountered while analysing the data. Here you will do the same thing. The data will be provided to you in a list. You will also be given a number check.  You will return whether the number check is above average or no.

----------------------------------------------------------------------
Input:
A list with two elements:
The first element will be the list of data of integers and
The second element will be an integer check.

Output:
True if check is above average and False otherwise

----------------------------------------------------------------------
Sample input:
[ [2,4,6,8,10],  4]

Sample output:
False

----------------------------------------------------------------------
Sample input:
[ [2,4,6,8,-10],  4]

Sample output:
True"""

#Take input here
#we will take input using ast sys
import ast
input_str = input()
input_list = ast.literal_eval(input_str)

#Remember how we took input in the Alarm clock Question in previous Session?
#Lets see if you can finish taking input on your own

data=input_list[0]
check=input_list[1]

#start writing your code to find if check is above average of data 

from functools import reduce
sum = reduce( lambda a,b: a +b, data )
avg = sum/ len(data)

print( check > avg )

