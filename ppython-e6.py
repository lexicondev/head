a = list(input("Enter word").lower())
c = list(reversed(a))
if a == c:
    print("This is a palindrome")
    print(a)
    print(c)
else:
    print("This isn't a palindrome")
    print(a)
    print(c)