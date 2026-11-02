#1.Readlines-retutns a list containing each line in the file as a list item. It takes no parameters.
f=open('Chap9-File_input_ouput/03_file.txt')
lines=f.readlines()
print(lines,type(lines))
f.close()

#2.Readline-returns a single line from the file. It takes no parameters.
# f=open('Chap9-File_input_ouput/03_file.txt')
# line=f.readline()
# print(line,type(line))
# f.close()

#Using While loop to read all lines in the file using readline() function.
f=open('Chap9-File_input_ouput/03_file.txt')
line=f.readline()
while(line!=""):
    print(line)
    line=f.readline()
f.close()