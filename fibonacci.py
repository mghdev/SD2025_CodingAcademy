# The Fibonacci sequence goes 1 1 2 3 5 8 13 21 34 55 89 ...
# Each element in the sequence is the sum of the previous two.
# The rules are:
#   fibonacci(0) is 1
#   fibonacci(1) is 1
#   fibonacci(n) is fibonacci(n-1) + fibonacci(n-2)

def fibonacci(n):
    #=======================
    # TODO
    # Calculate the nth number in the Fibonacci sequence
    # Return only the nth number in the sequence, not the entire sequence up to that point.
    # Hints: 
    # Use at least 3 variables to hold successive elements of the sequence
    # Use a loop to advance through the sequence one number at a time
    # Each time you want to advance the sequence, you can shuffle the values of your 3 variables around 
    # to help you compute the next value without losing the old ones that you still need
    
    return 0
    #=======================


def main():
    assert fibonacci(0) == 1, "fibonacci failed test with n = 0"
    assert fibonacci(2) == 2, "fibonacci failed test with n = 2"
    assert fibonacci(20) == 10946, "fibonacci failed test with n = 20"
    assert fibonacci(40) == 165580141, "fibonacci failed test with n = 40"
    print("Passed all automated tests.")

if __name__ == "__main__":
    main()