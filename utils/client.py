import requests
from utils.log import logger

METHOD = ['GET','POST','PUT','DELETE']

class UnsupportMethod(Exception):
    pass

class HttpClient:
    """
    http请求的client。初始化时传入url、method等，可以添加headers和cookies，但没有auth、proxy。

    >>> HTTPClient('http://www.baidu.com').send()
    <Response [200]>
    """
    def __init__(self,url,method='GET',headers=None):
        self.session = requests.session()
        self.url = url
        if method not in METHOD:
            raise UnsupportMethod('不支持%s这个方法'%method)
        self.method = method.upper()
        self.set_headers(headers)
    def set_headers(self,headers):
        if headers:
            self.session.headers.update(headers)
    def send(self,params=None,data=None):
        response = self.session.request(method=self.method,url=self.url,data=data,params=params)
        response.encoding = 'utf-8'
        logger.debug('请求成功{0}\n{1}'.format(response,response.text))
        return response