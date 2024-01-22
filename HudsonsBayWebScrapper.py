import os 
import webbrowser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from Scroll import scroll
from SideBar import SideBar
from selenium.webdriver.support import expected_conditions as EC
import time

# Open the website in a new browser window
url = "https://www.thebay.com/" # The website we are going to scrape
driver = webdriver.Chrome()
driver.get(url) #
driver.implicitly_wait(10) # this lets webdriver wait 10 seconds for the website to load
driver.maximize_window() # Maximize the browser window

#Brands I would want to search for
brands = ["Nike", "Lacoste", "Polo Ralph Lauren"]

#Sizes I would want to search for
sizes = ["Large", "X-Large"]

for brand in brands:
    # Find the textbox by its HTML attribute (e.g., ID or name) and enter text
    textbox = driver.find_element("name", "q")
    textbox.send_keys(brand)
    

    # Find the search button by its HTML attribute and click it
    search_button = driver.find_element("name", "search-button")
    search_button.click() 

    # Wait for search results to load (if necessary)
    WebDriverWait(driver, 10).until(
        lambda d: d.find_elements(By.XPATH, "//a[@href]")
    )
    
    counter = 1
    
    link_list = []  # List to store the links to the product pages
    while True:
        
        scroll(driver) #Uses the scroll function from Scroll.py to scroll down the page

        WebDriverWait(driver, 10).until(
            lambda d: d.find_elements(By.XPATH, "//a[@href]")
        )
        
        # Collecting URLs
        product_urls = [elem.get_attribute("href") for elem in driver.find_elements(By.XPATH, "//a[@href]")] 
        # elem is the element in the list of elements, get_attribute("href") is the attribute of the element we want to get (href)
        # href is the link to the product page
        for url in product_urls:
            if 'product' in url and any(size in url for size in sizes):
                print(url)
                link_list.append(url)
                
        try:
            page_elements = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//a[contains(@aria-label, 'Page ')]"))
            )
        
            page_numbers = [int(el.get_attribute("aria-label").split(" ")[1]) for el in page_elements]
            page_numbers.sort()
            page_button_xpath = f"//a[@aria-label='Page {page_numbers[counter]}']"
            page_button = driver.find_element(By.XPATH, page_button_xpath)
            page_button.click()
            # Wait for search results to load (if necessary)
            counter += 1
        except: 
            break


#<span class="save-percentage">(34% OFF)</span>

#Add an error logging system like if the product isn't found
#Make it more dynamic so you can open multiple chrome instances at once