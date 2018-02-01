# Demo showing basic interaction using the Beautiful Soup library
# Beautiful Soup docs: https://www.crummy.com/software/BeautifulSoup/bs4/doc/

import requests

# import the third party library Beautiful Soup
from bs4 import BeautifulSoup

# call the get method from requests in order to obtain a response from the url
response = requests.get('https://en.wikipedia.org/wiki/S100A14')

html = response.text

soup = BeautifulSoup(html, 'html.parser')

