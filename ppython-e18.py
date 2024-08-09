import random

def num(prompt):
    while True:
        x = input(prompt)
        if x.isdigit():
            x = list(x)
            if len(x) != 4:
                print("Enter a 4 digit number bro")
            else:
                return x
        else:
            print("Not a number buddy")
r = list(str(random.randint(1000,9999)))
def cab(prompt):
    x = num(prompt)
    c = 0
    b = 0
    
    for i in range(0,4):
        if x[i] == r[i]:
            b+=1
        elif x[i] in r and x[i] != r[i]:
            c+=1
    else:
        if b < 4:
            print(c,"Cow/s",b,"Bull/s")
            cab(": ")
        else:
            for i in range(50):
                print("Good job you did it, good job you did it, good job you did it, good job you did it")
            print("\n\nI printed it 50 times to show that I 50 appreciate you")
            
    
if __name__ == "__cab__":
    cab("Enter your numero: ")
cab("Enter your numero: ")
            