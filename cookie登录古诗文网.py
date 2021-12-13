#__VIEWSTATE: Dn9b0jSWhF5kbV7r5PcRw+khMuGILYRESWvDZeTWPvk8CPGxBYQwXPWAGUpq9rBjMnrbNhQi3jLbNpB7ZA/lDNtfu3uhNmOdNsniaM1kNrQQL+6xJdg9WrYpuuk=
#__VIEWSTATEGENERATOR: C93BE1AE
#from: http://so.gushiwen.cn/user/collect.aspx
#email: 595165358@qq.com
#pwd: action
#code: 79G4
#denglu: 登录

#__VIEWSTATE  __VIEWSTATEGENERATOR  code(验证码)
#以上三个都是可变化的量
#难点：（1）__VIEWSTATE  __VIEWSTATEGENERATOR 一般情况下看不到的数据，都是在页面的源码中
#      所以需要获取页面的源码，然后获取以上两个量的值
#     （2）验证码
import requests
from bs4 import BeautifulSoup
# 这是登录页面的url地址
url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
}
# 获取页面源码
response = requests.get(url=url, headers=headers)
content = response.text
# 解析页面源码，然后获取__VIEWSTATE  __VIEWSTATEGENERATOR
soup = BeautifulSoup(content,'lxml')
#获取__VIEWSTATE
viewstate = soup.select('#__VIEWSTATE')[0].attrs.get('value')
# 获取__VIEWSTATEGENERATOR
viewstategenerator = soup.select('#__VIEWSTATEGENERATOR')[0].attrs.get('value')
# 获取验证码图片
code = soup.select('#imgCode')[0].attrs.get('src')
code_url = 'https://so.gushiwen.cn' + code

#下载图片
#import urllib.request
#urllib.request.urlretrieve
#以上方法有问题，验证码图片不同步
#应使用requests里面有一个方法session(),通过session的返回值，就能使用请求变成一个对象
session = requests.session()
response_code = session.get(code_url)
# 注意此时使用二进制数据，因为我们使用的是图片的下载
content_code = response_code.content
# wb模式就是将二进制文件写入到文件
f = open('验证码.jpg', 'wb')
f.write(content_code)
f.close()
# 获取验证码的图片之后，下载到本地，然后观察验证码
# 观察之后，然后在控制台输入这个验证码
# 就可以吧这个值传给code的参数，就可以登录
code_name = input('验证码：')

# 点击登录
data_post = {
    '__VIEWSTATE': viewstate,
    '__VIEWSTATEGENERATOR': viewstategenerator,
    'from': 'http://so.gushiwen.cn/user/collect.aspx',
    'email': '595165358@qq.com',
    'pwd': 'action',
    'code': code_name,
    'denglu': '登录'
}
#将requests改成session后就能保证验证码和登录请求是同一个
response_post = session.post(url=url, headers=headers, data=data_post)
content_post = response_post.text
f = open('gushi.html', 'w', encoding='utf-8')
f.write(content_post)


