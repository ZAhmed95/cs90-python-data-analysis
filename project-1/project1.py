import numpy as np
import pandas as pd

df = pd.read_csv('data.csv')

# STEP 1: HYPOTHESES GENERATION

# You don't have to do anything in this step.
# Look over these 7 hypotheses we will test in this project:
"""
1. Utility: items that are used more regularly usually sell more than products only used in specific circumstances.
2. Store Capacity: larger stores can obviously hold more items, so they should sell more.
3. Display Area: the more visible an item is, the more likely it is to be sold.
4. City Type: stores located in more affluent and urban areas should have higher total sales.
5. Store Age: older stores should sell more, due to an established reputation.
6. Item Weight: lighter items should sell more, due to convenience of carrying them by hand.
7. Maximum Retail Price: cheaper items should sell more in general (but does the increased amount sold outweigh the lower profit per item?)
"""
# this is a list of the feature columns,
# i.e. the columns we actually care about to test our hypotheses
feature_columns = [
  "Item_Weight",
  "Item_Fat_Content",
  "Item_Visibility",
  "Item_Type",
  "Item_MRP",
  "Outlet_Establishment_Year",
  "Outlet_Size",
  "Outlet_Location_Type",
  "Outlet_Type"
]

# STEP 2: DATA EXPLORATION

# Task 1: find unique values
def find_unique_values(data):
  """
  This function takes a dataframe and returns a series.
  This series contains the total number of unique values for each column in the original DF.
  The returned series should have 12 elements, 1 for each original column in the DF.
  """
  # write your code here

  # you can modify the return statement
  return
  
# Task 2: list which of the feature columns contain numerical data,
# and which contain categorical data
"""
Numerical columns:

Categorical columns:

"""

# Task 3: find out which columns have null values
def find_null_values(data):
  """
  This function takes a dataframe as input, and find how many null values are in each column.
  The output is a series containing the number of null values in each column.
  The series should have 12 elements, one for each column.
  """
  # write your code here

  # you can modify the return statement
  return

# Task 4: Find if any columns contain nonsensical data
# Answer with the name of the column, and what kind of nonsensical data it contains
# For example (not a real answer):
# The Outlet_Establishment_Year column contains nonsensical data.
# It contains years like 2050, which are in the future and thus cannot be valid.
"""
Answer here:

"""

# Task 5: Find if any columns contain values that can be merged
# For example (not a real answer):
# The Item_Type column contains values that can be merged.
# 'Dairy' and 'dairy' are the same, so they can be combined.
"""
Answer here:

"""

# STEP 3: DATA CLEANING

# Task 1: Fill any null values in numerical columns with the group average
# For example, if Item_Weight has a null value, use the average weight for that item
# to fill it, NOT the total average weight
def fill_numerical_null_values(data):
  """
  This function takes a single dataframe, and fills in the null values in the numerical columns
  with the average value based on Item_Identifier.
  """
  # First, create a DF that contains the average value per item

  # Then, use the average value per item to fill in the null values

  return

# Task 2: Fill in any null values in categorical columns with the group mode
# For example, if a row is missing Outlet_Size, use the most frequent size for that Outlet_Identifier
# to fill the missing value
def fill_categorical_null_values(data):
  """
  This function takes a single dataframe, and fills in the null values in the categorical columns
  with the mode value based on Outlet_Identifier.
  """
  # First, create a DF that contains the mode value per outlet

  # Then, use the mode value per outlet to fill in the null values

  return


# Task 3: Combine any values that can be merged.
# Previously in Step 2, you found any values that could be combined
# Now, go through the DF and combine those values
def merge_values(data):
  """
  This function takes a single DF and merges any similar values in the columns
  """
  # First, create a dictionary map of which values to convert

  # Then, go through each value in the appropriate column,
  # and use the map to convert it

  return


# STEP 4: FEATURE ENGINEERING

# Task 1: Creating a new feature
# Use the Outlet_Establishment_Year column to create a new column
# called Outlet_Age, which contains its age as of 2013.
def create_outlet_age(data):
  """
  This function creates the 'Outlet_Age' column in the dataframe, using the Outlet_Establishment_Year
  column as input.
  """
  # write your code here

  return


# Task 2: Create dummy columns for the categorical features
# In Step 2, you recognized which columns contain categorical data.
# Now, for each categorical column, create dummy columns that will contain
# the encoded value of the categorical data.
def create_dummy_columns(data):
  """
  This function creates dummy columns for each categorical column
  """
  # write your code here

  return
