#WAP to print multiplication table fora given number using while loop

n=int(input("Enter the number u want table for:"))
i=0
while(i<11):
    print(f"{n}X{i}={n*i}")
    i+=1