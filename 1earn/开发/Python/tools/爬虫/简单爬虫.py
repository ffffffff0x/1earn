# -- coding: utf-8 --
import requests
import re
import os

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
url = ("https://www.anquanke.com/post/id/")
Number= int(input("[+]请你输入开始ID："))
print('================================开始检测网页================================')

aaaa=1
while aaaa:
    f = open('存在网页的地址.txt', 'a+')  # 写入一个文件
    Number += 1
    requrl= (url+"{}".format(str(Number)))
    response = requests.get(url=requrl,headers=headers)



    #print(response.text)
    #result=re.findall('title: ".*"", // 分享标题',response.text,re.DOTALL)
    #print(result)



    if response.status_code == 404:
        print("[+]当前请求链接:"+requrl+"   存在不网页   ",+response.status_code, )
        pass
    if response.status_code == 500:
        print("[+]当前请求链接:"+requrl+"   存在不网页   ",+response.status_code, )
        pass
    else:
        f.write("当前请求链接:"+requrl+"\n")
        print("[+]当前请求链接:"+requrl+"   存在网页     ",+response.status_code, )
        f.close()

