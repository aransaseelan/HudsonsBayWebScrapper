import os 
import webbrowser
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Open the website in a new browser window
url = "https://www.thebay.com/" # The website we are going to scrape
driver = webdriver.Chrome()
driver.get(url)
driver.implicitly_wait(100) # this lets webdriver wait 10 seconds for the website to load
driver.maximize_window() # Maximize the browser window

# Find the textbox by its HTML attribute (e.g., ID or name) and enter text
textbox = driver.find_element("name", "q")
textbox.send_keys("Your search query")

""" # Find the search button by its HTML attribute and click it
search_button = driver.find_element("id", "searchButtonId")
search_button.click() """

driver.quit() # Close the browser
