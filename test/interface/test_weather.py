# coding=utf-8
import json
import unittest
from utils.client import HttpClient
from utils.config import Config
from parameterized import parameterized
from utils.log import logger

source_dict = dict(city='深圳',key=Config().get('weather_key',index=1),error_code=0)

class TestWeather(unittest.TestCase):
    URL = Config().get('juhe_simple_weather')
    def setUp(self):
        self.client = HttpClient(url=self.URL,method='GET')
    #使用参数化测试接口，注意传入参数的格式
    @parameterized.expand([['深圳','de5148ef8cabaf81c0d1c83c84098379',1]])
    def test_response(self,city,key,error_code):
        params = dict(city=city,key=key)
        response = self.client.send(params=params)
        # logger.info('响应结果%s'%(json.dumps(response.json(),ensure_ascii=False,indent=4)))
        cur_error_code = response.json()['error_code']
        self.assertEqual(error_code,cur_error_code)
if __name__ == '__main__':
    # print('请求的参数',params)
    # unittest.main()
    pass