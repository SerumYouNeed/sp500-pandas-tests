import pandas as pd

df = pd.read_csv("^spx_d.csv")

# print(df.head())
# print(df.tail())
# print(df.describe())

# print(df.info())
# print(df['High'].max()) 
# print(df['High']) 

high_2020 = df[df['Date'] == 2020].max()
print(high_2020)