#3.Append-'a' mode is used to append the data to the file. If the file does not exist, it will create a new file.
st="appended text!!!"
f=open('Chap9-File_input_ouput/04_file.txt','a')
f.write(st)
f.close()