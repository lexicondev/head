import random
o = random.randint(3,22)
p = random.randint(3,22)
a = []
b = []
c = []
for i in range(1,o):
    n = random.randint(1,22)
    a.append(n)
for i in range(1,p):
    m = random.randint(1,22)
    b.append(m)



for x in a:
    for y in b:
        c.append(x) if x == y else False
            
print(a)
print(b)
print(c)            