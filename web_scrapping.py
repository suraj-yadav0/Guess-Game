from bs4 import BeautifulSoup
import requests


def web_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    for title in soup.find_all('h2', {'class': "story-heading"}):
        t = title.string
        if t is not None:
            print(t)

web_page('http://www.nytimes.com')