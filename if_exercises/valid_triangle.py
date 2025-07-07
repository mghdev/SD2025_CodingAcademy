# A triangle can be formed from 3 sides if the two shorter sides combined are longer than (not equal to) the longest side

def isValidTriangle(a,b,c):
    #=======================
    # TODO
    # Figure out if side lengths a, b, and c can form a valid triangle
    # Use if-statements to determine which side is the longest one so you can compare it to the sum of the other two
    # return True if the sides can form a triangle, return False if they can't
    
    return False
    #=======================
    


def main():
    assert isValidTriangle(3,4,5), "isValidTriangle failed test with a = 3, b = 4, c = 5"
    assert isValidTriangle(1,1,1), "isValidTriangle failed test with a = 1, b = 1, c = 1"
    assert isValidTriangle(2,4,9) == False, "isValidTriangle failed test with a = 2, b = 4, c = 9"
    assert isValidTriangle(9,4,2) == False, "isValidTriangle failed test with a = 9, b = 4, c = 2"
    assert isValidTriangle(4.0,6.6,2.5) == False, "isValidTriangle failed test with a = 4, b = 9, c = 2"
    assert isValidTriangle(2,3,5) == False, "isValidTriangle failed test with a = 2, b = 3, c = 5"
    print("Passed all automated tests.")

if __name__ == "__main__":
    main()