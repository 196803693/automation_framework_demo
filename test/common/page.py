from test.common.browser import Browser
from selenium.webdriver.support.select import Select
import time
from utils.log import logger

class StaleElementReferenceException(Exception):
    pass

class Page(Browser):
    def __init__(self,page=None,browser_type='chrome'):
        #保证只有一个driver
        if page:
            self.driver = page.driver
        else:
            super().__init__(browser_type)
    def get_driver(self):
        return self.driver
    def find_element(self,*args):
        return self.driver.find_element(*args)
    def find_elements(self,*args):
        return self.driver.find_elements(*args)
    def select_by_index(self,webelement,index=0):
        Select(webelement).select_by_index(str(index))