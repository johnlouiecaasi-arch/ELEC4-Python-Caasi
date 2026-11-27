# Name: John Louie C. Caasi
# Section: IV-BSIT-A
# Activity: P4 - Safe Menu Program
# Date: November 22, 2026


# Function for displaying the program menu
def show_menu():
    print("\n===== SAFE MENU PROGRAM =====")
    print("[1] Division Calculator")
    print("[2] Open a Text File")
    print("[3] Exit")


# Function for performing division
def division_calculator():
    print("\n===== DIVISION CALCULATOR =====")

    try:
        # Ask the user to enter two numbers
        first_number = float(input("Enter the first number: "))
        second_number = float(input("Enter the second number: "))

        # Perform the division
        result = first_number / second_number

    except ValueError:
        print("Invalid input! Please enter numeric values.")

    except ZeroDivisionError:
        print("Error! Division by zero is not allowed.")

    else:
        # This runs when no exception occurs
        print("Result:", result)

    finally:
        # This always runs whether an error occurs or not
        print("Division operation finished.")


# Function for opening and displaying a text file
def open_text_file():
    print("\n===== OPEN TEXT FILE =====")

    filename = input("Enter the file name: ").strip()

    try:
        # Open the file in read mode
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()

    except FileNotFoundError:
        print("Error! The file does not exist.")

    except PermissionError:
        print("Error! You do not have permission to open this file.")

    else:
        # This runs when the file is opened successfully
        print("\n===== FILE CONTENTS =====")

        if content:
            print(content)
        else:
            print("The file is empty.")

    finally:
        # This always runs after the file operation
        print("File operation finished.")


# Main program
while True:
    show_menu()

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        division_calculator()

    elif choice == "2":
        open_text_file()

    elif choice == "3":
        print("Thank you for using the Safe Menu Program!")
        break

    else:
        print("Invalid menu choice! Please select from 1 to 3.")
