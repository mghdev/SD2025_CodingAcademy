# The 'for' loop is a statement specialized at iterating over sequences
# The syntax is:
#
# for identifier in iterable:
#     body code
#
# Or, to describe it in different words:
#
# for variable_name in list:
#     body code


my_list = [4,1,22]
for num in my_list:
    print(num)


# This for-loop executes the body code once for each value in 'my_list', in order
# Each time the body is executed, the next element from 'my_list' is assigned to 'num'
# Here is an equivalent while-loop:

i = 0
while i < len(my_list):
    num = my_list[i]
    print(num)
    i += 1


# There is a type called 'range' that is commonly used with for-loops. Let's look at how it works then get some examples with for-loops.
# range(n) creates a sequence of all integers from 0 to n-1
r = range(8)
print(list(r))

# range also supports the start,stop,step system from slice operations
r = range(2,15,3)
print(list(r))


# There are a few common ways of using the for-loop.

# Iterating through a sequence:
# This example prints only the multiples of 3 from 'num_list':
num_list = [-3,5,7,9,15]
for x in num_list:
    if x%3 == 0:
        print(x)

# Using 'range()' to repeat some code a fixed number of times:
for i in range(5):
    print("KABOOM.")


# Using 'range(n)' to do something once for each number starting at 0 up to n-1:
for i in range(7):
    print("@"*i)


# Combining the elements of a list into a single result:
num_list = [-3,5,7,9,15]
result = 0
for x in num_list:
    result += x


# Searching for a specific element in a list, for example the largest one:
num_list = [-3,5,7,9,15]
max = num_list[0]
for x in num_list:
    if x > max:
        max = x