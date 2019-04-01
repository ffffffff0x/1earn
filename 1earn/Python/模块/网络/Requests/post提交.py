import requests

aaa = ["1","2","3"]
url = "http://www.qq.com/spider.php?type=add_domain"
data = {"type": aaa}
res = requests.post(url, data=data, proxies={"http":"http://127.0.0.1:8080"}).text

#aaa=1&aaa=2&aaa=3



aaa = ["1","2","3"]
url = "http://www.qq.com/spider.php?type=add_domain"
data = {"type[]": aaa}
res = requests.post(url, data=data, proxies={"http":"http://127.0.0.1:8080"}).text

#aaa[]=1&aaa[]=2&aaa[]=3