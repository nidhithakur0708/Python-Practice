#WAP to rename a file to renamed a file to "renamed_by_python.txt"

with open("Chap9-ps/11_problem11.txt") as f:
    content = f.read()

with open("Chap9-ps/11_renamed_by_python.txt",'w') as f:
    f.write(content)