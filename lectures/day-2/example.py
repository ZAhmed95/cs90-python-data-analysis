# print to console
# print('hello')

x = 5
# print(x)

x = "John"
# print(x)

# mathematical operations
a = 5
b = 3

# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a // b)
# print(a % b)

# python list
n = [1, 3, 5, 4, 6]
# print(n)

# print(n[2])
# print(n[0])
# print(n[-1])
# print(len(n))

n[2] = 7
n[-1] = 10
# print(n)

n.append(3)
# print(n)

# python dictionary
d = {
  'first_name': "John",
  'last_name': "Doe",
  'age': 30,
  'numbers': n
}
print(d)

print(d['first_name'])

d['first_name'] = "Jack"
print(d['first_name'])

d['weight'] = 170

# python function
def add(a, b):
  return a + b

x = 4
y = 3

z = add(x,y)
print(z)
