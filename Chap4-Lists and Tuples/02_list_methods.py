##List Methods-Will Change the Original List

#String Methods-Return a New String, Does not change the original string


friends=['Apple','Orange',45,2345.23,False,"Ram","Shyam"]
print(friends)

#1.Append Method-Adds an item to the end of the list
friends.append("Nidhi")
print(friends)

#2.sort Method-Sorts the list in ascending order
l1=[1,5,3,2,4]
l1.sort() #Sorts the list in ascending order
print(l1)


#3.reverse Method-Reverses the order of the list
l1.reverse()
print(l1)

#4.insert Method-Adds an item at the specified index
l1.insert(2,100) #Inserts 100 at index 2
print(l1)

#5.pop Method-Removes the item at the specified index and returns it
l1.pop(2) #Removes the item at index 2 and returns it
print(l1)

#6.remove Method-Removes the first item with the specified value
l1.remove(3) #Removes the first item with the value 3
print(l1)
