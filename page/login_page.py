import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.helpers import URL,USERNAME,PASSWORD
#esperas explicitas, encapsulado
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class LoginPage:
    _INPUT_NAME = (By.NAME, 'user-name') #nombre del campo by.name el selector  
    _INPUT_PASSWORD =  (By.NAME,'password')
    _LOGIN_BUTTON =  (By.NAME,'login-button')
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(URL)
    
    def login(self, username=USERNAME, password=PASSWORD):
        
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self._INPUT_NAME)
        ).send_keys(username)
        
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self._INPUT_PASSWORD)
        ).send_keys(password)

        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self._LOGIN_BUTTON)
        ).click()#espero 5 hasta que valido que existe

