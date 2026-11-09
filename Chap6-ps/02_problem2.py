#2.WAP to find out whether a student is pass or fail if it requires a total of 40% and atleast 33 & in each subject to pass.Assume 3 subjects and tae marks as input from the users,

m1=int(input("Enter marks 1:"))
m2=int(input("Enter marks 2:"))
m3=int(input("Enter marks 3:"))

#Check for total percentage

total_precentage=((m1+m2+m3)/300)*100

if(total_precentage>40 and (m1>=33 and m2>=33 and m3>=33)):
    print("You are pass",total_precentage)
else:
    print("You are failed,try again later",total_precentage)

