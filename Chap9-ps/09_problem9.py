#9.WAP to find wheter a file is identical and matches the content of another file
with open("Chap9-ps/09_file1.txt") as f:
    content1=f.read()
with open("Chap9-ps/09_file2.txt") as f:
    content2=f.read()
if content1==content2:
    print("Both files are identical")
else:
    print("Both files are not identical")