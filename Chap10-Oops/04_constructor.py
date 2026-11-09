
class Employee:
    #__init__ is a dunder method automaticalled called on object initialization
    def __init__(self,name,salary,language):
        print("Constructor is called automatically when an object is created")
        self.name=name #Instance attribute
        self.salary=salary #Instance attribute
        self.language=language #Instance attribute

    @staticmethod
    def say_hello():
        print("Hello!")

nidhi=Employee("Nidhi",1200000,"Python")
print(nidhi.name, nidhi.salary, nidhi.language)