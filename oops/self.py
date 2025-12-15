class Employee:
  name="Nisha" # class attribute
  language="Python"
  salary=1200000

  # self parameter
  def getInfo(self):
    print(f"Name is {self.name}, language is {self.language}, and salary is {self.salary}")

  # we need to pass self param to all the class functions otherwise it will throw an error saying that Employee.greet() takes 0 positional arguments but 1 was given
  def greet(self):
    print("Good Morning!!")

  # but if we donot want to use any class attribut inside function and dont want to use self params then we have to use @staticmethod decorator
  @staticmethod
  def sayNamastey():
    print("Namastey!!")


e = Employee() # object attribute 
e.language = "Javascript"
print(e.name, e.language, e.salary)

e.sayNamastey()
e.greet()
e.getInfo()
# Employee.getInfo(e) is same as e.getInfo()
