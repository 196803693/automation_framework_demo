from utils.config import DRIVER_PATH
from selenium import webdriver
import time

driver_path = DRIVER_PATH + '\chromedriver.exe'
class Browser(object):
    def __init__(self,browser_type='chrome'):
        if browser_type == 'chrome':
            self.driver = webdriver.Chrome(executable_path=driver_path)
    def get(self,url):
        self.driver.get(url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        return self
    def save_screenshot(self):
        self.driver.save_screenshot()
    def close(self):
        self.driver.close()
    def quit(self):
        self.driver.quit()
    def sleep(self,second):
        time.sleep(second)
if __name__ == '__main__':
    b = Browser()
    b.get('http://120.78.122.10:4010/')
    time.sleep(2)
    b.quit()