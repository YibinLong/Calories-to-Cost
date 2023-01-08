import requests
from bs4 import BeautifulSoup

url = "https://www.mcdonalds.com/ca/en-ca/full-menu/beef.html"

r = requests.get(url)

soup = BeautifulSoup(r.content, 'html.parser')
burger_urls = soup.select('.cmp-category__item')

print(burger_urls[0].select_one('a')['href'])

burger_arr = []
for burger in burger_urls:
    burger_arr.append(
        'https://www.mcdonalds.com' + burger.select_one('a')['href']
    )

print(burger_arr)

