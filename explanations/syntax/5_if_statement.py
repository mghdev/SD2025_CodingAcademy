# The first compound statement we will look at is called the 'if' statement

# The syntax for an if-statement is:
# if condition:
#     body

# Here is a quick example:
a = 22
if a > 20:
    print("The variable was greater than 20.")
    print("... I can have multiple lines of code in the body of a single if-statement.\n")

# Description:
# The word 'if' followed by a boolean (True/False) expression which we will call the 'condition', then a colon ':', then a new line
#    On the new line, start with one additional level of indentation -- this usually means a tab or 4 single spaces.
#    After the indentation, you can type basically any code you want. There can be multiple lines of indented code made up of multiple statements and expressions.
#    This indented code is called the 'body' of the if-statement.
#    When the condition evaluates to True, the body will be executed.
#    When the condition evaluates to False, the body is skipped and program execution continues from the end of the if-statement
# 'if' statements will enable you to control which parts of a script get executed (or not) under certain conditions
# This is one part of a bunch of systems collectively called 'control flow'

# Notes on indentation:
#    You MUST be consistent across the entire file with how you indent; it is an error to mix tabs and spaces, or to mix how many spaces you use.
#    You SHOULD be conistent across all of your code in all files; otherwise it may be painful to copy and re-use sections of code.

# The condition can contain any boolean expression, no matter how complicated:
x1 = 50
if ((True or 1-1<0) and (((2+2)%3==0) and True) or x1 == 100/2) :
    print("That crazy thing was True.\n")


# Since the body is allowed to contain statements, if-statements can be nested.
# Nested if-statements result in multiple levels of indentation:
a = 25*2
b = 625**0.5
if not a == b:
    print("a and b were different:",a,b)
    a = a/4
    if a == b:
        print("a was divided by 4, and now a and b are equal:",a,b)
        b = 40
b = 3
print("Now b is 3 no matter what happened before:",b)
print("")


# You can also create a block of code to be executed if the condition evaluates to False using an 'else' clause:
# if condition:
#     body code
# else:
#     else body code
x = 90-max(50,100)
if x > 0:
    x = 0
    print("Positive changed to zero.\n")
else:
    print("x is not positive.\n")


# Or, you can chain multiple ifs and elses together with 'elif' (short for else if)
x = 90-max(50,100)
if x > 0:
    x = 0
    print("Positive changed to zero:",x,"\n")
elif x < 0:
    x = -x
    print("Negative changed to positive:",x,"\n")
else:
    print("x was zero to begin with:",x,"\n")


# In the context of if-statement condition expressions, there are some funny rules about what is considered true and false:
# False, None, any type of numeric value equal to 0, and empty containers like the empty str "" or empty list [] are all considered false
# *Everything else* is considered true
if 27:
    print("1) Yes.")
else:
    print("1) No.")

if []:
    print("2) Yes.")
else:
    print("2) No.")

if len("abc")-3:
    print("3) Yes.")
else:
    print("3) No.")