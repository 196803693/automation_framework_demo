from HTMLTestRunner import HTMLTestRunner
from utils.config import REPORT_PAHT
import unittest

report_path = REPORT_PAHT + '\\test_report02.html'
test_index = unittest.defaultTestLoader.discover('./',pattern='test_baidu_http.py')

with open(report_path,'wb') as f:
    runner = HTMLTestRunner(f,verbosity=2,title='测试接口',description='这是今天的报告，请查收')
    runner.run(test_index)