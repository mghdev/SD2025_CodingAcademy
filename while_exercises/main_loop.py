# For this exercise, you will implement a simple version of a very useful pattern.
# It is used in apps ranging from games to web servers to Python's interactive mode.
# Depending on the context, it may be called a 'main loop', 'event loop', 'message loop', or 'game loop'
# The idea is to have a loop that repeats endlessly and handles inputs and events until it receives some sort of signal to exit.

def main():
    #=======================
    # TODO
    # Here is pseudocode describing what you should do:
    #
    # Create a variable that tracks whether the loop should continue
    # While the loop should continue
    #    Ask the user for text input
    #    If the user typed "exit"
    #        Update the loop variable to indicate that the loop should terminate
    #    Otherwise,
    #        (In general, process the input/events here)
    #        For this script specifically, print their input, but in reverse
    should_continue = True
    while should_continue:
        pass
    #=======================

if __name__ == "__main__":
    main()