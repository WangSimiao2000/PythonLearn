"""
北京新发地：
一个动态页面
请求方式post
请求参数：
limit：默认20 展示的数据数量
current：页数
"""
import requests
import csv

file = open('蔬菜大全.csv', 'w', encoding='utf-8-sig', newline='')
csv_file = csv.writer(file)
csv_file.writerow(['菜品名称', '最低价', '最高价', '平均价', '产地', '单位', '发布时间'])
url = "http://www.xinfadi.com.cn/getCat.html"
hd = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/73.0.3683.75 Safari/537.36 "
}
for i in range(1, 10):  # 1-9
    print('当前爬取页面第{}页'.format(i))
    limit = ''
    current = ''
    if i == 1:
        pass
    else:
        limit = 20
        current = i
    data = {
        "limit": limit,
        "current": current,
        "pubDateStartTime": '',
        "pubDateEndTime": '',
        "prodPcatid": '',
        "prodCatid": '',
        "prodName": ""
    }
    res = requests.post(url, data=data, headers=hd)
    res_data = res.json()
    res_list = res_data['list']
    for i in res_list:
        prodName = i['prodName']
        lowPrice = i['lowPrice']
        highPrice = i['highPrice']
        avgPrice = i['avgPrice']
        place = i['place']
        unitInfo = i['unitInfo']
        pubDate = i['pubDate']
        r = [prodName, lowPrice, highPrice, avgPrice, place, unitInfo, pubDate]
        csv_file.writerow(r)
