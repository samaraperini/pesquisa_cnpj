from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def acessar_url(driver: WebDriver, url: str):
        return driver.get(url)   
 
def encontrar_elemento(driver: WebDriver, elemento):
    return driver.find_element(by = By.XPATH, value = elemento)

def clicar(elemento: WebElement) -> None:
    return elemento.click()

def escrever(elemento: WebElement, texto: str) -> None:
    elemento.send_keys(texto)

def aguardar_clicavel(driver: WebDriver, localizador_elemento: str, tipo_elemento: str = 'XPATH', tempo_espera: int = 60) -> WebElement:
    return WebDriverWait(driver, tempo_espera).until(EC.element_to_be_clickable((By().__getattribute__(tipo_elemento.upper()), localizador_elemento)))

