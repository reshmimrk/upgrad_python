"""Let’s say you have two lists A and B. Identify the elements which are common in the two lists A and B and 
return them in a sorted manner. For example 
Sample Input :

A = [5, 1, 3, 4, 4, 5, 6, 7]

B = [3, 3, 5, 5, 1 ,7 ,2]

Sample Output:

[1,3,5,7]"""

list_1 = [5, 1, 3, 4, 4, 5, 6, 7]
list_2 = [3, 3, 5, 5, 1 ,7 ,2]

#Type your answer here

answer = sorted(list(set(list_1) & set(list_2)))

print(answer)

