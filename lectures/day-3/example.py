def hello_world():
  print("hello world")

# hello_world()

def hello_name(name):
  print("hello " + name)

# hello_name("Zaheen")

def four_params(a, b, c, z):
  return a + b + c + z

result = four_params(1,2,3,10)

# print(result)

# loops allow you to repeat code

# while loop
x = 5
while (x < 10):
  # x = x + 1
  x += 1

# print(x)

# for loop
# for i in range(10):
#   print(i)

# for x in range(15,3,-1):
#   print(x)

n = [3,4,1,2,5,6]

# # print(n[0])
# total = 0
# for i in range(5):
#   print(total)
#   # total = total + n[i]
#   total += n[i]

def total(numbers):
  total = 0
  for i in range(len(numbers)):
    # total = total + n[i]
    total += n[i]
  return total

# print(total(n))

# list comprehension

# use a loop to double every number in a list
def doubler(numbers):
  for i in range(len(numbers)):
    # numbers[i] = numbers[i] * 2
    numbers[i] *= 2
  return numbers

# print(doubler(n))

m = [i * 2 for i in n]
# print(m)

def square(x):
  return x*x

l = [square(i) for i in n]
print(l)