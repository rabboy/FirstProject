import requests
from bs4 import BeautifulSoup as b
 
URL = 'https://youla.ru/moskva?q=lego%20back%20to%20the%20future'
r = requests.get(URL)
print(r.status_code)