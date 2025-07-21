# scraper.py
import requests
from bs4 import BeautifulSoup

def scrape_books(query):
    base_url = "https://books.toscrape.com/catalogue/page-{}.html"
    books = []

    for page in range(1, 6):
        url = base_url.format(page)
        res = requests.get(url)
        soup = BeautifulSoup(res.text, "html.parser")
        articles = soup.find_all("article", class_="product_pod")

        for article in articles:
            title = article.h3.a["title"]
            price_raw = article.find("p", class_="price_color").text.strip()
            price = price_raw.replace("Â", "").replace("£", "").strip()

            try:
                price_float = float(price)
            except ValueError:
                continue

            rating = article.p.get("class")[1]
            link = "https://books.toscrape.com/catalogue/" + article.h3.a["href"]

            if query.lower() in title.lower():
                books.append({
                    "title": title,
                    "price": price_float,
                    "rating": rating,
                    "link": link
                })

    return books
