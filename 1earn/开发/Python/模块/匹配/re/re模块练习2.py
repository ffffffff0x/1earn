import re



'''
字符组 ： [字符组]
1 [1]                       匹配1
2 [123]　　　　　　  匹配1、2、3
3 [0-9]　　　　　　　匹配任意一个数字
4 [a-z]　　　　　　　匹配任意一个小写字母
5 [A-Z]　　　　　　　匹配任意一个大写字母
6 [A-Za-z]　　　　　 匹配任意一个字母
'''

s1="Zll5201314"
print(re.findall('[1]',s1))
print(re.findall('[123]',s1))
print(re.findall('[0-9]',s1))
print(re.findall('[a-z]',s1))
print(re.findall('[A-Z]',s1))
print(re.findall('[a-zA-Z]',s1))
print(re.findall('[A-Za-z0-3]',s1))


print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")


'''
元字符：
 1 .　　　　匹配除换行符以外的任意字符
 2 \w　　　 匹配字母或者数字或者下划线
 3 \s　　　  匹配任意空白字符
 4 \d　　　  匹配数字
 5 \n　　　  匹配换行符
 6 \t　　　　匹配制表符tab
 7 \b　　　　匹配一个单词的结尾
 8 ^　　　　匹配字符串的开始
 9 $　　　　匹配字符串的结尾
10 \W　　　匹配非字母或下划线或数字
11 \D　　　匹配非数字
12 \S　　　匹配非空白符
13 |　　　　匹配|前或者后的内容
14 ()　　　　匹配括号内的表达式，也表示一个组
'''

s2="love_u 520"
print(re.findall('.',s2))
print(re.findall('\w',s2))
print(re.findall('\s',s2))
print(re.findall('\d',s2))
print(re.findall('\n',s2))
print(re.findall('\b',s2))
print(re.findall('^l',s2))
print(re.findall('520$',s2))
print(re.findall('\W',s2))
print(re.findall('\D',s2))
print(re.findall('\S',s2))
print(re.findall('love|u',s2))


print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")


"""
量词:
1 *   重复零次或者多次 
2 +　　重复1次或者多次
3 ?　　重复零次或者一次
4 {n}　　重复n次
5 {n,}　　重复n次或者更多次
6 {n,m}　　重复n到m次
"""


s3="555 5"
print(re.findall('5*',s3))
print(re.findall('5+',s3))
print(re.findall('5?',s3))
print(re.findall('5{2,3}',s3))
print(re.findall('5{2}',s3))
print(re.findall('5{3}',s3))


print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")


"""
常见的正则表达式应用:
1 手机号（国内）：^[1-9][3478]\d{9}
2 电话号（国内）：[0-9-()（）]{7,18}
3 邮编：\d{6}
4 QQ：[1-9]([0-9]{5,11})
5 身份证号：\d{17}[\d|x]|\d{15}
6 邮箱：\w[-\w.+]*@([A-Za-z0-9][-A-Za-z0-9]+\.)+[A-Za-z]{2,14}
7 网址：^((https|http|ftp|rtsp|mms)?:\/\/)[^\s]+
8 日期：\d{4}(\-|\/|.)\d{1,2}\1\d{1,2}
9 用户名：[A-Za-z0-9_\-\u4e00-\u9fa5]+
"""

