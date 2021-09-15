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

    def verify_logout(self):
        self.elementClick(self._commonfeatures_button,locatorType='id')
        self.elementClick(self._logout_link,locatorType="id")



