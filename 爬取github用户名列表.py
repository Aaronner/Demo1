import urllib.request
from lxml import etree
from bs4 import BeautifulSoup

# 定制请求
def create_request(page):
    base_url = 'https://github.com/search?'
    end_url = 'p='+str(page)+'&q=user&type=Users'
    url = base_url+end_url
    print(url)
    headers = {
        'referer': 'https://github.com/search?q=&ref=simplesearch',
        'cookie': '_octo=GH1.1.464749147.1637648274; _device_id=c5409839d5e27ab6b0fd3e7e0f7a7b12; has_recent_activity=1; user_session=-enFttFoiqjIlLzoQU7eOtiZEGDEnM8bRBa21QjB555_fkk6; __Host-user_session_same_site=-enFttFoiqjIlLzoQU7eOtiZEGDEnM8bRBa21QjB555_fkk6; logged_in=yes; dotcom_user=Aaronner; tz=Asia%2FShanghai; color_mode=%7B%22color_mode%22%3A%22auto%22%2C%22light_theme%22%3A%7B%22name%22%3A%22light%22%2C%22color_mode%22%3A%22light%22%7D%2C%22dark_theme%22%3A%7B%22name%22%3A%22dark%22%2C%22color_mode%22%3A%22dark%22%7D%7D',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
    }
    request = urllib.request.Request(url=url, headers=headers)
    return request

# 获取响应信息
def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content

#提取并下载目标数据
def down_load(content):
    soup = BeautifulSoup(content, 'lxml')
    name_list = soup.select('div[class="f4 text-normal"] a')
    for name in name_list:
        print(name.get_text())

# 主程序入口
if __name__ == '__main__':
    start_page = int(input('起始页：'))
    end_page = int(input('结束页：'))
    for page in range(start_page, end_page+1):
        request = create_request(page)
        content = get_content(request)
        down_load(content)