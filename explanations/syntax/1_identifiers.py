# An 'identifier' is a name defined by the programmer that refers to some object.
# Identifiers can contain upper- and lower-case letters, digits, and underscores  A-Z, a-z, 0-9, _
# Identifiers must start with a letter or underscore, NOT a digit.
# These are valid identifiers:
# a
# var1
# DOOM
# _local
# o_0_s_I_l_L_y_0_o
#
# These are not valid identifiers:
# 2a
# 5nine_r27

# The most common use of identifiers is to name variables
# A 'variable' is a container for data. They hold a value that can be re-used and potentially modified while a program is running.
# Variables are created with the 'assignment' operator '='
a = 5
var1 = "this is a str"
DOOM = 40 + 2
# The syntax is:
# identifier = expression
# The identifier on the lefthand side of the '=' operator becomes the name of a variable. The value of the expression on the righthand side is stored in the variable.

# Outside of the lefthandide of an assignment, a variable name evaluates to the value stored in the variable.
# To see the value stored in a variable while in interactive mode, simply type an expression containing only that variable's name:
a
var1
DOOM

# Once created, variables can be used in more complex expressions in the same ways you could use a literal value.
a + 2
b = 3
a + b
var2 = var1
WAR = DOOM*2

# assignment can also be used to change the value stored in an existing variable:
a = 2
a = 6
a = a + 3

# Note that assignment is NOT itself an expression; it does not evaluate to a value.
# This will raise a SyntaxError:
# (a = 3) + 2

# Another extremely common use for identifiers is to name 'functions'
# We will cover functions in much more detail later.
# For now, think of a function as some pre-existing code that you can execute using its name.
# You will learn about functions that you can call to produce various effects; one thing that all functions do is 'return' a value.
# This means that a function call is an expression, it evaluates to something.
# The basic syntax for a function call is:
# function_name()
# The name of the function, followed by a pair of parentheses. If the function needs some kind of input, then:
# function_name(arguments)
# Function arguments are like input values that the function will use to (usually) produce the value it returns.
# Multiple arguments to the same function are separated by commas.

# Calling some built-in functions:
# Try these out in interactive mode.
len("drachma")  # len() returns the number of elements in a sequence. This expression evaluates to 7
max(1,5)        # max() returns the largest of its arguments. This expression evaluates to 5
min(-1,6,2,-3)  # min() returns the smallest of its arguments. This expression evaluates to -3
bin(12)

# Some examples calling built-in functions related to types:
type(5)
type("abc") # the type() function returns the type of the value passed as an argument
float(7)    # This expression evaluates to 7.0 -- many built-in types come with a function for creating an object of that type. 
int(3.2)    # What do you think this function call returns?
list("abc")


# It is a good idea to pick a system for how you format your variable and function names and stick to it.
# That way, reading a name in your code will always tell you something about what the name refers to, even if the name itself is confusing.
# I personally recommend that variable names be all lower-case with underscores between words, like this:
example_var_name = 0
my_favorite_number = 22
flavor = "Vanilla"

# For variables that are only used for a few lines of code right after being created, a single letter or a letter and a number can be ok:
i = 0
x1 = 32
x2 = 5
j = -4


# Some more example code using the syntax features we've talked about so far:
a = 1
b = 1
c = 2
d = a+b-c
number_list = [a,b,c,d]
a = float(b+c) - 0.5 + number_list[3]
a = a*2
t = type(a)


# Finally, I will mention that there are some very specific names you are not allowed to use as your own identifiers called 'keywords'
# These are identifiers that have some special meaning built in to the Python language. For a full list, visit:
# https://docs.python.org/3/reference/lexical_analysis.html#keywords

# We will look at some of these keywords in the next lesson.