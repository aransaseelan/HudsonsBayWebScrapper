import os 
import webbrowser
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait

# Open the website in a new browser window
url = "https://www.thebay.com/" # The website we are going to scrape
driver = webdriver.Chrome()
driver.get(url)
driver.implicitly_wait(100) # this lets webdriver wait 100 seconds for the website to load
driver.maximize_window() # Maximize the browser window

driver.implicitly_wait(5) # Wait for 5 seconds

#Brands I would want to search for
brands = ["Nike", "Lacoste", "Polo Ralph Lauren"]

for brand in brands:
    # Find the textbox by its HTML attribute (e.g., ID or name) and enter text
    textbox = driver.find_element("name", "q")
    textbox.send_keys(brand)

    # Find the search button by its HTML attribute and click it
    search_button = driver.find_element("name", "search-button")
    search_button.click() 

    #Clicks each product on the page
    products = driver.find_elements_by_class_name("product-tile")
    
    # List to hold all product URLs
    product_urls = []

