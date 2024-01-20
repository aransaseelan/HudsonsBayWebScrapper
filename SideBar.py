import os 
import webbrowser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.support import expected_conditions as EC


def SideBar(driver):
    
    page_elements = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, "//a[contains(@aria-label, 'Page ')]"))
    )
    
    page_numbers = [int(el.get_attribute("aria-label").split(" ")[1]) for el in page_elements]
    page_numbers.sort()
    
    
    sales_button = driver.find_element(By.XPATH, "//a[@aria-label='Page 2']")
    sales_button.click()
