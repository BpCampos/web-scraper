import pandas as pd
import requests
from bs4 import BeautifulSoup
import time

contador = 0


def scrape_page(url):
    response = requests.get(url)

    if contador == 0:
        print(f'Status: {response.status_code}')
        contador += 1

    if response.status_code == 200:
        html_content = response.content
    else:
        print(f'Failed to retrieve the content: {response.status_code}')

    soup = BeautifulSoup(html_content, 'html.parser')

    data = []

    for item in soup.find_all('a', class_='product-card--wrapper'):
        title = item.find('h3').text
        discount = item.find(class_='product-discount').text.strip()
        price_integer = item.find(class_='integer').contents[0]
        price_decimal = item.find(class_='decimal').contents[0]
        final_price = price_integer + price_decimal
        final_price = final_price.replace(',', '.')
        data.append({
            'title': title,
            'discount': discount,
            'price': float(final_price)
        })

    return data


def scrape_pages():
    all_data = []

    for page_number in range(1, 25):
        if page_number == 1:
            page_data = scrape_page(
                'https://www.nuuvem.com/br-pt/catalog/drm/steam/platforms/pc/price/promo/sort/bestselling/sort-mode/desc')
            all_data.extend(page_data)
        else:
            print(f"Scraping page: {page_number}")
            page_data = scrape_page(
                f'https://www.nuuvem.com/br-pt/catalog/drm/steam/platforms/pc/price/promo/sort/bestselling/sort-mode/desc/page/{page_number}')
            all_data.extend(page_data)
        time.sleep(2)

    print('Scrape successfully completed')
    return all_data


df = pd.DataFrame(scrape_pages())
df = df.sort_values(by=['discount'], ascending=False)
df.to_csv('~/Desktop/output.csv', sep=',', index=False)
