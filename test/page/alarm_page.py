from test.common.page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class AlarmPage(Page):
    report = (By.XPATH,"//a[contains(@href,'reports')]")
    def turn_to_reports_page(self):
        #<a onclick="urlFun()" ondragstart="return false" href="/reports">报表</a>
        self.find_element(*self.report).send_keys(Keys.ENTER)