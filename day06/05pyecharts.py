"""
安装
    pip install pyecharts
"""

from pyecharts.charts import Bar
from pyecharts.globals import ThemeType #主题配置
from pyecharts import options as opts

# 创建对象
# bar = Bar()
# bar.add_xaxis( ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"] )
# bar.add_yaxis("淘宝商品", [5, 20, 36, 10, 75, 90] )
# # render 会生成本地 HTML 文件，默认会在当前目录生成 render.html 文件
# # 也可以传入路径参数，如 bar.render("mycharts.html")
# bar.render('淘宝商品展示柱状图.html')


bar = (
    Bar(
        # init_opts=opts.InitOpts(theme=ThemeType.DARK)
        init_opts=opts.InitOpts(theme='dark')
    )
    .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
    .add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
    .render()
)