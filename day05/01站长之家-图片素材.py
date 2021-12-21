
"""
1、起始链接： https://sc.chinaz.com/tupian/
2、获取所有的分类链接
3、遍历请求分类链接， 获取下面的子页面
4、子页面中 获取真实的图片链接
5、下载图片
"""
import requests
from bs4 import BeautifulSoup
import time

class ZhanZhangImg():
    def __init__(self):
        # 初始化方法
        # 需要在调用 这个类的时候，直接生成一些属性，可以进行调用
        # base_url 初始的请求链接
        self.base_url = "https://sc.chinaz.com/tupian/"
        # 请求头
        self.headers = {
            "user-agent":"Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.41"
        }
        # 最终保存的图片名称和图片链接
        self.tagPage_content = {}

    def requests_get(self, url, headers):
        # 定义请求的功能，请求完之后直接返回响应对象
        return requests.get(url, headers=headers)

    def home_parser(self,html):
        #这个方法功能主要是解析图片首页的标签定位，获取所有的标签链接，然后返回
        # html：这个页面的源码
        href_list = []
        #创建BeautifulSoup对象
        soup = BeautifulSoup(html, 'html.parser')
        # 根据分析定位div中的feilei_a 返回所有div是列表类型
        feilei_list = soup.find_all('div', attrs={"class":"feilei_a"})
        for feilei in feilei_list:
            # 通过feilei这个标签，获取里面的所有a标签
            a_all = feilei.find_all('a')
            for a in a_all:
                #每一个a标签里面有href属性 和title属性，还有文本内容
                #提取href属性
                href = 'https://sc.chinaz.com' + a['href']
                # 提取文本内容
                # title = a.string
                # print(href, title)
                href_list.append(href)
        return href_list



    def set_encoding(self, obj):
        # 设置编码方式，不在将中文转成 乱码了
        obj.encoding = 'utf-8'
        return obj

    def tagPage_parser(self, html):
        # 每个图片分类下的页面解析, 需要定位提取每个小图的链接，在进行处理

        soup = BeautifulSoup(html, 'html.parser')
        img_all = soup.find('div', attrs={'id':"container"}).find_all('img')
        for img in img_all:
            #获取图片的链接
            src2 = img.get('src2')
            # 获取图片的名称
            # img_name = img['alt']
            img_name = img.get('alt')
            #使用这个方法，img_name如果有内容那就是链接
            #如果img_name没有内容，那么get方法返回的就是一个None
            if img_name and src2:
                # print(img_name, src2)
                # 获取到图片链接之后，做进一步链接处理，得到大图的链接
                # //scpic2.chinaz.net/Files/pic/pic9/202112/apic36931_s.jpg
                href = 'https:' + src2.replace('scpic2', 'scpic').replace('_s','')
                # print( img_name, href, '     ', src2)
                # img_name: 这个字典的key
                # href ：等于这个字典的value
                self.tagPage_content[img_name] = href

    def save_imgFile(self, obj, filename):
        # 传入一个对象obj，保存图片
        # obj： 请求图片链接返回的对象
        # filename : 保存的图片名称
        with open('./img/{}.png'.format(filename), 'wb') as file:
            # content :获取响应对象中的二进制内容
            file.write( obj.content )

    def run(self):
        #启动方法
        # 第一步：直接请求图片首页
        # self.headers['cookie'] = '这是添加cookie值'  这一行是演示添加请求头属性，没有具体意义
        res = self.requests_get(self.base_url, self.headers)
        res = self.set_encoding(res)  # 设置它的编码方式
        # res.encoding = 'utf-8' #简便方式
        # 第二步：将首页返回的对象源码进行解析提取， 提取图片的分类
        home_href_list = self.home_parser(res.text) #返回所有的图片标签链接
        # 遍历获取的标签链接进行请求
        for href in home_href_list:
            #请求标签链接，返回标签响应对象
            tag_res = self.requests_get(href, self.headers)
            tag_res = self.set_encoding(tag_res)
            self.tagPage_parser(tag_res.text)
            # time.sleep(1)
            break  # 这个限制是为了更好演示爬取效果，

        # tagPage_content :包含了 图片名称、图片的链接
        # self.tagPage_content ： 是保存的字典
        # items 方法返回的格式是：  [ (key, value ), (), () ...]
        for key,value in self.tagPage_content.items():
            # value:图片的链接
            # key： 图片的名称
            # print('当前这个value值是： ', value)
            img_res = self.requests_get(value, self.headers)
            self.save_imgFile(img_res, key)


zz = ZhanZhangImg()
zz.run()