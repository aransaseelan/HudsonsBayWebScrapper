
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

from HudsonsBayWebScrapper import link_list
driver = webdriver.Chrome()

sale_percentage = driver.find_element(By.CLASS_NAME, 'save-percentage')
