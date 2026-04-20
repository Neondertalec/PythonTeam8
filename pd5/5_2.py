import requests
import re
from bs4 import BeautifulSoup

url = 'https://www.filmas.lv/movie/3478/'

resp = requests.get(url, timeout=10)
resp.raise_for_status()
html = resp.text

soup = BeautifulSoup(html, 'html.parser')
print("Title: " + soup.select_one('div.content .movie-content .atsauksmes_medijos').parent.find('h2').getText().strip())

for child in soup.select_one('div.content .movie-data').children:
    title = child.next_element.getText().strip("\n\t: ")
    if title in ['Gads', 'Ilgums', 'Režisors']:
        print(f"{title}: {child.next_element.next_sibling.getText().strip("\n\t: ")}")
    elif title in ['Lomās', 'Lomās/Epizodēs']:
        print(f"{title}: {len(child.next_element.next_sibling.find_all())}")