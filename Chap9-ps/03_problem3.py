#WAP to generate tables from 2 to 20 and in different files


def generateTable(n):
    table=''
    for i in range(1,11):
        table += f"{n} x {i} = {n*i}\n"
    with open(f"Chap9-ps/tables/table_{n}.txt",'w') as f:
        f.write(table)


for i in range(2,21):
    generateTable(i)