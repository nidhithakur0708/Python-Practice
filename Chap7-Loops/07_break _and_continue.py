#Break-abruptly comes out the the loop

for i in range(100):
    if(i==34):
        break  #Exit the loop right now
    print(i)

#Continue-Skip this iteration
for i in range(100):
    if(i==14):
        continue  #Only skip this iteration and the code below it and move to the next iteration
    print(i)
