from selenium import webdriver
path = 'chromedriver.exe'
browser = webdriver.Chrome(path)
browser.get('https://www.jd.com/')

content = browser.page_source
print(content)