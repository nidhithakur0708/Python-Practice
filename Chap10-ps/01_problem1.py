#WAP to make a class programmer for storing information of few programers at Microsft

class Programmer:
    company="Microsoft"
    def __init__(self,name,salary,pincode):
        self.name=name
        self.salary=salary
        self.pincode=pincode

p=Programmer("John",100000,560001)
print(p.name,p.salary,p.pincode,p.company)