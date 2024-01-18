import os 
import requests
import webbrowser
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

url = "https://www.thebay.com/" # The website we are going to scrape
driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window() # Maximize the browser window

# Find the textbox by its HTML attribute (e.g., ID or name) and enter text
textbox = driver.find_element("id", "textboxId")
textbox.send_keys("Your search query")

# Find the search button by its HTML attribute and click it
search_button = driver.find_element("id", "searchButtonId")
search_button.click()


response = requests.get(url) # Get the response from the website

if response.ok: 
    print(response.status_code) # 200 means it is a success
else :
    print(response.status_code) # 403 means it is a failure

driver.quit() # Close the browser
