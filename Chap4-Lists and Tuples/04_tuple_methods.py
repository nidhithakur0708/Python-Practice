
#Methods will not change the original tuple, they will return a new tuple

a=(1,45,23,5454,"Nidhi",False)
print(a)

#1.Count Method
no=a.count(45) #Counts the number of occurrences of 45 in the tuple
print(no)

#2.Index Method
idx=a.index("Nidhi") #Returns the index of the first occurrence of the specified value
print(idx)

#len
print(len(a)) #Returns the number of items in the tuple