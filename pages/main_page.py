import time

from selenium.webdriver.common import actions

from base.selenium_driver import SeleniumDriver

class MainPage(SeleniumDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # locators
    _products_page = "//span[@class='title' and (contains(text(),'Products'))]"
    _sort_button = "product_sort_container"#class
    _addtocart_button = "//button[contains(text(),'Add to cart')]"#xpath
    _cart_button = "shopping_cart_link"#class
    _Sauce_backbag_link= "//div[@class='inventory_item_name' and contains(text(),'Sauce Labs Backpack')]"
    _select_container_dd ='select_container'#class


    #actions
    def productpage(self):
        self.waitForElement(locator='self._products_page',locatorType='xpath',timeout=13, pollFrequency=0.5)

        self.isElementDisplayed(self._products_page)

    def selectcontainer(self):
        self.waitForElement(self._select_container_dd,locatorType='class',timeout=13, pollFrequency=0.5)

        self.isElementDisplayed(self._select_container_dd)

    def clickItemLink(self, itemname):
        self.waitForElement(itemname, locatorType='partiallink',
                               timeout=11, pollFrequency=0.5)

        self.elementClick(itemname, locatorType='partiallink')

    def displayitem(self):
        self.waitForElement(self._Sauce_backbag_link, locatorType='xpath',timeout=12, pollFrequency=0.5)
        self.isElementDisplayed(self._Sauce_backbag_link, locatorType='xpath')


    def ClickAddtoCart(self):
        self.elementClick(self._addtocart_button,locatorType='xpath')

    def ClickCart(self):
        self.elementClick(self._cart_button,locatorType='class')


    #methods
    def verifyitem(self):
        result  = self.displayitem()
        return result

    def AddtoCartCheckout(self,itemname):

        self.clickItemLink(itemname)
        self.ClickAddtoCart()
        self.ClickCart()

    def verifyingProductpageDisplay(self):
        result = self.productpage()
        return result

    def vselectcontainer(self):
        result = self.selectcontainer()
        return result






    # _username_field = "item_5_title_link"  # id
    # _password_field = "item_4_title_link"  # id
    # _login_button = "item_1_title_link"  # id
    # _username_field = "item_3_title_link"  # id
    # _password_field = "item_0_title_link"  # id
    # _login_button = "item_2_title_link"#id

