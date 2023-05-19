"""
Reverse Words
Description
You will be given a sentence in the form of a string. You have to reverse the order of the words in the sentence. 
Remember not to reverse the individual words, but the order of words. Check the sample input-output for further clarification.

----------------------------------------------------------------------
Input:
A string, which will consist of a few spaces.

Output:
The words in reverse order."""

#take input here

sentence=input()

#reverse the words of the sentence here

split_sentence = sentence.split(' ')

# approach 1
# output = []
# for i in range(len(split_sentence)-1,-1,-1):
#     output.append(split_sentence[i])

# out_str = ' '.join(output)
# print((out_str))


###another approach instead of for loop use reverse function

split_sentence.reverse()

out_str = ' '.join(split_sentence)
print((out_str))
