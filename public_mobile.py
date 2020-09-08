import requests
from bs4 import BeautifulSoup as bs
from config import user, password

URL = 'https://selfserve.publicmobile.ca/'
LOGIN_ROUTE = ''

HEADERS = {
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'}
