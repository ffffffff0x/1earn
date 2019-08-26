# -- coding: utf-8 --
import requests
import re

url = ("https://ifconfig.me/")
print("\n")
print('================================start!================================')
print("\n")
response = requests.get(url=url).content.decode('utf-8')
ipaddress = re.findall(r"\d+.\d+.\d+.\d+",response)[0]
print('================================'+ipaddress+'=============================')
