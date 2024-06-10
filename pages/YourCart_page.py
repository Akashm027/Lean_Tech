import pytest
from selenium.webdriver.common.by import By
from Lean_Tech.base.base_driver import BaseDriver


class YourCart(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    Checkout_field = "checkout"
    info_page_title = "Checkout: Your Information"
    info_page_element = '//span[@class="title"]'


    def click_to_check_out(self):
        return self.driver.find_element(By.ID,self.Checkout_field).click()

    def get_info_page_title(self):
        return self.driver.find_element(By.XPATH,self.next_page_field)

    def checkout_cart(self):
        self.click_to_check_out().click()
        value = self.get_info_page_title().text
        print("Title of info page: ", value)
        assert value == self.info_page_title
        print("Verified addition in cart and continuing to proceed further into information page ")











