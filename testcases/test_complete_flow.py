import time
import softest
from selenium import webdriver
import pytest
from Lean_Tech.pages.Login_page import LoginPage
from Lean_Tech.pages.Products_page import ProductsPage
from Lean_Tech.pages.YourCart_page import YourCart
from Lean_Tech.pages.CheckoutInformation_page import CheckoutInfo
from Lean_Tech.pages.CheckoutOverview_page import CheckoutOverview

@pytest.mark.usefixtures("setup")
class TestCompleteFlow():

    def test_complete_flow(self):

        #Login to page
        lp = LoginPage(self.driver)
        lp.login_to_sauce_labs()
        time.sleep(1)

        #Adding 3 products in cart
        pp = ProductsPage(self.driver)
        pp.add_to_cart()
        time.sleep(1)

        #Checking ot from cart
        ycp = YourCart(self.driver)
        ycp.click_to_check_out()
        time.sleep(1)


        #Checkout with information
        ci = CheckoutInfo(self.driver)
        ci.checkout_cart()
        time.sleep(2)

        #Verify items in cart and Final Checkout
        co = CheckoutOverview(self.driver)
        co.Verify_items_and_finish()
        time.sleep(10)






