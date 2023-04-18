"""Statistics
Description
Given a positive integer 'n', write a program that computes the mean, the standard deviation and the variance of the numbers starting from 0 to n-1, rounded off to two decimal places.


Sample Input 1: 16
Sample Output 1: 
7.5

4.61

21.25

Explanation: 7.5, 4.61, and 21.5 are the mean, standard deviation and variance of the list of numbers from 0 to 15(included).
Sample Input 2: 23
Sample Output 2: 

11.0

6.63

44.0"""

import numpy as np
n=int(input())
# write your code here

arr = np.arange(n)
print(round(np.mean(arr),2))
print(round(np.std(arr),2))
print(round(np.var(arr),2))