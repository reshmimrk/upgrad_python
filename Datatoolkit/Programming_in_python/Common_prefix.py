"""
Description
You will be given two strings. You have to find the largest prefix common in both the strings.



----------------------------------------------------------------------

Input:

Two lines of input, one string on each line



Output:

The common largest prefix for both strings. Check sample input/output for clarification. -1 if no prefix is common.



----------------------------------------------------------------------

Sample input:

abshdksajd

abshiehand



Sample output:

absh



----------------------------------------------------------------------

Sample input:

upgradData

upGradScience



Sample output:

upgrad



----------------------------------------------------------------------

Sample input:

upgrad

upGradScience



Sample output:

upgrad



----------------------------------------------------------------------

Note: the last sample input/output clearly shows the code is not case sensitive."""


#input has been taken for you

string1=input()
string2=input()

#start writing your code to find largest common prefix here

string1 = string1.lower()
string2 = string2.lower()

l1 = len(string1)
l2 = len(string2)

min_len = min(l1, l2)
flag = 0
for i in range(min_len):
    if string1[i] != string2[i]:
        flag = 1
        break

if i == 0:
    print(-1)
elif flag == 0: # not satisfying the not equal to condition till the end of for loop, then need to print till the last element of the 
                # shorter string
    print(string1[:i+1])
elif flag == 1:  # when 'i' is less than min length
    print(string1[:i])
