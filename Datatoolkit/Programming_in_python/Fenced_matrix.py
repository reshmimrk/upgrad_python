"""enced Matrix
Description
You will be given two positive integers m and n. You have to make a list of lists (which can be visualised as a matrix) of size m*n,
 that is m sublists (rows), with each sublists having n integers (columns). The matrix should be such that it should have 1 on the 
 border and 0 everywhere else. See sample input and output for more clarification.
----------------------------------------------------------------------
Input:
Two integers separated by a comma
Output:
A list of lists of size m*n printed like matrix as shown in the sample output.
----------------------------------------------------------------------

Sample input:

4,5
Sample output:

[1, 1, 1, 1, 1]
[1, 0, 0, 0, 1]
[1, 0, 0, 0, 1]
[1, 1, 1, 1, 1]
----------------------------------------------------------------------

Sample input:

3,3
Sample output:

[1, 1, 1]
[1, 0, 1]
[1, 1, 1]


----------------------------------------------------------------------

Sample input:

3,2



Sample output:

[1, 1]
[1, 1]
[1, 1]
"""

#take input on your own here
import ast
input_ints = ast.literal_eval(input())
m = input_ints[0]
n = input_ints[1]

#start writing code here


output = [[1]*n if (i==0 or i==(m-1)) else [0]*n for i in range(m) ]

for i in range(0,m):
    if i!=0 or i !=(m-1):
        output[i][0] = 1
        output[i][n-1] = 1
    print(output[i])
