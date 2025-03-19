import pandas as pd
df = pd.read_csv('date.csv')
df['Date'] = pd.to_datetime(df['Date'], format='%y/%m/%d', errors='coerce')
print(df.to_string())