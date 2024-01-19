import os 
import webbrowser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
import time


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