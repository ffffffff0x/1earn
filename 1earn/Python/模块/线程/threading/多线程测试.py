import threading

# 导入 threading 模块并且创建一个叫 doubler 的常规函数。
# 这个函数接受一个值，然后把这个值翻一番。它还会打印出调用这个函数的线程的名称，并在最后打印一行空行。
def doubler(num):
    print(threading.current_thread().getName()+'\n')
    print(num*2)
    print()

# 入口
if __name__=='__main__':
    for i in range(5):
        # 创建五个线程并且依次启动它们。
        # Args 参数看起来有些奇怪，那是因为我们需要传递一个序列给 doubler 函数
        # 但它只接受一个变量，所以我们把逗号放在尾部来创建只有一个参数的序列。
        my_thread=threading.Thread(target=doubler,args=(i,))
        my_thread.start()
