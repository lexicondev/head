from bs4 import BeautifulSoup
import requests

def lis(prompt, prompt2):
    url = input(prompt)
    r = requests.get(url)
    r_html = r.text
    soup = BeautifulSoup(r_html,"html.parser")
    f = open(input(prompt2)+".txt","a")
    f.write(soup.text)
    f.close()
def red(phil,lip):
    with open(phil,"r") as file:
        line = file.readline()
        while line:
            lip.append(line.strip())
            line = file.readline()

    
def dup(l1,l2):
    prime = input(l1) + ".txt"
    happy = input(l2) + ".txt"
    p =[]
    h = []
    dp = []
    red(prime,p)
    red(happy, h)
    for i in p:
        for j in h:
            if i == j:
                dp.append(i)
    print(dp)

    
dup("Enter first text name: ", "Enter second text name: ")