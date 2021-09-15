import time
import pytest
import unittest
from utilities.teststatus import TestStatus
from ddt import ddt,data,unpack
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.cart_page import CartPage
from pages.common_features import CommonFeatures

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class Test_Main_Page(unittest.TestCase):

    @pytest.fixture(autouse=True)

    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.mp = MainPage(self.driver)
        self.cp = CartPage(self.driver)
        self.cf = CommonFeatures(self.driver)
        self.ts = TestStatus(self.driver)
        self.driver.implicitly_wait(10)


    @pytest.mark.run(order=1)
    @data(("standard_user", "secret_sauce","Sauce Labs Backpack"))
    @unpack
    def test_successful_login(self,username,password,itemname):
        self.lp.login(username,password)
        time.sleep(5)
        result = self.mp.verifyitem(itemname)
        self.ts.mark("test_successful_login",result,"TC1 Completed")

    @pytest.mark.run(order=2)
    @data(("standard_user", "secret_sauce","Sauce Labs Backpack"))
    @unpack
    def test_display_added_items(self,username,password,itemname):
        self.mp.AddtoCartCheckout(itemname)
        self.cp.verifyAddedItem(itemname)
        result = self.cp.verifyAddedItem(itemname)
        self.ts.mark("test_display_added_items",result,"TC2 Completed")

    @pytest.mark.run(order=3)
    @data(("standard_user", "secret_sauce"))
    @unpack
    def test_successful_logout(self, username, password):
        self.cf.verify_logout()
        self.lp.login(username, password)
        self.cf.verify_logout()
        result = self.lp.verifyloginbuttondisplay()
        self.ts.mark("test_successful_login", result, "TC3 Completed")


