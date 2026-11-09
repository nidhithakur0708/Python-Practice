# Write a program to find the maximum of the numbers in a list using the reduce function
from functools import reduce
l=[23,45,67,78,45,78,38,99]


def greater(a,b):
    if(a>b):
        return a
    else:
        return b

print(reduce(greater,l))