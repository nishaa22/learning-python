# readlines function of file reads lines one by one and return a list
# f = open("file.txt")
# lines = f.readlines()
# print(lines, type(lines))
# f.close()

# readline funtion reads one line at a time and return string
# f1 = open("file.txt")
# line1 = f1.readline()
# print(line1, type(line1))
# line2 = f1.readline()
# print(line2, type(line2))
# line3 = f1.readline()
# print(line3, type(line3))
# line4 = f1.readline()
# print(line4, type(line4))
# line5 = f1.readline()
# print(line5, type(line5)) # this will return an empty string
# f1.close()

# we can also perform this readline function using loop
f1 = open("file.txt")
line = f1.readline()
while(line!=""):
  print(line, type(line))
  line = f1.readline()
f1.close()