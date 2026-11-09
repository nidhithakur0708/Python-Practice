# Write a program to filter a list of numbers which are divisible by 5.

l=[34,565,56,34,67,45,67,32,35]

def divisible_by_five(n):
    if(n%5==0):
        return True
    return False

f=list(filter(divisible_by_five,l))
print(f)