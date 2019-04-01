# -*- coding: utf-8 -*-
import re

"""
匹配中文
在某些情况下，我们想匹配文本中的汉字，有一点需要注意的是，中文的 unicode 编码范围 主要在 [\u4e00-\u9fa5]，
这里说主要是因为这个范围并不完整，比如没有包括全角（中文）标点，不过，在大部分情况下，应该是够用的。
假设现在想把字符串 title = u'你好，hello，世界' 中的中文提取出来，可以这么做：
"""



s1 = u'你好，hello，世界'
pattern = re.compile('[\u4e00-\u9fa5]+')
result = pattern.findall(s1)

print (result)


print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")


'''
贪婪匹配
在 Python 中，正则匹配默认是贪婪匹配（在少数语言中可能是非贪婪），也就是匹配尽可能多的字符。
比如，我们想找出字符串中的所有 div 块：
'''

s2 = 'aa<div>test1</div>bb<div>test2</div>cc'
pattern = re.compile(r'<div>.*</div>')
result = pattern.findall(s2)

print (result)


print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")


'''
由于正则匹配是贪婪匹配，也就是尽可能多的匹配，因此，在成功匹配到第一个 </div> 时，它还会向右尝试匹配，查看是否还有更长的可以成功匹配的子串。
如果我们想非贪婪匹配，可以加一个 ?，如下：
'''

s3 = 'aa<div>test1</div>bb<div>test2</div>cc'
pattern = re.compile(r'<div>.*?</div>')    # 加上 ?
result = pattern.findall(s3)

print (result)


print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")


pattern = re.compile(r'\d+')

print (pattern.match('123, 123'))
print (pattern.search('234, 234'))
print (pattern.findall('345, 345'))




