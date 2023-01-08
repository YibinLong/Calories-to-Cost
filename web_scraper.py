'''
def save_html(html, path):
    """
    Save html to path
    """
    with open(path, 'wb') as f:
        f.write(html)

save_html(r.content, 'google_com')

def open_html(path):
    """
    Open html file
    """
    with open(path, 'rb') as f:
        html = f.read()

html = open_html('google_com')
'''

import requests
from bs4 import BeautifulSoup
from selenium import webdriver

def get_burger_names():
    url = "https://www.mcdonalds.com/ca/en-ca/full-menu/beef.html"

    r = requests.get(url)

    soup = BeautifulSoup(r.content, 'html.parser')
    burger_names = soup.find_all("div", {"class":"cmp-category__item-name"})

    burger_arr = []
    for burger in burger_names:
        burger_arr.append(burger.text.strip())
    
    return burger_arr

def get_burger_urls():
    url = "https://www.mcdonalds.com/ca/en-ca/full-menu/beef.html"

    r = requests.get(url)

    soup = BeautifulSoup(r.content, 'html.parser')
    burger_urls = soup.select('.cmp-category__item')

    burger_arr = []
    for burger in burger_urls:
        burger_arr.append(
            'https://www.mcdonalds.com' + burger.select_one('a')['href']
        )

    return burger_arr

chrome_driver_path = 'C:/Users/Yibin/Downloads/chromedriver.exe'

driver = webdriver.Chrome(chrome_driver_path)

burger_urls = get_burger_urls()

for url in burger_urls:
    driver.get(url)
    html = driver.page_source

    soup = BeautifulSoup(html, 'html.parser')

    calorie_element = soup.select_one(".sr-only-pd").text.strip()

    burger_name = soup.select_one(".cmp-product-details-main__heading-title").text.strip()

    print(burger_name + ': ' + calorie_element)
