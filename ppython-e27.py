#Tanky enemy felled
P1 = "x"
P2 = "y"
board = [["1","2","3"],["4","5","6"],["7","8","9"]]
play = True
dub = [0,1,2]
def num(prom):
    while True:
        x = input(prom)
        if x.isdigit():
            return x
        else:
            print("Not Valid brooooo")
def rec(li):
    spr = ""
    for ele in li:
        tem = list(ele)
        for boy in tem:
            spr += boy+" "
        spr += "\n" 
    print(spr)
def pos(pus,p):
    while pus <= 9:
        if pus <= 3:
            if board[0][pus-1] == "y" or board[0][pus-1] == "x":
                print("That spot is already taken")
                break
            else:
                board[0][(pus-1)] = p
                print("Choose where to play",p)
                rec(board)
                break
        elif pus >3 and pus <= 6:
            if board[1][pus-4] == "y" or board[1][pus-4] == "x":
                print("That spot is already taken")
                break
            else:
                board[1][dub[(pus-4)]] = p
                print("Choose where to play",p)
                rec(board)
                break
        elif pus > 6 and pus <=9:
            if board[2][pus-7] == "y" or board[2][pus-7] == "x":
                print("That spot is already taken")
                break
            else:
                board[2][dub[pus-7]] = p
                print("Choose where to play",p)
                rec(board)
                break
while play:
    rec(board)
    des = int(num(": "))
    pos(des,P1)
    desy = int(num(": "))
    pos(desy,P2)
else:
    play = False