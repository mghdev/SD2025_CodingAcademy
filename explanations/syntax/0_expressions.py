# Everything after a '#' is a comment and will be ignored by the Python interpreter.
# The files in this directory will describe many features of basic Python syntax in comments, then give a few examples in code.
# For the first few lessons, launch an interactive session of your Python interpreter and follow along with the code examples.

# An 'expression' is some code that can be evaluated. 
# When code is being executed, this means expressions get processed to produce a single value, like a number, some text, a list, or a truth value.
# The most straightforward kind of expression is just a 'literal' value, like these:
23          # the type for whole numbers is called 'int'
0
5.7         # the type for numbers with a decimal point is called 'float'  (short for 'floating point number')
"capybara"  # the type for sequences of characters/text is called 'str'   (short for 'string')
[0,4]       # this particular type of sequence is called 'list'
True        # True/False are 'bool'
False
# In general, these will become whatever Python uses to directly represent the literal value that was typed, with no other processing steps.

# Multiple expressions can be combined into a single larger expression with 'operators'
# Operators perform some action to produce a value based on other values. 
# Here are some of Python's arithmetic operators: +, -, *, /, **, //, %
# Taking '-' as an example, expressions using the subtraction operator can be built up out of either one or two other expressions:
# expression - expression   ('binary' operator, uses 2 values to produce a new value)
# -expression               ('unary' operator, acts on a single value)
# Here are a bunch of examples of valid expressions using the arithmetic operators and literals:
2+5
5+2
-7
3.0-1
2+5*3-1
"a"+"b"
5*2.2
15.9/3
2**3
3**2
10%3
7//2
"c"*5
# These follow all of the typical rules for the order of operations.
# Remember that each of these is an expression: a bit of code that gets processed into a value when executed.
# Expressions on their own don't *do* anything else, they just become a value.
# If you run this script, it will not produce any output on your screen or change anything on your disk; it just evaluates a bunch of expressions then exits.

# You can use parentheses to group expressions and control the order of operations. Inner parentheses are evaluated first.
(2+5)*(3-1)
-(1+1)
((5+1)-(3-2))/(1+1)+2

# There are other kinds of operator, too. We will cover many of these in more detail later.
# Comparison operators: ==, >, <, >=, <=
# These produce a bool (True / False) value.
4 == 7
4 < 7
2.0 >= 2
"bee" > "bed"

# Operators for boolean expressions: not, and, or
not True
(3+2 > 4) and (-12 < 0)
False or 22%2 == 0

# The subscript operator for pulling individual elements out of a sequence: []
# For indexed sequences like list and str, the first element is at index 0, followed by index 1, then 2, and so on
"alphabet"[0]   # this evaluates to "a"
"alphabet"[1]   # this evaluates to "l"
"alphabet"[2]   # this evaluates to "p"
[2,4,8,16,32][1] # 4


# There are other pieces that expressions can be built from besides literals and operators.
# The next lesson will cover some more of these pieces.