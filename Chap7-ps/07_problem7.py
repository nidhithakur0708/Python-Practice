#WAP to print the following star pattern
'''
  * 2sp 1s
 *** 
*****
'''
n =int(input("Enter the number: "))
for i in range(1,n+1):
    print(" "*(n-i),end="") #to not add a new line by default ,prevent it by end=""
    print("*"*(2*i-1),end="")
    print("")
