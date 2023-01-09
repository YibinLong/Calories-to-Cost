import requests
from bs4 import BeautifulSoup
import re 

url = "https://mcdonaldsprices.com/mcdonalds-canada-menu/"
r = requests.get(url)

soup = BeautifulSoup(r.content, 'html.parser')
rows = soup.select('tbody tr')

dct = dict()
for row in rows:
    try:
        name = row.select('td')[0].text.strip()
        name = re.sub("[\(\[].*?[\)\]]", "", name).strip()
        price = row.select('td')[1].text.strip()

        dct[name] = price
    except IndexError:
        continue

def get_price_dict():
    return dct