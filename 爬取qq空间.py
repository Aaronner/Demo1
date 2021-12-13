import urllib.request
import urllib.parse

url = 'https://user.qzone.qq.com/1391097343/infocenter'

headers = {
    #'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh-TW;q=0.9,zh;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'if-modified-since': 'Mon, 29 Nov 2021 03:10:23 GMT',
    'sec-ch-ua': '''" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"''',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
    'cookie': '1391097343_totalcount=2948; 1391097343_todaycount=0; RK=rp6gSwv+N3; ptcz=ba81e9dd16c724667f0d0d95bb7c52a54341d73ac6229240a5cb431ff1fca2c7; ptui_loginuin=1391097343; qz_screen=1920x1080; pgv_pvid=8933697230; QZ_FE_WEBP_SUPPORT=1; uin=o1391097343; skey=@uvG5Q32ET; p_uin=o1391097343; pt4_token=Ha2bzg8jRqvi6OIzRGWrsz9D8Cr*-mO6MmbE7vLDn6U_; p_skey=77CJ7T94rdAB-dXGp-MBC-cd5e76IFbyYVMWsz*s40A_; Loading=Yes; pgv_info=ssid=s6643120338; cpu_performance_v8=1; __Q_w_s__QZN_TodoMsgCnt=1'
}

request = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
f = open('qqzone.html', 'w', encoding='utf-8')
f.write(content)
f.close()