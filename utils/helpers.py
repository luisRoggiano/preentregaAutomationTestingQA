from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime 

URL = 'https://www.saucedemo.com/'
USERNAME = 'standard_user'
PASSWORD = 'secret_sauce'
SCREENSHOT_PATH = r'E:\curso-automation-testing\preentregaAutomationTestingQA\test\screenshots'

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

def take_screenshot(driver, test_name, test_file_path):
    test_dir = os.path.dirname(os.path.abspath(test_file_path))
    screenshot_dir = os.path.join(test_dir, "screenshots")
    if not os.path.exists(screenshot_dir):
        os.makedirs(screenshot_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y_%m_%d_%H-%M-%S")
    filename = f"{test_name}_{timestamp}.png"
    filepath = os.path.join(screenshot_dir, filename)
    try:
        driver.save_screenshot(filepath)
        print(f"\n✅ Captura guardada en: {filepath}")
    except Exception as e:
        print(f"\n❌ Error al guardar la captura de pantalla: {e}")





    
