from utils.config import DRIVER_PATH,REPORT_PAHT
from selenium import webdriver
import time
import os

driver_path = DRIVER_PATH + '\chromedriver.exe'
class Browser(object):
    def __init__(self,browser_type='chrome'):
        if browser_type == 'chrome':
            self.driver = webdriver.Chrome(executable_path=driver_path)
    def get(self,url):
        self.driver.get(url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        return self
    def save_screenshot(self,name='screenshot'):
        day = time.strftime('%Y-%m-%d',time.localtime())
        screenshot_path = REPORT_PAHT + '\screenshot_%s' % day
        if not os.path.exists(screenshot_path):
            os.makedirs(screenshot_path)
        tm = time.strftime('%H%M%S',time.localtime())
        screenshot = self.driver.save_screenshot(screenshot_path +'\\%s_%s.PNG'%(name,tm) )
        return screenshot
    def close(self):
        self.driver.close()
    def quit(self):
        self.driver.quit()
    def sleep(self,second):
        time.sleep(second)
if __name__ == '__main__':
    b = Browser()
    b.get('http://www.baidu.com')
    b.save_screenshot()