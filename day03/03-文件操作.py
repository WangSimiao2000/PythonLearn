"""
    open('文件名称'，'操作符')
    文件名
        .txt
        .mp3
        .jpg
        .png
        .mp4
        .flv

        相对路径
            根据当前这个文件
            当前目录下：./
            当前文件的上一级：../
            当前文件的上两级：../../
        绝对路径
            从根目录进行寻找
    操作符
        r(read):读取文件
        w(write):先清空再写入
        a(append):追加写入
        rb:二进制读取文件
        wb:二进制先清空再写入
        ab:二进制追加写入

"""

# File = open("./test.txt", 'w')
# File.write('hello world')
# File.close()

# file_read = open('test.txt', 'r')
# print(file_read.read())

# with
# with open('test.txt', 'w') as f:
#     f.write()

import requests
url = ""
hd = {
    "user-agent": ""
}
response = requests.get()