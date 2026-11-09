#Multilevel Inheritance
#Programmer inherits employeee and Manager inherits Programmer

class Employee:
    a=1

class Programmer(Employee):  
    b=2

class Manager(Programmer):
    c=3

o=Employee()
print(o.a)
#print(o.b) #error

o=Programmer()
print(o.a,o.b)

o=Manager()
print(o.a,o.b,o.c)