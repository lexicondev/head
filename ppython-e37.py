x = "  --- "
y = " |   |"
def gridder(desx,desy):
    dx = int(input(desx))
    dy = int(input(desy))
    for i in range(dx):
        print(x*dy)
        print(y*dy)
    print(x*dy)
gridder("Number of rows: " ,"Number of columns: ")