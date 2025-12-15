# Single Inheritance

class Employee:
  def getInfo(self, name, company):
    print(f"Name of the employee is {name} and company is {company}")

class Programmer(Employee):
  def __init__(self, salary):
    self.salary = salary
    print(f"Salary is {self.salary}")

e = Employee()
e.getInfo("Nisha", "Microsoft")

p = Programmer("1200000")
p.getInfo("Nishu", "Google")

