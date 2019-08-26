import re

"""
findall()方法：
此方法是在整个字符串中匹配指定字符或者字符串，并且将所有满足条件的结果返回到一个列表中，如下：
"""
s1="abac"
print(re.findall('a',s1))
print(re.findall('ab',s1))


print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")


"""
search()方法：
此方法是在整个字符串中查找满足匹配条件的字符或者字符串，一旦找到一个就不再继续查找，并返回包含查找值的对象，可以用.group()方法进行查看，如下：
"""

s2="abac"
print((re.search('a',s2)).group())


print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")


"""
match()方法：
此方法是用来从开头位置查找是否满足匹配条件，如果没有就会返回None，如果有，则会返回一个包含查找值的对象，可以用group()方法进行查看，如下：
"""

s3="abac"
print((re.match('a',s3)).group())
print(re.match('b',s3))


print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")


"""
split()方法：
此方法用来对一个字符串进行切分，如下：
"""

s4="abac"
print(re.split('[ab]',s4))              # 先按'a'分割得到''和'bcd',在对''和'bcd'分别按'b'分割


print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")


"""
sub()以及subn()方法：
"""

print(re.sub('\d', '*', 'a1b2c3'))      #将数字替换成'*'，默认替换所有的数字
print(re.sub('\d', '*', 'a1b2c3', 1))   #将数字替换成'*'，参数1表示只替换1个
print(re.subn('\d', '*', 'a1b2c3'))     #将数字替换成'*'，返回一个元祖(替换后的字符串,替换的次数)


print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")


"""
compile()方法：
此方法是先把正则表达式编译好，以方便多次使用，如下：
"""

s5="abc123eeee"
obj = re.compile('\d{3}')               #将正则表达式编译成为一个 正则表达式对象，规则要匹配的是3个数字
print((obj.search(s5)).group())         #正则表达式对象调用 search，参数为待匹配的字符串


print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")


"""
finditer()方法：
此方法与findall类似，只不过返回的不是一个列表，而是一个生产器，可以用next(iter).group()来查看里面的值，如下：
"""

s6="ds3sy4784a"
ret = re.finditer('\d', s6)   #finditer 返回一个存放匹配结果的迭代器
print(ret)                              # <callable_iterator object at 0x10195f940>
print(next(ret).group())                #查看第一个结果
print(next(ret).group())                #查看第二个结果
print([i.group() for i in ret])         #查看剩余的左右结果


