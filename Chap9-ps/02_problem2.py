import random
def game():
    print("You are playing a game")
    score=random.randint(1,100)
    #Fetch hiscore
# Fetch hiscore safely
    with open("Chap9-ps/02_problem2.txt") as f:
        file_content = f.read()

        if file_content != "":
            hiscore = int(file_content)
        else:
            hiscore = 0
    print(f"You score:{score}")
    if(score>hiscore):
        #write this hiscore to the file
        with open("Chap9-ps/02_problem2.txt","w") as f:
            f.write(str(score))
    return score

game()

