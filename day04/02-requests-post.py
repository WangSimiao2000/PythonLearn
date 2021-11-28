"""
post请求：我们需要提交数据表单的方法
"""
import requests
"""
通过代码获取cookie
并且获取书架信息
"""
# 请求的url
url = "https://passport.17k.com/ck/user/login"
hd = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/73.0.3683.75 Safari/537.36 "
}
formdata = {
    "loginName": "18280297960",
    "password": "youarehappy123"

}
"""
post参数：
url：请求的链接地址
data：请求需要提交的表单数据（字典类型）
header：请求头
"""
response = requests.post(url, data=formdata, headers=hd)
# 获取cookie
res_headers = response.headers  # 获取响应头的头部信息
set_cookie = res_headers['Set-Cookie']
cookie_split = set_cookie.split(';')
accessToken = ''
for i in cookie_split:
    if 'accessToken' in i:
        accessToken = i.split(',')[-1].strip()

# 书架请求连接
books_url = "https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919"
hd2 = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/73.0.3683.75 Safari/537.36",
    "cookie": accessToken
}
books_response = requests.get(books_url, headers=hd2)
books = books_response.json()
books_list = books['data']
for i in books_list:
    print(i['bookName'])
