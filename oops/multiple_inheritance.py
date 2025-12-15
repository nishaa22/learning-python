# Multiple Inheritance

class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id
        print("Employee constructor called")

    def get_employee_info(self):
        print(f"Name: {self.name}, ID: {self.emp_id}")


class Developer:
    def __init__(self, language):
        self.language = language
        print("Developer constructor called")

    def get_dev_info(self):
        print(f"Primary Language: {self.language}")


class Manager:
    def __init__(self, team_size):
        self.team_size = team_size
        print("Manager constructor called")

    def get_manager_info(self):
        print(f"Team Size: {self.team_size}")


class TechLead(Employee, Developer, Manager):
    def __init__(self, name, emp_id, language, team_size):
        Employee.__init__(self, name, emp_id)
        Developer.__init__(self, language)
        Manager.__init__(self, team_size)
        print("TechLead constructor called")

    def get_full_info(self):
        self.get_employee_info()
        self.get_dev_info()
        self.get_manager_info()


tl = TechLead("Nisha", 101, "Python", 5)
tl.get_full_info()
