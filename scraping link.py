import requests
import re
from bs4 import BeautifulSoup as BS

url = 'http://google.com'

data =  requests.get(url)

soup  = BS(data.content, "html5lib")

link_list =[]

for link in soup.find_all('a'):
    if (re.match('(http):[\S]+',link.get('href'))):
        link_list.append(link.get('href'))

print(link_list)

