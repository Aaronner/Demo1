# 定制更高级的请求头
# urllib.request.urlopen(url)
# 不能定制请求头
# urllib.request.Request(url,headers,data)
# 可以定制请求头
# Handler
# 定制更高级的请求头（随着业务逻辑的复杂 请求对象的定制已经满足不了我们的需求
# （动态cookie和代理不能使用请求对象的定制）
# 示例
import urllib.request
url = 'http://www.baidu.com/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
}
request = urllib.request.Request(url=url, headers=headers)
handler = urllib.request.HTTPHandler()
opener = urllib.request.build_opener(handler)
response = opener.open(request)
content = response.read().decode('utf-8')
print(content)
