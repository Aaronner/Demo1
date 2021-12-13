from selenium import webdriver
import time
#创建浏览器对象
path = 'chromedriver.exe'
browser = webdriver.Chrome(path)
#url
url = 'https://baidu.com'
browser.get(url)
time.sleep(2)

# 获取文本框对象
input = browser.find_element_by_id('kw')
#在文本框中输入周杰伦
input.send_keys('周杰伦')
time.sleep(2)
#获取百度一下按钮
button = browser.find_element_by_id('su')
#点击按钮
button.click()
time.sleep(2)
#滑到底部
js_bottom = 'document.documentElement.scrollTop=100000'
browser.execute_script(js_bottom)
time.sleep(2)
#获取下一页按钮
next = browser.find_element_by_xpath('//a[@class="n"]')
#点击下一页
next.click()
time.sleep(2)
#回去
browser.back()
time.sleep(2)
#前进
browser.forward()
time.sleep(2)
#退出浏览器
browser.quit()