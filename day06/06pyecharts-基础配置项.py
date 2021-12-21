from pyecharts.charts import Bar
from pyecharts import options as opts



bar = (
    Bar(
        # init_opts=opts.InitOpts(theme=ThemeType.DARK)
        init_opts=opts.InitOpts(theme='dark')
    )
    .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
    .add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
    .add_yaxis("商家B", [8, 14, 66, 81, 20, 47])
    #全局配置项
    .set_global_opts(
        # 标题配置项
        # 参数是英文加下划线的组合， 类 是驼峰写法
        title_opts=opts.TitleOpts(
            #标题
            title='我是一个主标题',
            #主标题跳转链接
            title_link='https://www.baidu.com'
        ),

        # 图例配置项
        legend_opts=opts.LegendOpts(
            #是否显示
            is_show=True
        ),

        #工具箱配置项
        toolbox_opts=opts.ToolboxOpts(
            #显示
            is_show=True
        ),

        #提示框配置项
        tooltip_opts=opts.TooltipOpts(
            #更改文字样式
            textstyle_opts=opts.TextStyleOpts(
                #文字颜色
                color='green',
                font_size=80
            ),
            # 更改提示框背景颜色
            background_color='pink'
        ),

        #视觉映射配置项
        # visualmap_opts=opts.VisualMapOpts(
        #     # 是否展示
        #     is_show=True
        # )

        #区域缩放配置
        datazoom_opts=opts.DataZoomOpts(
            is_show=True
        )
    )



    .render()
)