"""Calendar
Description
You are planning to go to your friend's wedding and you have long events all month, lasting at least a few days. 
You have the start and end dates of events and your task is to find out events overlapping with the wedding date.

The code for taking input has already been written for you, please don't modify that, but do read and try to understand 
the way input has been taken. You will be asked to take input on your own for most of the problems here onwards. 
Taking data in a suitable format is an important skill for a Data Scientist.

----------------------------------------------------------------------
Input:
The input will contain a list of lists where each sub-list has only two elements representing the start and end date of an event, 
the start date will be less than or equal to the end date. The next line of input will have a wedding date. 

Output:
The output should have the number of events overlapping with the wedding date.

----------------------------------------------------------------------
Sample input:
[ [29,31], [23,26], [24,25] ]
24

Sample output:
2

Explanation:
There are three events in the month.
Event 1= from date 29 to 31
Event 2= from date 23 to 26
Event 3= from date 24 to 25
Wedding is on 24. This means it will clash with Event 3 and Event 2, that is two events.
The output is therefore 2.

----------------------------------------------------------------------
Sample input:
[ [1, 4], [7, 10], [8, 8], [14, 23] ]
26

Sample output:
0"""


#taking input
import ast
input_str1 = input()
input_list1 = ast.literal_eval(input_str1)
events = input_list1

wedding = int(input())


#start writing from here

count = 0
for event in events:
    if (event[0] <= wedding)  and (wedding <= event[1]):
        count = count +1
print(count)