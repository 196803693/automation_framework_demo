import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

os.system('taskkill /f /im chromedriver.exe')
URL = 'https://www.baidu.com/'
driver_path = os.path.dirname(os.getcwd())+'\drivers\chromedriver.exe'
driver = webdriver.Chrome(executable_path=driver_path)
driver.get(URL)
driver.maximize_window()
driver.implicitly_wait(5)
driver.find_element(By.ID,'aa').send_keys('疫情')
driver.find_element(By.ID,'su').click()
time.sleep(3)
driver.quit()