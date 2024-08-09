x = []
def num(prompt):
    while True:
        global c
        c = input(prompt)
        if c.isdigit():
            c = int(c)
            return c
        else:
            print("Enter a valid fucker")

num("Enter the num")
for q in range(1,c+1):
    if c%q == 0:
        x.append(q)
        
print(x)
