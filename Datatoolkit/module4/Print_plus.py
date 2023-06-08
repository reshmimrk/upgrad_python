"""
Print "+"
Description
Given a single positive odd integer 'n' greater than 2, create a NumPy array of size (n x n) 
with all zeros and ones such that the ones make a shape like '+'. The lines of the plus must be 
present at the middle row and column.
Hint: Start by creating a (n x n) array with all zeroes using the np.zeros() function and then fill in 
the ones at the appropriate indices. Use integer division (//) to access the middle rows and columns

Examples:

Input 1:

3

Output 1:

[[0 1 0]

 [1 1 1]

 [0 1 0]]

Input 2:

5

Output 1:

[[0 0 1 0 0]

 [0 0 1 0 0]

 [1 1 1 1 1]

 [0 0 1 0 0]

 [0 0 1 0 0]]



Explanation: Notice that the 1s in the arrays make a shape like '+'."""

# Read the input
n = int(input())

# Import the NumPy package
import numpy as np 

# Write your code here

a = np.zeros([n, n], dtype=int)

centre = n//2

a[centre,:] = 1
a[:,centre] = 1
print(a)

