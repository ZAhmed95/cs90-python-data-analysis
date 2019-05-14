# Project 3

This project involves creating a basic classifier model from scratch, which will predict the labels for the digits 0-9 after being given 8x8 greyscale images to train on.

The way the model will work:

For each possible label, the model stores a 'positive' coefficient array and a 'negative' coefficient array. The positive array contains high coefficient values where the images have dark pixels, and the negative array contains high coefficient values where the images have zeros or light pixels.

An image's score is determined by multiplying its pixels with the positive coefficient array, subtracting the product of the pixels and the negative coefficient array, then adding up the values.

So, for example, an image of a 0 should get a very high score when using the coefficient arrays for the label 0, because the pixels should properly align with the high positive coefficients, and avoid the high coefficients in the negative coef array.

Meanwhile, an image of a  1 being scored with those same coefficient arrays should get a lower score, because some of the dark pixels will fall in the 'negative' zones and subtract from the score, while not all of the 'positive' zones will be filled with pixels to increase the score.

## Instructions

The code structure for the project can be found in `project3.py`.

This project is slightly different in structure to the previous ones, due to its complex nature. I want you to focus on the actual logic behind the data science part, not get caught up in figuring out Python syntax.

Therefore, whereas the other projects were mostly empty and required you to write all the code, this project is mostly 'fill in the blanks': there are 15 `TODO` labels in the comments, which is where you have to write code. The rest of the structure is already written for you; **DO NOT** change anything that's already written.

Following the code in the python file is the best way to understand your tasks for this project. Here, I will list a general outline of the high level steps.

### Step 1: Write the fit method

The fit method for the classifier is responsible for taking input and output data and prepping the model for prediction. Follow the instructions in the fit method outline already written to complete it.

### Step 2: Write the predict method

The predict method takes in a set of input data and outputs labels for each data point. It should use whatever the fit method set up (in this case, the coefficient arrays) to make its decisions. Follow the instructions in the comments to complete the function.

### Step 3: Prepare the model

Split the data into training and testing sets, then fit the model using the training data.

### Step 4: Evaluate the model

Use the predict method on the testing data to generate some predicted labels. Then, compare the predicted results with the actual results to compute the accuracy of the model.