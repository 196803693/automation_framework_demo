'''抽取器，从结果中抽取想要的数据'''
import json
import jmespath
class JMESExtractor(object):
    def extract(self,query=None,body=None):
        try:
            return jmespath.search(query,json.loads(body))
        except Exception as e:
            raise ValueError('Invalid query' + query + ':'+e)


if __name__ == '__main__':
    from utils.client import HttpClient
    res = HttpClient(url='http://wthrcdn.etouch.cn/weather_mini?citykey=101010100').send()
    print(res.text,'\n','***********************')
    j = JMESExtractor()
    j_1 = j.extract("data.forecast[0].date",res.text)
    j_2 = j.extract("data.ganmao",res.text)
    print(j_1,j_2)