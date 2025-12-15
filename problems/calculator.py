# Write a program to create a calculator using a class which will calculate square, cube and square root and cube root

class Calculator:
  def __init__(self, n):
    self.n = n
  
  def getSquare(self):
    print(f"square of {self.n}: ", self.n*self.n)

  def getCube(self):
    print(f"cube of {self.n}: ", self.n*self.n*self.n)  
  
  def getSquareRoot(self):
    print(f"square root of {self.n}: ", self.n**(1/2))  

  def getCubeRoot(self):
    print(f"cube root of {self.n}: ", self.n**(1/3))

c = Calculator(27)
c.getSquare()
c.getCube()
c.getCubeRoot()
c.getSquareRoot()