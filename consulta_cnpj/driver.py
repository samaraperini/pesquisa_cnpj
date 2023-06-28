from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options

def abrir_navegador():
        options = Options()
        options.add_argument("--private")
        options.add_argument("--disable-extensions")
        return webdriver.Firefox(options=options, service=FirefoxService(GeckoDriverManager().install()))        

 