from urllib import parse
from lxml import etree
# xpath解析
#（1）本地文件
tree = etree.parse('a.html')
p_list = tree.xpath('//body/p/text()')
f = open('a.txt', 'w', encoding='utf-8')
f.write(p_list)
