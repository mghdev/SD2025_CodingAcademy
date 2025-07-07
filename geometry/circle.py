# The Python Standard Library's 'math' module defines the number pi as:
# pi = 3.141592653589793
# This import statement will grant access to that 'pi' variable within this script
from math import pi
# Now you can write expressions like:
# var = 7*pi + pi/2

def circumference(r):
    #=======================
    # TODO
    # Find the circumference of a circle with radius r
    # Calculate the circumference and assign it to the variable c
    c = 0
    #=======================
    return c


def area(r):
    #=======================
    # TODO
    # Find the area of a circle with radius r
    # Calculate the area and assign it to the variable a
    a = 0
    #=======================
    return a


def main():
    # Here are some examples of code calling these functions
    print("A circle of radius",1,"has circumference",circumference(1))

    radii = [0,4.5,10.0]
    for r in radii:
        print("A circle of radius",r,"has area",area(r))
    
    r = float(input("\nEnter the radius of a circle: "))  # input returns a string, remember to convert to a float!
    print("A circle of radius",r,"has circumference",circumference(r),"and area",area(r),"\n")
    

if __name__ == "__main__":
    main()