# write a function in which user can play a game and return an integer as a scrore and store that score in a file and update the hiscore if the new score is greater than the previous score
import random

def game():
  print("You are playing a game")
  score = random.randint(1,62)
  # fetching the hiscore
  with open("hiscore.txt") as f:
    hiscore = f.read()
    if(hiscore!=""):
      hiscore = int(hiscore)
    else:
      hiscore = 0
  print("Your score: ", score)
  if(score>hiscore):
    # writing the hiscore in file
    with open("hiscore.txt","w") as f:
      f.write(str(score))

  return score

game()