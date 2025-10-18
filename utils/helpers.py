from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options # <-- ¡ESTA FALTABA!
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

    # quitar aviso de cambio de contraseña insegura
    chrome_options = Options()
    
    # 1. Ignorar el Gestor de Contraseñas de Google y las notificaciones
    chrome_options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    })
    
    # 2. Argumentos de supresión (Mantenemos para cobertura)
    chrome_options.add_argument("--disable-features=OptimizationGuide")
    chrome_options.add_argument("--disable-features=PasswordManagerV1")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-notifications")
    
    # 3. Solución definitiva: Forzar un perfil de usuario Temporal/Invitado
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--guest") 
    
    service = Service(ChromeDriverManager().install())
    
    # Inicializar el driver con todas las opciones
    driver = webdriver.Chrome(service=service, options=chrome_options) 
    
    driver.implicitly_wait(5)

    return driver

def login_saucedemo(driver):
    driver.get(URL)
    # PROCESO DE LOGUEO
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