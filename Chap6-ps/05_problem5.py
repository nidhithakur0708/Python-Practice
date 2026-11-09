#WAP which finds whether a given name is present in the list or not
user_list=["Nidhi","Shivam","Ram","Asha","Atul"]
user_name=input("Enter a user name:")
if(user_name in user_list):
    print("Name is present in the list")
else:
    print("Name is not present in the list")