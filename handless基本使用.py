from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.options import Options
#chrome_options = Options()
#chrome_options.add_argument('--headless')
#chrome_options.add_argument('--disable-gpu')
#path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
#chrome_options.binary_location = path
#browser = webdriver.Chrome(chrome_options=chrome_options)
#browser.get('http://www.baidu.com/')
#browser.save_screenshot('bb.png')
#封装
def share_browser():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
    chrome_options.binary_location = path
    browser = webdriver.Chrome(chrome_options=chrome_options)
    return browser

browser = share_browser()
url = 'https://baidu.com/'
browser.get(url)
browser.save_screenshot('cc.png')