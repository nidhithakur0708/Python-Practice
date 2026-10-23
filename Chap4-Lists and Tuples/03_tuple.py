#Tuple is same as list but it is immutable. It means we can not change the value of tuple once it is created. Tuple is defined by using () brackets. Tuple can be used to store multiple items in a single variable. Tuple is faster than list because of its immutability.

a=(1,2,5,6)
print(type(a)) #Prints the type of a which is tuple

# b=(1) -This is not a tuple, it is an integer. To create a tuple with a single element, you need to add a comma after the element.
b=(1,) #This is a tuple with a single element
print(type(b)) #Prints the type of b which is tuple

a[0] = 10 #This will give an error because tuple is immutable and we cannot change the value of a tuple once it is created.




