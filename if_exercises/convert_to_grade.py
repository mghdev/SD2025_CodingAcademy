def convertScoreToGrade(score):
    #=======================
    # TODO
    # Convert a numerical score between 0 and 100 to a letter grade
    # Based on what range the score is in, return a str containing the correct letter using if-statements.
    # 0-59 -> "F"
    # 60-69 -> "D"
    # 70-79 -> "C"
    # 80-89 -> "B"
    # 90+  -> "A"
    
    return "F"
    #=======================


def main():
    assert convertScoreToGrade(0) == "F", "convertScoreToGrade failed test with score = 0"
    assert convertScoreToGrade(59) == "F", "convertScoreToGrade failed test with score = 59"
    assert convertScoreToGrade(60) == "D", "convertScoreToGrade failed test with score = 60"
    assert convertScoreToGrade(70) == "C", "convertScoreToGrade failed test with score = 70"
    assert convertScoreToGrade(80) == "B", "convertScoreToGrade failed test with score = 80"
    assert convertScoreToGrade(90) == "A", "convertScoreToGrade failed test with score = 90"
    print("Passed all automated tests.")

if __name__ == "__main__":
    main()