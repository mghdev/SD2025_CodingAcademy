# To quote wikipedia:
# Every year that is exactly divisible by four is a leap year, except for years that are exactly divisible by 100, 
# but these centurial years are leap years if they are exactly divisible by 400. 
# For example, the years 1700, 1800, and 1900 are not leap years, but the years 1600 and 2000 are.

# 'year' will be an int
def isLeapYear(year):
    #=======================
    # TODO
    # Figure out if 'year' is a leap year or not.
    # Use the modulo operator '%' to determine whether the year is divisible by 4, 100, and/or 400
    # Use if-statements to return True when the year meets the requirements for a leap year
    # Return False otherwise.
    # Remember that there is no year 0
    
    return False
    #=======================

def main():
    assert isLeapYear(1) == False, "isLeapYear failed test"
    assert isLeapYear(4), "isLeapYear failed test"
    assert isLeapYear(444), "isLeapYear failed test"
    assert isLeapYear(1700) == False, "isLeapYear failed test"
    assert isLeapYear(1600), "isLeapYear failed test"
    print("Passed all automated tests.")

if __name__ == "__main__":
    main()