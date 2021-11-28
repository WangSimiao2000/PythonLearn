"""
网易云
    1. 下载全部歌手的全部音乐
    2. 分析几个歌手的页面布局及歌曲的布局
    3. 先进行单个歌手的音乐下载
    4. 再进行多个歌手的音乐下载
"""

import time
import requests
from bs4 import BeautifulSoup

# 请求的链接
song_url = "https://music.163.com/artist?id=3684"
# 请求头
hd = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/96.0.4664.45 Safari/537.36 "
}
# 构造请求
res = requests.get(song_url, headers=hd)
print(res)
html = res.text
soup = BeautifulSoup(html, 'html.parser')
# span_all = soup.find_all('span', attrs={"class":"txt"})
# for span in span_all:
#     print(span)
#     print('='*200)
ul_hide = soup.find('ul', attrs={"class": "f-hide"})
print(ul_hide)
a_all = ul_hide.find_all('a')
for a in a_all:
    # print(a)
    # 提取歌曲名
    name = a.string
    # 提取href属性
    href = a.attrs['href']
    ids = href.split('=')[-1]
    url = "https://music.163.com/song/media/outer/url?id="+ids
    print(name, url)
    # song_res = requests.get(url, headers=hd)
    # with open('{}.mp3'.format(name), 'wb')as f:
    #     f.write(song_res.content)
    # time.sleep(3)
    print('='*200)
