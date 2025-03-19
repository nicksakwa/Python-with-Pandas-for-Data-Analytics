import pandas as pd
df = pd.read_csv('date.csv')
print(df.drop_duplicates(inplace = True))
