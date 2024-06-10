import pytest
from selenium.webdriver.common.by import By
from Lean_Tech.base.base_driver import BaseDriver


class CheckoutInfo(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    FName = "Walter"
    Lname = "White"
    Postal_code = "123456"
    next_page_value = "Checkout: Overview"

    FName_field = "first-name"
    Lname_field = "last-name"
    Postal_code_field = "postal-code"
    next_page_field = '//span[@class="title"]'
    click_continue_field ='continue'


    def first_name_element(self):
        return self.driver.find_element(By.ID,self.FName_field)

    def Last_name_element(self):
        return self.driver.find_element(By.ID,self.Lname_field)

    def postal_code_element(self):
        return self.driver.find_element(By.ID,self.Postal_code_field)

    def next_page_title(self):
        return self.driver.find_element(By.XPATH,self.next_page_field)

    def click_on_continue(self):
        return self.driver.find_element(By.ID, self.click_continue_field)

    def checkout_cart(self):
        self.first_name_element().send_keys(self.FName)
        self.Last_name_element().send_keys(self.Lname)
        self.postal_code_element().send_keys(self.Postal_code_field)
        self.click_on_continue().click()
        value = self.next_page_title().text
        print("Title of page Overview_page: ",value)
        assert value == self.next_page_value
        print("Added users details successfully")


