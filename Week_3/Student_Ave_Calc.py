# Program to calculate average marks and determine pass/fail

choice = "Y"

# Repeat the program while the user chooses Y
while choice == "Y":

    # Input three quiz marks
    quiz_1 = float(input("Enter Quiz 1 mark: "))
    quiz_2 = float(input("Enter Quiz 2 mark: "))
    quiz_3 = float(input("Enter Quiz 3 mark: "))

    # Calculate average mark
    average = (quiz_1 + quiz_2 + quiz_3) / 3

    # Display average
    print("Average Mark =", average)

    # Determine pass or fail
    if average >= 50:
        print("PASS")
    else:
        print("FAIL")

    # Ask whether to continue
    choice = input("Continue? Select Y/N: ").upper()

print("Program Ended")