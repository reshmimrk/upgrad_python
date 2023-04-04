"""
Description
Given a string, write a Python program to find the largest substring of uppercase characters 
and print the length of that substring. Check the sample inputs and outputs for a better understanding.
---------------------------------------------------------------------------------------------------
Input - String
Output - String
---------------------------------------------------------------------------------------------------

Sample Input - I lovE PRogrAMMING
Sample Output - 6

Explanation - AMMING is the largest substring with all characters in uppercase continuously """

#Take input here
test_str = input()

#Write the code here

len_substr = 0 
max_len = 0
i = 0 # for looping

while i < len(test_str)-1:
    if test_str[i].isupper(): # check the i'th element is upper
        if len_substr == 0:
            len_substr +=1  #increment by 1
            if test_str[i+1].isupper(): # check next element is upper
                len_substr +=1 # increment by 1
        else:  # if len_substr not equal to zero means already checked the i'th element, need to check i+1'th element only
             if test_str[i+1].isupper():
                len_substr +=1
    

        if len_substr > max_len:
            max_len = len_substr

        
    else:
        len_substr = 0

    if i >= len(test_str):
            break # break if i value is greater than length of string-1
    
    i=i+1


print(max_len)
