#Check that tuple type cannot be changed in Python

a=(23,45,3423,"nidhi")
a[2]=56

'''
Traceback (most recent call last):
  File "e:\Nidhi Thakur\My Folder\Chap4-ps\03_problem3.py", line 4, in <module>
    a[2]=56
    ~^^^
TypeError: 'tuple' object does not support item assignment   
PS E:\Nidhi Thakur\My Folder>  
'''