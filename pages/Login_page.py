import pytest
import softest
from selenium import webdriver
from selenium.webdriver.common.by import By
from Lean_Tech.base.base_driver import BaseDriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class LoginPage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    Uname = "standard_user"
    Pass = "secret_sauce"
    Username_id_field = "user-name"
    Password_id_filed = "password"
    Login_button_field = "login-button"
    Product_page_title_Field = '//div[@class="header_secondary_container"]/span'
    Product_page_title = "Products"

    def waiting_period(self):
        self.wait().until(EC.presence_of_element_located((By.XPATH,self.Product_page_title_Field)))

    def get_username_id(self):
        return self.driver.find_element(By.ID, self.Username_id_field)

    def get_password_id(self):
        return self.driver.find_element(By.ID, self.Password_id_filed)

    def get_login_button(self):
        return self.driver.find_element(By.ID, self.Login_button_field)

    def product_next_page_title(self):
        return self.driver.find_element(By.XPATH, self.Product_page_title_Field)



    def login_to_sauce_labs(self):
        self.get_username_id().send_keys(self.Uname)
        self.get_password_id().send_keys(self.Pass)
        self.get_login_button().click()
        self.waiting_period()
        value = self.product_next_page_title().text
        assert value == self.Product_page_title
        print("Logged in as standard user")








