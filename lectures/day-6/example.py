# Today's topics:

# selective assignment using slicing
# reshaping arrays
# combining arrays
# saving to and reading from files

import numpy as np

n = np.array([
  [1, 2, 3, 4],
  [5, 6, 7, 8]
])

m = np.array([9, 10, 11, 12])

a = [1,2,3,4,5]

# print(a[2::2])

# print(m[1::])

# print(n[:,:3])

a[2] = 6
# print(a)

# change the last three elements of a to 7
for i in range(-3,0):
  a[i] = 7

m[-3:] = 7

# print(m)

n[:,::2] = 7

# print(n)

# Reshaping a numpy array

sevens = np.full((4,3), 7)
rands = np.random.random((3,6))

nums = np.arange(1,9,1)
# print(nums)

nums2 = nums.reshape(2,4)
# print(nums2)

nums3 = nums2.reshape(8)
# print(nums3)

nums.resize((2,4))
# print(nums)

m2 = np.append(m, 5)
# print(m2)

# Combining arrays
list1 = [1,2,3,4]
list2 = [8,9,10]

list3 = list1 + list2
# print(list3)

c = np.array([1,2,3,4])
d = np.array([5,6,7,8])
# NOT what we want: this will add the elements in each array
e = c + d
# print(e)

e = np.concatenate([c, d])
# print(e)

# print(n)
n2 = np.arange(1,13).reshape((3,4))
# print(n2)

n3 = np.concatenate([n, n2])
# print(n3)

n2 = np.arange(1,13).reshape((2,6))
# print(n2)

n4 = np.concatenate([n, n2], axis=1)
# print(n4)

# Saving numpy arrays to files
np.save('test.npy', n)

n5 = np.load('test.npy')
# print(n5)

# Saving multiple arrays to the same file
np.savez('test2.npz', c, d)
# Getting the saved arrays
n6 = np.load('test2.npz')
 # you can either loop through the items() method
for i in n6.items():
  print(i[1])

# or use index brackets [] and pass in the array name, e.g. 'arr_0', 'arr_1'
print(n6['arr_0'])