'''

    Web scraper to get word probability

'''

from attr import attrib
from requests import get
from bs4 import BeautifulSoup

def scrape():

    url = 'https://www.google.com/search?q=hello+test'

    req = get(url)

    soup = BeautifulSoup(req.content, 'html5lib')

    result = soup.find('div', attrs='{id="result-stats"}')

    print(result)

if __name__ == '__main__':
    scrape()