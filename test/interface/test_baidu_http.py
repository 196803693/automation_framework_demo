import unittest
from utils.client import HttpClient
from utils.config import Config
from utils.assertion import assertionHttpCode

class TestBaiduHttp(unittest.TestCase):
    URL = Config().get('baidu_url')
    def setUp(self):
        self.client = HttpClient(self.URL,method='GET')
    def test_index(self):
        response = self.client.send()
        assertionHttpCode(response,[200])
        self.assertIn('百度一下，你就知道',response.text)
if __name__ == '__main__':
    unittest.main()
