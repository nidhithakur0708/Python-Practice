# class Employee:
#     a=1
#     def show(self):
#         print(f"The class attribute value of a is {self.a}")


# e=Employee()
# e.a=45
# e.show() #This will 45 as obj instance is given priority



#Now to show class attribute overriding the obj attribute u use @classmethod and cls
class Employee:
    a=1
    @classmethod
    def show(cls):
        print(f"The class attribute value of a is {cls.a}")

e=Employee()
e.a=45
e.show()  #1