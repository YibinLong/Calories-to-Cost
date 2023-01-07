import requests
from bs4 import BeautifulSoup

url = 'https://www.allsides.com/media-bias/media-bias-ratings'
r = requests.get(url)
#print(r.content[:100])

soup = BeautifulSoup(r.content, 'html.parser')
rows = soup.select('tbody tr')

#select the first row
row = rows[0]
name = row.select_one('.source-title').text.strip()
print(name)

#select the news source
allsides_page = row.select_one('.source-title a')['href']
allsides_page = 'https://www.allsides.com' + allsides_page
print(allsides_page)

#grab the bias from the site
bias = row.select_one('.views-field-field-bias-image a')['href']
bias = bias.split('/')[-1]
print(bias)
