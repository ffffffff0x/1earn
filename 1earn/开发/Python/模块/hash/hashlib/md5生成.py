import hashlib
import threading

lock = threading.Lock()
curTask = 1
maxTask = 1000000

f = open('test.txt', 'w')
def thread():
    global lock
    global curTask
    global maxTask

    while 1:
        lock.acquire()  # 取任务  #这个过程不能被打断
        myTask = curTask
        curTask = curTask + 1
        lock.release()

        if myTask >= maxTask:  # 所有任务已经完成就退出
            break

        print(myTask)
        f.write(str(myTask)+"-"+hashlib.md5(str(myTask).encode(encoding='UTF-8')).hexdigest()+'\n')

# 多线程执行
threadNum = 200
threadlist = []
for i in range(threadNum):
    threadlist.append(threading.Thread(target=thread))

for i in threadlist:
    i.start()
for i in threadlist:
    i.join()

f.close()