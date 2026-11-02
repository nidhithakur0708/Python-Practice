'''
1-for snake
-1-for water
0-gun
'''
#There was a observation when computer-You ==-1 or 2 thats when u lose else u win
import random

computer=random.choice([0,-1,1])
youstr=input("Enter your choice: ")
youDict={'s':1,'w':-1,'g':0}
reverseDict={1:"Snake",-1:"Water",0:"Gun"}
you=youDict[youstr]

print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

if(computer==you):
    print("Its a draw!")
else:
    if((computer-you)==-1 or (computer-you)==2):
        print("You Lose")
    else:
        print("You Win!")


