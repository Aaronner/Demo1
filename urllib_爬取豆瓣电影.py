#https://movie.douban.com/j/chart/top_list?type=11&
# interval_id=100%3A90&action=&start=40&limit=20

#https://movie.douban.com/j/chart/top_list?type=11&
# interval_id=100%3A90&action=&start=20&limit=20

#https://movie.douban.com/j/chart/top_list?type=11&
# interval_id=100%3A90&action=&start=0&limit=20

# 下载前十页数据
# 步骤：1.请求对象的定制
#     2.获取响应的数据
#      3.下载
import urllib.request
import urllib.parse
# 定义定制对象函数
def create_request(page):
    base_url = 'https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
    }
    data = {
        'start': (page-1)*20,
        'limit': 20
    }
    # data编码
    data = urllib.parse.urlencode(data)
    url = base_url + data
    request = urllib.request.Request(url=url, headers=headers)
    return request
# 获取网页源码
def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content
# 下载数据
def down_load(page, content):
    f = open('豆瓣页：'+str(page)+".json", 'w', encoding='utf-8')
    f.write(content)
# 主程序入口
if __name__ == '__main__':
    start_page = int(input('起始页：'))
    end_page = int(input('结束页：'))
    for page in range(start_page, end_page+1):
        request = create_request(page)
        content = get_content(request)
        down_load(page, content)