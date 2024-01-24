import os 
import webbrowser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.support import expected_conditions as EC


counter = 2
max_page = 0

def SideBar(driver, run_once_flag):
    global counter  # Declare counter as global to modify it
    global max_page  # Declare max_page as global to access and modify it
    if run_once_flag:
        page_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(@aria-label, 'Total pages: ')]"))
        )
        # Extract the total number of pages
        aria_label = page_element.get_attribute("aria-label")
        max_page = int(aria_label.split(": ")[1]) if "Total pages: " in aria_label else 0
        run_once_flag = False
    
    print(max_page)
    print(counter)
    if counter <= max_page:
        sales_button_xpath = f"//a[@aria-label='Page {counter}']"
        sales_button = driver.find_element(By.XPATH, sales_button_xpath)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, sales_button_xpath))
        ).click()
        counter += 1
