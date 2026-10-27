#WAP to find wheter a given number is prime or not
#if 1 divides and that number divides 


n=int(input("Enter a number to check if its prime"))
for i in range(2,n):
    if(n%i)==0:
        print("Number is not prime")
        break
else:
    print("Number is prime")