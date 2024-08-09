#WELCOME TO FUCKDLE
import random
hanger = {'o','|','/',"'\'",}
lip = []
with open("sowpods.txt","r") as file:
    line = file.readline()
    while line:
        lip.append(line.strip())
        line = file.readline()

def rec(li):
    spr =""
    for i in li:
        spr+=i+" "
    print(spr.upper())
def hangman(wordle):
    n = random.randint(0,len(lip))
    words = str(wordle[n]).lower()
    print("Welcome to Hangman(poor man's wordle)!")
    guess = input("Enter the letter to guess: ")
    wordlist = []
    wordlist.extend(words)
    blank = "_ "*len(wordlist)
    blanklist = list(blank.split())
    coun = 0
    collective = []
    while True:
        for i in range(len(wordlist)):
            if guess == wordlist[i]:
                blanklist[i] = guess
                for q in range(i,len(wordlist)):
                    while q:
                        if guess == wordlist[q]:
                            blanklist[q] = guess
                            break
                        else:
                            break
                if blanklist == wordlist:
                    rec(blanklist)
                    print("You've guessed the whole word, it is indeed",words.upper(),"and you got there in",coun,"times")
                    des = input("Wanna go again? Y: ").lower()
                    if des == "y":
                        hangman(wordle)
                    elif des == "":
                        hangman(wordle)
                    else:
                        print("Bye then brobers")
                        exit()
                    return False
                elif guess == wordlist[i]:
                    print("Correct")
                    rec(blanklist)
                    break
                else:
                    continue
            else:
                i+=1
        else:
            rec(blanklist)
            if guess != wordlist[i-1]:
                print("Incorrect")
        coun+=1
        if coun < len(words)*2:
            collective.append(guess.upper())
            print(coun,"Guesses",(len(words)*2)-coun,"Remaining\nLetters used",set(collective))
            guess = input("New guess: ")
        else:
            collective.append(guess.upper())
            print("You've lost the word was",words.upper(),"\nLetters used",set(collective))
            des = input("Wanna go again? Y: ").lower()
            if des == "y":
                hangman(wordle)
            elif des == "":
                hangman(wordle)
            else:
                print("Bye then broses")
                exit()
        
hangman(lip)
            
