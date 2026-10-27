#A spam comment is defined as a text with the following words
'''
"Make a lot of money" "buy now" "click this" "subscribe this"
'''
#write a program to detect these spams
#in key word
p1="Make a lot of money" 
p2="buy now"
p3="click this"
p4="subscribe this"

message=input("Enter you comment:")
if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
    print("This is a spam message")
else:
    print("This is not a spam message")