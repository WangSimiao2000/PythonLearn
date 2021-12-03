import re

import requests
from bs4 import BeautifulSoup


def get_song(singer_id):
    song_url = "https://music.163.com/artist?id={}".format(singer_id)

    # 请求头
    hd = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/96.0.4664.45 Safari/537.36 "
    }

    # 构造请求
    res = requests.get(song_url, headers=hd)
    html = res.text

    soup = BeautifulSoup(html, 'html.parser')
    ul_hide = soup.find('ul', attrs={"class": "f-hide"})
    # print(ul_hide)
    a_all = ul_hide.find_all('a')
    for a in a_all:
        # print(a)
        # 提取歌曲名
        name = a.string
        href = a.attrs['href']
        # 提取歌曲id
        ids = href.split('=')[-1]
        url = "https://music.163.com/song/media/outer/url?id=" + ids
        song_res = requests.get(url, headers=hd)
        # 处理特殊字符
        name = re.sub(r'[/\\:*?<>|\'\"]', '', name)
        with open('./music/{}.mp3'.format(name), 'wb') as f:
            f.write(song_res.content)
        # print(name, url)
        print(name + "   下载成功")
        print('=' * 200)


def get_singer_id():
    fenlei = "1001"

    hd = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"
    }
    for sort_id in range(65, 91):
        url = "https://music.163.com/discover/artist/cat?id={}&initial={}".format(fenlei, sort_id)
        res = requests.get(url, headers=hd)
        soup = BeautifulSoup(res.text, 'html.parser')
        div = soup.find('div', attrs={"class": "m-sgerlist"})
        li_all = div.find_all('li')
        for li in li_all:
            # 根据标签来  标签.标签名  soup.title
            a_tab = li.a
            title = a_tab.attrs['title'].replace('的音乐', '')
            ids = a_tab.attrs['href'].split('=')[-1]
            # print(title, ids)
            get_song(ids)


get_singer_id()
