import pandas as pd
path="Pandas\marks_1.csv"
df = pd.read_csv(path, header=None, sep='|')

print(df)

df.index.name ="Row_Name"

print(df)