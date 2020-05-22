from test.common.page import Page
from selenium.webdriver.common.by import By

class IndexPage(Page):

    loc_system_name = (By.CSS_SELECTOR,'div.title-lg>b')
    @property
    def system_name(self):
        return self.find_element(*self.loc_system_name).text