import requests
import time
import os


# 下载
def save_file(content, filename, heroName):
    with open('./img/{}/{}.jpg'.format(heroName, filename), 'wb') as f:
        f.write(content)
        print('{}皮肤下载成功!'.format(filename))


# 获取单个英雄
def getSkins(ids):
    url = "https://game.gtimg.cn/images/lol/act/img/js/hero/{}.js?ts=2730003".format(ids)

    hd = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/96.0.4664.45 Mobile Safari/537.36 '
    }

    res = requests.get(url, hd)
    data = res.json()

    skins = data['skins']
    hero = data['hero']
    heroName = hero['name']

    # 创建英雄文件夹
    path = './img/{}'.format(heroName)
    if not os.path.exists(path):
        os.makedirs(path)

    # 下载英雄所有皮肤
    for skin in skins:
        mainImg = skin['mainImg']
        name = skin['name']
        if mainImg:
            print(mainImg)
            res_img = requests.get(mainImg, headers=hd)
            save_file(res_img.content, name, heroName)


# 得到所有英雄ID
def getHeroIds():
    url = "https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js?ts=2730005"
    hd = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/96.0.4664.45 Mobile Safari/537.36 '
    }
    res = requests.get(url, hd)
    data = res.json()
    hero_list = data['hero']
    for hero in hero_list:
        heroId = hero['heroId']
        heroName = hero['name']
        print('=============当前正在访问', heroName, '=============')
        getSkins(heroId)
        time.sleep(1)


getHeroIds()
