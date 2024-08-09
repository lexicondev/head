import random

def num(prompt):
    while True:
        i = input(prompt)
        if i.isdigit():
            return i
        else:
            print("Not a number buddy")

def gen():
            n = random.randint(1,3)
            ur = random.randint(0,len(u)-1)
            ar = random.randint(0,len(a)-1)
            sr = random.randint(0,len(s)-1)
            if n == 1:            
                p.append(a[ar])
            elif n == 2:
                p.append(u[ur])
            else:
                p.append(s[sr])


a = list("abcdefghijklmnopqrstuvwxyz")

u = list(''.join(a).upper())

s = list("`!@#$%^&*()_+.,?|:")

q = random.randint(0,1000)
p = [] 
def pg(prompt):
    print("Choose how strong you want your password to be:-\n1-Weak\n2-Mid(Based)\n3-Strong")
    i = int(num(prompt))
    if i == 1:
        while len(p) != 4:
            gen()
    elif i == 2:
        while len(p) != 8:
            gen()
    elif i == 3:
        while len(p) != 16:
            gen()

    else:
        print("       -----------\n       |  o   o  |\n       |    L    |\n>------|   ___   |------<\n       |         |\n       -----------")
        exit()

    print("Your password is: ", ''.join(p))
    w = input("Press Y if you wanna get another password bro:").lower()
    if w == "y":
         pg(":")
    else:
         print("See ya!")
         exit()

pg(":")
                    

            
