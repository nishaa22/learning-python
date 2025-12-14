# We need to close the file everytime we open it.
# we can get rid of closing the file by using with keyword

with open("file.txt") as f:
  print(f.read())