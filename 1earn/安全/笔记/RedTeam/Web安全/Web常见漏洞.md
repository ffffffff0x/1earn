# Web 常见漏洞

---

## 免责声明

`本文档仅供学习和研究使用,请勿使用文中的技术源码用于非法用途,任何人造成的任何负面影响,与本人无关.`

---

# 大纲

* **[点击劫持](#点击劫持)**

* **[任意文件下载-读取](#任意文件下载-读取)**

* **[文件包含漏洞](#文件包含漏洞)**
    * [日志中毒攻击](#日志中毒攻击)

* **[文件解析漏洞](#文件解析漏洞)**
    * [IIS](#iis)
    * [Nginx](#nginx)
    * [Apache](#apache)
    * [其他](#其他)

* **[文件上传漏洞](#文件上传漏洞)**

* **[信息泄露漏洞](#信息泄露漏洞)**
    * [目录遍历](#目录遍历)
    * [GIT源码泄露](#git源码泄露)
    * [SVN源码泄露](#snv源码泄露)
    * [DS_Store文件泄漏](#ds_store文件泄漏)
    * [网站备份压缩文件](#网站备份压缩文件)
    * [WEB-INF/web.xml信息泄露](#web-infwebxml信息泄露)
    * [idea文件夹泄露](#idea文件夹泄露)
    * [phpinfo信息泄露](#phpinfo信息泄露)
    * [JS敏感信息泄露](#js敏感信息泄露)
    * [各类APIkey泄露](#各类apikey泄露)

* **[http参数污染](#http参数污染)**

* **[php反序列化](#php反序列化)**

* **[SSRF](#ssrf)**

* **[URL跳转漏洞](#url跳转漏洞)**

* **[CRLF_Injection](#crlf_injection)**

* **[SQL_inje](#sql_inje)**

* **[XSS](#xss)**

* **[XXE](#xxe)**

* **[配置不当](#配置不当)**
    * [jwt攻击](#jwt攻击)
    * [代理配置不当](#代理配置不当)

* **[未验证来源](#未验证来源)**
    * [二维码劫持](#二维码劫持)
    * [CORS](#cors)
    * [CSRF](#csrf)
    * [jsonp信息泄露](#jsonp信息泄露)

---

**文章**
- [聊聊安全测试中如何快速搞定 Webshell](https://www.freebuf.com/articles/web/201421.html)
- [Web Service 渗透测试从入门到精通](https://www.anquanke.com/post/id/85910)

---

# 点击劫持

- [click-jacking](https://www.hacksplaining.com/exercises/click-jacking) - 一个简单的讲解关于点击劫持的网站

**案例**
- [Uber XSS + clickjacking](https://www.youtube.com/watch?v=5Gg4t3clwys)

---

# 任意文件下载-读取

**案例**
- [电信某分站配置不当导致敏感文件泄露](http://wy.zone.ci/bug_detail.php?wybug_id=wooyun-2015-095088)
- [一个任意文件读取漏洞记录](https://toutiao.io/posts/423535/app_preview)
- [南方周末邮件服务器任意文件读取漏洞](http://wooyun.jozxing.cc/static/bugs/wooyun-2013-045426.html)

---

# 文件包含漏洞

文件包含，是一个功能。在各种开发语言中都提供了内置的文件包含函数，其可以使开发人员在一个代码文件中直接包含（引入）另外一个代码文件。 比如 在 PHP 中，提供了：`include()`,`include_once()`,`require()`,`require_once()` 这些文件包含函数，这些函数在代码设计中被经常使用到。

大多数情况下，文件包含函数中包含的代码文件是固定的，因此也不会出现安全问题。 但是，有些时候，文件包含的代码文件被写成了一个变量，且这个变量可以由前端用户传进来，这种情况下，如果没有做足够的安全考虑，则可能会引发文件包含漏洞。 攻击着会指定一个“意想不到”的文件让包含函数去执行，从而造成恶意操作。 根据不同的配置环境，文件包含漏洞分为如下两种情况：
1. 本地文件包含漏洞：仅能够对服务器本地的文件进行包含，由于服务器上的文件并不是攻击者所能够控制的，因此该情况下，攻击着更多的会包含一些固定的系统配置文件，从而读取系统敏感信息。很多时候本地文件包含漏洞会结合一些特殊的文件上传漏洞，从而形成更大的威力。
2. 远程文件包含漏洞：能够通过 url 地址对远程的文件进行包含，这意味着攻击者可以传入任意的代码，这种情况没啥好说的，准备挂彩

因此，在 web 应用系统的功能设计上尽量不要让前端用户直接传变量给包含函数，如果非要这么做，也一定要做严格的白名单策略进行过滤。

**文章**
- [LFI、RFI、PHP 封装协议安全问题学习 - 骑着蜗牛逛世界](https://www.cnblogs.com/LittleHann/p/3665062.html#3831621)
- [php 文件包含漏洞 | Chybeta](https://chybeta.github.io/2017/10/08/php%E6%96%87%E4%BB%B6%E5%8C%85%E5%90%AB%E6%BC%8F%E6%B4%9E/)
- [文件包含漏洞](https://blog.csdn.net/le0nis/article/details/52043732)
- [文件包含漏洞(绕过姿势) ](https://thief.one/2017/04/10/2/)
- [文件包含漏洞原理分析](https://zhuanlan.zhihu.com/p/25069779)
- [文件包含漏洞总结 | 瓦都剋](http://byd.dropsec.xyz/2016/07/19/%E6%96%87%E4%BB%B6%E5%8C%85%E5%90%AB%E6%BC%8F%E6%B4%9E%E6%80%BB%E7%BB%93/)
- [本地文件包含漏洞利用技巧](https://www.secpulse.com/archives/55769.html)
- [Directory Traversal, File Inclusion, and The Proc File System](https://blog.netspi.com/directory-traversal-file-inclusion-proc-file-system/)
- [Exploiting PHP File Inclusion – Overview | Reiners' Weblog](https://websec.wordpress.com/2010/02/22/exploiting-php-file-inclusion-overview/)
- [Local File Inclusion with Magic_quotes_gpc enabled - NotSoSecure](https://www.notsosecure.com/local-file-inclusion-with-magic_quotes_gpc-enabled/)
- [Positive Technologies - learn and secure : Another alternative for NULL byte](https://blog.ptsecurity.com/2010/08/another-alternative-for-null-byte.html)
- [远程包含和本地包含漏洞的原理 - Kevins 的天空](https://blog.csdn.net/iiprogram/article/details/2349322)
- [聊聊安全测试中如何快速搞定Webshell](https://www.freebuf.com/articles/web/201421.html)

**案例**
- [IKEA官网本地文件包含(LFI)漏洞分析 - 嘶吼 RoarTalk](http://www.4hou.com/vulnerable/13759.html)

**几种利用方法**
- 常规利用

    `Payload: http://www.test.com/test.php?file=upload/hourse.jpg&x=phpinfo()`

- 文件协议读取

    其前提是得知道网站应用的绝对路径(物理路径):

    `Payload: http://www.test.com/test.php?file=file://D:/Server/htdocs/test/upload/hourse.jpg&x=phpinfo()`

    结果和上面一样,只是地址栏链接不一样.

- 压缩包文件读取

    依然需要知道压缩包文件的绝对路径

    `Payload: http://www.test.com/test.php?file=zip://D:/Server/htdocs/test/upload/shell.zip%23shell.php&x=phpinfo())`

- phar:// 相对路径运行 PHP 文件

    当我们想要运行自己的 PHP 文件,该咋做呐？通过文件包含(include,require 这类函数),首先构造一个这样的文件,将 webshell.php 添加到压缩文件 .zip,然后将压缩包后缀名改为 .jpg 反正合法的文件后缀即可(一般的操作是这样的,当只能上传图片的时候),最后使用 phar:// 按照相对路径读取并执行文件.

    `Payload:http://www.test.php?file=phar://upload/shell.jpg/shell.php?x=phpinfo()`

- 读取源码

    当我们没法儿上传文件,但是又想读取文件的源码来寻找别的漏洞从而进一步利用该怎么做呐？同样的利用 php://filter/ 协议可以实现,要注意的是,因为编码问题,一般我们会将读取的文件先 Base64 编码一下输出:

    `Payload:http://www.test.com/test.php?file=php://filter/read=convert.base64-encode/resource=upload/shell.php`

## 日志中毒攻击

`log poisoning`

**文章**
- [RCE with LFI and SSH Log Poisoning](https://www.hackingarticles.in/rce-with-lfi-and-ssh-log-poisoning/)
- [Apache Log Poisoning through LFI](https://www.hackingarticles.in/apache-log-poisoning-through-lfi/)
- [From Local File Inclusion to Remote Code Execution - Part 1 | Outpost 24 blog](https://outpost24.com/blog/from-local-file-inclusion-to-remote-code-execution-part-1)
- [SMTP Log Poisioning through LFI to Remote Code Execution](https://www.hackingarticles.in/smtp-log-poisioning-through-lfi-to-remote-code-exceution/)

---

# 文件解析漏洞

**文章**
- [解析漏洞总结 – erevus](http://www.vuln.cn/7070)

## IIS

**5.x/6.0 解析漏洞**

IIS 6.0 解析利用方法有两种

1. 目录解析

    `/xx.asp/xx.jpg`

2. 文件解析

    `wooyun.asp;.jpg `

第一种,在网站下建立文件夹的名字为 .asp、.asa 的文件夹,其目录内的任何扩展名的文件都被 IIS 当作 asp 文件来解析并执行.

例如创建目录 wooyun.asp,那么 `/wooyun.asp/1.jpg` 将被当作 asp 文件来执行.假设黑阔可以控制上传文件夹路径,就可以不管你上传后你的图片改不改名都能拿 shell 了.

第二种,在 IIS6.0 下,分号后面的不被解析,也就是说 `wooyun.asp;.jpg` 会被服务器看成是wooyun.asp

还有 IIS6.0 默认的可执行文件除了 asp 还包含这三种
```
/wooyun.asa
/wooyun.cer
/wooyun.cdx
```

- **案例**
    - [网站安全狗IIS6.0解析webshell访问限制bypass](https://shuimugan.com/bug/view?bug_no=71861)
    - [网站安全狗免杀神技+IIS6.0解析WebShell访问限制Bypass](https://shuimugan.com/bug/view?bug_no=104444)
    - [网站安全狗IIS6.0解析webshell访问拦截bypass](https://shuimugan.com/bug/view?bug_no=128432)
    - [桃源网络硬盘&IIS6.0解析漏洞](https://shuimugan.com/bug/view?bug_no=2632)

---

## Nginx

**IIS 7.0/IIS 7.5/Nginx <8.03 畸形解析漏洞**

在默认 Fast-CGI 开启状况下,黑阔上传一个名字为 wooyun.jpg,内容为

`<?PHP fputs(fopen('shell.php','w'),'<?php eval($_POST[cmd])?>');?>`

然后访问 wooyun.jpg/.php,在这个目录下就会生成一句话木马 shell.php

- **案例**
    - [用友软件某分站SQL注入漏洞+nginx解析漏洞](http://www.anquan.us/static/bugs/wooyun-2013-032250.html)
    - [新浪网分站多处安全漏洞(nginx解析+SQL注射等)小礼包 ](http://www.anquan.us/static/bugs/wooyun-2013-021064.html)
    - [kingsoft.com某x级域名nginx解析漏洞+爆路径 ](http://www.anquan.us/static/bugs/wooyun-2013-019253.html)

**Nginx <8.03 空字节代码执行漏洞**

影响版:0.5.,0.6., 0.7 <= 0.7.65, 0.8 <= 0.8.37

Nginx 在图片中嵌入 PHP 代码然后通过访问 `xxx.jpg%00.php` 来执行其中的代码

---

## Apache

Apache 是从右到左开始判断解析,如果为不可识别解析,就再往左判断.

比如 wooyun.php.owf.rar ".owf"和".rar" 这两种后缀是 apache 不可识别解析,apache 就会把 wooyun.php.owf.rar 解析成 php.

如何判断是不是合法的后缀就是这个漏洞的利用关键,测试时可以尝试上传一个 wooyun.php.rara.jpg.png…(把你知道的常见后缀都写上…)去测试是否是合法后缀

- **案例**
    - [安卓开发平台存在上传漏洞和 Apache 解析漏洞,成功获取 webshell](http://www.anquan.us/static/bugs/wooyun-2013-018433.html)

**.htaccess**

如果在 Apache 中 .htaccess 可被执行.且可被上传.那可以尝试在 .htaccess 中写入: `<FilesMatch "wooyun.jpg"> SetHandler application/x-httpd-php </FilesMatch>` 然后再上传 shell.jpg 的木马, 这样 shell.jpg 就可解析为 php 文件.

**CVE-2017-15715 Apache HTTPD 换行解析漏洞**

其 2.4.0~2.4.29 版本中存在一个解析漏洞,在解析 PHP 时,1.php\x0A 将被按照 PHP 后缀进行解析,导致绕过一些服务器的安全策略.

原理:在解析 PHP 时,1.php\x0A 将被按照 PHP 后缀进行解析.

用 hex 功能在 1.php 后面添加一个 \x0A

![](../../../../../assets/img/安全/笔记/RedTeam/Web安全/Web常见漏洞/1.png)

访问 http://10.10.10.131:8080/1.php%0A ,成功解析

---

## 其他

在 windows 环境下,`xx.jpg[空格]` 或 `xx.jpg.` 这两类文件都是不允许存在的,若这样命名,windows 会默认除去空格或点,黑客可以通过抓包,在文件名后加一个空格或者点绕过黑名单.若上传成功,空格和点都会被 windows 自动消除,这样也可以 getshell.

**CGI 解析漏洞**

`/.php`

---

# 文件上传漏洞

**文章**
- [简单粗暴的文件上传漏洞](https://paper.seebug.org/560/)
- [BookFresh Tricky File Upload Bypass to RCE](https://secgeek.net/bookfresh-vulnerability/)
- [Upload_Attack_Framework](https://www.slideshare.net/insight-labs/upload-attack-framework)
- [关于File Upload的一些思考](https://www.freebuf.com/articles/web/223679.html)

**靶场**
- [upload-labs](https://github.com/c0ny1/upload-labs)
    - writeup : [upload-labs-WalkThrough](../../../实验/Web/upload-labs-WalkThrough.md)

**案例**
- [实战渗透-看我如何拿下自己学校的大屏幕(Bypass) ](https://xz.aliyun.com/t/7786) - 大量字符 bypass waf 文件上传
- [渗透测试tips：两处有趣的文件上传到getshell](https://zhuanlan.zhihu.com/p/100871520) - 多个漏洞组合利用，无视 OSS 存储 getshell

---

# 信息泄露漏洞

**文章**
- [谈谈源码泄露](https://blog.csdn.net/GitChat/article/details/79014538)
- [敏感文件泄露](http://www.myh0st.cn/index.php/archives/62/)

**工具**
- [lijiejie/BBScan](https://github.com/lijiejie/BBScan) - 用于渗透测试前期，快速地对大量目标进行扫描，发现信息泄露等常见漏洞，找到可能的突破入口。
- [jerrychan807/WSPIH](https://github.com/jerrychan807/WSPIH) - 网站个人敏感信息文件扫描器
- [ring04h/weakfilescan](https://github.com/ring04h/weakfilescan) - 动态多线程敏感信息泄露检测工具

---

## 目录遍历

**案例**
- [京东商城两处任意目录遍历下载漏洞](http://wy.zone.ci/bug_detail.php?wybug_id=wooyun-2016-0214222)
- [2 Path Traversal Cases](https://jlajara.gitlab.io/posts/2020/03/29/Path_Traversal.html)

---

## GIT源码泄露

**简介**

当在一个空目录执行 git init 时,Git 会创建一个 `.git` 目录. 这个目录包含所有的 Git 存储和操作的对象. 如果想备份或复制一个版本库,只需把这个目录拷贝至另一处就可以了.

- `/.git/config`

**案例**
- [大众点评某站点 git 泄漏源代码](http://www.anquan.us/static/bugs/wooyun-2015-0117332.html)

**工具**
- [lijiejie/GitHack](https://github.com/lijiejie/GitHack) - 一个 `.git` 泄露利用脚本，通过泄露的.git文件夹下的文件，重建还原工程源代码。
- [gakki429/Git_Extract](https://github.com/gakki429/Git_Extract) - 提取远程 git 泄露或本地 git 的工具

---

## SVN源码泄露

- `/.svn/entries`

**案例**
- [我爱我家某处源码泄露](http://wy.zone.ci/bug_detail.php?wybug_id=wooyun-2015-0149331)

**工具**
- [kost/dvcs-ripper](https://github.com/kost/dvcs-ripper) - SVN/GIT/HG 等版本控制系统的扫描工具
- [admintony/svnExploit](https://github.com/admintony/svnExploit) - 一款 SVN 源代码利用工具，其完美支持 SVN<1.7 版本和 SVN>1.7 版本的 SVN 源代码泄露

---

## DS_Store文件泄漏

**简介**

`.DS_Store` 文件 MAC 系统是用来存储这个文件夹的显示属性的:比如文件图标的摆放位置.如果用户删除以后的副作用就是这些信息的失去.

这些文件本来是给 Finder 使用的,但它们被设想作为一种更通用的有关显示设置的元数据存储,诸如图标位置和视图设置. 当你需要把代码上传的时候,安全正确的操作应该把 `.DS_Store` 文件删除才正确.

因为里面包含了一些目录信息,如果没有删除,攻击者通过 `.DS_Store` 可以知道这个目录里面所有文件名称,从而让攻击者掌握了更多的信息.　

**案例**
- [TCL 某网站 DS_Store 文件泄露敏感信息](http://www.anquan.us/static/bugs/wooyun-2015-091869.html)

**工具**
- [lijiejie/ds_store_exp](https://github.com/lijiejie/ds_store_exp) - 一个 `.DS_Store` 文件泄漏利用脚本，它解析 `.DS_Store` 文件并递归地下载文件到本地。
- [anantshri/DS_Store_crawler_parser](https://github.com/anantshri/DS_Store_crawler_parser) - `.DS_Store` 文件解析脚本,递归地获取文件夹内的 `.ds_Store`

---

## 网站备份压缩文件

**简介**

该漏洞的成因主要有是管理员将备份文件放在到 web 服务器可以访问的目录下.

该漏洞往往会导致服务器整站源代码或者部分页面的源代码被下载,利用源代码中所包含的各类敏感信息,如服务器数据库连接信息,服务器配置信息等会因此而泄露,造成巨大的损失.

**案例**
- [百度某分站备份文件泄露](http://www.anquan.us/static/bugs/wooyun-2014-050622.html)
- [乐友商城 24GB 代码与数据库敏感文件泄露](http://wy.zone.ci/bug_detail.php?wybug_id=wooyun-2015-0124051)

---

## WEB-INF/web.xml信息泄露

**简介**

WEB-INF 是 Java 的 WEB 应用的安全目录.该目录原则上来说是客户端无法访问,只有服务端才可以可以访问.如果想在页面中直接访问其中的文件,必须通过 `web.xml` 文件对要访问的文件进行相应映射才能访问.

WEB-INF 主要包含一下文件或目录:
```
/WEB-INF/web.xml:Web 应用程序配置文件,描述了 servlet 和其他的应用组件配置及命名规则;
/WEB-INF/classes/:含了站点所有用的 class 文件,包括 servlet class 和非 servlet class,他们不能包含在 .jar 文件中;
/WEB-INF/lib/:存放 web 应用需要的各种 JAR 文件,放置仅在这个应用中要求使用的 jar 文件 , 如数据库驱动 jar 文件;
/WEB-INF/src/:源码目录,按照包名结构放置各个 java 文件;
/WEB-INF/database.properties:数据库配置文件.
```
不过在一些特定的场合却会让攻击者能读取到其中的内容,从而造成源码泄露.

**案例**
- [华为官网 WEB-INF 目录配置文件导致信息泄露](http://www.anquan.us/static/bugs/wooyun-2013-022906.html)

---

## idea文件夹泄露

**工具**
- [lijiejie/idea_exploit](https://github.com/lijiejie/idea_exploit) - 一个 `.idea` 文件泄漏利用脚本

---

## phpinfo信息泄露

**文章**
- [phpinfo 可以告诉我们什么](http://zeroyu.xyz/2018/11/13/what-phpinfo-can-tell-we/)
- [PHPINFO 中的重要信息](https://www.k0rz3n.com/2019/02/12/PHPINFO%20%E4%B8%AD%E7%9A%84%E9%87%8D%E8%A6%81%E4%BF%A1%E6%81%AF/)
- [amazing phpinfo() ](https://skysec.top/2018/04/04/amazing-phpinfo/)
- [phpinfo 中值得注意的信息](https://seaii-blog.com/index.php/2017/10/25/73.html)

**工具**
- [proudwind/phpinfo_scanner](https://github.com/proudwind/phpinfo_scanner) - 抓取 phpinfo 重要信息 - 我这里运行报错,解决方法是把15行的3个 nth-child 改为 nth-of-type

---

## JS敏感信息泄露

**文章**
- [JS 敏感信息泄露:不容忽视的 WEB 漏洞](https://www.secpulse.com/archives/35877.html)

**案例**
- [从JS信息泄露到Webshell](http://r3start.net/index.php/2019/07/15/546)

**相关工具**
- [m4ll0k/SecretFinder](https://github.com/m4ll0k/SecretFinder) - 通过正则在 JS 中发现敏感数据，如 apikeys、accesstoken、authorizations、jwt，..等等
- [Threezh1/JSFinder](https://github.com/Threezh1/JSFinder) - 通过在 js 文件中提取 URL,子域名

---

## 各类APIkey泄露

**文章**
- [Unauthorized Google Maps API Key Usage Cases, and Why You Need to Care](https://medium.com/@ozguralp/unauthorized-google-maps-api-key-usage-cases-and-why-you-need-to-care-1ccb28bf21e)
- [一些提取api key的正则表达式](https://bacde.me/post/Extract-API-Keys-From-Regex/)

以下正则来自 以下内容来自 <sup>[[一些提取api key的正则表达式](https://bacde.me/post/Extract-API-Keys-From-Regex/)]</sup>
```re
"aliyun_oss_url": "[\\w-.]\\.oss.aliyuncs.com"
"azure_storage": "https?://[\\w-\.]\\.file.core.windows.net"
"access_key": "[Aa](ccess|CCESS)_?[Kk](ey|EY)|[Aa](ccess|CCESS)_?[sS](ecret|ECRET)|[Aa](ccess|CCESS)_?(id|ID|Id)"
"secret_key": "[Ss](ecret|ECRET)_?[Kk](ey|EY)"
"slack_token": "(xox[p|b|o|a]-[0-9]{12}-[0-9]{12}-[0-9]{12}-[a-z0-9]{32})"
<!-- more -->

"slack_webhook": "https://hooks.slack.com/services/T[a-zA-Z0-9_]{8}/B[a-zA-Z0-9_]{8}/[a-zA-Z0-9_]{24}"
"facebook_oauth": "[f|F][a|A][c|C][e|E][b|B][o|O][o|O][k|K].{0,30}['\"\\s][0-9a-f]{32}['\"\\s]",
"twitter_oauth": "[t|T][w|W][i|I][t|T][t|T][e|E][r|R].{0,30}['\"\\s][0-9a-zA-Z]{35,44}['\"\\s]"
"heroku_api": "[h|H][e|E][r|R][o|O][k|K][u|U].{0,30}[0-9A-F]{8}-[0-9A-F]{4}-[0-9A-F]{4}-[0-9A-F]{4}-[0-9A-F]{12}"
"mailgun_api": "key-[0-9a-zA-Z]{32}"
"mailchamp_api": "[0-9a-f]{32}-us[0-9]{1,2}"
"picatic_api": "sk_live_[0-9a-z]{32}"
"google_oauth_id": "[0-9(+-[0-9A-Za-z_]{32}.apps.qooqleusercontent.com"
"google_api": "AIza[0-9A-Za-z-_]{35}"
"google_captcha": "6L[0-9A-Za-z-_]{38}"
"google_oauth": "ya29\\.[0-9A-Za-z\\-_]+"
"amazon_aws_access_key_id": "AKIA[0-9A-Z]{16}"
"amazon_mws_auth_token": "amzn\\.mws\\.[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}"
"amazonaws_url": "s3\\.amazonaws.com[/]+|[a-zA-Z0-9_-]*\\.s3\\.amazonaws.com"
"facebook_access_token": "EAACEdEose0cBA[0-9A-Za-z]+"
"mailgun_api_key": "key-[0-9a-zA-Z]{32}"
"twilio_api_key": "SK[0-9a-fA-F]{32}"
"twilio_account_sid": "AC[a-zA-Z0-9_\\-]{32}"
"twilio_app_sid": "AP[a-zA-Z0-9_\\-]{32}"
"paypal_braintree_access_token": "access_token\\$production\\$[0-9a-z]{16}\\$[0-9a-f]{32}"
"square_oauth_secret": "sq0csp-[ 0-9A-Za-z\\-_]{43}"
"square_access_token": "sqOatp-[0-9A-Za-z\\-_]{22}"
"stripe_standard_api": "sk_live_[0-9a-zA-Z]{24}"
"stripe_restricted_api": "rk_live_[0-9a-zA-Z]{24}"
"github_access_token": "[a-zA-Z0-9_-]*:[a-zA-Z0-9_\\-]+@github\\.com*"
"private_ssh_key": "-----BEGIN PRIVATE KEY-----[a-zA-Z0-9\\S]{100,}-----END PRIVATE KEY——"
"private_rsa_key": "-----BEGIN RSA PRIVATE KEY-----[a-zA-Z0-9\\S]{100,}-----END RSA PRIVATE KEY-----"
"稳定的 JWT 版本":"[= ]ey[A-Za-z0-9_-]*\.[A-Za-z0-9._-]*"
"所有 JWT 版本（可能误报）":"[= ]ey[A-Za-z0-9_\/+-]*\.[A-Za-z0-9._\/+-]*"
```

---

# http参数污染

**文章**
- [Web 应用里的 HTTP 参数污染 (HPP) 漏洞](https://blog.csdn.net/eatmilkboy/article/details/6761407)
- [浅谈绕过 waf 的数种方法](https://www.waitalone.cn/waf-bypass.html)
- [通过 HTTP 参数污染绕过 WAF 拦截](http://www.freebuf.com/articles/web/5908.html)

---

# php反序列化

**工具**
- [php 在线反序列化工具](https://www.w3cschool.cn/tools/index?name=unserialize)

---

# SSRF

很多 web 应用都提供了从其他的服务器上获取数据的功能.使用用户指定的 URL,web 应用可以获取图片,下载文件,读取文件内容等.这个功能如果被恶意使用,可以利用存在缺陷的 web 应用作为代理攻击远程和本地的服务器.这种形式的攻击称为服务端请求伪造攻击(Server-side Request Forgery).

一般情况下，SSRF 攻击的目标是从外网无法访问的内部系统。SSRF 形成的原因大都是由于服务端提供了从其他服务器应用获取数据的功能且没有对目标地址做过滤与限制。比如从指定URL地址获取网页文本内容，加载指定地址的图片，下载等等。

**文章**
- [SSRF 漏洞分析及利用](https://www.knowsec.net/archives/85/)
- [浅析 SSRF 原理及利用方式](https://www.anquanke.com/post/id/145519)
- [SSRF 利用与防御](https://hellohxk.com/blog/ssrf/)
- [聊一聊ssrf漏洞的挖掘思路与技巧](https://bbs.ichunqiu.com/thread-49370-1-1.html)
- [Bypassing SSRF Protection](https://medium.com/@vickieli/bypassing-ssrf-protection-e111ae70727b)

**案例**
- [My First SSRF Using DNS Rebinding](https://geleta.eu/2019/my-first-ssrf-using-dns-rebinfing/)
- [SSRF in Exchange leads to ROOT access in all instances](https://hackerone.com/reports/341876) - 通过对 ssrf 访问 Google Cloud Metadata,直至 RCE

**payload**
- [bugbounty-cheatsheet/cheatsheets/ssrf.md](https://github.com/EdOverflow/bugbounty-cheatsheet/blob/master/cheatsheets/ssrf.md)
- [AboutSecurity/Payload/SSRF](https://github.com/ffffffff0x/AboutSecurity/blob/master/Payload/SSRF/)

**工具**
- [In3tinct/See-SURF](https://github.com/In3tinct/See-SURF) - python 写的 ssrf 参数扫描工具
- [swisskyrepo/SSRFmap](https://github.com/swisskyrepo/SSRFmap) - 自动化 Fuzz SSRF 开发工具

---

# URL跳转漏洞

**文章**
- [URL 重定向及跳转漏洞](http://www.pandan.xyz/2016/11/15/url%20%E9%87%8D%E5%AE%9A%E5%90%91%E5%8F%8A%E8%B7%B3%E8%BD%AC%E6%BC%8F%E6%B4%9E/)
- [分享几个绕过 URL 跳转限制的思路](https://www.anquanke.com/post/id/94377)
- [浅析渗透实战中url跳转漏洞 ](https://xz.aliyun.com/t/5189)

---

# CRLF_Injection

**案例**
- [新浪某站CRLF Injection导致的安全问题](https://www.leavesongs.com/PENETRATION/Sina-CRLF-Injection.html)

---

# SQL_inje

**笔记**
- [SQLi 笔记](./SQLi.md)

---

# XSS

**笔记**
- [XSS 笔记](./xss.md)

---

# XXE

**笔记**
- [XXE 笔记](./xxe.md)

---

# 配置不当

## jwt攻击

**文章**
- [全程带阻:记一次授权网络攻防演练 (上) ](https://www.freebuf.com/vuls/211842.html)
- [对jwt的安全测试方式总结](https://saucer-man.com/information_security/377.html)
- [攻击JWT的一些方法 ](https://xz.aliyun.com/t/6776)
- [JWT攻击手册：如何入侵你的Token](https://mp.weixin.qq.com/s/x43D718Tw3LZ4QGFxjLjuw)
- [JSON Web Token Validation Bypass in Auth0 Authentication API](https://insomniasec.com/blog/auth0-jwt-validation-bypass)

**Tips**

搜索 JWT 的正则,来自 以下正则来自 以下内容来自 <sup>[[ticarpi/jwt_tool](https://github.com/ticarpi/jwt_tool#tips)]</sup>
```re
[= ]ey[A-Za-z0-9_-]*\.[A-Za-z0-9._-]*         -稳定的 JWT 版本
[= ]ey[A-Za-z0-9_\/+-]*\.[A-Za-z0-9._\/+-]*   -所有 JWT 版本（可能误报）
```

```python
import jwt
jwt.encode({'字段1':'test','字段2':'123456'},algorithm='none',key='')
```

**工具**
- [JSON Web Tokens - jwt.io](https://jwt.io/) - 在线的 jwt 生成
- [ticarpi/jwt_tool](https://github.com/ticarpi/jwt_tool) - 一个用于验证，伪造和破解JWT（JSON Web令牌）的工具包。
- [Ch1ngg/JWTPyCrack](https://github.com/Ch1ngg/JWTPyCrack)
- [crack JWT](https://pastebin.com/tv99bTNg)
- [brendan-rius/c-jwt-cracker](https://github.com/brendan-rius/c-jwt-cracker)
- [andresriancho/jwt-fuzzer](https://github.com/andresriancho/jwt-fuzzer)
- [ozzi-/JWT4B](https://github.com/ozzi-/JWT4B) - 即时操作 JWT 的 burp 插件
- [3v4Si0N/RS256-2-HS256](https://github.com/3v4Si0N/RS256-2-HS256) - JWT 攻击，将算法由 RS256 变为 HS256

## 代理配置不当

**案例**
- [新浪HTTP代理配置不当漫游内网](http://wy.zone.ci/bug_detail.php?wybug_id=wooyun-2015-0131169)
- [陌陌一处代理配置不当，已验证可绕过IP过滤探测敏感资源](http://wy.zone.ci/bug_detail.php?wybug_id=wooyun-2014-083202)
- [陌陌web服务器Path处理不当可以正向代理(idc机器/打不到办公网)](http://wy.zone.ci/bug_detail.php?wybug_id=wooyun-2016-0191121)
- [挖洞经验之代理不当日进内网](https://mp.weixin.qq.com/s/EtUmfMxxJjYNl7nIOKkRmA)
- [价值1万美金的谷歌内部主机信息泄露漏洞](https://mp.weixin.qq.com/s/hYZr6EjwE99uTQpzoJRp0g)

---

# 未验证来源

## 二维码劫持

**案例**
- [二维码劫持案例分析](https://www.freebuf.com/vuls/234121.html)

---

## CORS

**文章**
- [JSONP与CORS漏洞挖掘](https://www.anquanke.com/post/id/97671)
- [认识CORS漏洞](https://mp.weixin.qq.com/s/J11CnjkGTa1ILHdFqMhGDA)

**案例**
- [CORS Misconfiguration, could lead to disclosure of sensitive information](https://hackerone.com/reports/426165)
- [看我如何绕过Yahoo！View的CORS限制策略](https://www.freebuf.com/articles/web/158529.html)

**工具**
- [chenjj/CORScanner](https://github.com/chenjj/CORScanner) - 一个旨在发现网站的CORS错误配置漏洞的 python 工具

---

## CSRF

**文章**
- [CSRF攻击与防御](https://blog.csdn.net/stpeace/article/details/53512283)

**案例**
- [“借刀杀人”之CSRF拿下盗图狗后台](https://bbs.ichunqiu.com/thread-31779-1-20.html)
- [Periscope android app deeplink leads to CSRF in follow action](https://hackerone.com/reports/583987)

---

## jsonp信息泄露

**文章**
- [jsonp 原理详解——终于搞清楚 jsonp 是啥了](https://blog.csdn.net/hansexploration/article/details/80314948)

**案例**
- [中国联通某站 jsonp 接口跨域导致信息泄漏并可开通某些套餐 (运营商额外插入功能带来的风险) ](http://wy.zone.ci/bug_detail.php?wybug_id=wooyun-2016-0172305)
- [京东商城 JSONP+CSRF 导致某处信息泄露](https://shuimugan.com/bug/view?bug_no=121266)
- [迅雷某站 jsonp 劫持漏洞泄漏会话 ID,cookie](https://shuimugan.com/bug/view?bug_no=121639)
- [唯品会某处 JSONP+CSRF 泄露重要信息](https://shuimugan.com/bug/view?bug_no=122755)
- [新浪微博之点击我的链接就登录你的微博(JSONP 劫持)](https://shuimugan.com/bug/view?bug_no=204941)
- [苏宁易购多接口问题可泄露用户姓名、地址、订单商品 (jsonp 案例) ](https://shuimugan.com/bug/view?bug_no=118712)
- [通过 jsonp 可以获得当前用户的 QQ+crsf 刷收听](https://shuimugan.com/bug/view?bug_no=70690)
- [利用 JSONP 劫持可以泄漏 QQ 号](https://shuimugan.com/bug/view?bug_no=65177)
- [京东商城某处 jsonp 接口可泄露任意用户的搜索记录](https://shuimugan.com/bug/view?bug_no=44210)
- [新浪微博 JSONP 劫持之点我链接开始微博蠕虫+刷粉丝](https://shuimugan.com/bug/view?bug_no=171499)
- [fanwe O2O 用户密码可劫持 (通用/开源软件 jsonp 劫持案例) ](https://shuimugan.com/bug/view?bug_no=124949)
