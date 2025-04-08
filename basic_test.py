import pandas as pd

df = pd.read_csv("^spx_d.csv")

# print(df.head())
# print(df.tail())
# print(df.describe())

# print(df.info())
# print(df['High'].max()) 
# print(df['High']) 

mean_sp = df['Close'].mean()
higher_than_mean = df[df['Close'] > mean_sp]
first_occ = higher_than_mean['Date'].min()
print(first_occ)