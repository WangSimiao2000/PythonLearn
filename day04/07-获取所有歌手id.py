"""
网易云
    1. 下载全部歌手的全部音乐
    2. 分析几个歌手的页面布局及歌曲的布局
    3. 先进行单个歌手的音乐下载
    4. 再进行多个歌手的音乐下载
"""

import requests
from bs4 import BeautifulSoup

# 歌手分类链接

catalog = "1001"
# sort_id = '65'
for sort_id in range(65, 90):
    url = "https://music.163.com/discover/artist/cat?id={}&initial={}".format(catalog, sort_id)
    # print(url)
    # 请求头
    hd = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/96.0.4664.45 Safari/537.36 "
    }
    # 构造请求
    res = requests.get(url, headers=hd)
    soup = BeautifulSoup(res.text, 'html.parser')
    li_list = soup.find('div', attrs={"class": "m-sgerlist"}).find_all('li')
    for li in li_list:
        # 根据标签来 标签.标签名 soup.title
        a_tab = li.a
        title = a_tab.attrs['title'].replace('的音乐','')
        # 歌手的id
        ids = a_tab.attrs['href'].split('=')[-1]
        print(title, ids)
    break
