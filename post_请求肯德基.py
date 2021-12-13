import urllib.parse
import urllib.request
#定制请求
def create_request(page):
    url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'
    data = {
        'cname': '广州',
        'pid': '',
        'pageIndex': page, 
        'pageSize': '10',
    }
    data = urllib.parse.urlencode(data).encode('utf-8')
    heeaders = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
    }
    request = urllib.request.Request(url=url, data=data, headers=heeaders)
    return request

#获取网页源码
def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content
# 下载资源
def down_load(page,content):
    f = open('地址页：'+str(page)+'.json', 'w', encoding='utf-8')
    f.write(content)
if __name__ == '__main__':
    start_page = int(input('起始页：'))
    end_page = int(input('结束页：'))
    for page in range(start_page, end_page):
        request = create_request(page)
        content = get_content(request)
        down_load(page,content)