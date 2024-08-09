#Dodgy enemy felled
def num(prompt):
    while True:
        x = input(prompt)
        if x.isdigit():
            return x
        else:
            print("Not a number")
def drb(row, columns):
    rc = [0,0]
    cei = "--- "
    bor = "| | "
    print("We're doing this as RxC")
    r = num("Enter the number of rows: ")
    c = num("Enter the number of columns: ")
    for i in range(int(r)):
        rc[0] += 1
    for i in range(int(c)):
        rc[1] += 1
    rb = rc[0]
    cb = rc[1]
    for i in range(int(cb)):
        while rc[0] != 0:
            print(cei*cb)
            print(bor*cb)
            rc[0] -= 1
    print(cei*cb)
drb("Rows: ", "Columns: ")