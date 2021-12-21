

"""

根据标签截图 验证码
"""
import time
from  selenium import webdriver


driver = webdriver.Chrome()

driver.get('http://pt.1000phone.com/userLogin')
time.sleep(2)

# 先定位标签
tag_img = driver.find_element_by_css_selector('#app > div.bg.loginForSchool > div.content > div > form > div.el-form-item.authCode > div > img')
# 进行标签截图
tag_img.screenshot('验证码.png')

driver.quit()