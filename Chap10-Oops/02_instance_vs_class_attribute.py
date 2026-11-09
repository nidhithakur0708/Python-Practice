#Instance VS Class Attribute

class Employee:
    name="Nidhi"
    language="Python" #Class attribute

harry=Employee()
harry.name="Harry" #Object Attribute/Instance Attribute
print(harry.name, harry.language)

#Here harry.name will override the class attribute name for the object harry. So, it will print "Harry" instead of "Nidhi".