def num(n):
    while True:
        global x
        x = input(n)
        if x.isdigit():
            x = int(x)
            return x
        else:
            print("Try again buddy")    


def rpc(P1,P2):
    print("Welcome to RPC!\nPick your choice by number:\n1-Rock\n2-Paper\n3-Scissors")
    num(P1)
    print("Player One has chosen: ",x)
    P1 = x
    num(P2)
    print("Player Two has chosen: ",x)
    P2 = x
    if int(P1) > 3 or int(P2) > 3:
        print("That number ain't on the list boiiiiiiiiii, try again\n")
        rpc(P1,P2)
    else:
               
        while P1 == 1:
            if P2 == 1:
                print("It's a draw\nNew game it is!!!")
                rpc(P1,P2)
            elif P2 == 2:
                print("Congrats Player 2 for the W!")
                a = input("If you'd like to play again press Y: ").lower()
                if a == "y":
                    rpc(P1,P2)
                else:
                    print("Bye then!")
                    break
            elif P2 == 3:
                print("Congrats Player 1 for the W!")
                a = input("If you'd like to play again press Y: ").lower()
                if a == "y":
                    rpc(P1,P2)
                else:
                    print("Bye then!")
                    break
            else:
                return False
        
        while P1 == 2:
            if P2 == 2:
                print("It's a draw\nNew game it is!!!")
                rpc(P1,P2)
            elif P2 == 1:
                print("Congrats Player 1 for the W!")
                a = input("If you'd like to play again press Y: ").lower()
                if a == "y":
                    rpc(P1,P2)  
                else:
                    print("Bye then!")
                    break
            elif P2 == 3:
                print("Congrats Player 2 for the W!")
                a = input("If you'd like to play again press Y: ").lower()
                if a == "y":
                    rpc(P1,P2)  
                else:
                    print("Bye then!")
                    break
            else:
                return False
        while P1 == 3:
            if P2 == 1:
                print("It's a draw\nNew game it is!!!")
                rpc(P1,P2)
            elif P2 == 1:
                print("Congrats Player 2 for the W!")
                a = input("If you'd like to play again press Y: ").lower()
                if a == "y":
                    rpc(P1,P2)  
                else:
                    print("Bye then!")
                    break
            elif P2 == 2:
                print("Congrats Player 2 for the W!")
                a = input("If you'd like to play again press Y: ").lower()
                if a == "y":
                    rpc(P1,P2)  
                else:
                    print("Bye then!")
                    break    
            else:
                return False

          



rpc("Player 1: ","Player 2: ")