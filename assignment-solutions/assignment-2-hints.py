# This file contains hints for how to do assignment 2
# Below is code to perform the data analysis steps from assignment 2
# ONLY on a single student's data
# You will have to adapt this to process every row in the data

import numpy as np

grades = np.array([13, 16, 12, 17, 18, 11, 13, 15, 7,  19])

averages = np.array([0.0] * 10)
averages[0] = grades[0]
averages[1] = ( grades[0] + grades[1] ) / 2

averages[1] = sum(grades[:2]) / 2
averages[2] = sum(grades[:3]) / 3

for i in range(len(grades)):
  averages[i] = sum(grades[:i+1]) / (i+1)

print(averages)

# Step 2: differences
diff = np.array([0.0] * 9)

diff[0] = averages[1] - averages[0]
diff[1] = averages[2] - averages[1]

for i in range(9):
  diff[i] = averages[i+1] - averages[i]

print(diff)

avg = sum(diff) / 9

print(avg)