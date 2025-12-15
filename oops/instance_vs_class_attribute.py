class Employee:
  name="Nisha" # class attribute
  language="Python"
  salary=1200000

e = Employee() # object attribute 
e.language = "Javascript"
print(e.name, e.language, e.salary)

# instance attribute take preference over class attribute