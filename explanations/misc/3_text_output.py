# Starting with the next syntax lesson, it will be much better to follow along by writing your own scripts rather than only using interactive mode.
# So, we will take a quick detour away from syntax to talk about outputting text from your scripts.

# Create a file called 'printing.py' in this directory and type code you want to test out into that file.
# Run your script by typing this command into your console:
# python3 printing.py
# ... or by using a feature of your developer tools that executes a similar console command for you.

# To make a program output text to your console, call the built-in print() function
print("Hello World!")

# print() can take multiple arguments
print("First argument.","Second argument.","Third argument.")

# print() can handle many different types
num = 37.2
print(30,"white horses on a red hill",num,[0,1,2])

# Quick aside about function calls in general: any expression can be an argument, so...
# You can use a function call as an argument to another function.
print(max(13,17))

# You can print() mutliple lines in a single call with the special newline character "\n" or a multi-line str
print("\nFirst line.\nSecond line.\nThird line.\n")
print("""Triple quotes make a multi-
line
string
""")

# That covers all the main things you need to know about print, but here are a couple bonus features to look back at later:
# By default, print separates each argument with a blank space ' '
# To change that, you can assign your own value to the argument named 'sep'  (short for 'separator') like this:
print(2,4,7,21,sep="+")
print("Cats","dogs","chickens","pigs",sep=" and ")

# Similarly, if you don't want print() to advance to the next line after each call, you can set the 'end' argument
# 'end' is '\n' by default -- each print ends with a single newline unless you say otherwise
print("First call. ",end="")
print("Second call. ",end="blarg. ")
print("Third call.","Still the third call. ",end="Skip a line! \n\n")
print("Fourth call.")