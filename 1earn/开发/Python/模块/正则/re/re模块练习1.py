import re

str1 = "abc \\ 123 456 Myh0St"
print (re.findall("\\\\",str1))
print (re.findall(r"\d\Z",str1))
print (re.findall("[0-4]",str1))
print (re.findall("[a-z]",str1))


print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")


s = "aaa1 22 gg 333 ccc 4444 pppp 55555 666"
print (re.findall(r"\b\d{3}\b",s))
print (re.findall(r"\b\d{2,4}\b",s))


print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")


s2 = "aaa111aaa , bbb222 , 333ccc"
#print (re.findall(r"(?<=[a-z]+)\d+(?=[a-z]+)",s2 ))
print (re.findall(r"\d+(?=[a-z]+)",s2 ))    #‘(?=…)’后向界定    :括号中的’…’代表你希望匹配的字符串后面应该出现的字符串
print (re.findall(r"\d+(?!\w+)",s2))        #‘(?!...)’后向非界定  :只有当你希望的字符串后面不跟着’…’内容时才匹配。
print (re.findall(r"[a-z]+(\d+)[a-z]+",s2)) # 只返回()里面的


print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")


s3 = 'aaa111aaa,bbb222,333ccc,444ddd444,555eee666,fff777ggg,hhh888hhh'
print (re.findall(r"([a-z]+)\d+[a-z]+",s3))
print (re.findall(r"([a-z]+)\d+([a-z]+)",s3))
print (re.findall(r"([a-z]+)(\d+)([a-z]+)",s3))

#‘(?P<name>…)’ 命名组
print (re.findall(r"(?P<g1>[a-z]+)\d+(?P=g1)",s3))#找出被中间夹有数字的前后同样的字母
print (re.findall(r"([a-z]+)\d+\1",s3)) #‘\number’通过序号调用已匹配的组正则式中的每个组都有一个序号，序号是按组


print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")


s4 = "111aaa222aaa111,333bbb444bb33"
print (re.findall( r"(\d+)", s4 ))
print (re.findall( r"(\d+)([a-z]+)", s4 ))
print (re.findall( r"(\d+)([a-z]+)(\d+)", s4 ))
print (re.findall( r"(\d+)([a-z]+)(\d+)(\2)(\1)", s4 )) #数字、字母、数字、字母、数字相对称

print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

#compile( rule [,flag] ) 使用compile加速
s5 = "111,222,aaa,bbb,ccc333,444ddd"
print (re.compile(r"\d+\b").findall(s5)) #‘\b’  只用以匹配单词的词首和词尾。单词被定义为一个字母数字序列，因此词尾就

s6 = "123 456\n789 012\n345 678"
print (re.compile(r"^\d+",re.M).findall(s6)) # 匹配位于(M/多行)开头的数字
print (re.compile(r"\d+$",re.M).findall(s6)) #

