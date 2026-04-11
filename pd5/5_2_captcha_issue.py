import urllib.request, urllib.parse, urllib.error
import requests
import regex as rx
from bs4 import BeautifulSoup

url = 'https://www.imdb.com/title/tt6084202/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Connection': 'keep-alive'
}
#req = urllib.request.Request(url, headers=headers)
#html = urllib.request.urlopen(req).read()
resp = requests.get(url, headers=headers, timeout=10)
resp.raise_for_status()
html = resp.text

if 'challenge-container' in html or 'captcha' in html.lower():
    print("Bot protection / captcha detected")
    print(html[:500])

print(rx.findall('div.*', html))
print('before soup')
soup = BeautifulSoup(html, 'html.parser')

print('after soup')
spans = soup.find_all('span')

print(f'span count is: {len(spans)}')

for span in spans:
    print('test')
    print(span.string)