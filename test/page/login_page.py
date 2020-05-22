from test.common.page import Page
from selenium.webdriver.common.by import By

class LoginPage(Page):
    txtAccount = (By.ID, 'txtAccount')
    txtPassword = (By.ID, 'txtPassword')
    def login(self,username,password):
        self.find_element(*self.txtAccount).send_keys(username)
        self.find_element(*self.txtPassword).send_keys(password)
        self.driver.find_element_by_tag_name('button').click()

if __name__ == '__main__':
    lp = LoginPage()
    lp.get('http://120.78.122.10:4010/')
    lp.sleep(2)
    lp.login('admin','123456')
    lp.sleep(2)
    lp.quit()