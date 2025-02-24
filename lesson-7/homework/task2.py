class EmployeeRecordsManager:
    def __init__(self, filename):
        self.filename = filename

    def add_employee(self, emp_id, name, position, salary):
        with open(self.filename, 'a') as file:
            file.write(f"{emp_id},{name},{position},{salary}\n")

    def view_employees(self):
        try:
            with open(self.filename, 'r') as file:
                records = file.readlines()
                return [record.strip() for record in records]
        except FileNotFoundError:
            return []

    def search_employee(self, emp_id):
        try:
            with open(self.filename, 'r') as file:
                for line in file:
                    if line.startswith(f"{emp_id},"):
                        return line.strip()
        except FileNotFoundError:
            return None
        return None

    def update_employee(self, emp_id, name=None, position=None, salary=None):
        try:
            with open(self.filename, 'r') as file:
                records = file.readlines()

            updated_records = []
            for record in records:
                fields = record.strip().split(',')
                if fields[0] == emp_id:
                    if name:
                        fields[1] = name
                    if position:
                        fields[2] = position
                    if salary:
                        fields[3] = salary
                    updated_records.append(','.join(fields) + '\n')
                else:
                    updated_records.append(record)

            with open(self.filename, 'w') as file:
                file.writelines(updated_records)
        except FileNotFoundError:
            pass

    def delete_employee(self, emp_id):
        try:
            with open(self.filename, 'r') as file:
                records = file.readlines()

            with open(self.filename, 'w') as file:
                for record in records:
                    if not record.startswith(f"{emp_id},"):
                        file.write(record)
        except FileNotFoundError:
            pass

    def menu(self):
        while True:
            print("\nEmployee Records Manager")
            print("1. Add new employee record")
            print("2. View all employee records")
            print("3. Search for an employee by Employee ID")
            print("4. Update an employee's information")
            print("5. Delete an employee record")
            print("6. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                emp_id = input("Enter Employee ID: ")
                name = input("Enter Name: ")
                position = input("Enter Position: ")
                salary = input("Enter Salary: ")
                self.add_employee(emp_id, name, position, salary)
                print("Employee added successfully!")
            elif choice == '2':
                employees = self.view_employees()
                if employees:
                    print("Employee Records:")
                    for emp in employees:
                        print(emp)
                else:
                    print("No records found.")
            elif choice == '3':
                emp_id = input("Enter Employee ID to search: ")
                employee = self.search_employee(emp_id)
                if employee:
                    print("Employee Found:", employee)
                else:
                    print("Employee not found.")
            elif choice == '4':
                emp_id = input("Enter Employee ID to update: ")
                name = input("Enter new Name (leave blank to keep unchanged): ") or None
                position = input("Enter new Position (leave blank to keep unchanged): ") or None
                salary = input("Enter new Salary (leave blank to keep unchanged): ") or None
                self.update_employee(emp_id, name, position, salary)
                print("Employee updated successfully!")
            elif choice == '5':
                emp_id = input("Enter Employee ID to delete: ")
                self.delete_employee(emp_id)
                print("Employee deleted successfully!")
            elif choice == '6':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")




if __name__ == '__main__':
    manager = EmployeeRecordsManager("employees.txt")
    manager.menu()
