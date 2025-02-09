import requests
from bs4 import BeautifulSoup


url = 'http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture'


soup = BeautifulSoup(requests.get(url).text, 'html.parser')


print(soup.find('article').text)