# A 'simple statement' is a single line of code that *does* something.
# We've already seen one example of a statement: assignment. Assignment is a line of code that stores a value in a variable.
a = 2
s = "Hi, there."

# I would like to give a few more examples of simple statements.

# The 'pass' statement:
pass
# 'pass' does... nothing. It exists mostly to fill a line of code when you need one for syntax reasons, but aren't ready to put real code there yet.
# This is called a 'no-op', short for 'no operation'

# The 'return' statement
# This statement can only be placed inside function definitions, so I will write that out, too; don't worry about the details yet.
def myFunction():
    return 1+2
# The syntax is:
# return expression

# Whatever the expression after 'return' evaluates to will be what a call to the function evaluates to.
# Put another way, the 'return' statement tells a function what value to return.
myFunction()  # This function call is an expression, and it will evaluate to 3 because of the return statement I wrote earlier.


# The 'import' statement
import math
# Syntax:
# import module_name
# 'import' is for loading code from another 'module' (which just means a file) into the current module.
# We will cover this statement and using code from other modules in more detail later.
# As a quick example, the 'math' module contains the value of pi and a function for taking the absolute value of a number:
math.pi         # this expression evaluates to 3.141592653589793
math.fabs(-5)   # this expression evaluates to 5.0

# For a list of all the variables and functions in the math module, visit:
# https://docs.python.org/3/library/math.html
# To see a list of all the modules that come standard with python, visit:
# https://docs.python.org/3/library/index.html


# The 'asssert' statement
assert 4%2 == 0, "4 is not an even number, apprenty. Something is broken!"
# Syntax:
# assert expression, message
# 'assert' checks whether the expression after it evaluates to true
# if the expression is true, nothing else happens and the script continues
# if the expression is false, assert raises an error with the message
assert False, "This message will always show up in an AssertionError"

# There are also compound statements that take up more than one line of code and have interesting effects.
# We will cover some of those next.