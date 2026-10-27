#WAP to find the sum of first n natural numbers

i=0
sum=0
n=int(input('Enter the number n to find natural sum'))
while(i<n+1):
    sum+=i
    i+=1
print(sum)