# Web scraper

This project aims to create a simple web scraper for getting information about games discounts using libraries such as `Beautifulsoup`, `requests` and `pandas` to save the information as **CSV**.

## How to run it

### Run the pip command to install the necessary libraries

```
pip install requests pandas beautifulsoup4
```

### Change the HTML tag from the `find_all` function and the class that corresponds do the tag as well as the other HTML tags for the `find` function depending on the website you're scraping

```Python
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
```

### If the website you're scraping from has more than one page of content that you want, you can use the loop function
