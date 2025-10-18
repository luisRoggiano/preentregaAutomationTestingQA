import pytest                                                                           #pytest -v nos permite correr este arhivo usando la terminal
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))          #__file__ variable de la ruta del archivo actual, por que sería mediante el join path&.. abspath pasa de ruta relativa a ruta absoluta
from utils.helpers import login_saucedemo, get_driver
from selenium.webdriver.common.by import By
import time


@pytest.fixture(scope='session')                                                        #pytest.fixture(scope='session') mantiene la sesión iniciada mientras se ejecutan los test
def driver():
    
    driver = get_driver()                                                               #llamo a la función getDriver del file helpers (instanciamos)
    yield driver                                                                        #palabra reservada yield, le da al navegador el driver correcto. manteniendo el navegador abierto similar a scope
    #driver.quit()                                                                       #cerramos la ventana



def test_login(driver):
    login_saucedemo(driver)
    assert "/inventory.html" in driver.current_url                                      #verifica que estemos en la pagina correcta de inventory
    titulo = driver.find_element(By.CLASS_NAME, 'app_logo').text                        #verificamos el título
    assert titulo == 'Swag Labs'                                                        #verificamos que diga Swag Labs en el logo



#def test_catalogo():

def test_catalogo(driver):
    #login_saucedemo(driver)
    products = driver.find_elements(By.CLASS_NAME, 'inventory_list')                    #usamos findelements por que son muchos elementos
    assert len(products) > 0                                                            #verificamos que los elementos esten contenidos dentro del main container
    
def test_carrito(driver):
    #login_saucedemo(driver)
    products = driver.find_elements(By.CLASS_NAME, 'inventory_item')
    #totalProducts = len(products)

    products[0].find_element(By.TAG_NAME, 'button').click()                               #lista de los productos listados, y por tag accedemos al button de add to cart, agregandolo al carrito
    products[1].find_element(By.TAG_NAME, 'button').click()
    products[2].find_element(By.TAG_NAME, 'button').click()
    #verificamos que el carrito agrega los productos
    badge = driver.find_element(By.CLASS_NAME, 'shopping_cart_badge').text
    assert int(badge) == 3
    products[0].find_element(By.TAG_NAME, 'button').click()
    #verificamos que el arrito elimina productos
    badge = driver.find_element(By.CLASS_NAME, 'shopping_cart_badge').text
    assert int(badge) == 2