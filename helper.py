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
    print(run_once_flag)
    if run_once_flag:
        page_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(@aria-label, 'Total pages: ')]"))
        )
        # Extract the total number of pages
        aria_label = page_element.get_attribute("aria-label")
        max_page = int(aria_label.split(": ")[1]) if "Total pages: " in aria_label else 0 
        #Splits the string into a list of strings, using ":" as the separator
        run_once_flag = False
    
        if max_page == 0: #Some dont have a total pages since theres less or equal to three pages
            page_elements = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, "//a[contains(@aria-label, 'Page ')]"))
            )
            page_numbers = [int(el.get_attribute("aria-label").split(" ")[1]) for el in page_elements]
            page_numbers.sort()
            max_page = page_numbers[-1]
    
    print(max_page)
    print(counter)
    if counter <= max_page:
        sales_button_xpath = f"//a[@aria-label='Page {counter}']"
        sales_button = driver.find_element(By.XPATH, sales_button_xpath)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, sales_button_xpath))
        ).click()
        counter += 1

def scroll(driver):
    last_position = driver.execute_script("return window.pageYOffset;")

    while True:
        # Simulate pressing PAGE_DOWN key
        body = driver.find_element(By.TAG_NAME, "body")
        for i in range(5):
            body.send_keys(Keys.PAGE_DOWN)
        
        time.sleep(8)
        current_position = driver.execute_script("return window.pageYOffset;")
        if current_position == last_position:
            # If the position hasn't changed, we are at the bottom
            break
        last_position = current_position