#Digital Counter                https://codeforces.com/contest/495/problem/A
possibilites = {0:[0,8],
                1:[0,1,3,4,7,8,9],
                2:[2,8],
                3:[3,8,9],
                4:[4,8,9],
                5:[5,6,8,9],
                6:[6,8],
                7:[0,3,7,8,9],
                8:[8],
                9:[9,8]}
def spacer(x):
    spr = ""
    for i in x:
        spr+= i +' '
    spr = spr.split()
    for i in range(len(spr)):
        spr[i] = int(spr[i])
    return spr
def checker(x):
    a = x[0]
    b = x[1]
    res = []
    for i in possibilites[a]:
        for j in possibilites[b]:
            res.append(str(i)+str(j))
    return len(res)
n = input("")
print(checker(spacer(n)))
