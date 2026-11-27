# Name: John Louie C. Caasi
# Section: IV-BSIT-A
# Activity: P1 - Student Grade Calculator
# Date: November 21, 2026

# Global variable: Can be accessed throughout the main program
grades = []


# Function for accepting and validating student grades
def enter_grades():

    # Local variable: Only accessible inside the enter_grades() function
    student_grades = []

    # Ask how many grades the user wants to enter
    while True:
        try:
            number_of_grades = int(input("How many grades do you want to enter? "))

            if number_of_grades > 0:
                break
            else:
                print("Please enter a positive integer.")

        except ValueError:
            print("Invalid input! Please enter a positive integer.")

    # Accept each grade
    for i in range(number_of_grades):
        while True:
            try:
                grade = float(input(f"Enter grade {i + 1}: "))

                if 0 <= grade <= 100:
                    student_grades.append(grade)
                    break
                else:
                    print("Invalid grade! Enter a grade from 0 to 100.")

            except ValueError:
                print("Invalid input! Please enter a numeric grade.")

    return student_grades


# Function for calculating the average grade
def calculate_average(grades):
    total = sum(grades)
    average = total / len(grades)

    return average


# Function for determining the student's status
def get_status(average):
    if average >= 75:
        return "Passed"
    else:
        return "Failed"


# Function for finding the highest grade
def get_highest(grades):
    highest = max(grades)

    return highest


# Function for finding the lowest grade
def get_lowest(grades):
    lowest = min(grades)

    return lowest

# Function for displaying the program menu
def show_menu():
    print("\n===== STUDENT GRADE CALCULATOR =====")
    print("[1] Enter Grades")
    print("[2] Calculate Average")
    print("[3] Display Highest Grade")
    print("[4] Display Lowest Grade")
    print("[5] Check Student Status")
    print("[6] Exit")


# Main program
while True:
    show_menu()

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        grades = enter_grades()
        print("\nEntered Grades:", grades)

    elif choice == "2":
        if len(grades) > 0:
            average = calculate_average(grades)
            print("Average Grade:", round(average, 2))
        else:
            print("Please enter grades first!")

    elif choice == "3":
        if len(grades) > 0:
            highest = get_highest(grades)
            print("Highest Grade:", highest)
        else:
            print("Please enter grades first!")

    elif choice == "4":
        if len(grades) > 0:
            lowest = get_lowest(grades)
            print("Lowest Grade:", lowest)
        else:
            print("Please enter grades first!")

    elif choice == "5":
        if len(grades) > 0:
            average = calculate_average(grades)
            status = get_status(average)
            print("Student Status:", status)
        else:
            print("Please enter grades first!")

    elif choice == "6":
        print("Thank you for using the Student Grade Calculator!")
        break

    else:
        print("Invalid choice! Please select from 1 to 6.")

# Difference Between Local and Global Variables:
# A global variable is declared outside a function and can be accessed throughout the program.
# In this program, grades is a global variable used to store the grades entered by the user.
# A local variable is declared inside a function and can only be accessed within that function.
# In this program, student_grades is a local variable used inside the enter_grades() function.