#2.Create a class 'Pets' from class Animal and further create a class 'Dog' from 'Pets'.Add a method bark to class 'Dog'

class Animals:
    pass
class Pets(Animals):
    pass
class Dog(Pets):
    @staticmethod
    def bark():
        print("Bow bow!")

d=Dog()
d.bark()