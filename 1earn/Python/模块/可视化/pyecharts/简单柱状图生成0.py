from pyecharts import Bar

bar = Bar("第一个测试", "这里是副标题")
bar.use_theme('dark')   #更换主体色系

bar.add("服装",["a","b","c","d","e","f","g","h"],[1,2,3,4,5,6,7,8],
        is_more_utils=True)
#bar.print_echarts_options() # 该行只为了打印配置项，方便调试时使用


bar.render()    # 生成本地 HTML 文件

'''
如果想直接将图片保存为 png, pdf, gif 格式的文件，可以使用 pyecharts-snapshot。使用该插件请确保你的系统上已经安装了 Nodejs 环境。
    安装 phantomjs $ npm install -g phantomjs-prebuilt
    安装 pyecharts-snapshot $ pip install pyecharts-snapshot
    调用 render 方法 bar.render(path='snapshot.png') 文件结尾可以为 svg/jpeg/png/pdf/gif。请注意，svg 文件需要你在初始化 bar 的时候设置 renderer='svg'。
'''
bar.render(path='snapshot.png')





