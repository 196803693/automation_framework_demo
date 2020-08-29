import os
from selenium.webdriver.common.by import By
import unittest
from utils.config import Config,DATA_PAHT
from utils.log import logger
from utils.file_reader import ExcelReader
from parameterized import parameterized
from test.page.login_page import LoginPage
from test.page.index_page import IndexPage

account_path = DATA_PAHT + '\\user_account.xlsx'
account = ExcelReader(account_path, sheet=1).data

class TestLogin(unittest.TestCase):
    URL = Config().get('EAF-URL')
    txtAccount = (By.ID, 'txtAccount')
    txtPassword = (By.ID, 'txtPassword')
    print('文件路径', account_path)

    def setUp(self):
        os.system('taskkill /f /im chromedriver.exe')
        self.page = LoginPage().get(self.URL)
        self.page.sleep(2)
    def tearDown(self):
        self.page.sleep(1.5)
        self.page.quit()
    @parameterized.expand(account)
    def test_login(self,username,password):
        self.page = LoginPage(self.page)
        self.page.login(username,password)
        self.page = IndexPage(self.page)
        self.assertIsNotNone(self.page.system_name)
        logger.info(self.page.system_name)
if __name__ == '__main__':
    print(account)