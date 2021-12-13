import urllib.request

url_page = "http://lmg.jj20.com/up/allimg/tp05/19100120461512E-0-lp.jpg"
urllib.request.urlretrieve(url=url_page, filename='test.png')
