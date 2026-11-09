# class Number:
#     def __init__(self,n):
#         self.n=n
#     def __add__(self,num):
#         return self.n+num.n

# n=Number(1)
# m=Number(2)
# print(n+m)  #This is translated to 
# # n.__add__(m)
# #self.n+num.n(num is havin entire obj and from there we need n)


class Number:
    def __init__(self,n):
        self.n=n
    def __sub__(self,num):
        return self.n-num.n

x=Number(10)
y=Number(5)
print(x-y) #Translated to x.__sub__(y)