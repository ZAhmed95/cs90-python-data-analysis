# Today's topics:
# Finish up data cleaning:
# Outlier management

# Feature Engineering

import numpy as np
import pandas as pd

df = pd.read_csv('data.csv')

# Removing outliers: 2 methods
# 1. Standard deviation method
# 2. Interquartile range method

data = np.random.normal(size=10000)
# print(data)

# Standard deviation method
mean = np.mean(data)
std = np.std(data)

# print(mean, std)

filtered = data[np.abs(data - mean) < 3 * std]
outliers = data[np.abs(data - mean) >= 3 * std]
# print(filtered.shape)

# Interquartile Range method
data2 = np.random.normal(size=10000)

mean2 = np.mean(data2)
std2 = np.std(data2)

# print(mean2, std2)

q1, q3 = np.percentile(data2, [25, 75])

# print(q1, q3)

iqr = q3 - q1

lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr

# print(iqr, lower, upper)

filtered2 = data2[(data2 >= lower) & (data2 <= upper)]
outliers2 = data2[(data2 < lower) | (data2 > upper)]
# print(outliers2)

# Feature Engineering
# print(df[['Outlet_Identifier', 'Outlet_Establishment_Year']])

df['Outlet_Age'] = 2013 - df['Outlet_Establishment_Year']

df['Outlet_Older_Than_10'] = df['Outlet_Age'].apply(lambda age: True if age > 10 else False)

print(df[['Outlet_Identifier', 'Outlet_Establishment_Year', 'Outlet_Age', 'Outlet_Older_Than_10']])