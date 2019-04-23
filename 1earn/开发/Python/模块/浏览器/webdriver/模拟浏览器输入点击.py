import requests
import re
from selenium import webdriver



dirver=webdriver.Chrome("C:\\Users\\sfjm7\\Desktop\\chromedriver_win32\\chromedriver.exe")#指定chrome驱动
dirver.get("http://lab1.xseclab.com/xss2_0d557e6d2a4ac08b749b61473a075be1/index.php")
res=dirver.page_source

num=re.findall('(.*?)=<input type="text" name="v"',res)
result=eval(num[0].strip())

dirver.find_element_by_xpath("html/body/form/input[1]").send_keys(result) #模拟输入
dirver.find_element_by_xpath("html/body/form/input[2]").click() #模拟点击
res=dirver.page_source
print(res)

#感谢https://www.jianshu.com/p/729dcdb19a51