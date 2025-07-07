# You will also sometimes want to write scripts that are interactive;
# that is, scripts that allow a user to provide some inputs while the script is already running.
# The simplest tool to accomplish that is the built-in input() function

x = input("Enter some text: ")
print(x)   #simply echoes whatever the input was

# input() pauses execution of your script and waits for a user to enter a complete line of text (ending with a newline e.g. 'Enter') into the console
# it then returns the text entered by the user as a str
# If you want some other type, you'll have to remember to convert it:

x = float(input("Enter a number: "))
print(x+20)

# input() can take one argument, which is called a 'prompt'
# It simply prints the prompt before pausing to wait for the user's input
# The purpose of the argument is to *prompt* the user: to tell them what they should type.

a = int(input("Enter an integer: "))
b = float(input("Enter any real number: "))
c = input("What is your name? ")
print(a,b,c)
