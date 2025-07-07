def solveQuadratic(a,b,c):
    #=======================
    # TODO
    # solve the quadratic equation
    # ax^2 + bx + c = 0
    # Calculate and assign the two roots of the equation to the variables x1 and x2
    # It may simplify the expressions if you make a variable to hold an intermediate value.
    x1 = 0
    x2 = 0
    #=======================
    return x1,x2



def main():
    x1,x2 = solveQuadratic(1,-2,1) 
    assert x1 == 1 and x2 == 1 , "solveQuadratic failed test with a = 1, b = -2, c = 1"
    
    x1,x2 = solveQuadratic(2,-2,-12) 
    assert (x1 == 3 and x2 == -2) or (x1 == -2 and x2 == 3) , "solveQuadratic failed test with a = 2, b = -2, c = -12"
    
    x1,x2 = solveQuadratic(-3,-21,-36) 
    assert (x1 == -3 and x2 == -4) or (x1 == -4 and x2 == -3), "solveQuadratic failed test with a = -3, b = -21, c = -36"
    
    print("Passed all automated tests.")

if __name__ == "__main__":
    main()