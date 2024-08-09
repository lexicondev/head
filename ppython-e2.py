def eoo(prompt, prompt2):
    while True:
        x = input(prompt)
        y = input(prompt2)
        if x.isdigit() and y.isdigit():
            x = int(x)
            y = int(y)  
            if x % 4 == 0 and x % y == 0:
                print("This even dude is divisible by four and divides evenly onto ",y)
                return False
            elif x % 4 != 0 and x % y == 0:
                print("Even on",y," but ain't divisible by four")
                return False
            else:
                print("This boy is odd")
                return False
        else:
            print("Try again buddy, fix the wrong one")
    
eoo("enter your number to check: ", "enter the number to divide upon: ")