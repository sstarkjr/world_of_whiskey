import re
import pandas as pd
import requests
from bs4 import BeautifulSoup
import time

# https://www.youtube.com/watch?v=nCuPv3tf2Hg&ab_channel=JohnWatsonRooney

baseurl = "https://www.thewhiskyexchange.com"

headers = {
    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) \
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
}

current_date = time.strftime("%m/%d/%Y")

# Get URLs from base site
r = requests.get(f'https://www.thewhiskyexchange.com/brands/worldwhisky')
soup = BeautifulSoup(r.content, 'lxml')
producers_item = soup.find_all('li', class_="producers-item")
source_dict = {}
print('Aggregating Whiskeys from the following countries...')
print(list(item.text.strip() for item in producers_item))  # list of whiskey countries

for item in producers_item:
    country = item.text.strip()  # country
    for link in item.find_all('a', href=True):
        source = baseurl+link['href']
        print(country)
        print(source)
    source_dict[country] = source
# print(source_dict)
# print(len(source_dict))
# print(source_dict.keys())
# print(source_dict.values())

brand_urls = []
for v in source_dict.values():
    # print(v)
    r = requests.get(v)
    soup = BeautifulSoup(r.content, 'lxml')
    az_item = soup.find_all('li', class_='az-item')
    for link in az_item:
        for link_2 in link.find_all('a', href=True):
            # print(link_2.text) # brand of whiskey
            # list_of_whiskey_urls.append(baseurl+link_2['href'])
            # print(v, link_2.text.strip(), baseurl+link_2['href'])
            brand = link_2.text.strip()
            specific_link = baseurl+link_2['href']
            brand_urls.append(baseurl + link_2['href'])
print(f"{len(brand_urls)} brands of whiskey")

bottle_urls = []
for brand in brand_urls:
    r = requests.get(brand)
    soup = BeautifulSoup(r.content, 'lxml')
    bottles = soup.find_all('li', class_="product-grid__item")
    for bottle in bottles:
        bottle_list = bottle.find_all('a', href=True)
        for b2 in bottle_list:
            # print(baseurl+b2['href']) # url to get to individual bottle
            bottle_urls.append(baseurl+b2['href'])
print(f"{len(bottle_urls)} number of bottles")
whiskey_list = []
for u in bottle_urls:
    r = requests.get(u, headers=headers)
    soup = BeautifulSoup(r.content, 'lxml')
    name = soup.find('h1', class_="product-main__name").text.strip()
    price = soup.find('p', class_="product-action__price").text.strip()
    description = soup.find('div', class_="product-main__description").text.strip()
    size = soup.find('p', class_="product-main__data").text.strip().split("/")[0].strip()
    abv = soup.find('p', class_="product-main__data").text.strip().split("/")[1].strip()
    productlink = u

    try:
        if soup.find(class_='flavour-profile__group flavour-profile__group--character') == str("None"):
            list_of_flavors = "None"
        else:
            list_of_flavors = soup.find(class_='flavour-profile__group flavour-profile__group--character').text \
                .split("\n")
            while "Character" in list_of_flavors:
                list_of_flavors.remove("Character")
                list_of_flavors = list(filter(None, list_of_flavors))
    except:
        list_of_flavors = "None"

    try:
        style_list = soup.find(class_='flavour-profile__group flavour-profile__group--style').text.split("\n")
        while "Style" in style_list:
            style_list.remove("Style")
            style_list = list(filter(None, style_list))

    except:
        style_list = "None"


    try:
        rating_str = soup.find('p', class_="review-overview__content").text.strip()
        avg_rating = re.findall(r"(\d\.*\d*)", rating_str)[0]

    except:
        avg_rating = "no rating"

    try:
        num_rating_str = soup.find('p', class_="review-overview__content").text.strip()
        num_rating = re.findall(r"(\d\.*\d*)", num_rating_str)[1]

    except:
        num_rating = "no rating"

    try:
        subtitle = soup.find('ul', class_="product-main__meta").text.strip()
    except:
        subtitle = "No subtitle"

    whisky = {
        'name': name,
        'price': price,
        'description': description,
        'size': size,
        'abv': abv,
        'list_of_flavors': list_of_flavors,
        'style_list': style_list,
        'avg_rating': avg_rating,
        'num_rating': num_rating,
        'subtitle': subtitle,
        'current_date': current_date,
        'product_link': productlink
    }
    whiskey_list.append(whisky)
    print("Saving ", whisky['name'])

df = pd.DataFrame(whiskey_list)
df.to_csv('whiskey_list.csv')
print(df.shape)
df.drop_duplicates(subset=['name', 'price', 'description', 'size', 'abv'], inplace=True)
print(df.shape)


# Go to world of whiskeys
# Grab the different countries of the world
# Click into each country and get the a-z list
# Click each label to get its list of bottles, if necessary
# If multiple, get each  of  those links, click them
# if single, get that link, and click it
# Go to that link and record all necessary bottle info

# https://www.thewhiskyexchange.com/brands/worldwhisky
# https://www.thewhiskyexchange.com/brands/worldwhisky/32/irish-whiskey IRISH WHISKEY
# https://www.thewhiskyexchange.com/brands/worldwhisky/33/american-whiskey AMERICAN WHISKEY
# https://www.thewhiskyexchange.com/brands/worldwhisky/35/japanese-whisky JAPANESE WHISKEY
# https://www.thewhiskyexchange.com/brands/worldwhisky/34/canadian-whisky CANADIAN WHISKEY
# https://www.thewhiskyexchange.com/brands/worldwhisky/305/rest-of-the-world-whisky REST OF WORLD

# TODO include mode to try a limited run
# Add more commenting
# Edd exception clause to git rid of too broad exception issues
# Add logic to output data to a specific location
