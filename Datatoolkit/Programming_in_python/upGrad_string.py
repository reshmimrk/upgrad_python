"""pGrad String
Description
For the purpose of this question, we will define something called an upGrad string. Note that this definition is not valid 
outside this question. A string upGrad string if the frequency of its characters is something like 1, 2, 3, 4, .... 
That is a character appears only once, another appears twice, another appears thrice and so on. For example string 
'$yrr$ssrsr' is a upGrad string since the frequency of y:1, $:2, s:3, r:4, however string '$yrr$ssrsr%' will not be 
an upGrad string since it has two characters (y and %) with frequency 1. The frequency of characters should be of form 
1, 2, 3, 4, 5... only.

Given a string, can you determine if the string is upGrad string or no?

Input:

A string



Output:

Boolean depending whether the string is upGrad string or not

Sample input:

$yrr$ssrsr



Sample output:

True
Sample input:

$yrr$ssrsr%



Sample output:

False
Sample input:

ab#ab#aba



Sample output:

False



Sample input:

ab#ab#ab6a



Sample output:

True"""


#input has been taken for you
s=input()

#start writing your code to check if s is upgrad string or no

out_dict = {}

for char in s:
    if char not in out_dict:
        out_dict[char] = 1
    else:
        out_dict[char] = out_dict[char] + 1

sorted_values = sorted(list(out_dict.values()))

if sorted_values == list(range(1,max(sorted_values)+1)):
    print(True)
else:
    print(False)


