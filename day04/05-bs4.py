"""
bs4
    BeautifulSoup
    Beautiful Soup 是一个可以从HTML或XML文件中提取的python文件

    安装:pip install beautifulsoup4


"""

from bs4 import BeautifulSoup

html = open('05-test.html', 'r', encoding='utf-8').read()

# 创建一个对象 html.parser通用解析器
# soup = BeautifulSoup(html源码,'html.parser')
soup = BeautifulSoup(html, 'html.parser')
print(soup)

# tag 通过标签来定位提取 默认值返回第一个内容
# soup.标签名称
title = soup.title
print(title)
div = soup.div
print(div)

# .string 只有单独标签,标签内不能存在其他标签,才能获取文本内容
print(title.string)
print(div.string)
# .text 当前标签无论有多少个其他标签,直接获取所有标签文本内容
print(div.text)

# find 默认只返回一个内容,如果没有找到,返回none
# find('标签名称')
# find('标签名称', attrs={"属性名称":"对应的属性值"})
div = soup.find('div', attrs={"class": "div2"})
print(div)

# find_all 方法,默认能找到几个就返回几个,没有找到,就返回一个空列表
# find_all()
# find_all('标签名称', attrs={"属性名称":"对应的属性值"})
div_list = soup.find_all('div')
print(div_list[1])
div_2 = soup.find_all('div', attrs={"class": "div2"})
print(div_2)

img = soup.img
print(img)
# 提取属性值
src = img.attrs['src']
print(src)

src2 = img['src']
print(src2)
