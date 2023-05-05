"""Risk of Diabetes Based on BMI
Description
You've been given the pima_indian_diabetes dataset. Here are its first few rows:
Notice the BMI and Diabetes column. You need to find the BMI which is most likely to cause Diabetes. 
First round the BMI to an integer value and return which BMI has the most risk of diabetes based on the 0, 1
 diabetes values provided in the dataframe.

Expected Output: Just print a single integer denoting the value of the required BMI. 
(Please only output an integer value. For example, if the output is 30.0 please convert it to int and output 30.). """

# Import the Pandas package
import pandas as pd 

# Reading the input dataframe
pima = pd.read_csv('https://media-doselect.s3.amazonaws.com/generic/pLZK3n22ezVwAG2XOYW5qEx7V/pima_indian_diabetes.csv')

# Write your code here

# Round the BMI column
pima['BMI'] = round(pima['BMI'])

# print(pima["BMI"])
# Group the pima dataframe using the Diabetes column as values 
pima_g = pima.pivot_table(values = ['Diabetes'], index = 'BMI', aggfunc = 'sum')

# print("pima_g", pima_g)


# Sort the dataframe by the diabetes column
pima_g.sort_values(by = 'Diabetes', inplace = True, ascending = False)


print(int(pima_g.index[0]))


