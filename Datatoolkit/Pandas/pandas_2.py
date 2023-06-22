import pandas as pd
df = pd.read_csv('https://media-doselect.s3.amazonaws.com/generic/A08MajL8qN4rq72EpVJbAP1Rw/marks_1.csv', header=None, sep = '|')# Write your answer here

# df = pd.read_csv(path, header=None, sep='|')

print(df)

df.index.name ="Row_Name"

print(df)