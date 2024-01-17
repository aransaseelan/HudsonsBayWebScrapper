import os 
import requests
from bs4 import BeautifulSoup

url = "https://www.thebay.com/"

response = requests.get(url) #