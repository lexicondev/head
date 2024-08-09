import random
a = []
b = []
c = []

n = random.randint(1,22)
l = random.randint(1,22)


for i in range(n):
    m = random.randint(1,22)
    a.append(m)
for i in range(l):
    m = random.randint(1,22)
    b.append(m)
for i in range(len(a)):
    for j in range(len(b)):
        if a[i] == b[j]:
                c.append(a[i])
c = list(set(c))


print(a)
print(b)
print(c)