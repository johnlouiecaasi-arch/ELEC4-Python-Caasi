# Name: John Louie C. Caasi
# Section: IV-BSIT-A
# Activity: P2 - Custom Module: student_utils
# Date: November 21, 2026


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
