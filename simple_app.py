import pandas as pd
import numpy as np

def high_low_diff (high, low):
    diff = high - low
    return diff

def open_close_diff (open, close):
    diff = open - close
    return np.abs(diff)

df = pd.read_csv("^spx_d.csv")

# Zamiana typu danych
df['Date'] = pd.to_datetime(df['Date'])

# Dodanie nowej kolumny
df['Months'] = df['Date'].dt.strftime('%Y-%m')

# Obliczam średnią dla każdego miesiąca
monthly_mean = df.groupby('Months')['Close'].transform('mean')

# Dodaję kolumnę ze średnimi
df['Monthly_mean'] = monthly_mean

# Liczę różnice open/close
opens = np.array(df['Open'])
closes = np.array(df['Close'])
o_c_diff = open_close_diff(opens, closes)

df['open_close_diff'] = o_c_diff

print(df.head())

df.to_csv("open_close_diff.csv")


