import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
from utils.config import Config,DRIVER_PATH,DATA_PAHT
from utils.log import logger
from utils.file_reader import ExcelReader
from parameterized import parameterized
from test.page.login_page import LoginPage
from test.page.index_page import IndexPage

class TestLogin(unittest.TestCase):
    URL = Config().get('URL')
    txtAccount = (By.ID, 'txtAccount')
    txtPassword = (By.ID, 'txtPassword')
    account_path = DATA_PAHT + '\\user_account.xlsx'
    print('文件路径', account_path)
    account = ExcelReader(account_path).data

    def setUp(self):
        os.system('taskkill /f /im chromedriver.exe')
        self.page = LoginPage().get(self.URL)
        self.page.sleep(2)
    def tearDown(self):
        self.page.sleep(1.5)
        self.page.quit()
    @parameterized.expand([(account[0]['username'],str(account[0]['password'])),
                           (account[1]['username'],str(account[1]['password']))])
    def test_login(self,username,password):
        self.page.find_element(*self.txtAccount).send_keys(username)
        self.page.find_element(*self.txtPassword).send_keys(password)
        self.page.driver.find_element_by_tag_name('button').click()
        self.page = IndexPage(self.page)
        logger.info(self.page.system_name)
if __name__ == '__main__':
    unittest.main()