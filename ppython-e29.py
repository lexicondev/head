#Used Poe to resolve the issue in function pos, 1st time I resorted to Poe for ctrl c/v code, for now(21st March) I'll leave this code and come back when I'm better, I have been felled
P1 = "x"
P2 = "y"
dub = [0,1,2]
def flatten(xss):
    return [x for xs in xss for x in xs]
def num(prompt):    #Makes sure that the input is an int
    while True:
        x = input(prompt)
        if x.isdigit():
            return x
        else:
            print("Not a number")

def rec(li):      #Takes a list and makes it a str grid
    spr = ""
    for ele in li:
        tem = list(ele)
        for boy in tem:
            spr += boy+" "
        spr += "\n" 
    print(spr)
def pos(board, pus, p, disp):
    pus = int(pus)

    for i in range(len(board)):
        if pus in board[i]:
            j = board[i].index(pus)
            if disp[i][j] != "y" and disp[i][j] != "x":
                disp[i][j] = p
                print("Choose where to play", p + ": ")
                rec(disp)
                return
            else:
                print("Spot already taken!!")
                return

    print("Invalid input or spot out of range!!")
def gam(liss,toRec):     #Operates the game
    play = True
    while play:
        des = int(num("x: "))
        pos(liss,des,P1,toRec)
        desy = int(num("y: "))
        pos(liss,desy,P2,toRec)
    else:
        play = False

def drb(row, columns):     #Defines the grid's data
    rc = [0,0]
    ceiling = "--- "
    print("We're doing this as RxC")
    rows = input(row)
    col = input(columns)
    numboard = []
    listboard = []
    for i in range(int(rows)):
        rc[0] += 1
    for i in range(int(col)):
        rc[1] += 1
    col_count = rc[1]
    for i in range(int(col_count)):
        con = 0
        subist = []
        while rc[0] != 0:
            print(ceiling*col_count)
            j = 1
            dd = []
            board = []
            gg = []
            lislis = []
            spliced = []
            while j <= col_count:
                    q = j+(con*col_count)
                    q = str(q)
                    board.append((q))
                    a7 = str(board[j-1])
                    spr = ""
                    sp2 = ""
                    bor = "|"+a7+"| "
                    spr+=bor
                    dd.extend(spr)
                    j+=1
                    lislis.extend(a7)
            subist.append(lislis)
            gg.extend(subist)
            con +=1
            for ele in dd: #Takes the list with the values of the cells, and jams them into a single string
                sp2+=ele
            listboard.append(board)
            bbbb = [eval(i) for i in board]
            numboard.append(bbbb)
            lem = []
            lem2 = []
            i = 0
            while i < (len(board)):
                tem = [eval(q) for q in board[i]]
                lem.append(tem)
                i+=1
            
            spr += "\n" 
            print(sp2)
            rc[0] -= 1
    splicer = flatten(numboard)
    celsize = len(listboard[0])
    gam(numboard,listboard)
drb("Rows: ", "Columns: ")