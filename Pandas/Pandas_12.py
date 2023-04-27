""" In the dataframe created above, find the department that has the most efficient team 
(the team with minimum percentage of employees who need training)."""



import numpy as np
import pandas as pd

# The file is stored at the following path:
# 'https://media-doselect.s3.amazonaws.com/generic/NMgEjwkAEGGQZBoNYGr9Ld7w0/rating.csv'
df = pd.read_csv('https://media-doselect.s3.amazonaws.com/generic/NMgEjwkAEGGQZBoNYGr9Ld7w0/rating.csv')

# Provide your answer below
df["Training"] = df["Rating"].apply( lambda x: 'Yes' if x <=3.5 else 'No')
print(df.head())

#for count
# print("Finance = ", len(df[ (df["Department"] == "Finance") & (df["Training"] == "No") ]))
# print("Marketing = ", len(df[ (df["Department"] == "Marketing") & (df["Training"] == "No") ]))
# print("Sales = ", len(df[ (df["Department"] == "Sales") & (df["Training"] == "No") ]))
# print("HR = ", len(df[ (df["Department"] == "HR") & (df["Training"] == "No") ]))


#for percentage
Department_list = ["Finance", "Marketing", "Sales", "HR"]

for dep in Department_list:
    print(dep, " = ", round((len(df[ (df["Department"] == dep) & (df["Training"] == "No") ]) / len(df[df["Department"] == dep]))*100, 2))