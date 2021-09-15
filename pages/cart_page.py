import time

from base.selenium_driver import SeleniumDriver

class CartPage(SeleniumDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators
    _checkout_button = 'checkout'  # id

    def verifyAddedItem(self, itemname):
        result = self.isElementDisplayed(itemname, locatorType='partiallink')
        return result

    # def verifyCheckoutDisplay(self):
    #     result = self.isElementDisplayed(self._checkout_button, locatorType='id')
    #     return result

