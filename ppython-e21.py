from bs4 import BeautifulSoup
import requests

u = input("Choose the file's name: ")
name = u+".txt"
url = "https://www.nytimes.com"
r = requests.get(url)
r_html = r.text
soup = BeautifulSoup(r_html,'html.parser')
for link in soup.findAll('h2'):
    f = open(name,"a")
    f.write(link.text)
    f.write("\n")
    f.close()
