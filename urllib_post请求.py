from os import read
import json
import urllib.request
import urllib.parse
url = 'https://fanyi.baidu.com/sug'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
}

data = {
    'kw': 'her'
}
# post请求的参数，必须要进行编码
data = urllib.parse.urlencode(data).encode('utf-8')

# post请求的参数，是不会拼接在url后面的。而是需要放在请求对象定制的参数中
# 请求对象的定制
request = urllib.request.Request(url=url, data=data, headers=headers)
# 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(request)
# 获取响应的数据
content = response.read().decode('utf-8')
obj = json.loads(content)
print(obj)