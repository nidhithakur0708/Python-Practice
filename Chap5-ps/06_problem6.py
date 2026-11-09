#Create a empty dictionary.Allow 4 friends to enter theri language as values and use keys as theier names.Assume the names are unique

d={}

name=input("Enter friends name: ")
lang=input("Enter Language name: ")
d.update({name:lang})

name=input("Enter friends name: ")
lang=input("Enter Language name: ")
d.update({name:lang})

name=input("Enter friends name: ")
lang=input("Enter Language name: ")
d.update({name:lang})

name=input("Enter friends name: ")
lang=input("Enter Language name: ")
d.update({name:lang})

print(d)