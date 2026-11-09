#Create a empty dictionary.Allow 4 friends to enter theri language as values and use keys as theier names.Assume the names are unique

#8.Now if the language is same for 2 friends when what 
#Then nothing both all be stored for both friends

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