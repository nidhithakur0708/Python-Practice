#WAP to accept marks of 6 students and display them in a sorted manner

scores=[]
s1=int(input("Enter marks:"))
scores.append(s1)
s2=int(input("Enter marks:"))
scores.append(s2)
s3=int(input("Enter marks:"))
scores.append(s3)
s4=int(input("Enter marks:"))
scores.append(s4)
s5=int(input("Enter marks:"))
scores.append(s5)
s6=int(input("Enter marks:"))
scores.append(s6)

scores.sort()
print(scores)