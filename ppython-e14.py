def num(prompt):
    while True:
        x = input(prompt)
        if x.isdigit():
            return x
        else:
            print("Not a number bro, give it another try: ")

def dups(prompt):
    a = list(set(num(prompt)))
    print(a)

def dupl(prompt):
    a = list(num(prompt))
    c = []
    for j in a:
        if j not in c:
            c.append(j)

    print(c)        

dupl("This'll error")