
"""
从网页源代码中进行找寻


安装 moviepy
    pip install moviepy
"""
import json
import requests
from bs4 import BeautifulSoup
from moviepy.editor import VideoFileClip, AudioFileClip

def down_video_audio(url,  filename,  otype):
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.41",
        "referer": "https://www.bilibili.com"
    }
    res = requests.get(url, headers=headers)
    with open('{}.{}'.format(filename, otype), 'wb') as f:
        f.write(res.content)



url = "https://www.bilibili.com/video/BV1kq4y1B7ab?spm_id_from=333.5.0.0"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.41"
}
res = requests.get(url,headers=headers)
soup = BeautifulSoup(res.text, 'html.parser')
#1、获取源码中所有的script标签
script_list = soup.find_all('script')
#2、遍历script列表
for script in script_list:
    # 创建变量
    script_text = script.text
    #如果playinfo再这个标签文本里
    if 'window.__playinfo__' in script_text:
        #使用replace将多余的字符串处理为空，最终得到json数据转化前的格式
        script_text = script_text.replace('window.__playinfo__=','')
        print(script_text)
        # 用json方法将json字符串 转化成字典
        data = json.loads(script_text)
        #   提取视频的下载链接，但是视频没有声音
        video_baseUrl = data['data']['dash']['video'][0]['baseUrl']
        #  提取音频的下载链接  但是音频没有画面
        audio_baseUrl = data['data']['dash']['audio'][0]['baseUrl']


        # 下载视频和音频到本地

        #下载视频
        down_video_audio(video_baseUrl, '视频文件', 'mp4')
        #下载音频
        down_video_audio(audio_baseUrl, '音频文件', 'mp3')

        #======================================================
        #以上两个文件都下载了之后  就开始 将音频合并到视频中
        # 需要用到 moviepy 这个模块

        #创建视频的合并对象
        videoclip = VideoFileClip('./视频文件.mp4')
        #创建音频的合并对象
        audioclip = AudioFileClip('./音频文件.mp3')

        # 将音频文件对象写入到视频对象中
        # set_audio方法进行传递
        write_res = videoclip.set_audio(audioclip)
        # 写入完之后，保存到本地
        # write_videofile 这个方法就是写入到本地
        write_res.write_videofile('合并之后的文件.mp4')

        print('合并 成功并保存到本地')

