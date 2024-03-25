# lib/cli.py

import sys
from lib.helpers import (
    list_employees,
    find_employee_by_name,
    find_employee_by_id,
    create_employee,
    update_employee,
    delete_employee,
    list_department_employees  # Add this import if you have implemented this function
)

def main():
    while True:
        print("""
        Please select an option:
        0. Exit the program
        1. List all departments
        2. Find department by name
        3. Find department by id
        4: Create department
        5: Update department
        6: Delete department
        7. List all employees
        8. Find employee by name
        9. Find employee by id
        10: Create employee
        11: Update employee
        12: Delete employee
        13. List all employees in a department
        """)
        choice = input("> ")

        if choice == "0":
            sys.exit()
        elif choice == "1":
            # Call ORM methods related to Department class
            pass
        elif choice == "2":
            # Call ORM methods related to Department class
            pass
        elif choice == "3":
            # Call ORM methods related to Department class
            pass
        elif choice == "4":
            # Call ORM methods related to Department class
            pass
        elif choice == "5":
            # Call ORM methods related to Department class
            pass
        elif choice == "6":
            # Call ORM methods related to Department class
            pass
        elif choice == "7":
            list_employees()
        elif choice == "8":
            find_employee_by_name()
        elif choice == "9":
            find_employee_by_id()
        elif choice == "10":
            create_employee()
        elif choice == "11":
            update_employee()
        elif choice == "12":
            delete_employee()
        elif choice == "13":
            list_department_employees()
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
