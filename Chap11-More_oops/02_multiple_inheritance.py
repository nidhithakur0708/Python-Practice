class Employee:
    company="ITC"
    name="Default Name"
    salary=120000
    def show(self):
        print(f"The name of Employee is {self.company} and the salary is {self.salary}")


class Coder:
    language="Python"
    def printLanguage(self):
        print(f"Out of all language here is your lanaguage:{self.language}")


class Programmer(Employee,Coder): #All the properties of Employee class will be inherited by Programmer class
    company="Microsoft"
    def showLanguage(self):
        print(f"The name is {self.company} and the language is {self.language}")

a=Employee()
b=Programmer()


b.show()
b.printLanguage()
b.showLanguage()
