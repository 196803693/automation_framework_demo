from HTMLTestRunner import HTMLTestRunner
from utils.config import REPORT_PAHT
import unittest
from utils.mail import Email
report_path = REPORT_PAHT + '\\test_report.html'
test_report = unittest.defaultTestLoader.discover('./',pattern='test_report.py')

with open(report_path,'wb') as f:
    runner = HTMLTestRunner(f,verbosity=2,title='测试登录02',description='这是今天的报告，请查收')
    runner.run(test_report)
# email = Email(server='smtp.163.com',
#               sender='15730145041@163.com',
#               password='KVZERLKYJVXOCHPP',
#               receiver='zns_test01@163.com',
#               title='测试登录的报告',
#               message='这是今天的测试报告，请查收',
#               path=report_path
#               )
# email.send()