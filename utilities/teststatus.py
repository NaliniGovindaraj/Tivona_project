"""
@package utilities

CheckPoint class implementation
It provides functionality to assert the result

Example:
    self.check_point.markFinal("Test Name", result, "Message")
"""
import utilities.custom_logger as cl
import logging
from base.selenium_driver import SeleniumDriver


class TestStatus(SeleniumDriver):

    log = cl.customLogger(logging.INFO)


    def __init__(self, driver):

        super().__init__(driver)
        self.driver.implicitly_wait(10)
        self.resultList = []

    def setResult(self, testName, result, resultMessage):
        try:
            if result is not None:
                if result is True:
                    self.resultList.append("PASS")
                    self.log.error("### VERIFICATION SUCCESSFUL :: + " + resultMessage + testName)
                else:
                    self.resultList.append("FAIL")
                    self.log.error("### VERIFICATION FAILED :: + " + resultMessage + testName)
                    self.screenShot(resultMessage + testName)
            else:
                self.resultList.append("FAIL")
                self.log.error("### VERIFICATION FAILED :: + " + resultMessage + testName)
                self.screenShot(resultMessage + testName)
        except:
            self.resultList.append("FAIL")
            self.log.error("### Exception Occurred !!!")
            self.screenShot(resultMessage + testName)

    def mark(self, testName, result, resultMessage):
        self.setResult(testName, result, resultMessage)

    def markFinal(self, testName, result, resultMessage):

        self.setResult(result,resultMessage)

        if "FAIL" in self.resultList:
            self.log.error(testName + "###Failed###")
            print("nalini" + self.resultList)
            self.resultList.clear()
            assert True == False

        else:
            self.log.error(testName + "###PASS###")
            self.resultList.clear()
            assert True == True

