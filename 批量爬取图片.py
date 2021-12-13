import urllib.request
from lxml import etree

def create_request(page):
    if (page == 1):
        url = 'https://sc.chinaz.com/tupian/qinglvtupian.html'
    else:
        url = 'https://sc.chinaz.com/tupian/qinglvtupian_'+str(page)+'.html'
    headers = {
        'Cookie': 'cz_statistics_visitor=33e18871-1fc1-e87a-bc9d-198b477cb531; UM_distinctid=17d6a8da83bee3-029ac9a122bb51-978183a-1fa400-17d6a8da83c384; Hm_lvt_398913ed58c9e7dfe9695953fb7b6799=1638170209; __gads=ID=90904dee3dd0e047-22ac1c654fcf004c:T=1638170207:RT=1638170207:S=ALNI_Mac1rjo0vw1DHdA4rZFsHB9V0TGDg; CNZZDATA300636=cnzz_eid%3D126337106-1638165027-%26ntime%3D1638175827; Hm_lpvt_398913ed58c9e7dfe9695953fb7b6799=1638184566',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
    }
    request = urllib.request.Request(url=url, headers=headers)
    return request
def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content
    
def down_load(page, content):
    # 下载图片
    # 之前用的下载图片代码：
    # urllib.request.urlretrieve('图片的地址','文件名')
    # 服务器响应文件
    tree = etree.HTML(content)
    name_list = tree.xpath('//div[@id="container"]//a/img/@alt')
    src_list = tree.xpath('//div[@id="container"]//a/img/@src2')
    for i in range(len(name_list)):
        name = name_list[i]
        src = src_list[i]
        url = 'http:' + src
        print(url)
        url = url.replace('_s', '')
        print(url)
        urllib.request.urlretrieve(url=url, filename='./sex/'+name + '.jpg')

if __name__ == '__main__':
    start_page = int(input('起始页：'))
    end_page = int(input('结束页：'))
    for page in range(start_page, end_page+1):
        print(page)
        request = create_request(page)
        content = get_content(request)
        down_load(page, content)

        