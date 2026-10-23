name="Simran"
print(name[0:3]) #Sim (0 to the 2nd Index,last index is not included)

print(name[-4:-1]) #imr (from the 4th index from the end to the 1st index from the end)

print(name[:4]) #Simr (from the beginning to the 3rd index)
print(name[4:]) #ran (from the 4th index to the end of the string)

#Gaps in slicing
word="Amazing"
print(word[0:7:2]) #Aai (from the 0th index to the 6th index with a gap of 2 )