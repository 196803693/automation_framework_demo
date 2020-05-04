import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

os.system('taskkill /f /im chromedriver.exe')
URL = 'http://120.78.122.10:4010/'
driver_path = os.path.dirname(os.getcwd())+'\drivers\chromedriver.exe'
driver = webdriver.Chrome(executable_path=driver_path)
driver.get(URL)
driver.maximize_window()
time.sleep(3)
driver.find_element(By.ID,'txtAccount').send_keys('admin')
driver.find_element(By.ID,'txtPassword').send_keys('123456')
driver.find_element_by_tag_name('button').click()
time.sleep(3)
driver.quit()