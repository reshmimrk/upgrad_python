import numpy as np
import pandas as pd

# The file is stored at the following path:

f_path = 'https://media-doselect.s3.amazonaws.com/generic/A08MajL8qN4rq72EpVJbAP1Rw/marks_1.csv'
# f_path = 'Pandas/marks_1.csv'
# Provide your answer below
column_list = ["Name", "Subject", "Maximum Marks", "Marks Obtained", "Percentage"]

df = pd.read_csv(f_path, header =None, sep= '|', names=column_list)# Write your answer here
df.index.name = "S.No."

print(df)