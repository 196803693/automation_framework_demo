from test.common.page import Page
from selenium.webdriver.common.by import By
from utils.log import logger
import time
class ReportsPage(Page):
    #reportContainer > div:nth-child(1) > div > div.content > ul > li:nth-child(1)
    #// *[ @ id = "reportContainer"] / div[1] / div / div[2] / ul / li[1]
    # report_template > div.button-bar > button:nth-child(2)
    target_li = (By.XPATH, '//*[@id="reportContainer"]/div[1]/div/div[2]/ul/li[1]')
    target_div = (By.XPATH, "//div[contains(@title,'监控量历史数据报表')]")
    temp = (By.CLASS_NAME, 'temp')
    button_c2 = (By.CSS_SELECTOR, '#report_template > div.button-bar > button:nth-child(2)')
    def create_reports_dict(self):
        total_have_module_divs = self.find_elements(By.CLASS_NAME,"temp-list")
        logger.info('有模板的报表的数量是%d'%(len(total_have_module_divs)))
        reports_dict = {}
        for temp_list_div in total_have_module_divs:
            #//*[@id="reportContainer"]/div[3]/div/div[2]/ul/li[2]/div[2]/div/div[1]
            temp_list_div.find_element(By.XPATH,"//div[contains(@title,'编辑')]")   #编辑模板
            modify_elem = temp_list_div.find_element(By.XPATH,".//div[contains(@title,'编辑')]")
            modify_elem.click()
            #//*[@id="base_win_1597918501257"]/div/div[5]/span
            module_name = self.find_element(By.XPATH,"//div[@class='ui-window-title']/span").text
            report_name = module_name.split('[')[0]
            logger.info('当前报表名称：%s'%report_name)
            reports_dict[report_name] = temp_list_div   #将报表名称和temp_list_div放入字典
            self.find_element(By.XPATH,'//*[@id="report_0x00010011"]/div[2]/button[2]').click() #点击保存
            modify_result = self.find_element(By.CLASS_NAME,'ui-popup-msg').text
            logger.info('修改报表模板的结果是:%s',modify_result)
            self.find_element(By.CSS_SELECTOR,"[class='ui-popup-button ui-popup-button-ok']").click()   #点击确定
        logger.info('报表和关联li对应的字典是%s'%(str(reports_dict)))

    def search_monitor_history(self):
        #<div title="监控量历史数据报表" class="report-name">监控量历史数据报表</div>
        #判断是否是监控历史表,如果是就点击第一个模板查询
        report_li = self.find_element(*self.target_li)
        report_div = self.find_element(*self.target_div)
        if report_div.text == '监控量历史数据报表':
            temp_report = report_li.find_element(*self.temp)
            temp_report.click()
            self.find_element(*self.button_c2).click()
        else:
            logger.info('没有监控量历史数据报表')
    def test_main_reports(self):
        self.search_monitor_history()
