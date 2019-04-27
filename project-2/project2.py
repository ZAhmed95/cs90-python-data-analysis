# Step 1: Task 1:
# Import the packages you need to use here


# Import the data into a pandas dataframe



# Step 1: Task 2:
# Correlation table
# Use pandas to create a correlation table from the data



# Step 1: Task 3:
# Correlation heatmap
# Use matplotlib to plot a heatmap of the correlation table,
# So you can tell at a glance which columns are highly correlated by the color.
# Your heatmap must have:
# - axis labels
# - text labels for each image pixel, showing the numerical data from the corr table on the image
#   round the displayed numbers to 2 decimal places.

# Analyze the heatmap and list which features have high correlations (either positive or negative)
# and try to explain why their correlation is so high.

# Step 2: Task 1:
# Split the data into training and testing sets
# First, take the output column, Item_Outlet_Sales, out of the dataframe. Store it separately in a variable
# Then, use scikit learn's test train split functionality to split the input and output data,
# using an 80-20 split between training data and testing data.



# Step 2: Task 2:
# Train the model
# Use the training input data you got from the last step to train a linear regression model.



# Step 3: Task 1:
# Test the model
# Use the 'score' function of the linear model, and the testing part of the data,
# To see how your model performs.



# Step 3: Task 2:
# Plot the coefficients
# Create a BAR graph to plot the coefficients generated by the linear model.
# There should be 1 coefficient for each column in the data.
# Make sure the plot includes:
# - a title
# - labels for each feature column in the x axis