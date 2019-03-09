# Today's topics:
# Intro to pandas
# Series:
# Creating a series
# The 'index' of a series
# Accessing elements in a series
# Slicing
# Filtering
# Slice assignment
# DataFrame
# Creating a dataframe
# Indexing a df
# Slicing
# Filtering
# Slice assignment
# Reindexing
# Adding elements
# Removing elements

import pandas as pd

# SERIES
# this is what pandas calls a 1D array or list

# Creating a series
# from a standard list
a = pd.Series([1, 2, 3, 4, 5])
# print(a)

# The index column
b = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
# print(b)

# Reindexing

c = b.reindex(['e', 'd', 'c', 'b', 'a', 'f'])
# print(c)

# Fancy indexing
# print(b[['a', 'c', 'd']])

# Slicing
# print(a)
# print(a[:3])

# print(b)
# print(b['a':'c'])

# Filtering
# print(b[b >= 3])

# Slice assignment
# print(a)
a[:3] = 7
# print(a)

# print(b)
# b['a':'c'] = 7
# print(b)

# Filter assignment
# print(b)
b[b % 2 == 0] = 7
# print(b)

# DataFrame
# this is what pandas calls a 2D table of data

# Creating a dataframe

# from a dict of lists
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

# print(data)

# Indexing
# print(data[['ID', 'first name', 'last name']][:2])

# this will slice ROWS, not columns
# print(data[:2])

# Filtering
print(data[data['exam 1'] > 80])
