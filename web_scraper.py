import requests
import price_web_scraper
import re
import matplotlib.pyplot as plt
import operator
from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver

# unused function
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
    # Add more urls to get different types of McD foods
    urls = [
            "https://www.mcdonalds.com/ca/en-ca/full-menu/beef.html",
            "https://www.mcdonalds.com/ca/en-ca/full-menu/chicken.html",
            "https://www.mcdonalds.com/ca/en-ca/full-menu/sandwiches-and-wraps.html",
            "https://www.mcdonalds.com/ca/en-ca/full-menu/breakfast.html",
            "https://www.mcdonalds.com/ca/en-ca/full-menu/snacks-and-sides.html"]

    burger_arr = []
    for url in urls:
        r = requests.get(url)

        soup = BeautifulSoup(r.content, 'html.parser')
        burger_urls = soup.select('.cmp-category__item')
        
        for burger in burger_urls:
            burger_arr.append(
                'https://www.mcdonalds.com' + burger.select_one('a')['href']
            )

    return burger_arr

chrome_driver_path = 'C:/Users/Yibin/Downloads/chromedriver.exe'

driver = webdriver.Chrome(chrome_driver_path)

burger_urls = get_burger_urls()

calorie_dct = dict()
for url in burger_urls:
    driver.get(url)
    html = driver.page_source

    soup = BeautifulSoup(html, 'html.parser')

    calorie_element = soup.select_one(".sr-only-pd").text.strip()

    burger_name = soup.select_one(".cmp-product-details-main__heading-title").text.strip()

    calorie_dct[burger_name] = calorie_element

    # Sleep to give the page more time to load
    sleep(.2)

print(calorie_dct)

price_dct = price_web_scraper.get_price_dict()
print(price_dct)

calories_per_dollar = dict()
for key, value in calorie_dct.items():
    try:
        print(key + ": " + price_dct[key] + ' ' + value)

        calorie = int(re.search("\d+", value)[0])
        price = float(re.search("\d+\.\d+", price_dct[key])[0])

        calories_per_dollar[key] = calorie / price
    except KeyError:
        continue

# print(calories_per_dollar)

sorted_calories_per_dollar = dict(sorted(calories_per_dollar.items(), key=operator.itemgetter(1),reverse=True))

# Final result: Sorted dictionary of calories per dollar
print(sorted_calories_per_dollar)

# Plot the foods by calories per dollar
plt.bar(range(len(sorted_calories_per_dollar)), sorted_calories_per_dollar.values(), align='center')
plt.xticks(range(len(sorted_calories_per_dollar)), list(sorted_calories_per_dollar.keys()))

plt.show()

driver.quit()
