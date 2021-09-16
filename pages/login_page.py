from base.selenium_driver import SeleniumDriver
import time

class LoginPage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #locators
    _username_field = "user-name"#id
    _password_field = "password"#id
    _login_button = "login-button"#id

    # actions
    def EnterUsername(self,username):
        self.sendKeys(username,self._username_field,locatorType='id')

    def EnterPassword(self, password):
        self.sendKeys(password,self._password_field,locatorType='id')

    def ClickLogin(self):
        self.elementClick(self._login_button,locatorType='id')

    def login(self,username,password):
        self.EnterUsername(username)
        self.EnterPassword(password)
        self.ClickLogin()

    def verifyloginbuttondisplay(self):
        result = self.isElementDisplayed(self._login_button,locatorType='id')
        return result



