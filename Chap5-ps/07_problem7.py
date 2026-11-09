#Create a empty dictionary.Allow 4 friends to enter theri language as values and use keys as theier names.Assume the names are unique

#Q7.If the name of friend is same when what will happen
#Then the language entered later will be the final langauge

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