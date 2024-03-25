# lib/helpers.py

from lib.models.employee import Employee

def list_employees():
    employees = Employee.get_all()
    for employee in employees:
        print(employee)

def find_employee_by_name():
    name = input("Enter the employee's name: ")
    employee = Employee.find_by_name(name)
    if employee:
        print(employee)
    else:
        print(f"Employee {name} not found")

def find_employee_by_id():
    try:
        employee_id = int(input("Enter the employee's id: "))
        employee = Employee.find_by_id(employee_id)
        if employee:
            print(employee)
        else:
            print(f"Employee {employee_id} not found")
    except ValueError:
        print("Invalid input. Please enter a valid employee id.")

def create_employee():
    name = input("Enter the employee's name: ")
    job_title = input("Enter the employee's job title: ")
    try:
        department_id = int(input("Enter the employee's department id: "))
        employee = Employee(name=name, job_title=job_title, department_id=department_id)
        employee.save()
        print(f"Success: {employee}")
    except ValueError as e:
        print(f"Error creating employee: {e}")

def update_employee():
    try:
        employee_id = int(input("Enter the employee's id: "))
        employee = Employee.find_by_id(employee_id)
        if employee:
            new_name = input("Enter the employee's new name: ")
            new_job_title = input("Enter the employee's new job title: ")
            try:
                new_department_id = int(input("Enter the employee's new department id: "))
                employee.name = new_name
                employee.job_title = new_job_title
                employee.department_id = new_department_id
                employee.save()
                print(f"Success: {employee}")
            except ValueError as e:
                print(f"Error updating employee: {e}")
        else:
            print(f"Employee {employee_id} not found")
    except ValueError:
        print("Invalid input. Please enter a valid employee id.")

def delete_employee():
    try:
        employee_id = int(input("Enter the employee's id: "))
        employee = Employee.find_by_id(employee_id)
        if employee:
            employee.delete()
            print(f"Employee {employee_id} deleted")
        else:
            print(f"Employee {employee_id} not found")
    except ValueError:
        print("Invalid input. Please enter a valid employee id.")
