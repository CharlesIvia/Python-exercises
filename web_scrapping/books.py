# GOAL: Get  title of every book with a two star rating

import requests
import bs4

# https://books.toscrape.com/catalogue/page-2.html
# https://books.toscrape.com/catalogue/page-3.html


base_url = "https://books.toscrape.com/catalogue/page-{}.html"

res = requests.get(base_url.format(1))

soup = bs4.BeautifulSoup(res.text, "lxml")

products = soup.select(".product_pod")

example = products[0]
print(example)

# Books with two star rating
# Quick and dirty
example_str = str(example)

print("star-rating Two" in str(example))

# Alternative

example_class = example.select(".star-rating.Three")
print(example_class)

# Find title

title = example.select("a")[1]["title"]
print(title)

# Get  title of every book with a two star rating

two_star_titles = []

for n in range(1, 51):
    scrape_url = base_url.format(n)
    print(scrape_url)
    res = requests.get(scrape_url)

    soup = bs4.BeautifulSoup(res.text, "lxml")
    books = soup.select(".product_pod")

    for book in books:
        if len(book.select(".star-rating.Two")) != 0:
            book_title = book.select("a")[1]["title"]
            two_star_titles.append(book_title)
print(two_star_titles)
print(len(two_star_titles))
for book_title in two_star_titles:
    print(book_title)
