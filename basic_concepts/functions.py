# function
def greet():
  print("Good Morning")
greet()

# function with arguement
def greet(name):
  print("Good Morning " + name)
greet("Nisha")

# function with default arguement
def greet(name, ending="Thanks"):
  print(f"Good Morning {name}! {ending}")
greet("Nisha","Smile")
greet("Nishu")

# function with return statement
def sum(a,b):
  return a+b
print(sum(5,10))

# recursive function
# factorial
def factorial(n):
  if(n==1 or n==0):
    return 1
  else:
    return n * factorial(n-1)
n=int(input("Enter a number: "))
print(factorial(n))

# sum of n natural number using recursion
def sumOfNaturalNumber(n):
  if(n==1):
    return 1
  else:
    return n + sumOfNaturalNumber(n-1)
num = int(input("Enter the number: "))
print("Sum of n natural number is ", sumOfNaturalNumber(num))