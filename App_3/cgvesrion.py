class Employee:
    def __init__(self, emp_id, name, designation):
        self.emp_id = emp_id
        self.name = name
        self.designation = designation



class EmployeeManagementSystem:
    def __init__(self):
        self.employees = []

    def add_employee(self, emp_id, name, designation):
        employee = Employee(emp_id, name, designation)
        self.employees.append(employee)
        print("Employee added successfully.")

    def remove_employee(self, emp_id):
        for employee in self.employees:
            if employee.emp_id == emp_id:
                self.employees.remove(employee)
                print("Employee removed successfully.")
                return
        print("Employee not found.")

    def get_employee(self, emp_id):
        for employee in self.employees:
            if employee.emp_id == emp_id:
                return employee
        return None

    def generate_report(self):
        if not self.employees:
            print("No employees found.")
            return

        print("Employee Report:")
        print("----------------")
        for employee in self.employees:
            print(f"Employee ID: {employee.emp_id}")
            print(f"Name: {employee.name}")
            print(f"Designation: {employee.designation}")
            print("----------------")

# Example usage
ems = EmployeeManagementSystem()

while True:
    print("\nEmployee Management System")
    print("1. Add Employee")
    print("2. Remove Employee")
    print("3. Generate Report")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        emp_id = input("Enter employee ID: ")
        name = input("Enter employee name: ")
        designation = input("Enter employee designation: ")
        ems.add_employee(emp_id, name, designation)

    elif choice == "2":
        emp_id = input("Enter employee ID: ")
        ems.remove_employee(emp_id)

    elif choice == "3":
        ems.generate_report()

    elif choice == "4":
        print("Exiting the program...")
        break

    else:
        print("Invalid choice. Please try again.")
