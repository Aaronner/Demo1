# urllib和requests
# urllib
# (1)一个类型以及六个方法
# (2)get请求
# (3)post请求

# requests
# (1)参数使用params传递
# （2）参数无需urlencode编码
# （3）不需要请求对象的定制
# （4）请求资源路径中的？可加可不加
import requests
url = 'https://baidu.com/s'
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'zh-CN,zh-TW;q=0.9,zh;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': 'BIDUPSID=2DD0209EDADD8F519E026EF157652920; PSTM=1637636759; BAIDUID=2DD0209EDADD8F5114B8F1B43284ABBC:FG=1; BD_UPN=12314753; __yjs_duid=1_4025113a96df3089fb9747f77024ed3d1637636783344; sugstore=0; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BDSFRCVID_BFESS=MLKOJeC62ADBJznH60dCb5f7Q5Pmr9vTH6aoU6TlXZtf2dPFUdOWEG0PSM8g0KubwxFKogKK3gOTH4DF_2uxOjjg8UtVJeC6EG0Ptf8g0f5; H_BDCLCKID_SF_BFESS=tbFt_KDbtK_3Hnn4hPcqq4kX-xcahC6Ja54sbUbcBhcqEIL4Lf_-hjKBy-betM7aJCFfbC_bKt3NMxbSj4QobM0kh4Orhnc0fgLq_Rju3h5nhMJob67JDMP0XtOwbnTy523iob3vQpPMshQ3DRoWXPIqbN7P-p5Z5mAqKl0MLPbtbb0xb6_0DTJLDH_Jt58s2D63LPbMHtcsjJ6pKRoHh4It-fIX5-RLf2CeLl7F5l8-hRRwBUDByxvBDM-L5jQhJaCHbRv7HCQxOKQphUDBMqj3b4AJKR3Bb4jPoP5N3KJm8tP9bT3v5tDwMajn2-biWb7M2MbdJpbP_IoG2Mn8M4bb3qOpBtQmJeTxoUJ25DnJhbLGe6-MDjbXeaAfqbO2HjR8sJO8fMI5hh7_bf--D4Ajh4ke5fkqtIn93D5DJMDVfPcsyl5xy5K_hN7hbP6z3JKLb-0b-nkBShvHQT3m-lQbbN3itUr9KHQCWb3cWKOJ8UbSjMOPBTD02-nBat-OQ6npaJ5nJq5nhMJmb67JD-50eG-jtjDOJnCtV-OHa6rEqbTgbtL_h4L3ePcrBMRZ5mAqoqjg0qc0DlPCD-OT-6LEjnLtQPrHf6cnaIQqaMK-SbRyWROtD40rQRobWhb43bRTbhCy5KJvfJo62MjvhP-UyNbMWh37JgnlMKoaMp78jR093JO4y4Ldj4oxJpOJ5JbMonLafJOKHIClejDW3e; H_PS_PSSID=35294_35106_31254_35239_34584_34505_35246_34606_35329_35318_26350_35209_35145_35301; ab_sr=1.0.1_MGM3NjVkYmYzZDM5M2M1Y2Q5ZjZmZTllOGFkZTczYWU2YWVkMjM0NzNjYzk3ODNiMTJmMjIwYTIzNWFkOGYzYTVlNmM5ZjlhM2RhYzAzOWU1ZTljNjc0OTkxNTg2NWMxMDY3YmZlNGRjZGFiY2QyMjhiZGExOTMxYTJhYmQwM2E1MTU5N2QxZjM2ZjNhMGIzMjZlMTY4OGI4ZDZjZmEwOQ==; BAIDUID_BFESS=2DD0209EDADD8F5114B8F1B43284ABBC:FG=1; delPer=0; BD_CK_SAM=1; PSINO=6; COOKIE_SESSION=67108_0_8_9_14_4_1_0_8_4_2_0_438_0_0_0_1638270845_0_1638341121%7C9%23189181_5_1638171709%7C2; BD_HOME=1; H_PS_645EC=4ca0kV5Q%2FixvEde1dhZD%2BxZrX6%2F%2FQBvM%2B%2F8jKrZKVvrIInDfuikAE5pndYc; baikeVisitId=db724e8a-b353-4476-9c71-9560d155502f; BA_HECTOR=0l8gakak2ha0aga42d1gqe7090q; BDSVRTM=199',
    'Host': 'www.baidu.com',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
}
data = {
    'wd': '周杰伦'
}
response = requests.get(url=url, params=data, headers=headers)
response.encoding = 'utf-8'
content = response.text
file = open('ax.html', 'w', encoding='utf-8')
file.write(content)
file.close()