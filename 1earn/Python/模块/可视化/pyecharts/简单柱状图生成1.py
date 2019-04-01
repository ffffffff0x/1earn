from pyecharts import Bar

bar = Bar("test11111", "test22222")
attr = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
v1 = [2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3]
v2 = [2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3]
v3 = [3.6, 6.9, 1.0, 126.4, 128.7, 70.7, 375.6, 122.2, 48.7, 18.8, 11.0, 12.3]

bar.add("precipitation", attr, v1, mark_line=["average"], mark_point=["max", "min"],
        is_more_utils=True)
bar.add("test2", attr, v2, mark_line=["average"])
bar.add("test", attr, v3,  mark_point=["max", "min"])
bar.render()    # 生成一个html文件


