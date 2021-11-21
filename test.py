import requests
url = 'https://www.allsides.com/media-bias/media-bias-ratings'
r = requests.get(url)
print(r.content[:100])