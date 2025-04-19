import requests
from bs4 import BeautifulSoup


link = 'https://glints.com/id/opportunities/jobs/recommended'
r = requests.get(link)
