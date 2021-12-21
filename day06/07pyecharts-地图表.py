

from pyecharts import options as opts
from pyecharts.charts import Map
from pyecharts.faker import Faker #伪造数据

data = [['绵阳市',33],['德阳市',22],['成都市',99], ['达州市',66],['南充市',120],['宜宾市',77],['广元市',88]]

c = (
    Map()
    .add("四川省示意图", data, "四川")
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="Map-四川地图示例"
        ),
        #视觉映射
        visualmap_opts=opts.VisualMapOpts(
            is_show=True,
            range_color=[
                '#90EE90',
                '#98FB98',
                '#32CD32',
            ]
        )



    )
    .render("07map_base.html")
)