"""
中国知网
1、https://www.cnki.net/

分析是动态还是静态
针对请求，需要携带什么请求头参数

"""
from selenium import webdriver
import time
from bs4 import BeautifulSoup
import requests


driver = webdriver.Chrome()
driver.get('https://www.cnki.net/')
time.sleep(3)
driver.find_element_by_css_selector('#txt_SearchText').send_keys('四轴无人机')
driver.find_element_by_css_selector('body > div.wrapper.section1 > div.searchmain > div > div.input-box > input.search-btn').click()
time.sleep(5)
html = driver.page_source
driver.quit()
soup = BeautifulSoup(html, 'html.parser')
table_tr_all = soup.find('table',attrs={"class":"result-table-list"}).find('tbody').find_all('tr')
for tr in table_tr_all:
    a = tr.find('td',attrs={"class":"name"}).find('a')
    # a标签内的href属性，  文本
    href = 'https://kns.cnki.net' + a['href'].strip()
    title = a.text.strip()

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.43",
        "Referer": "https://kns.cnki.net/kns8/defaultresult/index",
    }

    res = requests.get(href, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    pdfDown = soup.find('a', attrs={"id": "pdfDown"})
    pdf_href = pdfDown['href']
    print('当前内容：{}, 当前下载pdf链接：{}'.format(title, pdf_href))