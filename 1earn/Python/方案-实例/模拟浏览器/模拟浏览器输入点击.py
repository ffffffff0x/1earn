import requests
import re
from selenium import webdriver

dirver=webdriver.Edge()
url="www.baidu.com"
dirver.get(url)

res=dirver.page_source
print(res)


