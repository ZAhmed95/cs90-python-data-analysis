# Today's topics:

# More Data Cleaning strategies
# Feature Engineering

import numpy as np
import pandas as pd

df = pd.read_csv('data.csv')

# Data Cleaning: nonsensical data

# Treat nonsensical data as missing data

# print(df['Item_Visibility'])

# avg = np.mean(df.loc[df['Item_Visibility'] > 0, 'Item_Visibility'])
# zero_item_visibility = (df['Item_Visibility'] == 0,'Item_Visibility')
# df.loc[zero_item_visibility] = avg

# print(df['Item_Visibility'])

# Grouping data values
# print(df['Item_Identifier'].unique().shape)


# Use pandas pivot_table to group item weights by unique item
item_weights_by_item = df.pivot_table(index='Item_Identifier', values='Item_Weight')
# print(type(item_weights_by_item))
# exit()

def get_avg_item_weight(item_id):
  try:
    return item_weights_by_item.loc[item_id, 'Item_Weight']
  except KeyError:
    return 0

missing_weight = df['Item_Weight'].isnull()
filled_weights = df.loc[missing_weight, 'Item_Identifier'].apply(get_avg_item_weight)
df.loc[missing_weight, 'Item_Weight'] = filled_weights

print(df)
