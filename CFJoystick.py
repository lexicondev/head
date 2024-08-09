#Determine the maximum number of minutes.            https://codeforces.com/contest/651/problem/A

import random

def charger(c1,c2,coun):
    if c1 < c2:
        active = c1
        inactive = c2
    elif c1 > c2:
        active = c2
        inactive = c1
    else:
        active = c1
        inactive = c2
    play = True
    while play:
        if active == 1 and inactive == 1:
            break
        else:
            coun +=1
            active += 1
            inactive -= 2
        if active <= 0 or inactive <= 0:
            play = False
            break
        else:
            charger(active, inactive, coun)
            return coun
    print(coun)
    

def game(prompt):
    org = input(prompt).split()
    count = 0
    joy1 = int(org[0])
    joy2 = int(org[1])
    charger(joy1,joy2,count)
game(" ")
    