"""

1、目标 爬取b站视频
2、通过模板url进行填充
    https://api.bilibili.com/x/player/playurl?cid=439766938&otype=json&bvid=BV1e34y1Z7nB
3、cid、 bvid

"""
import  requests
from selenium import webdriver
from bs4 import BeautifulSoup


class BSpider():
    def __init__(self):
        #初始化方法，构造模板链接
        self.tmp_url = "https://api.bilibili.com/x/player/playurl?cid={}&otype=json&bvid={}"
        self.headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.41"
        }



    def selenium_get(self, url):
        # 创建selenium对象，访问页面
        driver = webdriver.Chrome()
        driver.get(url)
        playerInfo = driver.execute_script('return window.playerInfo')
        html = driver.page_source  #获取网页源码
        driver.quit()
        return playerInfo, html

    def requests_get(self, url, headers):
        # 公共请求，
        return requests.get(url, headers=headers)

    def save_file(self, obj, filename):
        #  保存视频文件
        with open('./video/{}.mp4'.format(filename), 'wb')  as f:
            f.write( obj.content)

    def get_title(self, html):
        # 这个方法主要是获取 网页标题用于保存视频文件名称
        soup = BeautifulSoup(html, 'html.parser')
        return soup.title.string.strip()

    def run(self):
        #启动方法
        #1、第一步你要下载哪个链接的视频
        url = "https://www.bilibili.com/video/BV1e34y1Z7nB?spm_id_from=333.5.0.0"
        #2、访问获取playerInfo
        playerInfo, html = self.selenium_get(url)
        #3、拼接填充模板链接
        video_info_url = self.tmp_url.format(playerInfo['cid'], playerInfo['bvid'])
        #4、请求视频信息链接，提取里面的视频下载链接
        video_res = self.requests_get(video_info_url, self.headers)
        print(video_res.text)
        data = video_res.json()
        #5、解析获取视频下载链接
        video_down_url = data['data']['durl'][0]['url']
        #6、为了防止反爬得不到视频数据，添加referer 这个视频的来源是b站
        self.headers['referer'] = "https://www.bilibili.com"
        #7、请求视频下载链接，返回视频的对象
        down_response = self.requests_get(video_down_url, self.headers)
        #8、通过bs4获取当前页面的title标签内的文本，用于保存视频名称
        filename = self.get_title(html)
        #9、保存视频到本地
        self.save_file(down_response, filename)


bs = BSpider()
bs.run()