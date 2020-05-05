import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
from utils.config import Config
from utils.log import logger

class TestLogin(unittest.TestCase):
    URL = Config().get('URL')
    driver_path = os.path.dirname(os.getcwd()) + '\driver\chromedriver.exe'
    txtAccount = (By.ID, 'txtAccount')
    txtPassword = (By.ID, 'txtPassword')
    def setUp(self):
        os.system('taskkill /f /im chromedriver.exe')
        self.driver = webdriver.Chrome(executable_path=self.driver_path)
        self.driver.get(self.URL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        time.sleep(3)
    def tearDown(self):
        time.sleep(3)
        self.driver.quit()
    def test_login_0(self):
        self.driver.find_element(*self.txtAccount).send_keys('admin')
        self.driver.find_element(*self.txtPassword).send_keys('123456')
        self.driver.find_element_by_tag_name('button').click()
        title_lg = self.driver.find_element_by_css_selector('div.title-lg>b')
        system_name = title_lg.text
        logger.info(system_name)
    def test_login_1(self):
        self.driver.find_element(*self.txtAccount).send_keys('test01')
        self.driver.find_element(*self.txtPassword).send_keys('123456')
        self.driver.find_element_by_tag_name('button').click()
if __name__ == '__main__':
    unittest.main()
