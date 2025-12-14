import sys;

# version
print(sys.version)
print("Hello world")


# Indentation - atleast one space before print 
if 5>2:
  print("Five is greater than two!!")

if 5>2:
        print("Five is greater than two!!")


# this will give error because print statement should have same space before
# if 5>2:
#         print("Five is greater than two!!")
#     print("Five is greater than two!!")


# variable declaration
x=5
y="Good"
print(x,y)

# by default print statement execute in one line but if you want to print in one line, then make use of end 
print("Hello World!", end=" ")
print("I will print on the same line.")

# printing numbers
print(3 + 3)
print(2 * 5)
print("I am", 35, "years old.")

# variable casting 
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

x = 5
y = "John"
print(type(x))
print(type(y))


x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

x = y = z = "Orange"
print(x)
print(y)
print(z)


fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

x = 5
y = "John"
# print(x + y) error


# global variables
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

s="nisha"
en= s.encode()
print(en,en.decode())