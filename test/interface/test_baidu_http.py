import unittest
from utils.client import HttpClient
from utils.config import Config,REPORT_PAHT
from HTMLTestRunner import HTMLTestRunner

class TestBaiduHttp(unittest.TestCase):
    URL = Config().get('baidu_url')
    def setUp(self):
        self.client = HttpClient(self.URL,method='GET')
    def test_index(self):
        response = self.client.send()
        self.assertIn('百度一下，你就知道',response.text)

if __name__ == '__main__':
    report = REPORT_PAHT + '\\test_report02.html'
    with open(report,'wb') as f:
        runner = HTMLTestRunner(f, verbosity=2, title='接口测试报告', description='这是描述')
        runner.run(TestBaiduHttp('test_index'))
