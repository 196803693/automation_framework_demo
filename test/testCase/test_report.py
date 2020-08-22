import os
from selenium.webdriver.common.by import By
import unittest
from utils.config import Config,DATA_PAHT
from utils.log import logger
from utils.file_reader import ExcelReader
from parameterized import parameterized
from test.page.login_page import LoginPage
from test.page.index_page import IndexPage
from test.page.alarm_page import AlarmPage
from test.page.reports_page import ReportsPage
from test.page.reports_view_page import ReportsViewPage

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
                           ])
    def test_report(self,username,password):
        self.page = LoginPage(self.page)
        self.page.login(username,password)
        # self.page = IndexPage(self.page)
        # self.assertIsNotNone(self.page.system_name)
        # logger.info(self.page.system_name)
        # self.page.turn_to_alarm_page()
        # self.page = AlarmPage(self.page)
        # self.page.turn_to_reports_page()
        self.page.jump_to_reports_page(self.URL)
        self.page = ReportsPage(self.page)  #跳转到报表页面
        self.page.sleep(3)
        self.page.create_reports_dict()
        # self.page.test_main_reports()
        # self.page.search_monitor_history()
        # self.page = ReportsViewPage(self.page)
        # self.page.search_particle()  #颗粒度1h，查询
        self.page.sleep(3)
if __name__ == '__main__':
    unittest.main()