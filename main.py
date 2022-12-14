import requests
from bs4 import BeautifulSoup
import json


url = 'http://nlkr.gov.kg'
my_html = requests.get(url)
soup = BeautifulSoup(my_html.text, 'html.parser')
my_tag = 'page_title'
header = soup.find('h2', class_ = my_tag)

