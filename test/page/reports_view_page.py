from test.common.page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from utils.log import logger
import time

class ReportsViewPage(Page):
    # reportContainer > div.sp-content > div.main-left > div.button-group > select
    # reportContainer > div.sp-content > div.main-left > div.button-group > button:nth-child(2)
    #//*[@id="reportContainer"]/div[2]/div[1]/div[3]/button[2]
    particle_dict = {1:'1',2:'7',3:'30'}
    select_css = (By.CSS_SELECTOR,'#reportContainer > div.sp-content > div.main-left > div.button-group > select')
    button_all = (By.XPATH,'//*[@id="reportContainer"]/div[2]/div[1]/div[3]/button')
    table_id = (By.ID,'resultTable')
    def search_particle(self):
        '''选择各种参数，查询报表结果，index是颗粒度
        颗粒度从最细的开始查，如果查到没有数据就增加一级颗粒度再查
        '''
        select_ele = self.find_element(*self.select_css)
        button_elms = self.find_elements(*self.button_all)
        for i in range(3):
            self.select_by_index(select_ele, i)   #颗粒度依次选择5m，1h，1d
            button_elms[i].send_keys(Keys.ENTER)    #依次点击1天，7天，30天的按钮
            logger.info('带颗粒度报表查询，本次select编号是%d,button的名称是%s'%(i,button_elms[i].text))
            time.sleep(3)
            result_table = self.find_element(*self.table_id)
            result_tr_counts = len(result_table.find_elements(By.TAG_NAME,'tr'))
            logger.info('result_table内共有%d行'%result_tr_counts)
            if result_tr_counts == 1:   #表格只有标题行，说明没有有效数据
                logger.warning('查询%s天的数据结果为空'%(button_elms[i].text))


