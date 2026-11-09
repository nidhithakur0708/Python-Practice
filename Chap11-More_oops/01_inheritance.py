class Employee:
    company="ITC"
    salary=12000
    def show(self):
        print(f"The name of Employee is {self.company} and the salary is {self.salary}")


class Programmer(Employee): #All the properties of Employee class will be inherited by Programmer class
    company="Microsoft"
    def showLanguage(self):
        print(f"The name is {self.company} and the language is {self.language}")

a=Employee()
b=Programmer()
b.show()
print(a.company,b.company)
