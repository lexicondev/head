import random

n = random.randint(0,9)
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
          if k <= 9:
            a += 1
          else:
            a = a
          if k < n:
               print("More")
          elif k > n:
               print("Less")
          else:
               print(f"You're correct the number was {n} and you got there in {a} tries")   
               exit()  

guess("Enter your guess: ")
