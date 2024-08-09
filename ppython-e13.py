def num(prompt):
    while True:
        x = input(prompt)
        if x.isdigit():
            return x
        else:
            print("Not a number buddy")

def fib(prompt, prompt2):
    i = int(num(prompt))
    j = int(num(prompt2))
    c = []
    b = 0
    for q in range(i):
            d = b
            b = j
            j+=d
            c.append(j)
            j = int(c[q])
    print(c)

fib("Enter your operation number", "And the starting nuber")
