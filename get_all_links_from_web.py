import requests
from bs4 import BeautifulSoup

url='https://stackoverflow.com/'
reqs=requests.get(url)
soup=BeautifulSoup(reqs.text,'html.parser')

for link in soup.find_all('a'):
    print(link.get('href'))
