class Employee:
    salary=1200000
    language="Python" #Class attribute

    def getInfo(self):
        print(f"Salary: {self.salary}, Language: {self.language}")

    @staticmethod #Static method does not take self as an argument. It is not bound to the instance of the class. It can be called using the class name or the object name.
    def greet():
        print("Good Morning!")

nidhi=Employee()
nidhi.getInfo() #This will give nidhi as a argument hence we need to write self in the method definition. It will print the salary and language of the object nidhi.
#Employee.getInfo(nidhi)
nidhi.greet()