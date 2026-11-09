#1.map-Map applies a function to all the items in an input_list.

l=[1,2,3,4,5]
square=lambda x:x*x
sqList=map(square,l)
print(list(sqList))

#Filter-Filter creates a list of items for which the function returns true
def even(n):
    if(n%2==0):
        return True
    return False

onlyEven=filter(even,l)
print(list(onlyEven))

#reduce
from functools import reduce
def sum(a,b):
    return a+b

print(reduce(sum,l))
#This will run like 1+2,3 and then 3+4=7 then 7+rest and soo on