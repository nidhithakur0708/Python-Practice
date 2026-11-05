#The Perfect Guess

import random
print("The Perfect Guess Game!")

perfect_number=random.randint(1,100)

user_input=int(input("Enter a number guess:"))
user_chances=1

while(user_input!=perfect_number):
    if(user_input>perfect_number):
        user_input=int(input("Enter a lower number: "))
    elif(user_input<perfect_number):
        user_input=int(input("Enter a higher number: "))
    user_chances+=1

print(f"You got it in {user_chances} chance")