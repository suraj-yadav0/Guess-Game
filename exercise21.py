from bs4 import BeautifulSoup

import requests

url = 'https://en.wikipedia.org/wiki/Wiki'


soup = BeautifulSoup(requests.get(url).text, 'html.parser')


# print(soup.find('div'),{'id':'mw-content-text'})

text = ' '.join(p.get_text().strip() for p in soup.find_all('p') if p.get_text().strip())




with open('exercise21.txt','w',encoding='utf-8') as open_file:
    open_file.write(text)
