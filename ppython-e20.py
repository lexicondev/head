def num(prompt):
    while True:
            x = input(prompt)
            if x.isdigit():
                return x
            else:
                print("Not a number buddy")

def binsear(qual, item):
    i = list(sorted(num(qual)))
    j = int(num(item))
    bi = 0
    ei = len(i) - 1
    while bi <= ei:
        mp = bi + (ei - bi) // 2
        mp_val = int(i[mp])
        if j == mp_val:
            print("The number",j,"indeed exists in the list")
            return mp
        elif j < mp_val:
            ei = mp - 1
        else:
            ei = mp + 1
    else:
        print("Number doesn't exist in list")

binsear("Enter the numbers buddyyyyy: ","Enter the number to look for budddyyyyyyy: ")