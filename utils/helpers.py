from selenium import webdriver
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


URL = 'https://www.saucedemo.com/'
USERNAME = 'standard_user'
PASSWORD = 'secret_sauce'


def get_driver():

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    #driver.implicitly_wait(5)
    time.sleep(5)

    return driver
def login_saucedemo(driver):
    driver.get(URL)
    #PROCESO DE LOGUEO
    driver.find_element(By.NAME, 'user-name').send_keys(USERNAME)
    time.sleep(1)
    driver.find_element(By.NAME, 'password').send_keys(PASSWORD)
    time.sleep(1)
    driver.find_element(By.ID,'login-button').click()
    time.sleep(5)
        




    
