import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = 'https://www.imdb.com/title/tt6084202/'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/120.0'})
html = urllib.request.urlopen(req).read()

soup = BeautifulSoup(html, 'html.parser')

print(soup.prettify())