from app import app
from models import book
import urllib.request,json,xml
from models import book
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup as bs
import lxml
import re
Book= book.Book
# Getting api key
# api_key = app.config['BOOK_API_KEY']

# # Getting the movie base url
# base_url = app.config["BOOK_API_BASE_URL"]



def get_book():
    url = 'https://www.goodreads.com/search.xml?key=jCRKYMgy7fN9hxa2YlkQ&q=business'
    response = urllib.request.urlopen(url).read()
    res = bs(response, "lxml-xml")
    print(res)
    
    images = res.findAll('image_url')
    titles = res.findAll('title')

    book_results = zip(images, titles)
    return book_results


    
    