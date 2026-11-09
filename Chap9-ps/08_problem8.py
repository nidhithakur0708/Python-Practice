with open("Chap9-ps/08_this.txt") as f:
    content=f.read()

with open("Chap9-ps/08_copy_this.txt",'w') as f:
    f.write(content)