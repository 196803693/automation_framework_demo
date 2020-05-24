#首先得登录上，记住请求的时候用post，然后拿到cookies
import requests

#用requests.session()创建session对象，相当于创建了一个空的会话框，准备保持cookies。
session = requests.session()
url = 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-login.php'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'
    }
###一定要注意，如果有很多的登录参数的时候，不要忘记,,,,,,,,,,,,,,,,,,,,,,,!!!
data = {
    'log': 'spiderman',
    'pwd': 'crawler334566',
    'wp-submit': '登录',
    'redirect_to': 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn',
    'testcookie': '1'
}
#在创建的session下用post发起登录请求，session这个时候就包括 cookies 了。
# login_in = session.post(url, headers = headers, data = data)
login_in = session.request(method='POST',url=url,headers=headers,data=data)
print(type(login_in))
print(type(session.cookies))
print(type(session.headers))
print(session.headers)
print(session.cookies)