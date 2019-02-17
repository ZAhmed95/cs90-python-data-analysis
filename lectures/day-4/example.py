# Today's topics:

# string formatting

# conditionals

# filtering

# slicing

# cumulative list processing

# matrices (multi-dimensional lists)

# STRING FORMATTING

# i = 5

# # print "My number is 5.", where 5 is the value of i
# print("My number is 5.")
# # NOT GOOD

# # concatenation
# print("My number is " + str(i) + ".")

# # string.format() method
# print("My number is {}.".format(i))

# # % (percent) formatting
# print("My number is %s." % (i))

# # string.format() with keyword arguments
# print("My number is {x}.".format(x = i))

# # f-strings (format strings)
# print(f"My number is {i}.")

# CONDITIONALS

# allows you to execute some code ONLY if a certain condition is met

x = 12

# if (x < 10):
#   print(f"{x} is less than 10.")


# if/else

# if (x < 10):
#   print(f"{x} is less than 10.")
# else:
#   print(f"{x} is NOT less than 10.")

# if/elif/else statement: as many conditions as you want

# if (x < 10):
#   print(f"{x} is less than 10.")
# elif (x < 15):
#   print(f"{x} is less than 15.")
# else:
#   print(f"{x} is NOT less than 15.")

# most common conditional operators:
# == (equals)
# != (not equals)
# <  (less than)
# >  (greater than)
# <= (less than or equal to)
# >= (greater than or equal to)

# FILTERING

grades = [65, 78, 95, 62, 84, 97, 77, 85, 99, 70]

total = sum(grades)
# print(total)
average = total / len(grades)
# print(average)

above_average = [grade for grade in grades if grade > average]
# print(above_average)

# FILTERING is NOT the same as CONDITIONAL PROCESSING
pass_or_fail = ["pass" if grade > average else "fail" for grade in grades]
# print(pass_or_fail)

# DICTIONARY COMPREHENSION
# {65: 'fail', 78: 'fail', 95: 'pass'}
d = {grade: 'pass' if grade > average else 'fail' for grade in grades}
# print(d)

# SLICING
l = [0,1,2,3,4,5,6,7,8,9]

# print(l)

# get first 5 elements of list:
first_five = l[:5]
# print(first_five)

last_five = l[-5:]
# print(last_five)

n = l[2:9:3]
# print(n)

# easy list copy
copy_l = l[::]
# print(copy_l)

# easy list reverse
rev = l[::-1]
# print(rev)

# CUMULATIVE PROCESSING

l = [0,1,2,3,4,5,6,7,8,9]
# Problem: create a list of cumulative sums from l
# example output: [0, 1, 3, 6, 10...]
csums = [sum(l[:i]) for i in range(1, len(l)+1)]
print(csums)