# Multi-Level Inheritance
# Person -> Employee -> Manager

class Person:
    def __init__(self, name):
        self.name = name

    def show_name(self):
        print(f"Name: {self.name}")


class Employee(Person):
    def __init__(self, name, emp_id):
        super().__init__(name) # super calls the constructor of base class
        self.emp_id = emp_id

    def show_employee(self):
        print(f"Employee ID: {self.emp_id}")

class Manager(Employee):
    def __init__(self, name, emp_id, department):
        super().__init__(name, emp_id)
        self.department = department

    def show_manager(self):
        print(f"Department: {self.department}")

m = Manager("Nisha", 201, "IT")

m.show_name()
m.show_employee()
m.show_manager()
