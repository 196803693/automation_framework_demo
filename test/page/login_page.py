from test.common.page import Page
from selenium.webdriver.common.by import By
from utils.log import logger

class LoginPage(Page):
    txtAccount = (By.ID, 'txtAccount')
    txtPassword = (By.ID, 'txtPassword')
    def login(self,username,password):
        self.find_element(*self.txtAccount).send_keys(username)
        self.find_element(*self.txtPassword).send_keys(password)
        self.driver.find_element_by_tag_name('button').click()

    def jump_to_reports_page(self,URL):
        self.get(URL+'reports')

if __name__ == '__main__':
    lp = LoginPage()
    lp.get('http://10.111.222.155:4010/')
    lp.sleep(2)
    d = {}
    def test(self): #测试字典里可以存放元素对象
        a = self.find_element(*self.txtAccount)
        d['aaaa'] = a
        logger.info('字典是',str(d))
    test(lp)
    lp.login('admin','123456')
    lp.sleep(2)
    lp.quit()