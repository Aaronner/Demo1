import urllib.request
import json
import jsonpath
url = 'https://dianying.taobao.com/cityAction.json?activityId&_ksTS=1638254248596_137&jsoncallback=jsonp138&action=cityAction&n_s=new&event_submit_doGetAllRegion=true'

headers = {
    'accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
    'accept-language': 'zh-CN,zh-TW;q=0.9,zh;q=0.8,en;q=0.7',
    'cookie': 't=357e6929008dcce3bdbfe0ad44f51be0; cookie2=1966b8541360c81875cf2fab5eda36c7; v=0; _tb_token_=e87bdfdeee33; cna=600jGprB+20CAXkglkOsh++o; xlly_s=1; tb_city=440100; tb_cityName="uePW3Q=="; tfstk=cpkdBuqvMFYnIpEt0XdiF4p6bHKGauY85MalehakmE2vBeWRFsfinxhV_BZ7uyKO.; l=eBjQN1ceg-slvaxNBOfZhurza779MIRAguPzaNbMiOCP93fp5JqFW6I7m0T9CnGVhsmkR3uQQyaYBeYBqC2sjqj4axom48Dmn; isg=BL6-x9x4U8yCm4foWWv4T0fvD9QA_4J5VKRsAmjHWYH8C17l0I1RiaXlg9fHM3qR',
    'referer': 'https://dianying.taobao.com/?spm=a1z21.3046609.city.4.32c0112aW9xsCA&city=440100',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest'
}
request = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
content = content.split('(')[1].split(')')[0]
f = open('淘票票.json', 'w', encoding='utf-8')
f.write(content)
obj = json.load(open('淘票票.json', 'r', encoding='utf-8'))
aa = jsonpath.jsonpath(obj, '$..regionName')
print(aa)