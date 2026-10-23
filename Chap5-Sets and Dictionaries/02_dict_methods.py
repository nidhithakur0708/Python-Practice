#Dict Methods
marks={
    'Nidhi':100,
    'Shivam':89,
    'Rohan':23,
    0:"harry"
}
#1.items-returns a list of (key,value) tuples.
print(marks.items())

#2.keys
print(marks.keys())

#3.values
print(marks.values())

#4.update
#If key value pairs present it updates and if not there it will be added
marks.update({"Nidhi":99,"Renuka":90})
print(marks)

#5.get-Returns values of specifies keys
print(marks.get("Nidhi")) 

#Difference in both the methods !!!!!!!!
print(marks.get("Nidhi1"))  #Returns None if not Present
# print(marks["Nidhi1"]) #Returns Error if not present

#6.pop-removes the specified key
marks.pop('Rohan')
print(marks)

#7.popitem()-removes the last inserted key value pairs
marks.popitem()
print(marks)