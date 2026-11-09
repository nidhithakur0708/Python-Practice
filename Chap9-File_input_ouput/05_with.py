f=open("Chap9-File_input_ouput/05_file.txt")
print(f.read())
f.close()

#The same can be written using with statement. The advantage of using with statement is that it automatically takes care of closing the file once the block of code is executed.

with open("Chap9-File_input_ouput/05_file.txt") as f:
    print(f.read())