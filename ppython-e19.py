import requests
from bs4 import BeautifulSoup

url = "https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture"
r = requests.get(url)
r_html = r.text
soup = BeautifulSoup(r_html,"html.parser")
results = soup.find('div', class_='body__inner-container')
art = results.find_all('p')
for i in art:

    print(i.text)