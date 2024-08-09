def rev(prompt):
    x = input(prompt)
    a = list(x.split())
    b = (a[::-1])
    print(x)
    print(str(a))
    print(' '.join(b))

rev("Enter the reversable to beable: ")