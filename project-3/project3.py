import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split

# matplotlib is not used for this project,
# but you can use the 'show' function defined below
# if you want to visualize any of the rows as images
# NOTE: for convenience, I've changed the function to take
# a 1D array of data, and the function reshapes it inside into 2D
import matplotlib.pyplot as plt
def show(row, cmap='Greys', **kwargs):
  plt.imshow(row.reshape((8,8)), cmap=cmap, **kwargs)
  plt.show()

# Load the digit dataset
dataset = datasets.load_digits()

images = dataset.images
data = dataset.data
target = dataset.target

class Classifier:
  def __init__(self):
    self.labels = None # list of all possible labels in data
    self.coefs = {} # dict of coefficient arrays for each label
    self.thresholds = None # dict of threshold values to use for each label
  
  # STEP 1: write the 'fit' function, to take input and output data and create coefficient arrays
  # fit method to train the classifier with data
  # The parameters:
  # X: 2D np array, each row is an array of input variables
  # Y: 1D np array, each row is a label
  def fit(self, X, Y):
    # switch out X and Y for copies, so the originals don't get changed
    X, Y = X.copy(), Y.copy()
    # n is the length of the entire data (i.e. # of rows of data)
    # m is the feature size, aka length of each row in X
    n, m = X.shape

    # TASK 1:
    # get all unique label values, and store them in self.labels
    self.labels = # TODO: Fill this in
    
    # For each label in labels, we create 2 coef arrays in self.coefs
    # one for 'positive' matching, and another for 'negative' matching
    for label in self.labels:
      label_coefs = {
        'positive': np.zeros(m),
        'negative': np.zeros(m)
      }
      self.coefs[label] = label_coefs
    
    # So, if one of the labels was 0,
    # you would access each coef array like this:
    # self.coefs[0]['positive'], self.coefs[0]['negative']
    
    # TASK 2:
    # Normalize the input data, so every value is from 0 to 1
    # i.e. if the max is 16, 16 becomes 1, 15 becomes 0.9375, 8 becomes 0.5, etc.
    # This is rather simple: just divide X by the maximum value in X
    X = # TODO: Fill this in

    # Loop through the input data
    for i in range(n):
      # get the data row
      row = X[i]
      # get the label for this row
      label = Y[i]
      # get the positive and negative coef arrays for this label
      pos = self.coefs[label]['positive']
      neg = self.coefs[label]['negative']
      
      # TASK 3: update the positive coef array
      # Subtasks:
      # 1: take the current data row, and square each value, storing the results in a new variable
      squared = # TODO: Fill this in by squaring the current data row
      # 2: cumulative average: we have to add this new squared row to the positive coef array
      # use the cumulative average formula to combine the values
      pos = # TODO: Fill this in
      
      # done updating postive coefficient, now do something similar for negative:
      
      # TASK 4: update the negative coef array
      # Subtasks:
      # 1: invert the values: the values are from 0 to 1,
      # flip them so the ones that used to be closer to 0 are now closer to 1,
      # and vice versa. e.g. 0 becomes 1, 1 becomes 0, 0.2 becomes 0.8, 0.5 stays 0.5, etc.
      inverted = # TODO: Fill this in to invert the values in the current row
      # 2: square the new values, just like before
      squared = # TODO: Fill this in
      # 3: update the negative coef array, again using cumulative average
      # this should be practically the same code as you wrote above, just replacing 'pos' with 'neg'
      neg = # TODO: Fill this in
      
      # update the coefs dictionary with the new coef arrays
      self.coefs[label]['positive'] = pos
      self.coefs[label]['negative'] = neg

    # fitting complete, the coefficient arrays have been created.
    # these will be used in the 'predict' method to decide what label to give each datapoint
    return
          
      
  # STEP 2: write the predict method that will assign labels to unseen data points
  # predict method to output predicted labels for given data
  def predict(self, X):
    # TASK 1: create a 'label' function, which takes a single row of data,
    # and outputs a label for it.
    def label(row):
      # subtasks:
      # 1: score this row using the coef arrays for each label
      # create an empty dict of scores
      scores = {label: 0 for label in self.labels}
      # loop through each label
      for label in self.labels:
        # get the coef arrays for this label
        pos = self.coefs[label]['positive']
        neg = self.coefs[label]['negative']
        # use the coef arrays to score this row, store it in the correct spot in the scores dict
        # remember: the score is the sum of the positive product minus the negative product 
        scores[label] = # TODO: fill this in
        
      # 2: Choose the label with the highest score
      # Find which label has the highest score in the scores dict, and return it
      # we have the output_label variable that will eventually contain the final result
      output_label = self.labels[0] # arbitrary starting point
      # TODO: change output_label to the label with the highest score
      
      # after changing output_label to the correct value, return it
      return output_label
      
    # TASK 2: apply the label function you just wrote to each row in the input array
    # return the resulting array of labels
    return # TODO: fill this in with code that applies the 'label' function to each row
  
# STEP 3: Prepare the model
# TASK 1: split the data
# This should be easy at this point: use train test split to split 'data' and 'target',
# 80% for training, 20% for testing
train_X, test_X, train_Y, test_Y = # TODO: fill this in
# Verify that this line prints appropriate looking shapes for the training/testing data
print(train_X.shape, test_X.shape, train_Y.shape, test_Y.shape)

# TASK 2: Fitting the model
# subtasks:
# 1: same as we did for LinearRegression and SVC, instantiate your Classifier and store it in the variable c
c = # TODO: fill this in
# 2: Call the fit method, passing in the training data
# TODO: fill this in

# STEP 4: Evaluating the model
# TASK 1: Call the predict method on your model, passing in the test X data as input.
predicted_Y = # TODO: fill this in
# TASK 2: compare how many labels in the predicted results match the expected results (test_Y)
# Print out the accuracy, which is (number of matches) / (total number of test data points)
# TODO: calculate and print the accuracy

# Final thoughts:
# The accuracy of this classifier seems low at first (and it definitely is, compared to something like SVC),
# but remember to always compare a classifier to the base case: random guessing.
# If we used random guessing with our 10 labels, the expected accuracy would be only around 10%,
# So even a poor accuracy of around 50% still means our classifier is a bit smarter than random guesses.
# Another thing to note is that if you run train_test_split, fit, and predict multiple times,
# you will get wildly different accuracy results. This shows that our classifier is very flaky,
# even with a relatively large sample of data, the predictions vary greatly depending on the input.

# This last question is not graded as part of the assignment, but just designed to make you think about data modeling:
# What could we improve in this classification model to make it perform better and more consistently?