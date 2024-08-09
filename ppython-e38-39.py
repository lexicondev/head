from datetime import date

def checkname(prompt):
    while True:
        global name 
        name = input(prompt)
        if name.isalpha():
            print(f"Alright then {name}")
            return name
        else:
            print("Nooo brooo")

def checkage(prompt):
    while True:
        global age
        age = input(prompt)
        if age.isdigit():
            print(f"Alright then {name}, you're {age} years old")
            return age
        else:
            print(f"How do you have letters in your age {name}??")
        
def pers(name, age, prompt):
    today = date.today()
    year = today.year
    age2h = 100 - int(age)
    year2h = age2h + year
    num = input(prompt)
    num = int(num)
    while True:
        if age2h <= 0:
            print("Happy birthday champ you're already a hundreder!!!")
            return 0
        else:
            for i in range(num):
                print(f"Alright then {name} you should be turning 100 in {age2h} years, on the year {year2h}")
            break
checkname("Name boy")
checkage("Age Boy")
pers(name, age, "Pick a lucky number")