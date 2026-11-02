#WAP to replace the word '######' with '####' in a same file

with open("Chap9-ps/04_problem.py") as f:
    content = f.read()
    new_content = content.replace("######","######")

with open("Chap9-ps/04_problem.py",'w') as f:
    f.write(new_content)
