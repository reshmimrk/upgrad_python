"""A number k is beautiful if it is of the form 3n+1, is pretty if it is of the form 3n+2 and is sexy if it is of form 3n.
Given a number k, print if it is beautiful, pretty or sexy.

Sample input:
21

Sample output:
sexy

Sample input:
22

Sample output:
beautiful

Sample input:
23

Sample output:
pretty
"""

#input has been taken for you

k=int(input())

#check if the number is beautiful, pretty or sexy

for i in range(0,k+1):
    if k == ((3*i) + 1):
        print("beautiful")
        break
    elif k == ((3*i) + 2):
        print("pretty")
        break
    elif k == (3*i):
        print("sexy")
        break