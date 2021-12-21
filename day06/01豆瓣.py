"""
豆瓣影评

"""
from selenium import webdriver
import time
from bs4 import BeautifulSoup
import csv

#写入csv文件
with open('豆瓣影评.csv', 'w', encoding='utf-8-sig' , newline='') as f:
    csv_file = csv.writer(f)
    csv_file.writerow(['评语', '评分','时间'])

    driver = webdriver.Chrome()
    driver.get('https://movie.douban.com/subject/1292052/comments?limit=20&status=P&sort=new_score')

    num = 0
    while True:
        time.sleep(1)
        # 获取源码，利用bs4来进行解析
        html = driver.page_source
        #创建soup对象
        soup = BeautifulSoup(html, 'html.parser') # html5lib, lxml,

        #找寻comments下面的div内容
        commentItems = soup.find_all('div', attrs={"class":"comment-item"})
        for i in commentItems:

            commentInfos = i.find('span',attrs={"class":"comment-info"}).find_all('span')
            #评分标签
            star = commentInfos[1]['title'].strip()
            # 评分时间
            star_data = commentInfos[-1].text.strip()
            #评论
            comment = i.find('span',attrs={"class":"short"}).text
            csv_file.writerow([comment, star, star_data])

        #点击下一页
        driver.find_element_by_css_selector('#paginator > a').click()
        num += 1
        if num == 10:
            break
    driver.quit()