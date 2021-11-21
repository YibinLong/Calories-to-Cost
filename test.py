import requests
from bs4 import BeautifulSoup


url = 'https://www.allsides.com/media-bias/media-bias-ratings'
r = requests.get(url)
#print(r.content[:100])

soup = BeautifulSoup(r.content, 'html.parser')
rows = soup.select('tbody tr')

row = rows[0]
name = row.select_one('.source-title').text.strip()

print(name)