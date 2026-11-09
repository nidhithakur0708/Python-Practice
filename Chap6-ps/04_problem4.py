#WAP to find wheteer a given username contains less than 10 characters or not

userName=input("Enter you userName:")

string_length=len(userName)
if(string_length>=10):
    print("This username has more than 10 characters")
else:
    print("This username has less than 10 characters")