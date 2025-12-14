import random
# lets make the game of rock, paper, scissors
"""
rock: 1
paper: -1
scissors: 0
"""

yourDict = {
  "r":1,
  "p":-1,
  "s":0
}
reverseDict = {
  1:"Rock",
  -1:"Paper",
  0:"Scissors"
}
print("WELCOME TO ROCK, PAPER, SCISSORS GAME")
print("You can write initials like r,p,s")
computer = random.choice([-1,0,1])
choice = input("Please enter your choice: ")
you = yourDict[choice]

print(f"You chose {reverseDict[you]} and computer chose {reverseDict[computer]}")

if(computer==you):
  print("Its a draw")
else:
  if(computer==1 and you==-1):
    print("You Win")
  elif(computer==1 and you==0):
    print("You Lose")
  elif(computer==-1 and you==0):
    print("You Win")
  elif(computer==-1 and you==1):
    print("You Lose")
  elif(computer==0 and you==1):
    print("You Win")
  elif(computer==0 and you==-1):
    print("You Lose")
  else:
    print("Something went wrong!!")