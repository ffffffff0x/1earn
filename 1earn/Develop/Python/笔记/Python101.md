# Python101

---

## 加解密

**HASH**
```py
import hashlib

# md5, sha1, sha224, sha256, sha384, sha512
s = 'hello world'
m = hashlib.md5()
m.update(s.encode('utf8'))
print(m.digest())
print(m.hexdigest())

# ripemd160, whirlpool
s = 'hello world'
m = hashlib.new('ripemd160', s.encode('utf8'))
print(m.digest())
print(m.hexdigest())
```

**RSA gmpy2**
```py
import gmpy2

p = 168870409632549765296862502254899759857248288652407554850383477768823119986297924033151555409082356346297282197467254809081931208549224155851315637344747298357415893525472097154103238042019866682938382139834279447488738548244853184293595933654527554670457923545588565351501521501815389298997833861578226633099
q = 136505636991931352215759862754723380107419404176934963805672183755717752956589135238497377957828097441347957566489629211243389022288160648357324629288547621047463026266886900467398707294913322326802718447765393605735412855505214780439471729354761056917299208670362196028628829497574575055117449119342100056517
e = 65537

n = p * q
fn = (p - 1) * (q - 1)
d = gmpy2.invert(e, fn)

# encode
plain = "hello world"
cipher = gmpy2.powmod(int(plain.hex(),16), e, n)
print cipher

# decode
cipher = 17123126358168532314364171789745947147158203528255189528376034042576955961464108007241396193221317579386199055678187296416631757350036173529280264692509105557539380445658352098757386832691606291403716717255406122398828996166165137869000756490419628668837727171987655840934249710275220041791912411702429566338522067039808551028470065040909781794268938955092150084715883613062506445552253043511850366325327543440113474870896494812927181373067664361593089869517445577240126156141735331979758927134194252186254770372018574046630061371952143328299376196926784339615150604268752279279335534713614030849861471450015448322452
plaint = gmpy2.powmod(cipher, d, n)
s = '%x' % plaint
if len(s) % 2 != 0:
    s = '0' + s
print(s)
```

---

## 编码

**中文转十六进制**
```py
>>> '测试'.encode('utf-8')
b'\xe6\xb5\x8b\xe8\xaf\x95'
```

**字节数组与十六进制**
```py
# 字节数组
byte = b'\x01\x02\x03\x04\x05\x06\x07\x08'
byte = b'hello world'

# 十六进制
h = 0x01020304

# 字符串 -> 字节数组
s = 'hello world'
hb = s.encode('utf8')

# 字节数组 -> 字符串
hb = b'\x68\x65\x6c\x6c\x6f\x20\x77\x6f\x72\x6c\x64'
s = hb.decode('utf8')
```

**二进制格式转换**

`[0xab, 0xbc, 0xcd, 0xde] -> '\xab\xbc\xcd\xde'`
```py
s = [0xab, 0xbc, 0xcd, 0xef]
print(bytes(s))
```

`'\xde\xad\xbe\xef' -> [222, 173, 190, 239]`
```py
s = '\xde\xad\xbe\xef'
res = list(s)
# res [222, 173, 190, 239]
```

`'\xab\xbc\xcd\xde' -> 'abbccdde'`
```py
s = '\xab\xbc\xcd\xde'
res = binascii.hexlify(s)
# res = abbccdde
```

`'aabbccdd' -> '\xaa\xbb\xcc\xdd'`
```py
s = 'aabbccdd'
res = binasicc.unhexlify(s)
# res = \xaa\xbb\xcc\xdd
```

`'\xde\xad\xbe\xef' -> 0xdeadbeef`
```py
s = '\xde\xad\xbe\xef'
res = int.from_bytes(s, 'big')
# res = 0xdeadbeef
```

`0xdeadbeef -> '\xde\xad\xbe\xef'`
```py
s = 0xdeadbeef
print(int.to_bytes(s, 4, 'big'))
```

**ASCII 转 HEX**
```py
import binascii

s = b'fmcd\IRWOCEHRG[OYS[Uh'
print(binascii.b2a_hex(s))
```

```py
import codecs
codecs.encode(b"c", "hex")
```

**HEX 转 ASCII**
```py
import codecs
codecs.decode("7061756c", "hex")
```

**base64 编解码**
```py
import base64
>>> base64.b64encode(b'binary\x00string')
b'YmluYXJ5AHN0cmluZw=='
>>> base64.b64decode(b'YmluYXJ5AHN0cmluZw==')
b'binary\x00string'
```

**url safe 的 base64 编解码**
```py
>>> base64.b64encode(b'i\xb7\x1d\xfb\xef\xff')
b'abcd++//'
>>> base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff')
b'abcd--__'
>>> base64.urlsafe_b64decode('abcd--__')
b'i\xb7\x1d\xfb\xef\xff'
```

**base64 换表**
```py
import base64
str1 = "Wj1gWE9xPSGUQ0KCPCGET09WR1qSzZ=="   #str1是要解密的代码

string1 = "ZYXABCDEFGHIJKLMNOPQRSTUVWzyxabcdefghijklmnopqrstuvw0123456789+/"    #string1是改过之后的base64表
string2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

print (base64.b64decode(str1.translate(str.maketrans(string1,string2))))
```

---

## 数值转换

```py
# 字符 -> 十进制
>>> s = 'a'
>>> d = ord(s)
97

# 十进制 -> 字符
>>> d = 97
>>> s = chr(d)
'a'

# 十进制 -> 十六进制
>>> d = 123456
>>> h = hex(d)
'0x1e240'

# 十进制 -> 二进制
>>> d = 123456
>>> b = bin(d)
'0b11110001001000000'

# 十六进制 -> 十进制
>>> h = '1e240'
>>> d = int(h, 16)
123456

>>> h = 0x1e240
>>> print(h)
123456

# 十六进制 -> 二进制
>>> h = 0x1e240
>>> b = bin(h)
'0b11110001001000000'

# 二进制 -> 十进制
>>> b = '11110001001000000'
>>> d = int(b, 2)
123456

>>> b = 0b11110001001000000
>>> print(b)
123456

# 二进制 -> 十六进制
>>> b = 0b11110001001000000
>>> h = hex(b)
'0x1e240'
```

---

## 字符串转换

```py
# 字符串 -> 十六进制字符串
# Python2
>>> s = "hello world"
>>> hs = s.encode('hex')
'68656c6c6f20776f726c64'

# Python3
>>> s = 'hello world'.encode('utf8')
>>> hs = s.hex()
'68656c6c6f20776f726c64'
>>> hs = binascii.hexlify(s)
b'68656c6c6f20776f726c64'

# 字符串 -> 十进制字符串
>>> s = "hello world"
>>> ds = ' '.join(['{:d}'.format(ord(c)) for c in s])
'104 101 108 108 111 32 119 111 114 108 100'

# 字符串 -> 二进制字符串
>>> s = "hello world"
bs = ' '.join(['{0:08b}'.format(ord(c)) for c in s])
'01101000 01100101 01101100 01101100 01101111 00100000 01110111 01101111 01110010 01101100 01100100'

# 十六进制字符串 -> 字符串
# Python2
>>> hs = '68656c6c6f20776f726c64'
>>> s = hs.decode('hex')
'hello world'
# Python3
>>> hs = '68656c6c6f20776f726c64'
>>> s = bytes.fromhex(hs)
b'hello world'

# 十六进制字符串 -> 十进制字符串
# Python2
>>> hs = '68656c6c6f20776f726c64'
>>> ds = ' '.join(['%d' % int(hs[x*2:x*2+2], 16) for x in range(len(hs)/2)])
'104 101 108 108 111 32 119 111 114 108 100'
# Python3
>>> hs = '68656c6c6f20776f726c64'
>>> ds = ' '.join(['%d' % int(hs[x*2:x*2+2], 16) for x in range(math.floor(len(hs)/2))])
'104 101 108 108 111 32 119 111 114 108 100'

>>> hs = '68 65 6c 6c 6f 20 77 6f 72 6c 64'
>>> ds = ' '.join(['%d' % int(x, 16) for x in hs.split(' ')])
'104 101 108 108 111 32 119 111 114 108 100'

# 十六进制字符串 -> 二进制字符串
# Python2
>>> hs = '68656c6c6f20776f726c64'
>>> bs = ' '.join(['{0:08b}'.format(int(hs[x*2:x*2+2], 16)) for x in range(len(hs)/2)])
'01101000 01100101 01101100 01101100 01101111 00100000 01110111 01101111 01110010 01101100 01100100'
# Python3
>>> hs = '68656c6c6f20776f726c64'
>>> bs = ' '.join(['{0:08b}'.format(int(hs[x*2:x*2+2], 16)) for x in range(math.floor(len(hs)/2))])
'01101000 01100101 01101100 01101100 01101111 00100000 01110111 01101111 01110010 01101100 01100100'

>>> hs = '68 65 6c 6c 6f 20 77 6f 72 6c 64'
>>> bs = ' '.join(['{0:08b}'.format(int(x, 16)) for x in hs.split(' ')])
'01101000 01100101 01101100 01101100 01101111 00100000 01110111 01101111 01110010 01101100 01100100'

# 十进制字符串 -> 字符串
>>> ds = '104 101 108 108 111 32 119 111 114 108 100'
>>> s = ''.join([chr(int(x)) for x in ds.split(' ')])
'hello world'

# 十进制字符串 -> 十六进制字符串
>>> ds = '104 101 108 108 111 32 119 111 114 108 100'
>>> hs = ''.join(['%02x' % int(x) for x in ds.split(' ')])
'68656c6c6f20776f726c64'

# 十进制字符串 -> 二进制字符串
>>> ds = '104 101 108 108 111 32 119 111 114 108 100'
>>> hs = ' '.join(['{0:08b}'.format(int(x)) for x in ds.split(' ')])
'01101000 01100101 01101100 01101100 01101111 00100000 01110111 01101111 01110010 01101100 01100100'

# 二进制字符串 -> 字符串
>>> bs = '01101000 01100101 01101100 01101100 01101111 00100000 01110111 01101111 01110010 01101100 01100100'
>>> s = ''.join([chr(int(x, 2)) for x in bs.split(' ')])
'hello world'

# 二进制字符串 -> 十六进制字符串
>>> bs = '01101000 01100101 01101100 01101100 01101111 00100000 01110111 01101111 01110010 01101100 01100100'
>>> hs = ''.join(['%02x' % int(x, 2) for x in bs.split(' ')])
'68656c6c6f20776f726c64'

# Python2
>>> bs = '0110100001100101011011000110110001101111001000000111011101101111011100100110110001100100'
>>> hs = ''.join(['%02x' % int(bs[i*8:i*8+8], 2) for i in range(len(bs)/8)])
'68656c6c6f20776f726c64'
# Python3
>>> bs = '0110100001100101011011000110110001101111001000000111011101101111011100100110110001100100'
>>> hs = ''.join(['%02x' % int(bs[i*8:i*8+8], 2) for i in range(math.floor(len(bs)/8))])
'68656c6c6f20776f726c64'

# 二进制字符串 -> 十进制字符串
>>> bs = '01101000 01100101 01101100 01101100 01101111 00100000 01110111 01101111 01110010 01101100 01100100'
>>> ds = ' '.join(['%d' % int(x, 2) for x in bs.split(' ')])
'104 101 108 108 111 32 119 111 114 108 100'

# Python2
>>> bs = '0110100001100101011011000110110001101111001000000111011101101111011100100110110001100100'
>>> hs = ' '.join(['%d' % int(bs[i*8:i*8+8], 2) for i in range(len(bs)/8)])
'104 101 108 108 111 32 119 111 114 108 100'
# Python3
>>> bs = '0110100001100101011011000110110001101111001000000111011101101111011100100110110001100100'
>>> hs = ' '.join(['%d' % int(bs[i*8:i*8+8], 2) for i in range(math.floor(len(bs)/8))])
'104 101 108 108 111 32 119 111 114 108 100'
```

---

## 字符串处理

**每个字符减 1**
```py
string=bytearray(b"gmbh|ZPV`GJOE`JU`IBIB~")
for i in range(len(string)):
    string[i]-=1;
print(string)
```

**数组中每个字符与自身位数异或**
```py
data=[0x66,0x6D,0x63,0x64,0x7F,0x5C,0x49,0x52,0x57,0x4F,0x43,0x45,0x48,0x52,0x47,0x5B,0x4F,0x59,0x53,0x5B,0x55,0x68]
for i in range(len(data)):
    data[i]^=i
print(bytearray(data))
```

**十六进制不带 0x 补零 (ASCII 字节类型)**
```py
arr = [0x4B, 0x43, 0x09, 0xA1, 0x01, 0x02, 0xAB, 0x4A, 0x43]
def print_bytes_hex(data):
    lin = ['%02X' % i for i in data]
    print(" ".join(lin))
print_bytes_hex(arr)
```

**十六进制不带 0x 补零 (字符串类型)**
```py
arr = 'Work'
def print_string_hex(data):
    lin = ['%02X' % ord(i) for i in data]
    print(" ".join(lin))
print_string_hex(arr)
```

**字符串反转**
```py
str='test123'
print(str[::-1])
```

---

## 声音

```py
print("\a")
```

**windows**
```py
import winsound
duration = 1000     # millisecond
freq = 440          # Hz
winsound.Beep(freq, duration)
# FREQ是频率(以赫兹为单位)，而持续时间是毫秒(毫秒)。
```

**linux**
```bash
apt install speech-dispatcher
```
```py
import os
os.system('spd-say "your program has finished"')
```

```bash
apt install sox
```
```py
import os
duration = 1        # second
freq = 440          # Hz
os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (duration, freq))
```

---

## 执行系统命令

**os**
```py
import os
os.system("whoami")
```

```py
import os
nowtime = os.popen('whoami')
print(nowtime.read())
```

**commands**
```py
import commands
status, output = commands.getstatusoutput('date')
print(output)
```

---

## 延时

**sleep()**
```py
time.sleep(1)   # 延时1秒
```

---

## 时间戳

**time()**

> time() 返回当前时间的时间戳（1970纪元后经过的浮点秒数）。

```py
print(time.time())
```

---

## 输出

**python字符串去掉前缀b**

需要去掉字符串的前缀b,只需要进行utf-8的转换即可，即
```py
data = data.decode(“utf-8”).
```

---

## 安全脚本

**写 python 目录遍历 POC 时遇到的问题**
- https://mazinahmed.net/blog/testing-for-path-traversal-with-python/

---

## Docker Engine SDK

```bash
pip3 install docker
```

**运行一个容器，并执行容器中的一个命令**

```py
import docker
client = docker.from_env()
r = client.containers.run("alpine", ["echo", "hello", "world"])
print(str(r, encoding='utf-8'))
```

**列出所有镜像**

```py
import docker
client = docker.from_env()
for image in client.images.list():
  print(image.id)
```

---

## mysql

```bash
pip3 install PyMySQL
```

**连接 Mysql 的 TESTDB 数据库**
```py
#!/usr/bin/python3
import pymysql

# 打开数据库连接
db = pymysql.connect(host='localhost',
                     user='testuser',
                     password='test123',
                     database='TESTDB')

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute()  方法执行 SQL 查询
cursor.execute("SELECT VERSION()")

# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()

print ("Database version : %s " % data)

# 关闭数据库连接
db.close()
```

**创建数据库表**

```py
#!/usr/bin/python3

import pymysql

# 打开数据库连接
db = pymysql.connect(host='localhost',
                     user='testuser',
                     password='test123',
                     database='TESTDB')

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute() 方法执行 SQL，如果表存在则删除
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

# 使用预处理语句创建表
sql = """CREATE TABLE EMPLOYEE (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,
         SEX CHAR(1),
         INCOME FLOAT )"""

cursor.execute(sql)

# 关闭数据库连接
db.close()
```

---

## oss2

- https://help.aliyun.com/document_detail/32027.html

**创建examplebucket存储空间**

```py
# -*- coding: utf-8 -*-
import oss2

# 阿里云账号AccessKey拥有所有API的访问权限，风险很高。强烈建议您创建并使用RAM用户进行API访问或日常运维，请登录RAM控制台创建RAM用户。
auth = oss2.Auth('<yourAccessKeyId>', '<yourAccessKeySecret>')
# Endpoint以杭州为例，其它Region请按实际情况填写。
bucket = oss2.Bucket(auth, 'http://oss-cn-hangzhou.aliyuncs.com', '<yourBucketName>')

# 设置存储空间为私有读写权限。
bucket.create_bucket(oss2.models.BUCKET_ACL_PRIVATE)
```

**上传文件**

```py
# -*- coding: utf-8 -*-
import oss2

# 阿里云账号AccessKey拥有所有API的访问权限，风险很高。强烈建议您创建并使用RAM用户进行API访问或日常运维，请登录RAM控制台创建RAM用户。
auth = oss2.Auth('<yourAccessKeyId>', '<yourAccessKeySecret>')
# Endpoint以杭州为例，其它Region请按实际情况填写。
bucket = oss2.Bucket(auth, 'http://oss-cn-hangzhou.aliyuncs.com', '<yourBucketName>')

# 上传文件到OSS。
# <yourObjectName>由包含文件后缀，不包含Bucket名称组成的Object完整路径，例如abc/efg/123.jpg。
# <yourLocalFile>由本地文件路径加文件名包括后缀组成，例如/users/local/myfile.txt。
bucket.put_object_from_file('<yourObjectName>', '<yourLocalFile>')
```
