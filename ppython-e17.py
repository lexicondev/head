from bs4 import BeautifulSoup
import requests
import attrs
url = "https://www.nytimes.com"
r = requests.get(url)
r_html = r.text
soup = BeautifulSoup(r_html,'html.parser')
for link in soup.findAll('h2'):
    print(link.text)
