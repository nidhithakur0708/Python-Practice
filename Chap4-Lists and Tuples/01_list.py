'''
Container to store items for any data types
'''

friends=['Nidhi','Riya','Anjali','Pooja',45,False,True,3.14]
print(friends[0])

#Unlike Strings ,Lists are mutable, we can change the value of a list once it is created
friends[3]="Pooja Thakur"
print(friends)


#Slicing in List-works same as strings
print(friends[0:4]) #Nidhi,Riya,Anjali,Pooja Thakur

