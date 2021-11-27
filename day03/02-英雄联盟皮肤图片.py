"""
1. requests
    网络请求库
    urllib

    第三方模块需要安装    pip install requests
    相关报错:
        timeout
    更改pip安装源
        pip install -i https://pypi.tuna.tsinghua.edu.cn/simple requests

    找寻user-agent
        打开浏览器,右键检查,点击那天work,刷新网页,在下列请求中,点击一项,看右边的headers,找到request header里的user-agent

    2. 状态码
        100-199: 用于指定客户端应和应的某些动作。
        200-299: 用于表示请求成功
        300-399: 用于已经移动的文件并且常被包含在定位头信总中指定新的地址信总
        400-499: 用于指出客户端的错误
        500-599: 用于指出服务器借误
"""

import requests

# 指定请求链接
url = "https://101.qq.com/#/hero-detail?heroid=1&tab=skin&hero2_id=14"
# 请求头部信息
hd = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/96.0.4664.45 Safari/537.36 "
}
# 构造请求
response = requests.get(url, headers=hd)
print(response)
# 查看状态码
print(response.status_code)
# 查看头部信息
print(response.headers)
# 查看源码html代码
# print(response.text)
# 图片,音视频
print(response.content)
# 查看json()
# print(response.json())

with open('黑暗之女.png', 'wb')as f:
    f.write(response.content)
