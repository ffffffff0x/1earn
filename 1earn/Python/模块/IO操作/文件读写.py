
f = open('test.txt', 'w')
f.write('hello world')
f.close()

f = open('test.txt', 'r')
print(f.read())
f.close()

#二进制文件
#前面讲的默认都是读取文本文件，并且是UTF-8编码的文本文件。要读取二进制文件，比如图片、视频等等，用'rb'模式打开文件即可：
f = open('a.png', 'rb')
print(f.read())
f.close()

