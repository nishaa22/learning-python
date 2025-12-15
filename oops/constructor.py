class Employee:
  name = "Nisha" # class attribute
  language = "Python"
  salary = 1200000

  # __init__ is a dunder method which is invoked automatically when we create an object
  # def __init__(self):
  #   print("I am creating an object")
  
  # we can also pass other arguements inside init method
  def __init__(self, name, salary, language):
    self.name = name
    self.salary = salary
    self.language = language
    print("I am creating an object")

  # self parameter
  def getInfo(self):
    print(f"Name is {self.name}, language is {self.language}, and salary is {self.salary}")


# e = Employee() # object attribute 
# e.language = "Javascript"
# print(e.name, e.language, e.salary)

# e.getInfo()

# e1 = Employee() # init method will be invoked when we create object here

e2 = Employee("Nishu","1300000","NextJS")
print(e2.name, e2.salary, e2.language)