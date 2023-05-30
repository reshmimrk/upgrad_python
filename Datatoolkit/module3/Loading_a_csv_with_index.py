"""Loading a csv with index
Description
Using the file ‘marks.csv’, create a dataframe as shown below.

You must be able make the first column of the file as the index and name it 'S.No.'. 
Also, the columns must be renamed as shown in the image."""

import numpy as np
import pandas as pd

# The file is stored at the following path:
# 'https://media-doselect.s3.amazonaws.com/generic/A08MajL8qN4rq72EpVJbAP1Rw/marks_1.csv'
# Provide your answer below
f_path = 'https://media-doselect.s3.amazonaws.com/generic/A08MajL8qN4rq72EpVJbAP1Rw/marks_1.csv'

# Provide your answer below
column_list = ["Name", "Subject", "Maximum Marks", "Marks Obtained", "Percentage"]

df = pd.read_csv(f_path, header =None, sep= '|', names=column_list)# Write your answer here
df.index.name = "S.No."# Write your answer here

print(df)