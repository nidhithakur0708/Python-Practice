#4.Add a static method in problem 4 to greet the user with helloooo

class MyClass:
    a = 10  # Class attribute
    @staticmethod #We are not using self or cls, so we can use static method
    def greet():
        print("Helloooo there!")

nidhi=MyClass()  # Create an object of MyClass
nidhi.greet()  # Call the static method to greet the user