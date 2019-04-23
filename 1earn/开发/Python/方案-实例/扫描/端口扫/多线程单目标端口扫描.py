import requests
import threading
import socket
import time


ip = input('Please Start IP:(default:127.0.0.1)')
if ip == '':
    ip = '127.0.0.1'
curPort = 1
maxPort = 65535
lock = threading.Lock()

def thread():
    global lock
    global curPort
    global maxPort
    global ip

    lock.acquire()
    myPort = curPort
    curPort = curPort + 1
    lock.release()

    #print('Now Scaning %s:%d' % (ip, myPort))
    try:
        sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sk.settimeout(1)
        sk.connect((ip, myPort))
        sk.settimeout(None)
        print('Server %s Port %d Open OK!' % (ip, myPort))
        sk.close()

        # 结果保存在文件中
        f = open("IP_Port_%s.txt" % ip, 'a')
        f.write(ip + ':' + str(myPort) + '\n')
        f.close()

    except Exception:
        a = 1

threadNum = 500
value=131
b=1

while b<131:
    print(1+(500*(b-1)), "~",500*(b))
    threadlist = []
    for i in range(threadNum):
        threadlist.append(threading.Thread(target=thread))

    for i in threadlist:
        i.start()
    for i in threadlist:
        i.join()

    time.sleep(1.5)
    b=b+1



