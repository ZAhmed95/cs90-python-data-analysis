# Today's topics
# Filtering by multiple columns
# Indexing rows
# Numpy ufuncs
# DataFrame.apply

import pandas as pd

columns = ['ID', 'first name', 'last name', 'assignment 1', 'project 1', 'exam 1', 'exam 2']
students = {
  'ID': [1145, 1251, 1050, 1664, 1314],
  'first name': ["John", "Alice", "Bob", "Steve", "Karl"],
  'last name': ["Jonson", "Peters", "Bobson", 'Stevenson', "Marx"],
  'assignment 1': [5, 7, 10, 9, 8],
  'project 1': [19, 17, 20, 16, 15],
  'exam 1': [78, 85, 95, 77, 82],
  'exam 2': [88, 72, 92, 86, 67]
}

data = pd.DataFrame(students, index=students['ID'])
# print( data[ (data['exam 1'] > 80) | (data['exam 2'] > 80) ] )

# Indexing rows
# print(data.loc[[1251,1145]])

# print(data.iloc[[0,3,-1]])

import numpy as np

# numpy ufuncs (Universal functions)
# these work on both numpy arrays and pandas series/dataframes
nums = np.floor(np.random.random(10) * 10)
print(nums)

print(np.max(nums))
print(np.argmax(nums))