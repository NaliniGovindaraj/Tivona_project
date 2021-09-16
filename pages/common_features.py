from base.selenium_driver import SeleniumDriver

class CommonFeatures(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    #locators
    _commonfeatures_button = "react-burger-menu-btn"#id
    _allitems_link = "inventory_sidebar_link"
    _logout_link = "logout_sidebar_link"
    _about_link = "about_sidebar_link"
    _reset_link = "reset_sidebar_link"


    #actions

    def logout_function(self):
        self.elementClick(self._commonfeatures_button,locatorType='id')
        self.elementClick(self._logout_link,locatorType="id")


    def logout_display(self):
        self.elementClick(self._commonfeatures_button,locatorType='id')
        self.waitForElement(self._logout_link,locatorType='id',timeout=14,pollFrequency=1)
        re = self.isElementDisplayed(self._logout_link,locatorType='id')
        return re





