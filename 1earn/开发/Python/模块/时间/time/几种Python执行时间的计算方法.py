import time
import datetime

start = datetime.datetime.now()

for i in range(1,11):
    time.sleep(0.1)
    print(i)

end = datetime.datetime.now()

print((end-start).seconds,'秒')
#datetime.datetime.now()获取的是当前日期，在程序执行结束之后，这个方式获得的时间值为程序执行的时间。






import time

start = time.time()

for i in range(1,11):
    time.sleep(0.1)
    print(i)

end = time.time()
print(end-start,'秒')
#time.time()获取自纪元以来的当前时间（以秒为单位）。如果系统时钟提供它们，则可能存在秒的分数。所以这个地方返回的是一个浮点型类型。这里获取的也是程序的执行时间。




import time

start = time.clock()

for i in range(1,11):
    time.sleep(0.1)
    print(i)

end = time.clock()
print(end-start,'秒')
#time.clock()返回程序开始或第一次被调用clock（）以来的CPU时间。 这具有与系统记录一样多的精度。返回的也是一个浮点类型。这里获得的是CPU的执行时间。 
#注：程序执行时间=cpu时间 + io时间 + 休眠或者等待时间