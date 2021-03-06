"""
爬虫基础
    什么是爬虫
        是一种按照一定的规则,自动地抓取万维网信息的程序或脚本
    爬虫的分类
        通用网络爬虫
            根据一个种子url链接,扩展至整个web页面
            百度,必应,谷歌,360
        聚焦网络爬虫(主题)
            有目的的进行爬取
        增量式网络爬虫
            是指对已经下载的网站采取增量式更新和只爬行新产生的货已经发生变化的网页的爬虫
        深度式网络爬虫
            需要提交表单信息的,或需要传递一些参数,才可以访问数据

    爬虫的原理

    数据的分类
        用户产生的数据,微信数据,抖音
        政府的数据
        公司管理的数据
        自己爬的数据

    数据能干什么
        人工智能,机器学习,数据分析
        卖

    robots协议
        网站和爬虫协商的协议,网站中的某些站点不允许爬虫的访问

    反爬措施
        手机验证码
        IP封禁 代理
        文字混淆
        验证码:
            静态验证码
                图片验证
                文字验证
            动态验证码
        js加密
        点击验证
        滑块严重
        cookie 身份验证
        滑动轨迹
        防盗链 refer host

    解决反爬需要掌握哪些
        js, java, 安卓, 逆向, opencv, 机器学习

    http
        超文本传输协议,请求和应答
        特点
            无状态, 无保存
        端口:
            80
    https
        在http中,增加了一个ssl安全层
        特点
            有状态, 有保存
        端口:
            443

    url 的组成
        统一资源定位符
        https://baike.baidu.com/item/URL%E6%A0%BC%E5%BC%8F/10056474?fr=aladdin
        https://www.baidu.com/s?wd=url
        协议: https
        域名: baike.baidu.com
        端口: 443 (被隐藏了)
        查询路径: /item/URL
        查询参数: ?wd=url
        锚点:
            1. 网页中当前页面进行锚点定位
            2. 作用在网址的导航

    静态数据和动态数据
        静态数据: 爬取的数据,在html源码中,并且这个页面是静态页面
        动态数据: 通过一定的条件触发的,二次加载的数据

    google

"""