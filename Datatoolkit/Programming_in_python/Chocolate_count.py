"""How Many Chocolates?
Description
Sanjay loves chocolates. He goes to a shop to buy his favourite chocolate. There he notices there is an offer going on, 
upon bringing 3 wrappers of the same chocolate, you will get new chocolate for free. If Sanjay has m Rupees. 
How many chocolates will he be able to eat if each chocolate costs c Rupees?

----------------------------------------------------------------------
Input:
Two positive integers m and c separated by a comma. The first integer is m and the second integer is c 

Output:
A single integer denoting the number of chocolates Sanjay was able to eat in total.

----------------------------------------------------------------------
Sample input:
15, 2

Sample output:
10

Explanation:
First, he will get 15/2=7 chocolates. He then will return 6 wrappers for 2 chocolates. And lastly, these two wrappers 
and the one he previously had will get him one more chocolate, making a total of 7+2+1=10 chocolates."""


#take input here

in_string=input()

m = int(in_string.split(",")[0])

c = int(in_string.split(",")[1])

#start writing your code here

choc_num = m//c
w = m//c
while (w//3) != 0:
    choc_num = choc_num + (w//3)
    w = (w//3) + (w%3)  




#dont forget to print the number of chocolates Sanjay can eat

print(choc_num)