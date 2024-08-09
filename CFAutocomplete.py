#Autocomplete       https://codeforces.com/contest/53/problem/A

def coll(x):
    spr = ""
    for i in x:
        spr+=i
    return spr
def handler(x,phrase):
    org = []
    res = []
    bank = [i for i in range(x)]
    for i in range(x):
        bank[i] = input("")
    while len(bank) != 0:
        org.extend(bank[0])
        if org[0] == phrase[0]:
            if coll(phrase[0:len(phrase)]) == coll(org[0:len(phrase)]):
                res.append(coll(org))
        bank.pop(0)
        org = []
    res.sort()
    if len(res) > 0:
        print(res[0])
    else:
        print(coll(phrase))
word = list(input(""))
n = input("")
handler(int(n), word)