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
    #_cart_link = "//span[@class='shopping_cart_badge' and contains(text(),'1')]
    _cart_button = "shopping_cart_link"#class

    #actions
    # def productPage(self):
    #     self.isElementDisplayed(self._products_page,locatorType='xpath')
    #
    # def displaysortbutton(self):
    #     self.isElementDisplayed(self._sort_button,locatorType='CLASS')
    #
    # def displaycartbutton(self):
    #     self.isElementDisplayed(self._cart_button,locatorType='CLASS')

    def clickItemLink(self, itemname):
        self.elementClick(itemname, locatorType='partiallink')

    def displayitem(self,itemname):
        self.isElementDisplayed(itemname, locatorType='partiallink')

    def ClickAddtoCart(self):
        self.elementClick(self._addtocart_button,locatorType='xpath')

    def ClickCart(self):
        self.elementClick(self._cart_button,locatorType='class')


    def verifyingProductpageDisplay(self):
        result  = self.productPage()
        return result

    def verifyitem(self,itemname):
        result  = self.displayitem(itemname)
        return result

    def AddtoCartCheckout(self,itemname):
        time.sleep(5)
        self.clickItemLink(itemname)
        time.sleep(5)
        self.ClickAddtoCart()
        time.sleep(5)
        self.ClickCart()
        time.sleep(5)




    # _username_field = "item_5_title_link"  # id
    # _password_field = "item_4_title_link"  # id
    # _login_button = "item_1_title_link"  # id
    # _username_field = "item_3_title_link"  # id
    # _password_field = "item_0_title_link"  # id
    # _login_button = "item_2_title_link"#id





