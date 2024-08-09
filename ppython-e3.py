a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
def num(prompt):
    while True:
        global c
        c = input(prompt)
        if c.isdigit():
            return c
        else:
            print("Enter a valid fucker")
           
num("Enter a number")
for x in a:
    if x < int(c): b.append(x)
print(b) 
