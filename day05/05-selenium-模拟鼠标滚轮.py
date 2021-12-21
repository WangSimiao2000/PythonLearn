

import time
from selenium import webdriver

driver = webdriver.Chrome()


# driver.get('https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&wq=%E6%89%8B%E6%9C%BA&pvid=c0bd1a37eecc41b48751c5a1ac23386b&page=9&s=236&click=0')
# time.sleep(2)
# for i in range(10):
#     # 通过execute_script 方法 执行js代码
#     # 向下滑动 500像素的距离
#     driver.execute_script(  'window.scrollBy(0,500);'  )
#     time.sleep(0.5)









#==========================================
# 根据js代码 提取网页属性
driver.get('https://www.bilibili.com/video/BV1kq4y1B7ab?spm_id_from=333.5.0.0')
# 执行js代码，获取cid    bvid
playerinfo = driver.execute_script( 'return window.playerInfo'  )
print(playerinfo)

driver.quit()