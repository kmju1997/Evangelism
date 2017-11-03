import os
import json
from bs4 import BeautifulSoup as BS
import requests
import re

postreqdata = json.loads(open(os.environ['req']).read())
response = open(os.environ['res'], 'w')
text = requests.get(postreqdata['url'])
soup =  BS(text.content, 'html.parser')

anchor = soup.find_all('a')

link_list = []

for link in anchor:
    if(re.match('http:[\S]+',link.get('href'))):
        link_list.append(link.get('href'))

response.write(str(link_list))

response.close()
