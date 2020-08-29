'''
在这里添加各种自定义的断言，断言失败返回AssertionError就好
'''

#判断响应code
def assertionHttpCode(response,code_list):
    res_code = response.status_code
    if not code_list:
        code_list = [200]
    if res_code not in code_list:
        raise AssertionError('响应code不在列表中') #unittest自动判断用例Failure,不是Error