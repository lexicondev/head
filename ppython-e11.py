def num(prompt):
    while True:
        x = input(prompt)
        if x.isdigit():
            return x
        else:
            print("Aint a number bud")

def prim(prompt):
    i = int(num(prompt))
    for q in range(2, i):
        if i % q == 0:
            print("Not a prime\n")
            des = input("If you wanna try again type Y: ").lower()
            if des == "y":
                prim(prompt)
            else:
                exit()
    print("prime\n")
    des = input("If you wanna play again type Y: ").lower()
    if des == "y":
        prim(prompt)
    else:
        print("Bye then")
        exit()

prim("Enter your nummmm budddyyyyyy")                