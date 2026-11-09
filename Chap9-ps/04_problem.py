#WAP to replace the word '######' with '####' in a same file

with open("Chap9-ps/04_problem4.txt") as f:
    content = f.read()
    new_content = content.replace("Donkey","######")

with open("Chap9-ps/04_problem4.txt",'w') as f:
    f.write(new_content)
