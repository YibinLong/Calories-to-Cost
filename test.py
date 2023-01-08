import requests
from bs4 import BeautifulSoup

# Source: https://www.learndatasci.com/tutorials/ultimate-guide-web-scraping-w-python-requests-and-beautifulsoup/

url = 'https://www.allsides.com/media-bias/ratings'
r = requests.get(url)
#print(r.content[:100])

soup = BeautifulSoup(r.content, 'html.parser')
rows = soup.select('tbody tr') # Select all <tr> inside <tbody>

#select the first row
row = rows[0]
name = row.select_one('.source-title').text.strip()
# Q: What is select_one, and how does it know that .source-title gives me what I want?
print(name) # Expect: ABC News (Online)


# select the news source
allsides_page = row.select_one('.source-title a')['href']
allsides_page = 'https://www.allsides.com' + allsides_page
print(allsides_page)
# print(row.select_one('.source-title a')['href'])

# grab the bias from the first row
bias = row.select_one('.views-field-field-bias-image a')['href']
bias = bias.split('/')[-1]
print(bias)

# get the community feedback ratio
agree = row.select_one(".agree").text
agree = int(agree)

disagree = row.select_one(".disagree").text
disagree = int(disagree)

agree_ratio = agree / disagree

# Q: How do f strings work?
print(f"Agree: {agree}, Disagree: {disagree}, Ratio {agree_ratio:.2f}")

print(row.select_one('.community-feedback-rating-page'))

# Replicate Ratio Logic:
def get_agreeance_text(ratio):
    if ratio > 3: return "absolutely agrees"
    elif 2 < ratio <= 3: return "strongly agrees"
    elif 1.5 < ratio <= 2: return "agrees"
    elif 1 < ratio <= 1.5: return "somewhat agrees"
    elif ratio == 1: return "neutral"
    elif 0.67 < ratio < 1: return "somewhat disagrees"
    elif 0.5 < ratio <= 0.67: return "disagrees"
    elif 0.33 < ratio <= 0.5: return "strongly disagrees"
    elif ratio <= 0.33: return "absolutely disagrees"
    else: return None
    
print(get_agreeance_text(agree_ratio))

# Now, get data for every row in the page (not just the 1st row)

data= []

for row in rows:
    d = dict()
    
    d['name'] = row.select_one('.source-title').text.strip()
    d['allsides_page'] = 'https://www.allsides.com' + row.select_one('.source-title a')['href']
    d['bias'] = row.select_one('.views-field-field-bias-image a')['href'].split('/')[-1]
    d['agree'] = int(row.select_one('.agree').text)
    d['disagree'] = int(row.select_one('.disagree').text)
    d['agree_ratio'] = d['agree'] / d['disagree']
    d['agreeance_text'] = get_agreeance_text(d['agree_ratio'])
    
    data.append(d)

print(data[4])