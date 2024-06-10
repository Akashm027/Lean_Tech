import pytest
from selenium.webdriver.common.by import By
from Lean_Tech.base.base_driver import BaseDriver


class CheckoutOverview(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    click_button_field ='finish'
    value_of_final_page = "Thank you for your order!"
    final_page_element = "//h2[contains(text() ,'Thank you for your order!')]"
    cart_items_field = '//div[@class="cart_quantity"]'

    def total_item_in_cart(self):
        return self.driver.find_elements(By.XPATH,self.cart_items_field)

    def final_page_value(self):
        return self.driver.find_element(By.XPATH,self.final_page_element)

    def click_on_finish(self):
        return self.driver.find_element(By.ID, self.click_button_field)

    def Verify_items_and_finish(self):
        no_of_items_in_cart = len(self.total_item_in_cart())
        print("no of items in cart: ",no_of_items_in_cart)
        assert no_of_items_in_cart == 3
        self.click_on_finish().click()
        value = self.final_page_value().text
        print("Value of final page : ", value)
        assert value == self.value_of_final_page
        print("Order places successfully.. Execution completed")



