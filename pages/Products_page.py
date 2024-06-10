import pytest
import softest
from selenium import webdriver
from selenium.webdriver.common.by import By
from Lean_Tech.base.base_driver import BaseDriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class ProductsPage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    Product_field = '(//button[text()="Add to cart"])[1]'
    cart_title = '//span[@class="title"]'
    Product_page_title_Field = '//div[@class="header_secondary_container"]/span'
    Product_page_title = "Products"
    cart_page_xpath = "//div[@class='shopping_cart_container']"

    def add_to_cart_field(self):
        return self.driver.find_element(By.XPATH, self.Product_field)

    def move_to_cart_page(self):
        return self.driver.find_element(By.XPATH, self.cart_page_xpath)

    def cart_next_page_title(self):
        return self.driver.find_element(By.XPATH, self.cart_title)


    def add_to_cart(self):
        for i in range(1,4):
            self.add_to_cart_field().click()
        self.move_to_cart_page().click()
        value = self.driver.find_elements(By.XPATH,'//button[text()="Remove"]')
        assert len(value) == 3
        carts_title_val = self.cart_next_page_title().text
        assert carts_title_val == "Your Cart"
        print("Products added in cart")









