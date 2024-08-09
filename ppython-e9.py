import random

n = random.randint(0,10000)
def num(prompt):
        while True:
            global i
            i = input(prompt)
            if i.isdigit():
                i = int(i)
                return i
            elif i.lower() == "exit":
                print("See ya later")
                exit()
            else:
                print("That ain't a number buddy")

def guess(j):
     a = 0
     while j != n:
          num(j)
          k = int(i)
          a += 1
          if k < n:
               print("More")
          elif k > n:
               print("Less")
          else:
               print("You're correct the number was ", n, " and you got there in ", a, " tries")   
               exit()  

guess("Enter your guess")
