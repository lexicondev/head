import random

def picker(lis):
    lip = []
    with open(lis,"r") as file:
        line = file.readline()
        while line:
            lip.append(line.strip())
            line = file.readline()
    n = random.randint(0,len(lip))
    print(lip[n])
picker("sowpods.txt")