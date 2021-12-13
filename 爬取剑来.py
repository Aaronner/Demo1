import urllib.parse
import urllib.request
import json

url = 'http://www.jianlaixiaoshuo.com/book/7058.html'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
}
# 定制
request = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
file = open('a.html', 'w', encoding='utf-8')
file.write(content)
file.close()