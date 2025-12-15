s = "this is the String."

# convert string to lowercase
print(s.lower())

# convert string to uppercase
print(s.upper())

# convert first letter of all the words in uppercase in the string
print(s.title())

# convert first letter of the first word capital
print(s.capitalize())

# starts with
print(s.startswith("th"))

# ends with
print(s.endswith("ng"))

# trims the white space from the string
st = "    Hello world    "
print(st)
print(st.strip())
print(st.lstrip())
print(st.rstrip())

# replace and split
newString = "Hello world world"
print(newString.replace("world", "Nisha")) #replace all occurence 
print(newString.split()) # return list

# format method acts a template literal
k = "my name is {name} and my age is {age}"
print(k.format(name="Nisha", age=23))

# join two string
print("-".join(newString))

# letter count in string
print(newString.count("o"))

# length of string
print(len(newString))

# find method - return index of first occurence
print(newString.find("o"))


# CHECK METHODS:
a1 = "Hii3434"
a2 = "342344"
a3 = "Hello"
a4 = "@#$$dsf454"
a5 = "423.454"
a6 = "Ⅻ"
a7 = "१२३"
a8 = "½"

# isdigit method returns true if the string includes only numbers
print(a1.isdigit(), a2.isdigit(), a5.isdigit())

# isalpha method returns true if the string includes only alphabets
print(a1.isalpha(), a2.isalpha(), a3.isalpha())

# isalnum method returns true if the string includes number or alphabet
print(a1.isalnum(), a2.isalnum(), a3.isalnum(), a4.isalnum())

# isdecimal method returns true if the string have numbers
print(a5.isdecimal(),a1.isdecimal(), a2.isdecimal())

# isnumeric method returns true for roman number, fraction, hindi number, number 
print(a6.isnumeric(), a7.isnumeric(), a8.isnumeric(), a2.isnumeric())

# major difference between isdigit, isnumeric, isdecimal
# isdecimal only contains 0-9
# isdigit contains numbers, hindi numbers, superscript(power)
# isnumeric contains fraction, number, roman

# zfill methods adds 0 before number and make required digit number
print(a2, a2.zfill(10))

# encode method change the string to some encrypted string
print(s.encode())