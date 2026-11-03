class Employee:
    name="Nidhi"
    language="Python" #Class attribute
    salary=100000

harry=Employee()   
harry.name="Harry" #Object Attribute/Instance Attribute
print(harry.name, harry.salary, harry.language)

rohan=Employee()
rohan.name="Rohan"
print(rohan.name, rohan.salary, rohan.language)

#Here name is Object Attribute and salary and language are Class Attributes as they  directly belong to the class.
