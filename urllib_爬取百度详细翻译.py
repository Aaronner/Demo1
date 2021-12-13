from os import read
import json
import urllib.request
import urllib.parse

url = 'https://fanyi.baidu.com/v2transapi'

headers = {
    'Cookie': 'BIDUPSID=2DD0209EDADD8F519E026EF157652920; PSTM=1637636759; BAIDUID=2DD0209EDADD8F5114B8F1B43284ABBC:FG=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; __yjs_duid=1_4025113a96df3089fb9747f77024ed3d1637636783344; BAIDUID_BFESS=2DD0209EDADD8F5114B8F1B43284ABBC:FG=1; delPer=0; PSINO=6; FANYI_WORD_SWITCH=1; REALTIME_TRANS_SWITCH=1; SOUND_PREFER_SWITCH=1; SOUND_SPD_SWITCH=1; HISTORY_SWITCH=1; ZD_ENTRY=baidu; BCLID=7603466035909920609; BDSFRCVID=PTKOJeC62AE6m6vHCs7Lb5f7Q23bwA6TH6aodDEnDLxyi8J65aZGEG0PKf8g0KuMDNpzogKK3gOTH4DF_2uxOjjg8UtVJeC6EG0Ptf8g0f5; H_BDCLCKID_SF=tbFt_KDbtK_3Hnn4hPcqq4kX-xcahC6Ja54sbUbcBhcqEIL4Lf_-hjKBy-betM7aJCFfbC_bKt3NMxbSj4QobM0kh4Orhnc0fgLq_Rju3h5nhMJob67JDMP0XtOwbnTy523iob3vQpPMshQ3DRoWXPIqbN7P-p5Z5mAqKl0MLPbtbb0xb6_0-nDSHHKqqTtq3H; BCLID_BFESS=7603466035909920609; BDSFRCVID_BFESS=PTKOJeC62AE6m6vHCs7Lb5f7Q23bwA6TH6aodDEnDLxyi8J65aZGEG0PKf8g0KuMDNpzogKK3gOTH4DF_2uxOjjg8UtVJeC6EG0Ptf8g0f5; H_BDCLCKID_SF_BFESS=tbFt_KDbtK_3Hnn4hPcqq4kX-xcahC6Ja54sbUbcBhcqEIL4Lf_-hjKBy-betM7aJCFfbC_bKt3NMxbSj4QobM0kh4Orhnc0fgLq_Rju3h5nhMJob67JDMP0XtOwbnTy523iob3vQpPMshQ3DRoWXPIqbN7P-p5Z5mAqKl0MLPbtbb0xb6_0-nDSHHKqqTtq3H; H_PS_PSSID=35294_35106_31254_35239_35048_34584_34505_35246_34606_35318_26350_35209_35145_35301; BA_HECTOR=0k2h042g8h8l0h04kb1gq3jo10r; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1637981719,1637981739,1637982882,1637994244; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1637994244; ab_sr=1.0.1_NDJjOGViYjE3MjM5OTBmYzM0YmI1ODgwMjY4Y2MyNjY0OWQ2YWMyZjA2YTYzNTZhZmRiYzUyNDM1ZGM1YjQ4Y2EwMzAyZmUxYzc3MTQ0YWI0MTM1MjcwYTZjMzIyM2NjNWFhMGJjYzllYzJiMzY1NjdjZGRiZTYwOGRlMGExYjgyNDYzZjc2ZDgyNjVmODAxYmJmYWI2YTg1OGM3OWYzMQ==; __yjs_st=2_MzFkZTBiNTQwMjMwZmM0YWYwMzMxOGFjNzdlM2UzNDVhMTMxYTY1MzZiNjMwZDZiZGJkYzJhYjU0MmJjMzY1OTZkZDUwOGIyNzM5MTk1MWMxNDE5ZmI1MmUyZTMwNDZjMjNkYjFmMDEzY2EzNDFmNGYxYWIxZTNmOWRlYzRkYzM0MjdlNzdiM2EyNGE0NTAxMTVmYTE1NWJlYmQxMTg3ZDYxZWUzMmE1YTlkNmQwYTlkZWYyNTI3OGY5NDYxZWJjYjEzMGUzYTBhMjU3ZjU5MGNlNjgwNDk0MWZiZGI2YzZlZTM2NDI3OTVhN2FhNjJlODhmYmExMDA3OGEzMTc4OV83X2VmZjkxOWQw'
    }
data = {
    'from': 'en',
    'to': 'zh',
    'query': 'she',
    'transtype': 'realtime',
    'simple_means_flag': '3',
    'sign': '880544.625809',
    'token': '9d059d791db4aaecc2b4ab6a999ec558',
    'domain': 'common'
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
# python对象转换成json字符串
# ensure_ascii=flase : 忽略字符集编码
s = json.dumps(obj,ensure_ascii=False)
print(s)