#WAP tp find out wheter a given post is talking about "Harry" 

post=input("Enter the post: ")

if("Harry".lower() in post.lower()):
    print("Post is talking about harry")
else:
    print("Post is not talking about harry")