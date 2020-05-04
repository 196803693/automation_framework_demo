import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

class TestLogin(unittest.TestCase):
    URL = 'http://120.78.122.10:4010/'
    driver_path = os.path.dirname(os.getcwd()) + '\drivers\chromedriver.exe'
    txtAccount = (By.ID, 'txtAccount')
    txtPassword = (By.ID, 'txtPassword')
    def setUp(self):
        os.system('taskkill /f /im chromedriver.exe')
        self.driver = webdriver.Chrome(executable_path=self.driver_path)
        self.driver.get(self.URL)
        self.driver.maximize_window()
        time.sleep(3)
    def tearDown(self):
        time.sleep(3)
        self.driver.quit()
    def test_login_0(self):
        self.driver.find_element(*self.txtAccount).send_keys('admin')
        self.driver.find_element(*self.txtPassword).send_keys('123456')
        self.driver.find_element_by_tag_name('button').click()
    def test_login_1(self):
        self.driver.find_element(*self.txtAccount).send_keys('test01')
        self.driver.find_element(*self.txtPassword).send_keys('123456')
        self.driver.find_element_by_tag_name('button').click()
if __name__ == '__main__':
    unittest.main()