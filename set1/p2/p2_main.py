
# Name: John Louie C. Caasi
# Section: IV-BSIT-A
# Activity: P2 - Custom Module: student_utils
# Date: November 21, 2026

# Importing the custom module
import student_utils

# Importing specific functions from the custom module
from student_utils import get_highest, get_lowest

# Importing a built-in Python module
import datetime


# Main program
print("===== STUDENT GRADE REPORT =====")

# Ask how many grades the user wants to enter
while True:
    try:
        number_of_grades = int(input("How many grades will you enter? "))

        if number_of_grades > 0:
            break
        else:
            print("Please enter a number greater than zero.")

    except ValueError:
        print("Invalid input! Please enter a whole number.")


# Store the grades entered by the user
grades = []

# Accept and validate each grade
for i in range(number_of_grades):
    while True:
        try:
            grade = float(input(f"Enter grade {i + 1}: "))

            if 0 <= grade <= 100:
                grades.append(grade)
                break
            else:
                print("Invalid grade! Enter a grade from 0 to 100.")

        except ValueError:
            print("Invalid input! Please enter a numeric grade.")


# Calculate the average using the custom module
average = student_utils.calculate_average(grades)

# Determine the student's status using the custom module
status = student_utils.get_status(average)

# Find the highest and lowest grades
highest = get_highest(grades)
lowest = get_lowest(grades)


# Display the student grade report
print("\n===== GRADE REPORT =====")

print("Entered Grades:", grades)
print("Average Grade:", round(average, 2))
print("Highest Grade:", highest)
print("Lowest Grade:", lowest)
print("Student Status:", status)

# Display the date and time using the datetime module
report_date = datetime.datetime.now()

print("Report Generated:", report_date.strftime("%B %d, %Y - %I:%M %p"))

print("\n===== END OF REPORT =====")
