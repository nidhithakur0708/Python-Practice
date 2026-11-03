#Create a class with a class attribute a;create an obj from it and set 'a' directly using obj.a=0. Does it change the class attribute?

class MyClass:
    a = 10  # Class attribute

obj = MyClass()  # Create an object of MyClass
obj.a = 0  # Set the attribute directly on the object
print(f"Object attribute a: {obj.a}")  # Accessing object attribute
print(f"Class attribute a: {MyClass.a}")  # Accessing class attribute


#no the class attribute remains unchanged, the object has its own instance attribute 'a' which is separate from the class attribute.