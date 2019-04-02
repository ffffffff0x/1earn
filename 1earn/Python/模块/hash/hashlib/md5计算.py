import hashlib


#MD5计算
m = hashlib.md5()
#传入arg对象来更新hash的对象。必须注意的是，该方法只接受byte类型，否则会报错。这就是要在参数前添加b 来转换类型的原因
#同时要注意，重复调用update(arg)方法，是会将传入的arg参数进行拼接，而不是覆盖。必须注意这一点，因为你在不熟悉update()原理的时候，你很可能就会被它坑了。
m.update(b'123')
print(m.hexdigest())

#看下面例子
'''
>>> m = hashlib.md5()
>>> m.update(b'123')
>>> m.hexdigest()
'202cb962ac59075b964b07152d234b70'
>>> m.update(b'456')
>>> m.hexdigest()
'e10adc3949ba59abbe56e057f20f883e'

>>> hashlib.md5(b'123456').hexdigest()
'e10adc3949ba59abbe56e057f20f883e'
'''


#中文加密
'''此处先将数据转换成UTF-8格式的，使用网上工具对比下加密的结果，发现有的md5加密工具并不是使用UTF-8格式加密的。 
经测试目前发现可以转为UTF-8、GBK、GB2312、GB18030，不分大小写(因为GBK/GB2312/GB18030均是针对汉字的编码，所以md5加密后结果一样)。
'''
d='测试'
print(hashlib.md5(d.encode(encoding='UTF-8')).hexdigest())
print(hashlib.md5(d.encode(encoding='GBK')).hexdigest())
print(hashlib.md5(d.encode(encoding='GB2312')).hexdigest())
print(hashlib.md5(d.encode(encoding='GB18030')).hexdigest())

#hashlib.algorithms_guaranteed 是在所有平台上，保证被hashlib模块支持的hash算法名称的集合；
#hashlib.algorithms_available 当前运行的python编译器可用的hash算法名称的集合

#hashlib.algorithms_guaranteed 是 hashlib.algorithms_available的子集。
print(hashlib.algorithms_guaranteed)
print(hashlib.algorithms_available)

#同理sha256格式一样
print(hashlib.sha256(d.encode(encoding='UTF-8')).hexdigest())