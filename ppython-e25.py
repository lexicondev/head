#I hate binary search algo..., Enemy felled
import random

n = 100
n = list(range(n+1))

def num(prompt):
    while True:
        x = input(prompt)
        if x.isdigit():
            return x 
        else:
            print("Not acceptable")
def bin():
    beg = 0
    en = len(n)-1
    print("My initial guess is:")
    while beg<=en:
        mp = beg + (en-beg)//2
        mp_value=int(n[mp])
        print(mp_value)
        print("Is that your number?Y/N")
        d = input("Answer: ").lower()
        if d == "y":
            print("Your number is:",mp_value)
            return mp_value
        else:
            print("Higher or lower than your number?:-\n1-Higher\n2-Lower")
            an = num("Answer: ")
            an = int(an)
            if an == 1:
                en = mp - 1
            elif an == 2:
                beg = mp + 1
            else:
                print("Your number isn't here")
                exit()
            

bin()
