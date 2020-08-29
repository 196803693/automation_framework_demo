# coding=utf-8
import requests
import json
from functools import partial
from utils.config import Config
class TestWeather(object):
    @staticmethod
    def search(self,params):
        url = Config().get('juhe_simple_weather')
        r = requests.get(url, params=params)
        print('requests返回的类型是：',type(r))
        print('Search Params:\n', json.dumps(params,ensure_ascii=False))    #ensure_ascii=False是为了显示中文
        print('Search Response:\n', json.dumps(r.json(), ensure_ascii=False))
    def test_weather(self):
        cities = ['深圳','北京','重庆','湖北','河南']
        for c in cities:
            params = dict(city=c,key=Config().get('weather_key',index=1))
            f = partial(TestWeather.search,params)
            f.description = json.dumps(params,ensure_ascii=False)
            yield(f,)
if __name__ == '__main__':
    # params = dict(city='深圳',key=Config().get('weather_key',index=1))
    tw = TestWeather()
    for i in range(5):
        print(tw.test_weather().description)