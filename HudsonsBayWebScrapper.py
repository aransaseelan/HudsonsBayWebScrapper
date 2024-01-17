import os 
import requests
from bs4 import BeautifulSoup

url = "https://www.thebay.com/"

response = requests.get(url) # Get the response from the website

if response.ok: 
    print(response.status_code) # 200 means it is a success
else :
    print(response.status_code) # 403 means it is a failure