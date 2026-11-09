#WAP to give the line number where the word python in prsent in problem 6

with open("Chap9-ps/06_problem6.txt") as f:
    lines = f.readlines()

    lineno=1
    for line in lines:
        if "Python" in line:
            print(f"Python is present in line number:{lineno}")
            break
        lineno+=1
    else:
        print("Python is not present in the file")