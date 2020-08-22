from test.common.page import Page
from selenium.webdriver.common.by import By

class IndexPage(Page):
    #app > div > div.ctr-project-info > div.project-title
    # app > div > div > div.container-top.flex-left > div.block > div.title-lg > b
    loc_system_name = (By.CSS_SELECTOR,'div.project-title')
    operation_and_maintenance = (By.XPATH,'//body / div[1] / div[1] / ul / li[8] / a / div')
    @property
    def system_name(self):
        return self.find_element(*self.loc_system_name).text
    def turn_to_alarm_page(self):
        #body > div.ui - header - nav > div.ui - link - box > ul > li: nth - child(8) > a > div
        #/ html / body / div[1] / div[1] / ul / li[8] / a / div
        self.find_element(*self.operation_and_maintenance).click()