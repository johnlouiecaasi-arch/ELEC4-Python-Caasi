# Name: John Louie C. Caasi
# Section: IV-BSIT-A
# Activity: P3 - Student Record Manager
# Date: November 21, 2026


# List for storing student names
students = []

# Set for storing normalized names to prevent duplicates
student_name_set = set()


# Function for adding a student
def add_student():
    name = input("Enter student name: ").strip()

    if name == "":
        print("Student name cannot be empty!")
        return

    # Convert the name to lowercase for duplicate checking
    normalized_name = name.casefold()

    if normalized_name in student_name_set:
        print("Student already exists!")
    else:
        students.append(name)
        student_name_set.add(normalized_name)
        print(f"{name} has been successfully added!")


# Function for removing a student
def remove_student():
    name = input("Enter the student name to remove: ").strip()

    normalized_name = name.casefold()

    if normalized_name in student_name_set:
        # Find and remove the matching name from the list
        for student in students:
            if student.casefold() == normalized_name:
                students.remove(student)
                break

        # Remove the normalized name from the set
        student_name_set.remove(normalized_name)

        print(f"{name} has been successfully removed!")
    else:
        print("Student not found!")


# Function for searching a student
def search_student():
    name = input("Enter student name to search: ").strip()

    if name == "":
        print("Please enter a name to search!")
        return

    # Search using partial names without considering capitalization
    search_result = []

    for student in students:
        if name.casefold() in student.casefold():
            search_result.append(student)

    if len(search_result) > 0:
        print("\nSearch Results:")

        for student in search_result:
            print(student)
    else:
        print("No matching student found!")


# Function for displaying all students
def display_students():
    if len(students) == 0:
        print("No students found!")
        return

    # Sort student names alphabetically
    sorted_students = sorted(
    students,
    key=lambda name: name.split()[-1].casefold()
)

    print("\n===== STUDENT LIST =====")

    # Display students with numbers
    for number, student in enumerate(sorted_students, start=1):
        print(f"{number}. {student}")

    # Display the total number of students
    print("\nTotal Students:", len(students))


# Function for displaying the program menu
def show_menu():
    print("\n===== STUDENT RECORD MANAGER =====")
    print("[1] Add Student")
    print("[2] Remove Student")
    print("[3] Search Student")
    print("[4] Display All Students")
    print("[5] Exit")


# Main program
while True:
    show_menu()

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        add_student()

    elif choice == "2":
        remove_student()

    elif choice == "3":
        search_student()

    elif choice == "4":
        display_students()

    elif choice == "5":
        print("Thank you for using the Student Record Manager!")
        break

    else:
        print("Invalid choice! Please select from 1 to 5.")


# Difference Between Lists and Sets:
# A list stores multiple values and maintains their order.
# In this program, the students list stores all the student names.
# A set stores unique values and automatically prevents duplicate entries.
# In this program, student_name_set checks if a student name already exists.
