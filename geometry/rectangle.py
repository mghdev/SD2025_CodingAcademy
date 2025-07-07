def perimeter(w,h):
    #=======================
    # TODO
    # Find the perimeter of a rectangle with side lengths w and h  (width and height)
    # Calculate the perimeter and assign it to the variable p
    p = 0
    #=======================
    return p


def area(w,h):
    #=======================
    # TODO
    # Find the area of a rectangle with width w and height h
    # Calculate the area and assign it to the variable a
    a = 0
    #=======================
    return a


def main():
    # This is a more realistic example of how functions like perimeter(w,h) and area(w,h) might be tested, compared to what was shown in 'circle.py' and 'triangle.py'
    # We will discuss this in class. There are some pre-made tests like this for code you will write during the early parts of this course.
    assert perimeter(1,5)       == 12,  "perimeter failed test with w = 1, h = 5" 
    assert perimeter(2.2,1.0)   == 6.4, "perimeter failed test with w = 2.2, h = 1.0" 
    assert perimeter(0,1)       == 0,   "perimeter failed test with w = 0, h = 1" 
    assert perimeter(50.0,0)    == 0,   "perimeter failed test with w = 50.0, h = 0" 

    assert area(2,2)        == 4,   "area failed test with w = 2, h = 2" 
    assert area(0,100)      == 0.0, "area failed test with w = 0, h = 100" 
    assert area(1.0,5.5)    == 5.5, "area failed test with w = 1.0, h = 5.5" 
    
    print("Passed all automated tests.")


if __name__ == "__main__":
    main()
