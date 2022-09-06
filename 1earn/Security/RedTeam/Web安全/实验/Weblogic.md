# Weblogic

---

## 免责声明

`本文档仅供学习和研究使用,请勿使用文中的技术源码用于非法用途,任何人造成的任何负面影响,与本人无关.`

---

> 官网 : https://www.oracle.com/middleware/weblogic/

**简介**

Oracle Fusion Middleware（Oracle 融合中间件）是美国甲骨文（Oracle）公司的一套面向企业和云环境的业务创新平台。该平台提供了中间件、软件集合等功能。WebLogic Server 是其中的一个适用于云环境和传统环境的应用服务器组件。

**Tips**
- 老版本 weblogic 有一些常见的弱口令,比如 weblogic、system、portaladmin 和 guest,Oracle@123 等,用户名密码交叉使用.

**相关工具**
- [0xn0ne/weblogicScanner](https://github.com/0xn0ne/weblogicScanner) - weblogic 漏洞扫描工具
- [dr0op/WeblogicScan](https://github.com/dr0op/WeblogicScan) - 增强版 WeblogicScan、检测结果更精确、插件化、添加 CVE-2019-2618，CVE-2019-2729 检测，Python3 支持
- [rabbitmask/WeblogicScan](https://github.com/rabbitmask/WeblogicScan) - Weblogic 一键漏洞检测工具
- [rabbitmask/WeblogicScanLot](https://github.com/rabbitmask/WeblogicScanLot) - Weblogic 漏洞批量检测工具
- [TideSec/Decrypt_Weblogic_Password](https://github.com/TideSec/Decrypt_Weblogic_Password) - 整理了 7 种解密 weblogic 的方法及响应工具
- [Ch1ngg/WebLogicPasswordDecryptorUi](https://github.com/Ch1ngg/WebLogicPasswordDecryptorUi) - 解密 weblogic AES 或 DES 加密方法

**环境搭建**
- [QAX-A-Team/WeblogicEnvironment](https://github.com/QAX-A-Team/WeblogicEnvironment) - Weblogic 环境搭建工具

**相关文章**
- [利用Weblogic进行入侵的一些总结](http://drops.xmd5.com/static/drops/tips-8321.html)
- [Weblogic JRMP反序列化漏洞回顾](https://xz.aliyun.com/t/2479)
- [Oracle WebLogic RCE反序列化漏洞分析](https://www.anquanke.com/post/id/162390)
- [[漏洞预警]WebLogic T3 反序列化绕过漏洞 & 附检测POC](https://www.secfree.com/a/957.html)
- [Weblogic 常见漏洞分析](https://hellohxk.com/blog/weblogic/)

**版本判断**
- [第21篇：判断Weblogic详细版本号的方法总结](https://mp.weixin.qq.com/s/z6q1sBYcHYgzvak98QQmeA)
- [Oracle WebLogic Server](https://en.wikipedia.org/wiki/Oracle_WebLogic_Server)

**读取后台用户密文与密钥文件**

weblogic 密码使用 AES（老版本 3DES）加密，对称加密可解密，只需要找到用户的密文与加密时的密钥即可。

这两个文件均位于 base_domain 下，名为 SerializedSystemIni.dat 和 config.xml

SerializedSystemIni.dat 是一个二进制文件，所以一定要用 burpsuite 来读取，用浏览器直接下载可能引入一些干扰字符。在 burp 里选中读取到的那一串乱码，右键 copy to file 就可以保存成一个文件

![](../../../../assets/img/Security/RedTeam/Web安全/BS-Exploits/4.png)

config.xml 是 base_domain 的全局配置文件, 找到其中的 <node-manager-password-encrypted> 的值，即为加密后的管理员密码

![](../../../../assets/img/Security/RedTeam/Web安全/BS-Exploits/5.png)

通过解密工具可以获得后台密码

**CVE-2009-1975 xss 漏洞**
- 描述

    BEA Product Suite 10.3 中 WebLogic Server 组件中的未指定漏洞使远程攻击者可以影响与 WLS 控制台程序包相关的机密性，完整性和可用性。

- 影响版本
    - weblogic_server 10.3

- POC | Payload | exp
    - `http://www.example.com:7011/consolehelp/console-help.portal?_nfpb=true&_pageLabel=ConsoleHelpSearchPage&searchQuery="><script>alert('DSECRG')</script>`
    - [Oracle WebLogic Server 10.3 - 'console-help.portal' Cross-Site Scripting](https://www.exploit-db.com/exploits/33079)

**CVE-2014-4210 SSRF**
- 相关文章
    - [weblogic SSRF漏洞(CVE-2014-4210)检测利用](https://blog.csdn.net/qq_29647709/article/details/84937101)

- 影响版本
    - weblogic_server 10.0.2.0
    - weblogic_server 10.3.6.0

- POC | Payload | exp
    - `http://127.0.0.1:7001/uddiexplorer/SearchPublicRegistries.jsp?rdoSearch=name&txtSearchname=sdf&txtSearchkey=&txtSearchfor=&selfor=Business+location&btnSubmit=Search&operator=http://127.0.0.1:7000`

**CVE-2017-3248**
- 相关文章
    - [WebLogic反序列化漏洞重现江湖，CVE-2017-3248成功绕过之前的官方修复](https://paper.seebug.org/333/)

**CVE-2017-3506**
- POC | Payload | exp
    - [ianxtianxt/CVE-2017-3506](https://github.com/ianxtianxt/CVE-2017-3506)
        ```
        java -jar WebLogic-XMLDecoder.jar -s xxx.xxx.xxx.xxx:7001 /wls-wsat/CoordinatorPortType11 test.jsp
        ```

**CVE-2017-10271 XMLDecoder 反序列化漏洞**
- 描述

    Weblogic 的 WLS Security 组件对外提供 webservice 服务，其中使用了 XMLDecoder 来解析用户传入的 XML 数据，在解析的过程中出现反序列化漏洞，导致可执行任意命令。

- 影响版本
    - weblogic_server 10.3.6.0.0
    - weblogic_server 12.1.3.0.0
    - weblogic_server 12.2.1.1.0 ~ 12.2.1.2.0

- 相关文章
    - [WebLogic XMLDecoder反序列化漏洞复现](https://mochazz.github.io/2017/12/25/weblogic_xmldecode/)
    - [blog-hugo/content/blog/Weblogic-0day.md](https://github.com/kylingit/blog-hugo/blob/master/content/blog/Weblogic-0day.md)

- POC | Payload | exp
    - `<目标IP:端口>/wls-wsat/CoordinatorPortType11`
    - [1337g/CVE-2017-10271](https://github.com/1337g/CVE-2017-10271)

**CVE-2018-2628 反序列化漏洞**
- 描述

    2018年4月18日，Oracle 官方发布了4月份的安全补丁更新 CPU（Critical Patch Update），更新中修复了一个高危的 WebLogic 反序列化漏洞 CVE-2018-2628。攻击者可以在未授权的情况下通过 T3 协议对存在漏洞的 WebLogic 组件进行远程攻击，并可获取目标系统所有权限。

- 影响版本
    - weblogic_server 10.3.6.0.0
    - weblogic_server 12.1.3.0.0
    - weblogic_server 12.2.1.2.0 ~ 12.2.1.3

- 相关文章
    - [CVE-2018-2628 简单复现与分析 | xxlegend](http://xxlegend.com/2018/04/18/CVE-2018-2628%20%E7%AE%80%E5%8D%95%E5%A4%8D%E7%8E%B0%E5%92%8C%E5%88%86%E6%9E%90/)

- POC | Payload | exp
    - [shengqi158/CVE-2018-2628](https://github.com/shengqi158/CVE-2018-2628)

**CVE-2018-2893 WebLogic 反序列化漏洞**
- 描述

    Oracle 官方在2018年7月发布了关键补丁更新，其中包含了 Oracle WebLogic Server 的一个高危的 WebLogic 反序列化漏洞，通过该漏洞，攻击者可以在未授权的情况下远程执行代码。

- 影响版本
    - weblogic_server 10.3.6.0.0
    - weblogic_server 12.1.3.0.0
    - weblogic_server 12.2.1.2.0 ~ 12.2.1.3

- 相关文章
    - [天融信关于CVE-2018-2893 WebLogic反序列化漏洞分析](https://www.freebuf.com/column/178103.html)

- POC | Payload | exp
    - [pyn3rd/CVE-2018-2893](https://github.com/pyn3rd/CVE-2018-2893)

**CVE-2018-2894 未授权访问致任意文件上传/RCE 漏洞**
- 描述

    Oracle Fusion Middleware 中的 Oracle WebLogic Server 组件的 WLS - Web Services 子组件存在安全漏洞。攻击者可利用该漏洞控制 Oracle WebLogic Server，影响数据的保密性、可用性和完整性。

- 影响版本
    - weblogic_server 10.3.6.0.0
    - weblogic_server 12.1.3.0.0
    - weblogic_server 12.2.1.2.0 ~ 12.2.1.3

- 相关文章
    - [Weblogic CVE-2018-2894 漏洞复现](https://blog.csdn.net/qq_23936389/article/details/81256015)

- POC | Payload | exp
    - [LandGrey/CVE-2018-2894](https://github.com/LandGrey/CVE-2018-2894)
    - [PayloadsAllTheThings/CVE Exploits/WebLogic CVE-2018-2894.py ](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/CVE%20Exploits/WebLogic%20CVE-2018-2894.py)

**CVE-2018-3191**
- 描述

    Oracle Fusion Middleware 中的 WebLogic Server 组件 10.3.6.0 版本、12.1.3.0 版本和 12.2.1.3 版本的 WLS Core Components 子组件存在安全漏洞。攻击者可利用该漏洞控制组件，影响数据的保密性、完整性和可用性。

- 影响版本
    - weblogic_server 10.3.6.0.0
    - weblogic_server 12.1.3.0.0
    - weblogic_server 12.2.1.3.0

- 相关文章
    - [从流量侧浅谈WebLogic远程代码执行漏洞(CVE-2018-3191)](https://www.jianshu.com/p/f73b162c4649)

- POC | Payload | exp
    - [voidfyoo/CVE-2018-3191](https://github.com/voidfyoo/CVE-2018-3191)

**CVE-2018-3245**
- 描述

    Oracle Fusion Middleware 中的 WebLogic Server 组件 10.3.6.0 版本、12.1.3.0 版本和 12.2.1.3 版本的 WLS Core Components 子组件存在安全漏洞。攻击者可利用该漏洞控制组件，影响数据的保密性、完整性和可用性。

- 影响版本
    - weblogic_server 10.3.6.0.0
    - weblogic_server 12.1.3.0.0
    - weblogic_server 12.2.1.3.0

- 相关文章
    - [weblogic反序列化漏洞 cve-2018-3245](https://blog.51cto.com/13770310/2308371)

- POC | Payload | exp
    - [pyn3rd/CVE-2018-3245](https://github.com/pyn3rd/CVE-2018-3245)

**CVE-2018-3246**
- 描述

    Oracle Fusion Middleware 中的 WebLogic Server 组件 12.1.3.0 版本和 12.2.1.3 版本的 WLS - Web Services 子组件存在安全漏洞。攻击者可利用该漏洞未授权访问数据，影响数据的保密性。

- 影响版本
    - weblogic_server 12.1.3.0.0
    - weblogic_server 12.2.1.3.0

- 相关文章
    - [看我如何在Weblogic里捡一个XXE (CVE-2018-3246) ](https://www.freebuf.com/vuls/186862.html)

- POC | Payload | exp
    - [hackping/XXEpayload](https://github.com/hackping/XXEpayload/tree/master/xxe)
    - `http://127.0.0.1:8338/ws_utc/begin.do`

**CVE-2018-3252**
- POC | Payload | exp
    - [pyn3rd/CVE-2018-3252](https://github.com/pyn3rd/CVE-2018-3252)

**CVE-2019-2615 任意文件读取漏洞**
- 描述

    Oracle Fusion Middleware 中的 WebLogic Server 组件 10.3.6.0.0 版本、12.1.3.0.0 版本和 12.2.1.3.0 版本的 WLS Core Components 子组件存在安全漏洞。攻击者可利用该漏洞未授权访问数据，影响数据的保密性。

- 影响版本
    - weblogic_server 10.3.6.0.0
    - weblogic_server 12.1.3.0.0
    - weblogic_server 12.2.1.3.0

- POC | Payload | exp
    - [chiaifan/CVE-2019-2615](https://github.com/chiaifan/CVE-2019-2615)

**CVE-2019-2618 Weblogic Upload Vuln(Need username password)**
- 描述

    Oracle Fusion Middleware 中的 WebLogic Server 组件 10.3.6.0.0 版本和 12.1.3.0.0 版本和 12.2.1.3.0 版本的 WLS Core Components 子组件存在安全漏洞。攻击者可利用该漏洞未授权访问、更新、插入或删除数据，影响数据的保密性和完整性。

- 影响版本
    - weblogic_server 10.3.6.0.0
    - weblogic_server 12.1.3.0.0
    - weblogic_server 12.2.1.3.0

- POC | Payload | exp
    - [jas502n/cve-2019-2618](https://github.com/jas502n/cve-2019-2618)

**CVE-2019-2725 && CNVD-C-2019-48814**
- 描述

    4月17日，国家信息安全漏洞共享平台（CNVD）公开了 Weblogic 反序列化远程代码执行漏洞（CNVD-C-2019-48814）。由于在反序列化处理输入信息的过程中存在缺陷，未经授权的攻击者可以发送精心构造的恶意 HTTP 请求，利用该漏洞获取服务器权限，实现远程代码执行。

- 影响版本
    - weblogic_server 10.3.6.0.0
    - weblogic_server 12.1.3.0.0

- 相关文章
    - [CNVD-C-2019-48814 Weblogic wls9_async_response 反序列化RCE复现](https://www.jianshu.com/p/c4982a845f55)
    - [WebLogic RCE(CVE-2019-2725)漏洞之旅](https://paper.seebug.org/909/)
    - [weblogic wls9-async rce 复现 & 分析](https://iassas.com/archives/94f70d04.html)
    - [Weblogic反序列化远程代码执行漏洞（CVE-2019-2725）分析报告](https://www.anquanke.com/post/id/177381)
    - [Weblogic 反序列化远程代码执行漏洞（CVE-2019-2725)](https://co0ontty.github.io/2019/08/08/CVE_2019_2725.html)

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
- 描述

    2019年10月16日，WebLogic 官方发布了安全补丁公告，修复了包含 CVE-2019-2890 等高危漏洞。Weblogic 在利用 T3 协议进行远程资源加载调用时，默认会进行黑名单过滤以保证反序列化安全。漏洞 CVE-2019-2890 绕过了 Weblogic 的反序列化黑名单，使攻击者可以通过 T3 协议对存在漏洞的 Weblogic 组件实施远程攻击，但该漏洞利用条件较高，官方也归类为需要身份认证。

- 影响版本
    - weblogic_server 10.3.6.0.0
    - weblogic_server 12.1.3.0.0
    - weblogic_server 12.2.1.3.0

- POC | Payload | exp
    - [SukaraLin/CVE-2019-2890](https://github.com/SukaraLin/CVE-2019-2890)
    - [jas502n/CVE-2019-2890](https://github.com/jas502n/CVE-2019-2890)

**CVE-2020-2551 Weblogic RCE with IIOP**
- 描述

    最近 Oracle 发布了新一轮补丁,其中重点了修复多个高危安全漏洞.其中较为严重之一的则是 CVE-2020-2551.攻击者可以在未授权的情况下通过 IIOP 协议对存在漏洞的 WebLogic 进行远程代码执行的攻击.成功利用该漏洞的攻击者可以直接控制服务器,危害性极高。

- 影响版本
    - weblogic_server 10.3.6.0.0
    - weblogic_server 12.1.3.0.0
    - weblogic_server 12.2.1.3.0
    - weblogic_server 12.2.1.4.0

- 相关文章
    - [WebLogic CVE-2020-2551漏洞分析](https://paper.seebug.org/1138/)
    - [漫谈WebLogic CVE-2020-2551](https://www.anquanke.com/post/id/201005)

- POC | Payload | exp
    - [jas502n/CVE-2020-2551](https://github.com/jas502n/CVE-2020-2551)
    - [Y4er/CVE-2020-2551](https://github.com/Y4er/CVE-2020-2551)
    - [hktalent/CVE-2020-2551](https://github.com/hktalent/CVE-2020-2551)

**CVE-2020-2555 && CVE-2020-2883 Oracle Coherence 反序列化漏洞分析**
- 描述

    Oracle 官方在1月补丁中修复了 CVE-2020-2555 漏洞，该漏洞位于 Oracle Coherence 组件中。该组件是业内领先的用于解决集群应用程序数据的缓存的解决方案，其默认集成在 Weblogic12c 及以上版本中。

    该漏洞提出了一条新的反序列化 gadget，未经身份验证的攻击者通过精心构造的 T3 请求触发可以反序列化 gadget，最终造成远程命令执行的效果。

- 相关文章
    - [Oracle Coherence 反序列化漏洞分析（CVE-2020-2555）](https://paper.seebug.org/1141/)
    - [Weblogic ChainedExtractor葫芦兄弟漏洞分析（CVE-2020-2555、CVE-2020-2883）](https://www.secpulse.com/archives/140206.html)

- POC | Payload | exp
    - [Y4er/CVE-2020-2555](https://github.com/Y4er/CVE-2020-2555)
    - [Y4er/CVE-2020-2883](https://github.com/Y4er/CVE-2020-2883)

**CVE-2020-2963**
- 相关文章
    - [weblogic CVE-2020-2963、CNVD-2020-23019 反序列化漏洞分析与复现](https://mp.weixin.qq.com/s/RlEmkwit1cDxHhRBo-eY8A)

**CVE-2020-14645**
- 相关文章
    - [CVE-2020-14645——WebLogic反序列化](https://www.anquanke.com/post/id/231425)
    - [CVE-2020-14645漏洞复现利用](https://mp.weixin.qq.com/s/4bK0sMotY4FCcK_zS0iWbg)

- POC | Payload | exp
    - [Y4er/CVE-2020-14645](https://github.com/Y4er/CVE-2020-14645)

**CVE-2020-14756**
- POC | Payload | exp
    - [Y4er/CVE-2020-14756](https://github.com/Y4er/CVE-2020-14756)

**CVE-2020-14841**
- 相关文章
    - [cve 2020-14841 weblogic jndi注入绕过分析复现 附POC](https://mp.weixin.qq.com/s/qs783sbJSOHgGi8pbpExIA)

**CVE-2020-14882 && CVE-2020-14883**
- 影响版本
    * 10.3.6.0.0
    * 12.1.3.0.0
    * 12.2.1.3.0
    * 12.2.1.4.0
    * 14.1.1.0.0

- 相关文章
    - [漏洞分析｜Weblogic未授权访问及命令执行分析复现（CVE-2020-14882/14883）](https://mp.weixin.qq.com/s/GRtDqr45x-tNnoR2Qi5ISg)
    - [Weblogic CVE-2020-14882(10.x 12.x) 利用方式](https://mp.weixin.qq.com/s/QrVRGm5rNw7wz6LtD4rZyQ)
    - [CVE-2020-14882 weblogic 未授权命令执行复现](https://mp.weixin.qq.com/s/48VIwTkyFVXUTS78kNByhg)
    - [cve-2020-14882 weblogic 越权绕过登录分析](https://mp.weixin.qq.com/s/_zNr5Jw7tH_6XlUdudhMhA)
    - [CVE-2020-14882​&14883：Weblogic RCE复现](https://mp.weixin.qq.com/s/oVL9D69Xrdoez6T-sheJLg)
    - [CVE-2020-14882 eblogic Console远程代码执行漏洞复现（豪华版）](https://mp.weixin.qq.com/s/s2HnmoFHUBXQWfKvAMxtnw)

- POC | Payload | exp
    - [jas502n/CVE-2020-14882: CVE-2020-14882、CVE-2020-14883](https://github.com/jas502n/CVE-2020-14882)
    - [Weblogic远程代码执行-CVE-2020-14882](https://www.hedysx.com/2652.html)

**CVE-2021-2109**
- 影响版本
    * WebLogic 10.3.6.0.0
    * WebLogic 12.1.3.0.0
    * WebLogic 12.2.1.3.0
    * WebLogic 12.2.1.4.0
    * WebLogic 14.1.1.0.0

- 相关文章
    - [CVE-2021-2109：Weblogic远程代码执行分析复现](https://cloud.tencent.com/developer/article/1797518)

**CVE-2021-2394**
- 相关文章
    - [WebLogic CVE-2021-2394 RCE 漏洞分析](https://mp.weixin.qq.com/s/LbMB-2Qyrh3Lrqc_vsKIdA)

**CVE-2022-21371 Local File Inclusion**
- POC | Payload | exp
    - https://gist.github.com/picar0jsu/f3e32939153e4ced263d3d0c79bd8786
