# Today's topics:
# Feature Engineering: One Hot Encoding
# Data Modeling: Linear Regression
# Data Modeling: Cost Function

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

# print(df['Item_Type'].unique())

# df['Item_Type_Dairy'] = df['Item_Type'].apply(lambda item_type: 1 if item_type == 'Dairy' else 0)

# print(df[['Item_Type', 'Item_Type_Dairy']])

df['Original_Item_Type'] = df['Item_Type']
df_with_dummies = pd.get_dummies(df, columns=['Item_Type'])

# print(df_with_dummies[['Original_Item_Type', 'Item_Type_Dairy', 'Item_Type_Soft Drinks', 'Item_Type_Meat']])

# print(df['Outlet_Size'].unique())

outlet_size_map = {
  'Small': 0,
  'Medium': 1,
  'High': 2,
  np.nan: np.nan
}

df['Outlet_Size_Numeric'] = df['Outlet_Size'].apply(lambda size: outlet_size_map[size])

# print(df[['Outlet_Size', 'Outlet_Size_Numeric']])

df['Outlet_Size'] = df['Outlet_Size'].astype('category')
df['Outlet_Size'] = df['Outlet_Size'].cat.reorder_categories(['Small', 'Medium', 'High'])
df['Outlet_Size_Codes'] = df['Outlet_Size'].cat.codes
# print(df[['Outlet_Size', 'Outlet_Size_Codes']])

# Data Modeling: Linear Regression

x = np.arange(20)
y = 2 * x

plt.plot(x, y, '.')
plt.xlabel('Input')
plt.ylabel('Output')
# plt.savefig('example.png')

coefs = np.polyfit(x, y, 1)
# print(coefs)

# Linear equation:
# y = mx + b
# m = coefs[0]
# b = coefs[1]

m, b = np.polyfit(x, y, 1)
# print(m,b)

def f(x):
  return m * x + b

y_pred = f(x)

plt.plot(x, y, '.', x, y_pred,'g-')
# plt.savefig('test.png')

x = np.linspace(1,20,20)
# print(x)
y = 2 * x
x += np.random.random(x.shape)
y += np.random.random(y.shape) * 2 - 1

plt.clf()
plt.plot(x,y,'.')
# plt.savefig('test.png')

m,b = np.polyfit(x,y,1)
# print(m,b)

y_pred = f(x)
plt.clf()
plt.plot(x,y,'.', x,y_pred,'g-')
# plt.savefig('test.png')

# print(f(10))

# Residuals
res = y - y_pred
# print(res)

plt.clf()
plt.plot(x,res,'.')
# plt.savefig('test.png')

# Data Modeling: Mean Squared Error
mse = np.mean(res**2)
print(mse)