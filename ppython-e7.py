import random
b=[]
a = []
n = random.randint(1,15)
for j in range(n):
    q = random.randint(1,22)
    a.append(q)
for i in range(len(a)):
    b.append(a[i]) if a[i] % 2 == 0 else False

print(a)
print(list(set(b)))