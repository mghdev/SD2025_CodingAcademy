def findIntersectionPoint(a1,b1,a2,b2):
    #=======================
    # TODO
    # Find the intersection point of the two lines
    # y = a1 * x + b1
    # y = a2 * x + b2
    # Calculate and assign the coordinates of the intersection point to the variables x and y
    x = 0
    y = 0
    #=======================
    return (x,y)



def main():
    assert findIntersectionPoint(1,0,-1,0) == (0,0), "findIntersectionPoint failed test"
    assert findIntersectionPoint(1,0,2,-6) == (6,6), "findIntersectionPoint failed test"
    assert findIntersectionPoint(-1,10,4,1) == (1.8,8.2), "findIntersectionPoint failed test"
    print("Passed all automated tests.")

if __name__ == "__main__":
    main()