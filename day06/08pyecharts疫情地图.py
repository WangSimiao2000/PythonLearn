"""

疫情接口
    https://lab.isaaclin.cn/nCoV/api/area
"""

import requests
import json

# url = "https://lab.isaaclin.cn/nCoV/api/area"
# res = requests.get(url)
#读取本地json文件
f = open('yiqing.json', 'r', encoding='utf-8')
res = f.read()
# 将json字符串转化成字典
data = json.loads(res)
print(data)
results = data['results']
map_data = []
for i in results:
    # print(i)
    provinceShortName = i['provinceShortName']# 省名称
    confirmedCount = i['confirmedCount'] #累计确诊
    map_data.append( [ provinceShortName, confirmedCount ] )

print(map_data)


from pyecharts.charts import Map
from pyecharts import options as opts
c = (
    Map()
    .add("全国疫情累计确诊", map_data, "china")
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="Map-四川地图示例"
        ),
        #视觉映射
        visualmap_opts=opts.VisualMapOpts(
            is_show=True,
            range_color=[
                '#32CD32',
                '#FFA500',
                '#FF8C00',
                'red'
            ],
            #最小值
            min_=0,
            #最大值
            max_=10000
        )



    )
    .render("08疫情可视化.html")
)

