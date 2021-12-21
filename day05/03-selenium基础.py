"""
selenium

    Selenium是一个用于Web应用程序测试的工具。Selenium测试直接运行在浏览器中，就像真正的用户在操作一样

    是python的第三方插件库

    selenium      驱动      chrome

    驱动版本： chromedriver     #  大版本和chrome版本一致 96
    chrome版本： 96.0.4664.45     大版本是 96

    驱动下载地址： https://npm.taobao.org/mirrors/chromedriver/


安装
    pip install selenium
    pip install -i https://pypi.tuna.tsinghua.edu.cn/simple selenium


导入chromedriver.exe路径方法一
# driver = webdriver.Chrome( executable_path='C:\chromedriver_win32\chromedriver.exe')
# driver = webdriver.Chrome( executable_path=r'C:\chromedriver_win32\chromedriver.exe')

#导入文件路径方法二， 直接把chromedriver.exe 放在python安装路径下的 scripts这个文件夹内就ok了
# C:\ python的安装路径下\Python37\Scripts



"""

from selenium import webdriver
import time


# 创建driver对象
driver = webdriver.Chrome()

# 设置driver 为全屏  最大化
driver.maximize_window()

# 通过driver对象访问网站
driver.get( 'https://www.baidu.com'  )

# 强制等待1秒
time.sleep(1)
# 找寻输入框
kw = driver.find_element_by_css_selector('#kw')
# 输入内容
kw.send_keys('手机')
time.sleep(1)
# 找寻百度一下按钮
su = driver.find_element_by_css_selector('#su')
# 点击百度一下
su.click()

# 让代码等下浏览器，让浏览器充分加载完毕之后再截图
time.sleep(3)


# 截图功能， 截取整个窗口图片
driver.save_screenshot('百度一下吧.png')







# 关闭浏览器的方法
# driver.close() # 关闭当前标签页
driver.quit() # 关闭整个浏览器