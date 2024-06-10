from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class BaseDriver:
    def __init__(self,driver):
        self.driver = driver

    def wait(self):
        wait = WebDriverWait(self.driver, 10)
        return wait
