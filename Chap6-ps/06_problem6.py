'''
WAP to calculate the grade of students:

90-100->A
80-90->B
70-80->C
60-70->D
50-60->E
<50->F
'''

marks=int(input("Enter your marks"))

if(marks<=100 and marks >=90):
    print("Grade A")
elif(marks >=80):
    print("Grade B")
elif(marks >=70):
    print("Grade C")
elif(marks>=60):
    print("Grade D")
elif(marks>=50):
    print("Grade E")
else:
    print("Grade F")