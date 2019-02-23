
# Today's topics:
# Modules
# Matrices
# creating numpy arrays
# properties of numpy arrays
# numpy array operations
# slicing and filtering

# NumPy: Numerical Python

# import test

# test.say_hello("John")

# print(test.x)

from test import say_hello

# say_hello("John")

# import numpy
import numpy as np

# 2D list (matrix)
l2d = [
  [1,2,3,4],
  [5,6,7,8],
  [9,10,11,12]
]

# print(l2d)

a1 = [1, 2, 3, 4]
b1 = [5, 6, 7, 8]
c1 = [
  [2,3,4,5],
  [6,7,8,9]
]

# creating numpy arrays from python lists
a = np.array(a1)
b = np.array(b1)
c = np.array(c1)

# properties in numpy arrays
# get shape of array
# print(a.shape)
# print(c.shape)

# len() to get # of rows
# print(len(c))

# get the total number of elements
# print(c.size)

# this is how to access an element inside a 2D python list
# print(c1[0][2])
# this is how to access an element inside a 2D numpy array
# print(c[0,2])

# creating 'default' numpy arrays
# create an array of all one number
constants = np.full((4,3), 7)
# print(constants)
zeros = np.zeros((4,3))
# print(zeros)
ones = np.ones((4,3))
# print(ones)

# create a array of random numbers
randoms = np.random.random((4,3))
# print(randoms)

# create an evenly spaced range of integers
nums = np.arange(1,15,2)
# print(nums)

spaced = np.linspace(3,15,5)
# print(spaced)

# slicing
# print(a1[:3])
# print(a[:3])

# slicing 2d arrays
# print(c1)
sliced = [row[:2] for row in c1]
# print(sliced)

# print(c)
# print(c[:,-1:-3:-1])

# filtering
evens = [[i for i in row if i % 2 == 0] for row in c1]
# print(evens)

# print(c[c % 2 == 0])
# print(c[c <= 4])

l = [1,2,3,4,5]
n = np.array(l)

# Doing arithmetic operations on each element in a numpy array
# is much easier than with a python list
print([num * 2 for num in l])
print(n * 2)