def hypotenuse(a,b):
    #=======================
    # TODO
    # Find the length of the hypotenuse of a right-triangle with short sides a and b
    # Calculate the length of the hypotenuse and assign it to the variable c
    c = 0
    #=======================
    return c

def perimeter(a,b,c):
    #=======================
    # TODO
    # Find the perimeter of a triangle with side lengths a, b, and c
    # Calculate the perimeter and assign it to the variable p
    p = 0
    #=======================
    return p

def area(a,b,c):
    #=======================
    # TODO
    # Find the area of a triangle with side lengths a, b, and c
    # Use google if you're not sure how to find the area with only the sides (hint: it involves the perimeter)
    area = 0
    #=======================
    return area

def main():
    # The 'main' function will hold code that we want to execute when this script gets run directly.
    # It will not be executed when you import this module to use its functions in another file.
    print("A right triangle with sides 5 and 12 has a hypotenuse of length",hypotenuse(5,12))

    print("\nThe perimeter of a triangle with sides 4, 1, and 9 is",perimeter(4,1,9))

    print("\nThe area of a triangle with sides 3, 10, and 5 is",area(3,10,5))
    
    side_1 = float(input("\nEnter a side length: "))
    side_2 = float(input("Enter a second side length: "))
    print("A right triangle with sides",side_1,"and",side_2,"has a hypotenuse of length",hypotenuse(side_1,side_2))


# Python sets the special __name__ variable to "__main__" within this file when this script gets executed
if __name__ == "__main__":
    main()