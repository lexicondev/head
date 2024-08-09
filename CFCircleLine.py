#Circle Line        https://codeforces.com/contest/278/problem/A
 
n = input("")
d = input("\n")
q = input("\n")
bro = q.split()
for i in range(len(bro)):
    bro[i] = int(bro[i])
bro.sort()
org = d.split()
 
def decider(x, y):
    fv = []
    r = 0
    z = 0
    for i in range(x-1, y-1):
        r+=int(org[i])
    for i in range(x-2, ((y-1)-len(org))-1, -1):
        z+=int(org[i])
            
    fv.append(r)
    fv.append(z)
    if fv[0] <= fv[1]:
        print(fv[0])
    else:
        print(fv[1])
decider(bro[0], bro[1])