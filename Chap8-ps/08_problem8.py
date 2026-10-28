#WAP to print multiplication table of a given number

def multi_table(n):
    for i in range(1,11):
        print(f"{n}*{i}={n*i}")

multi_table(5)