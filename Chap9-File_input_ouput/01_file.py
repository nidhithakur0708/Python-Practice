#Open is a build in function in python which is used to open a file. It takes two parameters, the first parameter is the name of the file and the second parameter is the mode in which you want to open the file. The default mode is 'r' which means read mode.

f=open("Chap9-File_input_ouput/01_file.txt")
data=f.read()
print(data)
f.close()

