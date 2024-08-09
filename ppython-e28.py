def num(prompt):
    while True:
        x = input(prompt)
        if x.isdigit():
            return x
        else:
            print("Ain't a number bro")

def maks():
    a = int(num("Input first number: "))
    b = int(num("Input second number: "))
    c = int(num("Input third number: "))
    q = [a,b,c]
    q = sorted(q)
    print(q[2])
maks()