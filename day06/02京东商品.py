

from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

file = open('京东商品.csv', 'w', encoding='utf-8', newline='')
csv_file = csv.writer(file)
csv_file.writerow(['价钱','名称','评价数','商铺名'])



url = "https://www.jd.com/"
driver = webdriver.Chrome()
driver.get(url)
time.sleep(1)
driver.find_element_by_css_selector('#key').send_keys('手机')
driver.find_element_by_css_selector('#search > div > div.form > button > i').click()


while True:
    time.sleep(2)
    for i in range(15):
        driver.execute_script(  'window.scrollBy(0,500);'  )
        time.sleep(0.1)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    div_all = soup.find_all('div',attrs={"class":"gl-i-wrap"})
    for div in div_all:
        #获取价钱
        p_price = div.find('div',attrs={"class":"p-price"}).text.strip()
        #获取标题
        p_name = div.find('div',attrs={"class":"p-name"}).text.strip()
        #获取评论
        p_commit = div.find('div',attrs={"class":"p-commit"}).text.strip()
        #获取商铺名称
        p_shop = div.find('div',attrs={"class":"p-shop"}).text.strip()

        csv_file.writerow([p_price,p_name,p_commit,p_shop])

    #点击下一页 当没有找到此标签时，会报错
    try:
        driver.find_element_by_css_selector('#J_bottomPage > span.p-num > a.pn-next').click()
    except:
        break
    time.sleep(2)
# 最后一页
# driver.find_element_by_css_selector('#J_bottomPage > span.p-num > a.pn-next.disabled')
driver.quit()