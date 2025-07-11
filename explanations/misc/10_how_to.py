# How To Write a Python Program

# 1. Set up a main function. This can start exactly the same way every time:
def main():
    pass

if __name__ == "__main__":
    main()


# 2. Above the 'main' function, set up a function that will solve the problem you're working on.
#   For example, if you want to sum all the numbers in a list, you could start like this:
def sum(num_list):
    return 0

#   You have to decide on:
#       a name for the function, 
#       whether it needs any arguments (inputs) -- this is 'num_list' in the above example, 
#       And something default to return. Your default return value should have the same type as what the final function wants to return.
#   For example, if I want to write a function that returns a new list with only the odd numbers from an input list...
def oddsOnly(num_list):
    return []
#   ... then my default return value should be a list.
#   Usually things like 0, an empty list [], or an empty string "" make good default return values

# 3. In your 'main' function set up a couple of tests or use cases for the rest of the code. Then run your script to make sure it's set up right.
#   e.g. call sum() or call oddsOnly(), and print whatever they return
# This can take the form of a specific test case:
def main():
    my_list = [2,-1,7,13]
    print(sum(my_list))   # because I haven't finished the sum() function yet, this should print 0

if __name__ == "__main__":
    main()

# Or it could involve user input()


# 4. Implement the function that solves the problem you're working on, and return the result.
#      In the case of oddsOnly(), for example, the final product might look like this:
def oddsOnly(num_list):
    result = []
    for x in num_list:
        if x % 2 == 1:
            result += [x]
    return result

def main():
    test_list = [0,5,0,-3,14]
    print(oddsOnly(test_list))

if __name__ == "__main__":
    main()