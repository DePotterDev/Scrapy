import pandas as pd
import requests
from bs4 import BeautifulSoup

baseurl =  'https://www.thewhiskyexchange.com/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36'
}
productlinks = []

for x in range(1,8):
    print(x)
    r = requests.get(f'https://www.thewhiskyexchange.com/c/32/irish-whiskey?pg={x}')
    soup = BeautifulSoup(r.content, 'lxml')
    productlist = soup.find_all('li', class_='product-grid__item')

    for item in productlist:
        for link in item.find_all('a', href=True):
            productlinks.append(baseurl +  link['href'])


whiskeylist = []

for link in productlinks:

    r = requests.get(link, headers=headers)
    soup = BeautifulSoup(r.content, 'lxml')

    name = soup.find('h1', class_='product-main__name').text.strip()
    try:
        rating = soup.find('span',class_='star-rating').text.strip()
        reviews = soup.find('span',class_='review-overview__count').text.strip()
    except:
        rating = 'no rating'
        reviews = '0'
    
    price = soup.find('p', class_='product-action__price').text.strip()
    whiskey = {
        'name': name,
        'rating': rating,
        'reviews': reviews,
        'price': price
    }

    whiskeylist.append(whiskey)
    print('Saving: ', whiskey['name'] )

df =pd.DataFrame(whiskeylist)
print(df.head(15))
