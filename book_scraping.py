import sqlite3
import requests
from bs4 import BeautifulSoup
from scraping_getters import get_price, get_rating, get_title


url = "https://books.toscrape.com/catalogue/category/books/history_32/index.html"

def scraps_book(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    books = soup.find_all('article')
    all_books = []
    for book in books:
        all_books.append((get_title(book), get_price(book), get_rating(book)))
    save_books(all_books)

def save_books(all_books):
    connection = sqlite3.connect("books")
    c=  connection.cursor()
    c.execute('''CREATE TABLE books
              (title TEXT, price REAL, rating INTEGER)''')
    c.executemany("INSERT INTO books VALUES (?, ?, ?)", all_books)
    connection.commit()
    connection.close()

scraps_book(url)
