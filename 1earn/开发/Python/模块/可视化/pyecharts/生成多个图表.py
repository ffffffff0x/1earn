from pyecharts import Bar,Line
from pyecharts.engine import create_default_environment

bar = Bar("多图测试", "这里是第一个图表")
bar.use_theme('dark')   
bar.add("服装",["a","b","c","d","e","f","g","h"],[1,2,3,4,5,6,7,8],
        is_more_utils=True)


line=Line("多图测试", "这里是第二个图表")
line.add("服装",["a","b","c","d","e","f","g","h"],[1,2,3,4,5,6,7,8],
        is_more_utils=True)

env = create_default_environment("html")
# 为渲染创建一个默认配置环境
# create_default_environment(filet_ype)
# file_type: 'html', 'svg', 'png', 'jpeg', 'gif' or 'pdf'

env.render_chart_to_file(bar, path='bar.html')
env.render_chart_to_file(line, path='line.html')
